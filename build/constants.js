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
    APP_ID,
    APP_STORE_URL,
};