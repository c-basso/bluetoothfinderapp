const fs = require('fs');
const path = require('path');

const {
    URLS,
    SITE_URL,
    DEFAULT_LANGUAGE,
    LANGUAGES,
    APP_ID,
    APP_STORE_URL,
} = require('./constants');

const ROOT_DIR = path.join(__dirname, '..');
const TEMPLATE_PATH = path.join(__dirname, 'template.html');
const URLS_PATH = path.join(ROOT_DIR, 'urls.txt');
const LLMS_PATH = path.join(ROOT_DIR, 'llms.txt');
const SITE_CSS_PATH = path.join(ROOT_DIR, 'site.css');
const WEBMANIFEST_PATH = path.join(ROOT_DIR, 'site.webmanifest');

/** Placeholder in `*.json` for App Store product URL; replaced in `applyAppStoreFromConstants`. */
const APP_STORE_PLACEHOLDER = '__APP_STORE_URL__';

const BUILD_TIMESTAMP = Date.now();
const BUILD_DATE_ISO = new Date(BUILD_TIMESTAMP).toISOString().slice(0, 10);
const CURRENT_YEAR = new Date().getFullYear();

const DEFAULT_SITE_NAME = 'Bluetooth Finder';
const DEFAULT_OG_LOGO = `${SITE_URL}img/logo.webp`;

/**
 * `lang` = hreflang for the alternate link template
 * (`{{#each meta.alternate_languages as |lang|}}` + `{{lang.lang}}`, `{{lang.url}}`).
 */
const ALTERNATE_LANGUAGE_LINKS = URLS.map(({ code, hreflang, url }) => ({
    code,
    hreflang,
    lang: hreflang,
    url,
}));

const HTML_LANG_BY_CODE = {
    cn: 'zh-CN',
    jp: 'ja',
};

const OG_LOCALE_BY_LANGUAGE = {
    en: 'en_US',
    ru: 'ru_RU',
    es: 'es_ES',
    fr: 'fr_FR',
    de: 'de_DE',
    it: 'it_IT',
    pt: 'pt_PT',
    cn: 'zh_CN',
    jp: 'ja_JP',
    ko: 'ko_KR',
    nl: 'nl_NL',
    pl: 'pl_PL',
    ro: 'ro_RO',
    th: 'th_TH',
    tr: 'tr_TR',
    uk: 'uk_UA',
    vi: 'vi_VN',
};

const CANONICAL_URL_BY_LANGUAGE = new Map(URLS.map(({ code, url }) => [code, url]));

/** Styles for `/site.css` live at repo root; template links with `?v={{meta.version}}`. */
function assertSiteCssExists() {
    if (!fs.existsSync(SITE_CSS_PATH)) {
        throw new Error(`Missing ${SITE_CSS_PATH} (create or restore site.css next to index.html)`);
    }
    console.log(`✅ site.css present: ${SITE_CSS_PATH}`);
    console.log();
}

function syncWebManifest() {
    if (!fs.existsSync(WEBMANIFEST_PATH)) {
        return;
    }
    const m = JSON.parse(fs.readFileSync(WEBMANIFEST_PATH, 'utf8'));
    const rel = Array.isArray(m.related_applications) ? m.related_applications[0] : null;
    if (rel) {
        rel.url = APP_STORE_URL;
        rel.id = String(APP_ID);
    }
    fs.writeFileSync(WEBMANIFEST_PATH, `${JSON.stringify(m, null, 2)}\n`, 'utf8');
    console.log(`✅ site.webmanifest → App Store id ${APP_ID}`);
    console.log();
}

function writeUrlsFile() {
    fs.writeFileSync(URLS_PATH, URLS.map(({ url }) => url).join('\n'), 'utf8');
    console.log('✅ Successfully built urls.txt file');
    console.log(`📁 Output saved to: ${URLS_PATH}`);
    console.log();
}

function absoluteSiteUrl(maybe) {
    if (maybe == null || maybe === '') {
        return SITE_URL;
    }
    const s = String(maybe);
    if (/^https?:\/\//i.test(s)) {
        return s;
    }
    return `${SITE_URL.replace(/\/?$/, '/')}${s.replace(/^\//, '')}`;
}

