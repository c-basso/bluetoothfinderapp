#!/usr/bin/env python3
# Regenerate uk_seo.json; pl.json shape; UAH for offers; four steps: холодно, тепло, гаряче, дуже гаряче.
import json
from pathlib import Path

B = Path(__file__).parent

FAQ = [
    {
        "question": "Що таке Bluetooth Finder?",
        "answer": "Це застосунок на iPhone, що допомагає знайти ввімкнені поруч пристрої Bluetooth — навушники, динамік, годинник — за «гаряче–холодна» в чотири кроки (холодно, тепло, гаряче, дуже гаряче) і відсоток наближення. Спершу звужується зона, далі вже дивитесь руками й очима, а не вгадуєте випадково.",
    },
    {
        "question": "Як це працює?",
        "answer": "Застосунок сканує, показує список тих, хто передає сигнал, оновлює значення в реальному часі. Є кроки: холодно, тепло, гаряче, дуже гаряче, а також відсоток, і за можливості — бренд, модель, назва.",
    },
    {
        "question": "Чи знайду втрачені AirPods?",
        "answer": "Якщо навушники чи футляр в ефірі, увімкнені й видно в списку, можна рухатись за підказками, тоді звузити ділянку й дивитись, слухаючи й дивлячись. Це не гарантовані метри, а практичне звуження, перш ніж остаточно знайдете, де вони лежать.",
    },
    {
        "question": "Інші бренди, не лише Apple?",
        "answer": "Так: будь-який увімкнений і видимий в Bluetooth пристрій може потрапити в перелік — годинник, браслет, навушники, колонка. Кожен виробник інакше будить і оголошує, тому результат відрізняється.",
    },
    {
        "question": "Чи безкоштовно завантажити застосунок?",
        "answer": "Завантаження в App Store зазвичай безкоштовне. Частина функцій чи додаткових речей може бути в покупці в додатку — завжди дивіться опис у магазині.",
    },
    {
        "question": "Вимоги до телефону",
        "answer": "iPhone з iOS 17.1 або новіший згідно цієї версії, увімкнений Bluetooth, дозвіл в програми. Тривалість і батарея залежать від сценарію, фонової роботи й толпи.",
    },
    {
        "question": "Чи відсоток — це скільки метрів залишилось?",
        "answer": "Ні — це відносна величина, залежна від стін, металу, людей і ще купи факторів. Сполучайте відсоток із кроками «гаряча–холодна», а не вірте однією цифрою на відстань.",
    },
    {
        "question": "Чи працює в натовпі, на вокзалі, у магазині?",
        "answer": "Працює, але в списку кілька чи десятки рядків: читайте мітку пристрою, підходьте ближче, дивіться сигнал, глядіть, коли % росте. Що більше чужих навколо, то важливіша правильна назва в списку.",
    },
    {
        "question": "Чим відрізняється від Find My (Локатора) Apple",
        "answer": "Find My в екосистемі Apple, потребує облікового запису й нерідко, щоб пристрій вже зареєстрували, перш ніж він в хмарі. Bluetooth Finder насамперед працює з тим, що в ефірі в Bluetooth поруч, без заздалегідь пари. Це різні випадки, іноді доповнюються, але не взаємно замінні один до одного в усьому.",
    },
    {
        "question": "А якщо пристрій не в Find My і не Apple",
        "answer": "Тоді інколи, як увімкнений, у зоні й у скані — додаток дійсно зменшує площу, де шукати. Від великої відстані, крадіжок, вимкненого живлення, інших кроків — не обійдеться однією цією програмою.",
    },
]

