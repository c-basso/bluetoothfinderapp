/**
 * Minimal QR Code encoder (byte mode, error correction level M) → inline SVG.
 * No dependencies; based on the ISO/IEC 18004 algorithm as structured in
 * Project Nayuki's reference implementation (MIT). Used at build time to
 * render "scan with your iPhone" codes for desktop visitors.
 */

// ECC level M tables, index = version (1..40).
const ECC_CODEWORDS_PER_BLOCK = [-1, 10, 16, 26, 18, 24, 16, 18, 22, 22, 26, 30, 22, 22, 24, 24, 28, 28, 26, 26, 26, 26, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28];
const NUM_ERROR_CORRECTION_BLOCKS = [-1, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 8, 9, 9, 10, 10, 11, 13, 14, 16, 17, 17, 18, 20, 21, 23, 25, 26, 28, 29, 31, 33, 35, 37, 38, 40, 43, 45, 47, 49];
const ECC_FORMAT_BITS_M = 0; // M = 0b00

function getNumRawDataModules(ver) {
    let result = (16 * ver + 128) * ver + 64;
    if (ver >= 2) {
        const numAlign = Math.floor(ver / 7) + 2;
        result -= (25 * numAlign - 10) * numAlign - 55;
        if (ver >= 7) result -= 36;
    }
    return result;
}

function getNumDataCodewords(ver) {
    return Math.floor(getNumRawDataModules(ver) / 8) - ECC_CODEWORDS_PER_BLOCK[ver] * NUM_ERROR_CORRECTION_BLOCKS[ver];
}

function reedSolomonMultiply(x, y) {
    let z = 0;
    for (let i = 7; i >= 0; i--) {
        z = (z << 1) ^ ((z >>> 7) * 0x11d);
        z ^= ((y >>> i) & 1) * x;
    }
    return z & 0xff;
}

function reedSolomonComputeDivisor(degree) {
    const result = new Array(degree).fill(0);
    result[degree - 1] = 1;
    let root = 1;
    for (let i = 0; i < degree; i++) {
        for (let j = 0; j < result.length; j++) {
            result[j] = reedSolomonMultiply(result[j], root);
            if (j + 1 < result.length) result[j] ^= result[j + 1];
        }
        root = reedSolomonMultiply(root, 0x02);
    }
    return result;
}

function reedSolomonComputeRemainder(data, divisor) {
    const result = divisor.map(() => 0);
    for (const b of data) {
        const factor = b ^ result.shift();
        result.push(0);
        divisor.forEach((coef, i) => { result[i] ^= reedSolomonMultiply(coef, factor); });
    }
    return result;
}

function getBit(x, i) {
    return ((x >>> i) & 1) !== 0;
}

class QrCode {
    constructor(version, mask, dataCodewords) {
        this.version = version;
        this.size = version * 4 + 17;
        this.modules = [];
        this.isFunction = [];
        for (let i = 0; i < this.size; i++) {
            this.modules.push(new Array(this.size).fill(false));
            this.isFunction.push(new Array(this.size).fill(false));
        }
        this.drawFunctionPatterns();
        const allCodewords = this.addEccAndInterleave(dataCodewords);
        this.drawCodewords(allCodewords);

        if (mask === -1) {
            let minPenalty = Infinity;
            for (let i = 0; i < 8; i++) {
                this.applyMask(i);
                this.drawFormatBits(i);
                const penalty = this.getPenaltyScore();
                if (penalty < minPenalty) {
                    mask = i;
                    minPenalty = penalty;
                }
                this.applyMask(i); // undo (XOR)
            }
        }
        this.mask = mask;
        this.applyMask(mask);
        this.drawFormatBits(mask);
        this.isFunction = [];
    }