function writeLlmsFile(defaultLocaleData) {
    const appName = defaultLocaleData.header?.app_name || DEFAULT_SITE_NAME;
    const nFeatures = Array.isArray(defaultLocaleData.features?.items) ? defaultLocaleData.features.items.length : 0;
    const featureLine = nFeatures
        ? `${nFeatures} in-page feature highlights (scan, hot & cold, proximity %, device details, and more)`
        : 'Real-time scan, hot & cold guidance, proximity %, and device information';

    const version = defaultLocaleData.seo?.structured_data?.software_application?.softwareVersion;

    const lines = [
        `# ${appName}`,
        '',
        `> ${stripHtml(defaultLocaleData.meta?.description)}`,
        '',
        '## Main sections',
        `- [Home](${SITE_URL}): Bluetooth device finder app — landing, features, and download`,
        `- [FAQ](${SITE_URL}#faq): Questions about the app, accuracy, and supported devices`,
        `- [Localized pages](${SITE_URL}): Hreflang landing pages for supported markets`,
        '',
        '## Key facts',
        `- Product type: iOS app to find lost or nearby Bluetooth devices (e.g. AirPods, smartwatches, headphones)`,
        `- App Store: ${APP_STORE_URL} (id ${APP_ID})`,
        `- ${featureLine}`,
        `- OS: ${defaultLocaleData.app_info?.compatibility || 'Requires iOS 17.1 or later'}`,
        `- App size: ${defaultLocaleData.app_info?.file_size || '—'}`,
        `- Age rating: ${defaultLocaleData.app_info?.age_rating || '—'}`,
        `- Software version: ${version || '—'}`,
        `- Supported page languages: ${LANGUAGES.length}`,
        `- Last build date: ${BUILD_DATE_ISO}`,
        '',
        '## How it works',
        '1. Install from the App Store and allow Bluetooth when prompted.',
        '2. Scan for devices and pick the one you are looking for.',
        '3. Move using hot & cold cues and the proximity percentage until you are next to the device.',
        '',
        '## Language pages',
        ...ALTERNATE_LANGUAGE_LINKS.map(({ hreflang, url }) => `- [${hreflang}](${url})`),
        '',
        '## Contact and policies',
        `- Website: ${SITE_URL}`,
        defaultLocaleData.app_info?.developer ? `- Developer: ${defaultLocaleData.app_info.developer}` : null,
        `- Privacy: ${absoluteSiteUrl(defaultLocaleData.footer?.privacy_url)}`,
        `- Terms: ${absoluteSiteUrl(defaultLocaleData.footer?.terms_url)}`,
    ].filter(Boolean);

    fs.writeFileSync(LLMS_PATH, `${lines.join('\n')}\n`, 'utf8');
    console.log('✅ Successfully built llms.txt file');
    console.log(`📁 Output saved to: ${LLMS_PATH}`);
    console.log();
}

function ensureDirectoryExists(dirPath) {
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }
}

