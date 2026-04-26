# Ukrainian copy for build/uk.json (keys match pl.json top-level).
import json
from pathlib import Path

B = Path(__file__).parent
_SEO = json.loads((B / "uk_seo.json").read_text(encoding="utf-8"))

UK = {
    "meta": {
        "lang": "uk",
        "title": "Bluetooth Finder — знайдіть втрачений Bluetooth | AirPods, годинник, навушники",
        "description": "Bluetooth Finder допомагає знайти ввімкнені поруч AirPods, годинник, навушники, колонки Bluetooth. «Гаряча–холодна» в чотири кроки (холодно, тепло, гаряче, дуже гаряче) і відсоток наближення. Потрібен iOS 17.1+; завантаження в App Store зазвичай безкоштовне; внутрішні покупки вказані в магазині.",
        "keywords": "знайти bluetooth, втрачені airpods, пошук bluetooth, iPhone, сканер bluetooth, пристрій поруч, колонка bluetooth, годинник, знайти гаджет",
        "author": "Bluetooth Finder",
        "og_url": "https://bluetoothfinderapp.com/uk/",
        "og_title": "Bluetooth Finder — знайдіть пристрій Bluetooth поруч",
        "og_description": "Скан, «гаряча–холодна», відсоток. AirPods, годинник, навушники — якщо в зоні. iOS 17.1+; iPhone; завантаження зазвичай безкоштовно; можливі покупки в додатку.",
        "og_image": "https://bluetoothfinderapp.com/site_preview.png",
        "og_image_alt": "Bluetooth Finder — пошук пристрою",
        "og_image_width": "1140",
        "og_image_height": "599",
        "og_locale": "uk_UA",
        "twitter_url": "https://bluetoothfinderapp.com/uk/",
        "twitter_title": "Bluetooth Finder — швидко знайдіть Bluetooth-гаджет",
        "twitter_description": "AirPods, годинник, колонки. Кроки: холодно, тепло, гаряче, дуже гаряче, і відсоток.",
        "twitter_image": "https://bluetoothfinderapp.com/site_preview.png",
        "twitter_image_alt": "Bluetooth Finder",
        "twitter_image_width": "1140",
        "twitter_image_height": "599",
        "canonical": "https://bluetoothfinderapp.com/uk/",
        "og_type": "website",
        "twitter_card": "summary_large_image",
        "theme_color": "#0A0E27",
        "apple_mobile_web_app_status_bar_style": "default",
    },
    "header": {
        "application_name": "Bluetooth Finder — пошук пристроїв Bluetooth",
        "app_name_suffix": "Пошук пристроїв Bluetooth",
        "logo_alt": "Логотип Bluetooth Finder: AirPods, годинник, навушники",
        "app_name": "Bluetooth Finder",
        "title": "Bluetooth Finder",
        "tagline": "Поверніть забуте простіше.",
        "download_text": "Завантажити в App Store",
        "download_aria_label": "Завантажити Bluetooth Finder в App Store",
        "download_img_alt": "Завантажити Bluetooth Finder в App Store",
    },
    "screenshots": {
        "items": [
            {"src": "/img/1_cover_12_framed.webp", "alt": "Bluetooth Finder — головна"},
            {"src": "/img/2_scan_12_framed.webp", "alt": "Bluetooth Finder — скан"},
            {"src": "/img/3_track_12_framed.webp", "alt": "Bluetooth Finder — трекінг"},
            {"src": "/img/4_info_12_framed.webp", "alt": "Bluetooth Finder — інформація"},
        ],
    },
    "content": {
        "summary_label": "Коротко",
        "summary_tldr": "Bluetooth Finder — додаток на iPhone (iOS) для AirPods, годинника, колонки, інших увімкнених пристроїв Bluetooth поруч. «Гаряча–холодна» в чотири кроки (холодно, тепло, гаряче, дуже гаряче) і грубий відсоток наближення. Find My/Локатор не в усіх ситуаціях замінює один-в-один: ціль — вибрати курс у зоні радіо. Завантаження зазвичай безкоштовне, iOS 17.1+.",
        "intro1": "Загубили <strong>навушники</strong>, <strong>браслет</strong> чи <strong>колонку</strong>? <strong>Bluetooth Finder</strong> — <em>простий пошук Bluetooth</em>: перелік, вибір рядка, рух, перегляд кроку й відсотка. Коли квапитеся вийти чи обшукати кімнату, так швидше звужується зона.",
        "intro2": "Перелік близький до реального часу; усе, що в ефірі в Bluetooth, видно, щоби не крокувати підряд. Відсоток і кроки — оціночно: стіни, метал, натовп і батарея змінюють RF, читай сигнали разом, не вважай одне число відстанню в метрах.",
    },
    "features": {
        "title": "Чим Bluetooth Finder виділяється",
        "subtitle": "Що отримуєте в реальних умовах",
        "items": [
            {
                "number": "1",
                "title": "Миттєвий скан",
                "description": "Після дозволу додаток виявляє увімкнені пристрої, що в ефірі, і пише список, часто без складного налаштування — вже з першого запуску видно результат.",
            },
            {
                "number": "2",
                "title": "Гаряча–холодна: холодно, тепло, гаряче, дуже гаряче",
                "description": "Кроки показують, чи наближаєтесь: холодно — далі чи слабше, тепло/гаряче — ближче, дуже гаряче — вже в зоні, де можна діставати рукою. Це про силу сигналу, не крокомір; видно, чи йдете в правильну сторону.",
            },
            {
                "number": "3",
                "title": "Показник наближення, %",
                "description": "Вищий % зазвичай ближче в типових умовах, але це не метр на стрічці. Сполучайте з кроком «гаряча–холодна» й не вважайте одну цифру прямим залишком метрів.",
            },
            {
                "number": "4",
                "title": "Дані пристрою",
                "description": "Якщо в списку бренд, модель, назва — у кімнаті з кількома телефонами й навушниками легше вибрати свій рядок.",
            },
            {
                "number": "5",
                "title": "Сьогодні вдома, завтра в транспорті",
                "description": "Працює, коли радіо в гаджеті увімкнене в зоні. Шукаючи ті самі AirPods, браслет, колонку, менше пустого перебирання, ніж кидати всі кути одразу — залежить від сигналу й обстановки.",
            },
        ],
    },
    "how_to": {
        "title": "Як користуватися Bluetooth Finder",
        "description": "Відкрий, дай Bluetooth, дочекайся списку, обери потрібні навушники чи колонку. Ходь кімнатою чи коридором, дивись: холодно, тепло, гаряче, дуже гаряче і %; коли «дуже гаряче» і високий % — вже дуже близько. В натовпі головне — вибрати власну назву в списку, не чужу.",
    },
    "why_love": {
        "title": "Навіщо це",
        "description": "Менше вгадувань — курс натякують кроки й сигнал. «Гаряча–холодна» зрозуміло, % як підказка, в приміщенні й на вулиці, якщо пристрій в ефірі. Легко для тих, хто губить гаджети в роботі, в потязі, на дивані.",
    },
    "who_should_use": {
        "title": "Кому це",
        "description": "Власникам TWS, годинників, браслетів, портативних колонок, користувачам iOS 17.1+ удома, в дорозі, у шумі: спочатку звузити зону, далі вже пальцем і поглядом.",
    },
    "advanced_features": {
        "title": "Додатково",
        "description": "Список майже в реальному часі, кроки + % — швидше вловити тренд. Додаток зроблено легким; батарея — від тривалості й фонової роботи. Платні варіанти можливі; умови й ціни — в App Store.",
    },
    "final_cta": {
        "title": "Завантажте Bluetooth Finder сьогодні",
        "paragraph1": "Не витрачайте години на пусте ходження. <a href=\"__APP_STORE_URL__\" rel=\"noopener noreferrer\">У App Store</a> встановіть додаток, користуйтеся кроком «гаряча–холодна» і відсотком, щоб повернути AirPods, годинник, колонку чи інший ввімкнений у зоні Bluetooth, без зайвого нерву.",
        "cta_text": "Завантажити в App Store",
        "cta_aria_label": "Завантажити Bluetooth Finder в App Store",
        "cta_img_alt": "Завантажити Bluetooth Finder в App Store",
    },
    "footer": {
        "copyright": "© 2026 Bluetooth Finder. Усі права захищено.",
    },
    "app_info": {
        "category": "Продуктивність",
        "languages": "Українська (ця сторінка), English",
        "compatibility": "Потрібен iOS 17.1 або новіший",
    },
    "seo": _SEO,
}