    drawFunctionPatterns() {
        for (let i = 0; i < this.size; i++) {
            this.setFunctionModule(6, i, i % 2 === 0);
            this.setFunctionModule(i, 6, i % 2 === 0);
        }
        this.drawFinderPattern(3, 3);
        this.drawFinderPattern(this.size - 4, 3);
        this.drawFinderPattern(3, this.size - 4);
        const alignPatPos = this.getAlignmentPatternPositions();
        const numAlign = alignPatPos.length;
        for (let i = 0; i < numAlign; i++) {
            for (let j = 0; j < numAlign; j++) {
                if (!((i === 0 && j === 0) || (i === 0 && j === numAlign - 1) || (i === numAlign - 1 && j === 0))) {
                    this.drawAlignmentPattern(alignPatPos[i], alignPatPos[j]);
                }
            }
        }
        this.drawFormatBits(0);
        this.drawVersion();
    }

    drawFormatBits(mask) {
        const data = (ECC_FORMAT_BITS_M << 3) | mask;
        let rem = data;
        for (let i = 0; i < 10; i++) rem = (rem << 1) ^ ((rem >>> 9) * 0x537);
        const bits = ((data << 10) | rem) ^ 0x5412;
        for (let i = 0; i <= 5; i++) this.setFunctionModule(8, i, getBit(bits, i));
        this.setFunctionModule(8, 7, getBit(bits, 6));
        this.setFunctionModule(8, 8, getBit(bits, 7));
        this.setFunctionModule(7, 8, getBit(bits, 8));
        for (let i = 9; i < 15; i++) this.setFunctionModule(14 - i, 8, getBit(bits, i));
        for (let i = 0; i < 8; i++) this.setFunctionModule(this.size - 1 - i, 8, getBit(bits, i));
        for (let i = 8; i < 15; i++) this.setFunctionModule(8, this.size - 15 + i, getBit(bits, i));
        this.setFunctionModule(8, this.size - 8, true);
    }

    drawVersion() {
        if (this.version < 7) return;
        let rem = this.version;
        for (let i = 0; i < 12; i++) rem = (rem << 1) ^ ((rem >>> 11) * 0x1f25);
        const bits = (this.version << 12) | rem;
        for (let i = 0; i < 18; i++) {
            const color = getBit(bits, i);
            const a = this.size - 11 + (i % 3);
            const b = Math.floor(i / 3);
            this.setFunctionModule(a, b, color);
            this.setFunctionModule(b, a, color);
        }
    }

    drawFinderPattern(x, y) {
        for (let dy = -4; dy <= 4; dy++) {
            for (let dx = -4; dx <= 4; dx++) {
                const dist = Math.max(Math.abs(dx), Math.abs(dy));
                const xx = x + dx;
                const yy = y + dy;
                if (xx >= 0 && xx < this.size && yy >= 0 && yy < this.size) {
                    this.setFunctionModule(xx, yy, dist !== 2 && dist !== 4);
                }
            }
        }
    }

    drawAlignmentPattern(x, y) {
        for (let dy = -2; dy <= 2; dy++) {
            for (let dx = -2; dx <= 2; dx++) {
                this.setFunctionModule(x + dx, y + dy, Math.max(Math.abs(dx), Math.abs(dy)) !== 1);
            }
        }
    }

    setFunctionModule(x, y, isDark) {
        this.modules[y][x] = isDark;
        this.isFunction[y][x] = true;
    }

    addEccAndInterleave(data) {
        const ver = this.version;
        const numBlocks = NUM_ERROR_CORRECTION_BLOCKS[ver];
        const blockEccLen = ECC_CODEWORDS_PER_BLOCK[ver];
        const rawCodewords = Math.floor(getNumRawDataModules(ver) / 8);
        const numShortBlocks = numBlocks - (rawCodewords % numBlocks);
        const shortBlockLen = Math.floor(rawCodewords / numBlocks);
        const blocks = [];
        const rsDiv = reedSolomonComputeDivisor(blockEccLen);
        for (let i = 0, k = 0; i < numBlocks; i++) {
            const dat = data.slice(k, k + shortBlockLen - blockEccLen + (i < numShortBlocks ? 0 : 1));
            k += dat.length;
            const ecc = reedSolomonComputeRemainder(dat, rsDiv);
            if (i < numShortBlocks) dat.push(0);
            blocks.push(dat.concat(ecc));
        }
        const result = [];
        for (let i = 0; i < blocks[0].length; i++) {
            blocks.forEach((block, j) => {
                if (i !== shortBlockLen - blockEccLen || j >= numShortBlocks) result.push(block[i]);
            });
        }
        return result;
    }