function readJsonFile(filePath) {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function stripHtml(value) {
    if (typeof value !== 'string') {
        return value;
    }
    return value
        .replace(/<[^>]*>/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
}

function getOutputDirectory(lang) {
    return path.join(ROOT_DIR, lang === DEFAULT_LANGUAGE ? '.' : lang);
}

function getJsonPath(lang) {
    return path.join(__dirname, `${lang}.json`);
}

function getOutputPath(lang) {
    return path.join(getOutputDirectory(lang), 'index.html');
}

function getMissingTranslationFiles() {
    return LANGUAGES.map((lang) => ({ lang, jsonPath: getJsonPath(lang) })).filter(({ jsonPath }) => !fs.existsSync(jsonPath));
}

/**
 * Per-locale `site_preview.png` under `/{lang}/` if present, else default at site root.
 */
function getPreviewImageUrl(lang) {
    const relative = lang === DEFAULT_LANGUAGE ? 'site_preview.png' : `${lang}/site_preview.png`;
    const absolute = path.join(ROOT_DIR, relative);
    const usePath = fs.existsSync(absolute) ? relative : 'site_preview.png';
    return `${SITE_URL}${usePath}`;
}

function getCanonicalUrl(meta, lang) {
    return (
        meta.canonical ||
        meta.alternate_url ||
        meta.altenate_url ||
        CANONICAL_URL_BY_LANGUAGE.get(lang) ||
        SITE_URL
    );
}

function removeAlternateMetaFields(meta) {
    for (const key of Object.keys(meta)) {
        if (key.startsWith('alternate_')) {
            delete meta[key];
        }
    }
}

function normalizeMeta(data, lang) {
    data.meta = data.meta || {};
    removeAlternateMetaFields(data.meta);

    const canonicalUrl = getCanonicalUrl(data.meta, lang);
    const previewUrl = getPreviewImageUrl(lang);

    data.meta.lang = data.meta.lang || lang;
    data.meta.html_lang = data.meta.html_lang || HTML_LANG_BY_CODE[lang] || data.meta.lang;
    data.meta.version = BUILD_TIMESTAMP;
    data.meta.canonical = canonicalUrl;
    data.meta.alternate_default = SITE_URL;
    data.meta.alternate_languages = ALTERNATE_LANGUAGE_LINKS;
    data.meta.og_url = canonicalUrl;
    data.meta.twitter_url = canonicalUrl;
    data.meta.og_image = previewUrl;
    data.meta.twitter_image = previewUrl;
    data.meta.og_logo = data.meta.og_logo || DEFAULT_OG_LOGO;
    data.meta.og_site_name = data.meta.og_site_name || data.header?.app_name || DEFAULT_SITE_NAME;
    data.meta.og_locale = data.meta.og_locale || OG_LOCALE_BY_LANGUAGE[lang] || OG_LOCALE_BY_LANGUAGE.en;
    data.meta.last_updated_iso = BUILD_DATE_ISO;
}

function normalizeFooter(data) {
    if (typeof data.footer?.copyright === 'string') {
        data.footer.copyright = data.footer.copyright.replace(/\{year\}/g, String(CURRENT_YEAR));
    }
}

function ensureSeoShape(data) {
    data.seo = data.seo || {};
    data.seo.structured_data = data.seo.structured_data || {};
}

/**
 * `meta.app_store_id`, `header.download_url`, `final_cta.cta_url` and
 * any `__APP_STORE_URL__` in strings come from constants, not from JSON.
 */
function applyAppStoreFromConstants(data) {
    data.meta = data.meta || {};
    data.meta.app_store_id = String(APP_ID);
    data.header = data.header || {};
    data.header.download_url = APP_STORE_URL;
    if (data.final_cta) {
        data.final_cta.cta_url = APP_STORE_URL;
    }

    function visit(node) {
        if (Array.isArray(node)) {
            for (const el of node) {
                visit(el);
            }
            return;
        }
        if (node && typeof node === 'object') {
            for (const k of Object.keys(node)) {
                const v = node[k];
                if (typeof v === 'string' && v.includes(APP_STORE_PLACEHOLDER)) {
                    node[k] = v.split(APP_STORE_PLACEHOLDER).join(APP_STORE_URL);
                } else {
                    visit(v);
                }
            }
        }
    }
    visit(data);
}

/** Visible footer date; derived from build time (no manual edits in JSON). */
function localeTagForIntl(lang) {
    const og = OG_LOCALE_BY_LANGUAGE[lang];
    if (og) {
        return og.replace('_', '-');
    }
    return lang;
}

function setSeoLastUpdatedFromBuild(data, lang) {
    const d = new Date(BUILD_TIMESTAMP);
    try {
        data.seo.last_updated = d.toLocaleDateString(localeTagForIntl(lang), {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        });
    } catch {
        data.seo.last_updated = BUILD_DATE_ISO;
    }
}

function buildOrganizationStructuredData(data) {
    if (data.seo.structured_data.organization) {
        return;
    }
    data.seo.structured_data.organization = {
        '@context': 'https://schema.org',
        '@type': 'Organization',
        name: data.meta?.og_site_name || data.header?.app_name || DEFAULT_SITE_NAME,
        description: stripHtml(data.meta?.description),
        url: data.meta?.canonical || SITE_URL,
        logo: data.meta?.og_logo || DEFAULT_OG_LOGO,
    };
}

function buildSoftwareApplicationStructuredData(data) {
    const app = data.seo.structured_data.software_application;
    if (!app || typeof app !== 'object') {
        return;
    }
    app.url = data.meta?.canonical;
    app.downloadUrl = data.header?.download_url;
    if (app.offers && typeof app.offers === 'object') {
        app.offers.url = APP_STORE_URL;
    }
    delete app.aggregateRating;
    app.dateModified = BUILD_DATE_ISO;
}

function buildWebsiteStructuredData(data) {
    const fallbackName = data.meta?.og_site_name || data.header?.app_name || DEFAULT_SITE_NAME;

    if (!data.seo.structured_data.website) {
        data.seo.structured_data.website = {
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: fallbackName,
            description: stripHtml(data.meta?.description),
            inLanguage: data.meta?.lang,
            url: data.meta?.canonical || SITE_URL,
        };
        return;
    }
    if (typeof data.seo.structured_data.website === 'object') {
        const w = data.seo.structured_data.website;
        w.url = data.meta?.canonical;
        w.name = w.name || fallbackName;
        w.description = w.description || stripHtml(data.meta?.description);
        w.inLanguage = w.inLanguage || data.meta?.lang;
        delete w.potentialAction;
    }
}

function buildHowToStructuredData(data) {
    if (!data.seo.structured_data.howto) {
        data.seo.structured_data.howto = {
            '@context': 'https://schema.org',
            '@type': 'HowTo',
            name: stripHtml(data.meta?.title),
            description: stripHtml(data.meta?.description),
        };
    }
    if (typeof data.seo.structured_data.howto !== 'object') {
        return;
    }
    if (Array.isArray(data.how_it_works?.steps)) {
        data.seo.structured_data.howto.step = data.how_it_works.steps.map((s) => ({
            '@type': 'HowToStep',
            name: stripHtml(s?.title),
            text: stripHtml(s?.description),
        }));
    } else if (!data.seo.structured_data.howto.step) {
        data.seo.structured_data.howto.step = [];
    }
    if (!Array.isArray(data.seo.structured_data.howto.step)) {
        data.seo.structured_data.howto.step = [];
    }
    const howtoSteps = data.seo.structured_data.howto.step;
    if (Array.isArray(howtoSteps) && howtoSteps[0] && typeof howtoSteps[0] === 'object') {
        howtoSteps[0].url = APP_STORE_URL;
    }
}

function buildFaqStructuredData(data) {
    const items = Array.isArray(data.faq?.items) ? data.faq.items : Array.isArray(data.seo?.faq) ? data.seo.faq : [];

    if (items.length === 0) {
        if (!data.seo.structured_data.faqpage) {
            data.seo.structured_data.faqpage = {
                '@context': 'https://schema.org',
                '@type': 'FAQPage',
                mainEntity: [],
            };
        }
        return;
    }

    data.seo.structured_data.faqpage = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: items.map((f) => ({
            '@type': 'Question',
            name: stripHtml(f?.question),
            acceptedAnswer: {
                '@type': 'Answer',
                text: stripHtml(f?.answer),
            },
        })),
    };
}

function buildBreadcrumbStructuredData(data) {
    data.seo.breadcrumb_home = data.seo.breadcrumb_home || data.meta?.title || 'Home';
    data.seo.structured_data.breadcrumb_list = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        itemListElement: [
            {
                '@type': 'ListItem',
                position: 1,
                name: data.seo.breadcrumb_home,
                item: data.meta?.canonical,
            },
        ],
    };
}

