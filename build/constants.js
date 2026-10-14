const SITE_URL = "https://bluetoothfinderapp.com/";
const DEFAULT_LANGUAGE = 'en';

/**
 * App Store: https://apps.apple.com/us/app/bluetooth-finder/id6756609274
 * (short id-URL is locale-agnostic and still valid.)
 */
const APP_ID = '6756609274';
const APP_STORE_URL = `https://apps.apple.com/app/id${APP_ID}`;

const LANGUAGES = [
    DEFAULT_LANGUAGE,
    'es',
    'de',
    'fr',
    'it',
    'jp',
    'ko',
    'nl',
    'pl',
    'pt',
    'ro',
    'ru',
    'th',
    'tr',
    'uk',
    'vi',
];

/** BCP 47 hreflang values (URL path stays short: jp, cn, …). */
const HREFLANG_BY_CODE = {
    jp: 'ja',
    cn: 'zh-CN'
};

const URLS = LANGUAGES.map((code) => ({
    code,
    hreflang: HREFLANG_BY_CODE[code] || code,
    url: code === DEFAULT_LANGUAGE ? SITE_URL : `${SITE_URL}${code}/`
}));

const ADDITIONAL_URLS = [
    `${SITE_URL}llms.txt`
];

/**
 * Guide locales: each has its own data file and URL path.
 * EN guides live at /guides/<slug>/, ES at /es/guias/<slug>/, DE at /de/ratgeber/<slug>/, FR at /fr/guides/<slug>/, IT at /it/guide/<slug>/, JP at /jp/guides/<slug>/, KO at /ko/guides/<slug>/, NL at /nl/gidsen/<slug>/, PL at /pl/poradniki/<slug>/, PT (pt-BR) at /pt/guias/<slug>/, RO at /ro/ghiduri/<slug>/, RU at /ru/instrukcii/<slug>/, TH at /th/guides/<slug>/, TR at /tr/rehberler/<slug>/, UK at /uk/instrukciyi/<slug>/, VI at /vi/huong-dan/<slug>/.
 * Every non-EN guide carries `en_slug` so the versions can be linked with hreflang.
 */
const GUIDE_LOCALES = [
    { code: 'en', hreflang: 'en', dataFile: 'guides-en.json', path: 'guides' },
    { code: 'es', hreflang: 'es', dataFile: 'guides-es.json', path: 'es/guias' },
    { code: 'de', hreflang: 'de', dataFile: 'guides-de.json', path: 'de/ratgeber' },
    { code: 'fr', hreflang: 'fr', dataFile: 'guides-fr.json', path: 'fr/guides' },
    { code: 'it', hreflang: 'it', dataFile: 'guides-it.json', path: 'it/guide' },
    { code: 'jp', hreflang: 'ja', dataFile: 'guides-jp.json', path: 'jp/guides' },
    { code: 'ko', hreflang: 'ko', dataFile: 'guides-ko.json', path: 'ko/guides' },
    { code: 'nl', hreflang: 'nl', dataFile: 'guides-nl.json', path: 'nl/gidsen' },
    { code: 'pl', hreflang: 'pl', dataFile: 'guides-pl.json', path: 'pl/poradniki' },
    { code: 'pt', hreflang: 'pt', dataFile: 'guides-pt.json', path: 'pt/guias' },
    { code: 'ro', hreflang: 'ro', dataFile: 'guides-ro.json', path: 'ro/ghiduri' },
    { code: 'ru', hreflang: 'ru', dataFile: 'guides-ru.json', path: 'ru/instrukcii' },
    { code: 'th', hreflang: 'th', dataFile: 'guides-th.json', path: 'th/guides' },
    { code: 'tr', hreflang: 'tr', dataFile: 'guides-tr.json', path: 'tr/rehberler' },
    { code: 'uk', hreflang: 'uk', dataFile: 'guides-uk.json', path: 'uk/instrukciyi' },
    { code: 'vi', hreflang: 'vi', dataFile: 'guides-vi.json', path: 'vi/huong-dan' },
];

/** English guide slugs (kept for backwards compatibility). */
const GUIDE_SLUGS = require('./guides-en.json').guides.map(({ slug }) => slug);

/**
 * Hreflang groups for guide pages: one entry per EN guide (plus the hubs),
 * each listing the URL of every locale version. Used by sitemap.js.
 */
const GUIDE_GROUPS = (() => {
    const en = require('./guides-en.json').guides;
    const hubs = {};
    for (const loc of GUIDE_LOCALES) {
        hubs[loc.code] = `${SITE_URL}${loc.path}/`;
    }
    // en_slug → { localeCode: localizedSlug } for every non-EN locale.
    const bySlug = {};
    for (const loc of GUIDE_LOCALES.filter((l) => l.code !== 'en')) {
        for (const g of require(`./${loc.dataFile}`).guides) {
            if (g.en_slug) {
                (bySlug[g.en_slug] = bySlug[g.en_slug] || {})[loc.code] = g.slug;
            }
        }
    }
    const groups = [hubs];
    for (const g of en) {
        const group = { en: `${SITE_URL}guides/${g.slug}/` };
        for (const loc of GUIDE_LOCALES.filter((l) => l.code !== 'en')) {
            const slug = bySlug[g.slug]?.[loc.code];
            if (slug) {
                group[loc.code] = `${SITE_URL}${loc.path}/${slug}/`;
            }
        }
        groups.push(group);
    }
    return groups;
})();

/** All guide URLs, every locale (sitemap, IndexNow, urls.txt). */
const GUIDE_URLS = GUIDE_GROUPS.flatMap((group) => Object.values(group));

// Expected JSON-LD types that should be present on each generated page.
// Keep this list in sync with `build/template.html` structured data scripts.
// Note: MobileApplication is a subtype of SoftwareApplication and is acceptable
const EXPECTED_JSON_LD_TYPES = [
    'MobileApplication', // or 'SoftwareApplication' - MobileApplication is more specific
    'Organization',
    'WebSite',
    'HowTo',
    'FAQPage',
    'BreadcrumbList'
];

const INDEX_NOW_KEY = 'ss4jhZbfts8Rc6oerEe3DdIo';

// https://www.indexnow.org/searchengines.json
const INDEX_NOW_ENGINES = [
    'indexnow.yep.com',
    'search.seznam.cz',
    'searchadvisor.naver.com',
    'indexnow.amazonbot.amazon',
    'api.indexnow.org',
    'yandex.com',
    'bing.com'
];

module.exports = {
    SITE_URL,
    URLS,
    DEFAULT_LANGUAGE,
    LANGUAGES,
    EXPECTED_JSON_LD_TYPES,
    INDEX_NOW_KEY,
    INDEX_NOW_ENGINES,
    ADDITIONAL_URLS,
    GUIDE_SLUGS,
    GUIDE_URLS,
    GUIDE_LOCALES,
    GUIDE_GROUPS,
    APP_ID,
    APP_STORE_URL,
};