    drawCodewords(data) {
        let i = 0;
        for (let right = this.size - 1; right >= 1; right -= 2) {
            if (right === 6) right = 5;
            for (let vert = 0; vert < this.size; vert++) {
                for (let j = 0; j < 2; j++) {
                    const x = right - j;
                    const upward = ((right + 1) & 2) === 0;
                    const y = upward ? this.size - 1 - vert : vert;
                    if (!this.isFunction[y][x] && i < data.length * 8) {
                        this.modules[y][x] = getBit(data[i >>> 3], 7 - (i & 7));
                        i++;
                    }
                }
            }
        }
    }

    applyMask(mask) {
        for (let y = 0; y < this.size; y++) {
            for (let x = 0; x < this.size; x++) {
                let invert;
                switch (mask) {
                    case 0: invert = (x + y) % 2 === 0; break;
                    case 1: invert = y % 2 === 0; break;
                    case 2: invert = x % 3 === 0; break;
                    case 3: invert = (x + y) % 3 === 0; break;
                    case 4: invert = (Math.floor(x / 3) + Math.floor(y / 2)) % 2 === 0; break;
                    case 5: invert = ((x * y) % 2) + ((x * y) % 3) === 0; break;
                    case 6: invert = (((x * y) % 2) + ((x * y) % 3)) % 2 === 0; break;
                    case 7: invert = (((x + y) % 2) + ((x * y) % 3)) % 2 === 0; break;
                    default: throw new Error('bad mask');
                }
                if (!this.isFunction[y][x] && invert) this.modules[y][x] = !this.modules[y][x];
            }
        }
    }

    getPenaltyScore() {
        const N1 = 3, N2 = 3, N3 = 40, N4 = 10;
        let result = 0;
        const size = this.size;
        const line = (get) => {
            for (let a = 0; a < size; a++) {
                let runColor = false;
                let runLen = 0;
                const runHistory = [0, 0, 0, 0, 0, 0, 0];
                for (let b = 0; b < size; b++) {
                    if (get(a, b) === runColor) {
                        runLen++;
                        if (runLen === 5) result += N1;
                        else if (runLen > 5) result++;
                    } else {
                        this.finderPenaltyAddHistory(runLen, runHistory);
                        if (!runColor) result += this.finderPenaltyCountPatterns(runHistory) * N3;
                        runColor = get(a, b);
                        runLen = 1;
                    }
                }
                result += this.finderPenaltyTerminateAndCount(runColor, runLen, runHistory) * N3;
            }
        };
        line((y, x) => this.modules[y][x]);
        line((x, y) => this.modules[y][x]);
        for (let y = 0; y < size - 1; y++) {
            for (let x = 0; x < size - 1; x++) {
                const c = this.modules[y][x];
                if (c === this.modules[y][x + 1] && c === this.modules[y + 1][x] && c === this.modules[y + 1][x + 1]) result += N2;
            }
        }
        let dark = 0;
        for (const row of this.modules) dark = row.reduce((s, c) => s + (c ? 1 : 0), dark);
        const total = size * size;
        const k = Math.ceil(Math.abs(dark * 20 - total * 10) / total) - 1;
        result += k * N4;
        return result;
    }