function preparePageData(data, lang) {
    normalizeMeta(data, lang);
    normalizeFooter(data);
    ensureSeoShape(data);
    applyAppStoreFromConstants(data);
    setSeoLastUpdatedFromBuild(data, lang);
    buildOrganizationStructuredData(data);
    buildSoftwareApplicationStructuredData(data);
    buildWebsiteStructuredData(data);
    buildHowToStructuredData(data);
    buildFaqStructuredData(data);
    buildBreadcrumbStructuredData(data);
    return data;
}

function getValue(obj, keyPath) {
    return keyPath.split('.').reduce((value, key) => {
        if (value && typeof value === 'object' && key in value) {
            return value[key];
        }
        return undefined;
    }, obj);
}

/**
 * Resolves `section.items` in nested #each: outer `section` is a direct context key.
 */
function getValueFromContext(context, keyPath) {
    let v = getValue(context, keyPath);
    if (v !== undefined) {
        return v;
    }
    if (!keyPath.includes('.')) {
        return undefined;
    }
    const parts = keyPath.split('.');
    const first = parts[0];
    if (first in context) {
        const firstVal = context[first];
        if (firstVal && typeof firstVal === 'object' && firstVal !== null) {
            const rest = parts.slice(1).join('.');
            if (rest) {
                const inner = getValue(firstVal, rest);
                if (inner !== undefined) {
                    return inner;
                }
            } else {
                return firstVal;
            }
        }
    }
    return undefined;
}

function warnForTemplateIssue(lang, message) {
    console.warn(`Warning [${lang}]: ${message}`);
}

const LOOP_PLACEHOLDER_ROOTS = new Set(['item', 'feature', 'section', 'lang', 'screenshot', 'fact', 'row', 'faq']);

