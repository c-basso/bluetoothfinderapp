/**
 * Google Search Console export → gsc/ (git-ignored).
 *
 * Usage: node build/gsc-report.js [days=90]                 → last N days into gsc/
 *        node build/gsc-report.js 2026-10-15 2026-11-12     → fixed range into gsc/2026-10-15_2026-11-12/
 *        npm run gsc -- 2026-10-15 2026-11-12
 * Fixed ranges go to their own folder so before/after exports can be compared side by side.
 * Auth: service_account.json (the service account must be a user of the Search Console property,
 *       and the Search Console API must be enabled in its GCP project).
 * Output (CSV + JSON, overwritten on each run):
 *   gsc/queries.csv         query, clicks, impressions, ctr, position
 *   gsc/pages.csv           page, clicks, impressions, ctr, position
 *   gsc/query-page.csv      query, page, … (which page ranks for which query)
 *   gsc/countries.csv       country, …
 *   gsc/meta.json           property, date range, row counts
 */
const fs = require('fs');
const path = require('path');
const { google } = require('googleapis');
const { SITE_URL } = require('./constants');

const ROOT = path.join(__dirname, '..');
const GSC_DIR = path.join(ROOT, 'gsc');
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;
const KEY_PATH = path.join(ROOT, 'service_account.json');
const SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly';
const SITE_HOST = new URL(SITE_URL).hostname;
const PROPERTY_CANDIDATES = [`sc-domain:${SITE_HOST}`, SITE_URL];
const ROW_LIMIT = 25000;

function isoDate(d) {
    return d.toISOString().slice(0, 10);
}

function toCsv(header, rows) {
    const esc = (v) => {
        const s = v == null ? '' : String(v);
        return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
    };
    return [header.join(','), ...rows.map((r) => r.map(esc).join(','))].join('\n') + '\n';
}

async function pickProperty(sc) {
    const { data } = await sc.sites.list();
    const available = (data.siteEntry || []).map((s) => s.siteUrl);
    const found = PROPERTY_CANDIDATES.find((p) => available.includes(p));
    if (!found) {
        throw new Error(
            `Service account has no access to ${PROPERTY_CANDIDATES.join(' / ')}. Visible properties: ${available.join(', ') || 'none'}`
        );
    }
    return found;
}

async function query(sc, siteUrl, startDate, endDate, dimensions) {
    const rows = [];
    for (let startRow = 0; ; startRow += ROW_LIMIT) {
        const { data } = await sc.searchanalytics.query({
            siteUrl,
            requestBody: { startDate, endDate, dimensions, rowLimit: ROW_LIMIT, startRow, dataState: 'all' },
        });
        const batch = data.rows || [];
        rows.push(...batch);
        if (batch.length < ROW_LIMIT) break;
    }
    return rows.map((r) => [
        ...r.keys,
        r.clicks,
        r.impressions,
        Math.round(r.ctr * 10000) / 100,
        Math.round(r.position * 10) / 10,
    ]);
}

async function main() {
    const [arg1, arg2] = process.argv.slice(2);
    const fixedRange = DATE_RE.test(arg1 || '') && DATE_RE.test(arg2 || '');
    if (DATE_RE.test(arg1 || '') !== fixedRange) {
        throw new Error('Pass both dates: node build/gsc-report.js YYYY-MM-DD YYYY-MM-DD');
    }
    if (fixedRange && arg1 > arg2) {
        throw new Error(`Start date ${arg1} is after end date ${arg2}`);
    }
    const days = fixedRange ? null : Number(arg1) || 90;
    if (!fs.existsSync(KEY_PATH)) throw new Error(`Missing ${KEY_PATH}`);
    const key = require(KEY_PATH);
    const auth = new google.auth.JWT({ email: key.client_email, key: key.private_key, scopes: [SCOPE] });
    await auth.authorize();
    const sc = google.searchconsole({ version: 'v1', auth });

    const siteUrl = await pickProperty(sc);
    let startDate;
    let endDate;
    if (fixedRange) {
        [startDate, endDate] = [arg1, arg2];
    } else {
        const end = new Date();
        end.setDate(end.getDate() - 2); // GSC data lags ~2 days
        const start = new Date(end);
        start.setDate(start.getDate() - days + 1);
        [startDate, endDate] = [isoDate(start), isoDate(end)];
    }
    const OUT_DIR = fixedRange ? path.join(GSC_DIR, `${startDate}_${endDate}`) : GSC_DIR;
    console.log(`📊 ${siteUrl}  ${startDate} → ${endDate}  →  ${path.relative(ROOT, OUT_DIR)}/`);

    fs.mkdirSync(OUT_DIR, { recursive: true });
    const metrics = ['clicks', 'impressions', 'ctr_%', 'position'];
    const reports = {
        queries: ['query'],
        pages: ['page'],
        'query-page': ['query', 'page'],
        countries: ['country'],
    };
    const counts = {};
    for (const [name, dims] of Object.entries(reports)) {
        const rows = await query(sc, siteUrl, startDate, endDate, dims);
        rows.sort((a, b) => b[dims.length + 1] - a[dims.length + 1]); // by impressions
        fs.writeFileSync(path.join(OUT_DIR, `${name}.csv`), toCsv([...dims, ...metrics], rows));
        counts[name] = rows.length;
        console.log(`  ✅ ${path.relative(ROOT, OUT_DIR)}/${name}.csv  ${rows.length} rows`);
    }
    fs.writeFileSync(
        path.join(OUT_DIR, 'meta.json'),
        JSON.stringify({ siteUrl, startDate, endDate, generatedAt: new Date().toISOString(), counts }, null, 2) + '\n'
    );
}

main().catch((err) => {
    console.error('❌', err.message || err);
    process.exit(1);
});