    getAlignmentPatternPositions() {
        if (this.version === 1) return [];
        const numAlign = Math.floor(this.version / 7) + 2;
        const step = this.version === 32 ? 26 : Math.ceil((this.version * 4 + 4) / (numAlign * 2 - 2)) * 2;
        const result = [6];
        for (let pos = this.size - 7; result.length < numAlign; pos -= step) result.splice(1, 0, pos);
        return result;
    }

    finderPenaltyCountPatterns(runHistory) {
        const n = runHistory[1];
        const core = n > 0 && runHistory[2] === n && runHistory[3] === n * 3 && runHistory[4] === n && runHistory[5] === n;
        return (core && runHistory[0] >= n * 4 && runHistory[6] >= n ? 1 : 0)
            + (core && runHistory[6] >= n * 4 && runHistory[0] >= n ? 1 : 0);
    }

    finderPenaltyTerminateAndCount(currentRunColor, currentRunLength, runHistory) {
        if (currentRunColor) {
            this.finderPenaltyAddHistory(currentRunLength, runHistory);
            currentRunLength = 0;
        }
        currentRunLength += this.size;
        this.finderPenaltyAddHistory(currentRunLength, runHistory);
        return this.finderPenaltyCountPatterns(runHistory);
    }

    finderPenaltyAddHistory(currentRunLength, runHistory) {
        if (runHistory[0] === 0) currentRunLength += this.size;
        runHistory.pop();
        runHistory.unshift(currentRunLength);
    }
}

/** Encodes `text` (UTF-8, byte mode, ECC M) and returns a QrCode. */
function encodeText(text) {
    const bytes = Array.from(Buffer.from(String(text), 'utf8'));
    let version;
    let dataUsedBits;
    for (version = 1; version <= 40; version++) {
        const ccBits = version <= 9 ? 8 : 16;
        dataUsedBits = 4 + ccBits + bytes.length * 8;
        if (dataUsedBits <= getNumDataCodewords(version) * 8) break;
    }
    if (version > 40) throw new Error('QR: data too long');

    const bb = [];
    const append = (val, len) => { for (let i = len - 1; i >= 0; i--) bb.push((val >>> i) & 1); };
    append(0x4, 4); // byte mode
    append(bytes.length, version <= 9 ? 8 : 16);
    for (const b of bytes) append(b, 8);

    const capacityBits = getNumDataCodewords(version) * 8;
    append(0, Math.min(4, capacityBits - bb.length));
    append(0, (8 - (bb.length % 8)) % 8);
    for (let pad = 0xec; bb.length < capacityBits; pad ^= 0xec ^ 0x11) append(pad, 8);

    const dataCodewords = [];
    for (let i = 0; i < bb.length; i += 8) {
        dataCodewords.push(parseInt(bb.slice(i, i + 8).join(''), 2));
    }
    return new QrCode(version, -1, dataCodewords);
}

/**
 * Returns an inline `<svg>` string for `text`. One `<path>`, crisp edges,
 * `currentColor` for dark modules on a white quiet zone so it scans in dark themes too.
 */
function qrSvg(text, { border = 2, title = '' } = {}) {
    const qr = encodeText(text);
    const dim = qr.size + border * 2;
    const parts = [];
    for (let y = 0; y < qr.size; y++) {
        for (let x = 0; x < qr.size; x++) {
            if (qr.modules[y][x]) parts.push(`M${x + border},${y + border}h1v1h-1z`);
        }
    }
    const titleTag = title ? `<title>${String(title).replace(/[<&>"]/g, '')}</title>` : '';
    return `<svg class="qr-code" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${dim} ${dim}" shape-rendering="crispEdges" role="img"${title ? ` aria-label="${String(title).replace(/"/g, '')}"` : ' aria-hidden="true"'}>${titleTag}<rect width="100%" height="100%" fill="#fff"/><path d="${parts.join('')}" fill="#0A0E27"/></svg>`;
}

module.exports = { encodeText, qrSvg };