function shouldWarnMissingVar(pathExpression) {
    if (pathExpression.startsWith('seo.structured_data.')) {
        return false;
    }
    const root = pathExpression.split('.')[0];
    if (LOOP_PLACEHOLDER_ROOTS.has(root)) {
        return false;
    }
    return true;
}

function escapeHtmlAttr(value) {
    if (typeof value !== 'string') {
        return value;
    }
    return value
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

function applyFilters(value, filters, rawKey, lang) {
    let out = value;
    for (const f of filters) {
        if (f === 'json') {
            out = JSON.stringify(out);
        } else if (f === 'html_attr') {
            out = escapeHtmlAttr(String(out));
        } else {
            warnForTemplateIssue(lang, `Unknown filter "${f}" in ${rawKey}`);
        }
    }
    return out;
}

function replaceVariables(template, context, lang) {
    return template.replace(/\{\{([^}]+)\}\}/g, (match, key) => {
        const rawKey = key.trim();
        if (rawKey.startsWith('#each') || rawKey === '/each') {
            return match;
        }
        const [pathExpression, ...filters] = rawKey
            .split('|')
            .map((s) => s.trim())
            .filter(Boolean);
        const value = getValueFromContext(context, pathExpression);
        if (value === undefined) {
            if (shouldWarnMissingVar(pathExpression)) {
                warnForTemplateIssue(lang, `Variable ${pathExpression} not found in data`);
            }
            return match;
        }
        return applyFilters(value, filters, rawKey, lang);
    });
}

function cleanupJsonArtifacts(s) {
    return s
        .replace(/,\s*\n[\s\n]*\]/g, '\n            ]')
        .replace(/,\s*\]/g, ']');
}

function processEachBlocks(template, context, lang) {
    const eachPattern = /\{\{#each\s+([^\s]+)\s+as\s+\|([^|]+)\|\}\}([\s\S]*?)\{\{\/each\}\}/;
    let result = template;
    let match = result.match(eachPattern);
    while (match) {
        const [full, arrayPathRaw, varNameRaw, block] = match;
        const arrayPath = arrayPathRaw.trim();
        const varName = varNameRaw.trim();
        const array = getValueFromContext(context, arrayPath);
        if (!Array.isArray(array)) {
            if (array != null) {
                warnForTemplateIssue(lang, `${arrayPath} is not an array (got ${typeof array})`);
            } else if (!arrayPath.includes('.')) {
                warnForTemplateIssue(lang, `${arrayPath} is not an array or not found`);
            }
            result = result.replace(full, '');
            match = result.match(eachPattern);
            continue;
        }
        const rendered = cleanupJsonArtifacts(
            array
                .map((item) => {
                    const ctx = { ...context, [varName]: item };
                    return replaceVariables(processEachBlocks(block, ctx, lang), ctx, lang);
                })
                .join(''),
        );
        result = result.replace(full, rendered);
        match = result.match(eachPattern);
    }
    return result;
}

function renderTemplate(template, data, lang) {
    return cleanupJsonArtifacts(
        replaceVariables(processEachBlocks(template, data, lang), data, lang),
    );
}

function buildPage(template, lang) {
    const outDir = getOutputDirectory(lang);
    const outPath = getOutputPath(lang);
    const jsonPath = getJsonPath(lang);
    ensureDirectoryExists(outDir);
    const data = preparePageData(readJsonFile(jsonPath), lang);
    fs.writeFileSync(outPath, renderTemplate(template, data, lang), 'utf8');
    console.log(`✅ Successfully built index.html from template and ${lang}.json`);
    console.log(`📁 Output saved to: ${outPath}`);
}

function main() {
    const missing = getMissingTranslationFiles();
    if (missing.length > 0) {
        console.error(
            `❌ Missing translation files: ${missing
                .map((m) => `${m.lang}: ${path.basename(m.jsonPath)}`)
                .join(', ')}`,
        );
        process.exit(1);
    }
    assertSiteCssExists();
    syncWebManifest();
    const template = fs.readFileSync(TEMPLATE_PATH, 'utf8');
    const defaultData = preparePageData(readJsonFile(getJsonPath(DEFAULT_LANGUAGE)), DEFAULT_LANGUAGE);
    writeUrlsFile();
    writeLlmsFile(defaultData);
    for (const lang of LANGUAGES) {
        try {
            buildPage(template, lang);
        } catch (e) {
            console.error(`❌ Error building ${lang}:`, e.message);
            process.exit(1);
        }
    }
}

main();