STRUCTURED = {
    "software_application": {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Bluetooth Finder",
        "alternateName": "Застосунок, щоб знайти пристрої Bluetooth поруч",
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "iOS",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "UAH",
            "availability": "https://schema.org/InStock",
        },
        "description": "Додаток на iPhone (iOS 17.1+) шукає втрачені, увімкнені поруч пристрої Bluetooth: навушники, динаміки, годинники, з кроками «гаряча–холодна» (холодно, тепло, гаряче, дуже гаряче) і відсоток наближення, плюс бренд, модель, ім'я, якщо з'являються.",
        "image": {
            "@type": "ImageObject",
            "url": "https://bluetoothfinderapp.com/img/logo.webp",
            "width": 140,
            "height": 140,
            "caption": "Логотип Bluetooth Finder",
        },
        "screenshot": {
            "@type": "ImageObject",
            "url": "https://bluetoothfinderapp.com/img/1_cover_12_framed.webp",
            "width": 390,
            "height": 844,
        },
        "url": "https://bluetoothfinderapp.com/uk/",
        "author": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "publisher": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "keywords": "bluetooth, знайти, AirPods, навушники, iOS, сканер, пристрої Bluetooth",
        "inLanguage": "uk",
        "datePublished": "2024-12-31",
        "dateModified": "2026-04-26",
        "softwareVersion": "1.3",
        "fileSize": "25.3MB",
        "softwareRequirements": "Потрібен iOS 17.1 або новіший",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.5",
            "ratingCount": "100",
        },
    },
    "organization": {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Bluetooth Finder",
        "url": "https://bluetoothfinderapp.com/uk/",
        "logo": "https://bluetoothfinderapp.com/img/logo.webp",
        "description": "Bluetooth Finder — iPhone, пошук пристроїв Bluetooth українською.",
    },
    "website": {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Bluetooth Finder",
        "url": "https://bluetoothfinderapp.com/uk/",
        "description": "Українська сторінка: опис, таблиця, поширені питання, App Store.",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://bluetoothfinderapp.com/uk/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    },
    "howto": {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "Як знайти втрачений пристрій Bluetooth поруч за допомогою Bluetooth Finder",
        "description": "Встановіть, дайте дозвіл, оберіть рядок, кроки холодно–тепло–гаряче–дуже гаряче, відсоток, в кінці шукайте вузько руками й зором.",
        "step": [
            {
                "@type": "HowToStep",
                "position": 1,
                "name": "Встановити",
                "text": "App Store, iOS 17.1+; завантаження зазвичай безкоштовне, розмір близько 25,3 МБ, точні уточнення в магазині.",
            },
            {
                "@type": "HowToStep",
                "position": 2,
                "name": "Скан",
                "text": "Відкрийте, дайте дозвіл на Bluetooth, дочекайтесь список пристроїв поруч.",
            },
            {
                "@type": "HowToStep",
                "position": 3,
                "name": "Вибір",
                "text": "Позначте в списку ті навушники, динамік, годинник, що губите, за іменем, брендом, моделлю, якщо вони виписані.",
            },
            {
                "@type": "HowToStep",
                "position": 4,
                "name": "Гаряча–холодна",
                "text": "Рухайтесь, щоб крок зсувався: холодно, тепло, гаряче, дуже гаряче — ніж сильніший в ефірі, тим ближче.",
            },
            {
                "@type": "HowToStep",
                "position": 5,
                "name": "Відсоток",
                "text": "Переглядайте відсоток як додаткове, не в метр; комбінуй з усіма вказівниками, не тільки з цифрою.",
            },
            {
                "@type": "HowToStep",
                "position": 6,
                "name": "Забрати",
                "text": "Сигнал показує дуже близько — дивися вузьку зону: диван, пакет, кишеню, візуально, руками, як підказав скан.",
            },
        ],
    },
    "faqpage": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Що робить Bluetooth Finder",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Сканає, обира з списку, крокує за сильнішим сигналом з кроком холодно–тепло–гаряче–дуже гаряче та відсотками — суттєвіше звужує, ніж випадкова ходьба, без вигадки, що цифра=метр.",
                },
            },
            {
                "@type": "Question",
                "name": "Відрізнення від Find My на iPhone",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Find My поєднує реєстри, хмарний облік у Apple, Bluetooth Finder показує, увімкнено й в ефірі, одразу поруч. Сценарії схожі, але взаємнозаміщати не в усьому виходить.",
                },
            },
            {
                "@type": "Question",
                "name": "Відсоток замінює метр",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Ні: відсоток залежить від сили прийому; стіни, натовп, положення, батарея. Читай усе разом, не вважай одну цифру прямим залишком метрів.",
                },
            },
            {
                "@type": "Question",
                "name": "Чи платна завантаження",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Початок завантаження з App Store зазвичай безкоштовний; платні доповнення — у описі в магазині і в цінах в додатку.",
                },
            },
        ],
    },
    "breadcrumb_list": {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Головна",
                "item": "https://bluetoothfinderapp.com/uk/",
            }
        ],
    },
}

TOP = {
    "breadcrumb_home": "Головна",
    "last_updated_label": "Оновлено",
    "key_facts_title": "Bluetooth Finder у цифрах",
    "key_facts": [
        {"value": "25.3 MB", "label": "Розмір"},
        {"value": "iOS 17.1+", "label": "Система"},
        {"value": "4+", "label": "Вік"},
        {"value": "Безкоштовно (IAP)", "label": "Завантаження"},
        {"value": "напр. AirPods, годинник, навушники", "label": "Приклади"},
    ],
    "comparison_title": "Bluetooth Finder, Find My і звичайне сканування",
    "comparison_intro": "Чесне порівняння, без пустого маркетингу:",
    "comparison_col_feature": "Параметр",
    "comparison_col_bluetooth_finder": "Bluetooth Finder",
    "comparison_col_find_my": "Find My (Локатор)",
    "comparison_col_generic": "Звичайний переглядач",
    "comparison_rows": [
        {
            "feature": "Тип пристроїв",
            "bluetooth_finder": "Увімкнений, видимий в Bluetooth, у зоні прийому",
            "find_my": "Переважно Apple, часто зареєстрований в мережі заздалегідь",
            "generic": "Будь-який в списку, але без кроку «гаряча–холодна»",
        },
        {
            "feature": "Попереднє підключення",
            "bluetooth_finder": "Найчастіше, окремо не критично",
            "find_my": "Так, сценарій Find My / iCloud-мережі",
            "generic": "Найчастіше, не обов'язок",
        },
        {
            "feature": "Наближення",
            "bluetooth_finder": "Холодно, тепло, гаряче, дуже гаряче + %",
            "find_my": "Карта/відстань, де реалізовано",
            "generic": "Часто лише рядок, варіююча наочність",
        },
        {
            "feature": "Платформа",
            "bluetooth_finder": "iOS 17.1 і далі (цей додаток на iPhone)",
            "find_my": "Екосистема Apple, різні сценарії",
            "generic": "залежить",
        },
    ],
    "faq_title": "Поширені питання: Bluetooth Finder",
    "faq": FAQ,
    "structured_data": STRUCTURED,
}

out = json.dumps(TOP, ensure_ascii=False, indent=2) + "\n"
path = B / "uk_seo.json"
path.write_text(out, encoding="utf-8")
json.loads(out)
print("Wrote", path, path.stat().st_size)
