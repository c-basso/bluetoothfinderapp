# Turkish copy for build/tr.json (keys match pl.json top-level).
import json
from pathlib import Path

B = Path(__file__).parent
_SEO = json.loads((B / "tr_seo.json").read_text(encoding="utf-8"))

TR = {
    "meta": {
        "lang": "tr",
        "title": "Bluetooth Finder - Kayıp Bluetooth cihazı | AirPods, saat, kulaklık",
        "description": "Bluetooth Finder, açık AirPods, saat, kulaklık, hoparlör gibi yakındaki Bluetooth cihazlarını aramanıza yardımcı olur. «Sıcak–soğuk» dört aşama (soğuk, ılık, sıcak, çok sıcak) ve yakınlık için yüzde göstergesi. iOS 17.1+ gerekir. App Store’dan indirme genellikle ücretsiz; uygulama içi satın almalar App Store açıklamasındadır.",
        "keywords": "bluetooth bul, airpods bul, bluetooth tarama, iPhone uygulaması, yakındaki bluetooth, bluetooth cihaz bul, kulaklık arama, akıllı saat bul, bluetooth arayıcı",
        "author": "Bluetooth Finder",
        "og_url": "https://bluetoothfinderapp.com/tr/",
        "og_title": "Bluetooth Finder - Yakındaki Bluetooth cihazı",
        "og_description": "Tara, sıcak–soğuk, yüzde. AirPods, saat, kulaklık (menzildeyse). iOS 17.1+; iPhone; indirme genellikle ücretsiz, IAP olabilir.",
        "og_image": "https://bluetoothfinderapp.com/site_preview.png",
        "og_image_alt": "Bluetooth Finder - cihaz arama",
        "og_image_width": "1140",
        "og_image_height": "599",
        "og_locale": "tr_TR",
        "twitter_url": "https://bluetoothfinderapp.com/tr/",
        "twitter_title": "Bluetooth Finder - Bluetooth cihazını hızlı bul",
        "twitter_description": "AirPods, saat, hoparlör. Dört aşama: soğuk, ılık, sıcak, çok sıcak ve yüzde.",
        "twitter_image": "https://bluetoothfinderapp.com/site_preview.png",
        "twitter_image_alt": "Bluetooth Finder",
        "twitter_image_width": "1140",
        "twitter_image_height": "599",
        "canonical": "https://bluetoothfinderapp.com/tr/",
        "og_type": "website",
        "twitter_card": "summary_large_image",
        "theme_color": "#0A0E27",
        "apple_mobile_web_app_status_bar_style": "default",
    },
    "header": {
        "application_name": "Bluetooth Finder – Bluetooth cihaz arayıcı",
        "app_name_suffix": "Bluetooth cihaz arayıcı",
        "logo_alt": "Bluetooth Finder logosu: AirPods, saat, kulaklık",
        "app_name": "Bluetooth Finder",
        "title": "Bluetooth Finder",
        "tagline": "Unuttuğun cihaza daha çabuk ulaş.",
        "download_text": "App Store’da indir",
        "download_aria_label": "App Store’dan Bluetooth Finder’ı indir",
        "download_img_alt": "App Store’da Bluetooth Finder’ı indir",
    },
    "screenshots": {
        "items": [
            {"src": "/img/1_cover_12_framed.webp", "alt": "Bluetooth Finder - ana ekran"},
            {"src": "/img/2_scan_12_framed.webp", "alt": "Bluetooth Finder - tarama"},
            {"src": "/img/3_track_12_framed.webp", "alt": "Bluetooth Finder - yön"},
            {"src": "/img/4_info_12_framed.webp", "alt": "Bluetooth Finder - bilgi"},
        ],
    },
    "content": {
        "summary_label": "Kısaca",
        "summary_tldr": "Bluetooth Finder, iPhone (iOS) üzerinde yakındaki açık AirPods, saat, hoparlör ve diğer Bluetooth cihazlarını bulmaya yönelik uygulamadır. «Sıcak–soğuk» dört aşama (soğuk, ılık, sıcak, çok sıcak) ve göreli yüzde değerini okursunuz. Apple «Find My»nın tüm senaryolarda bire bir yerine geçmez: amaç, radyo menzili içinde yönlendirmek. İndirme genellikle ücretsiz; iOS 17.1 veya üzeri gerekir.",
        "intro1": "Kulaklık, bant mı, hoparlör mı unuttun? <strong>Bluetooth Finder</strong>, tarama yapan, listeden cihaz seçtiren basit bir <em>Bluetooth cihaz aracı</em>dır: listeyi aç, doğru satıra bas, ileri geri yürürken aşamaları ve yüzdeyi izle. Dışarı çıkarken veya odayı taradığında aranacak alanı daraltmana yardımcı olur.",
        "intro2": "Uygulama, menzilde yayın yapan cihazı neredeyse anlık yansıtır, böylece tüm bölgeyi aynı anda taramak zorunda kalmazsın. Göstergeler yakınsamak içindir; duvar, metal, kalabalık ve bateri sinyal gücünü değiştirir; tüm ipuçlarını birden, tek sayıyı yeterli sayma.",
    },
    "features": {
        "title": "Neden Bluetooth Finder fark yaratıyor",
        "subtitle": "Pratikte neleri alırsın",
        "items": [
            {
                "number": "1",
                "title": "Hızlı tarama",
                "description": "Bluetooth açıkken uygulama menzildeki yayın yapan cihazı duyup listeler. Çoğu kez ağır kurulma gerekmez: sonuç hızla görünür.",
            },
            {
                "number": "2",
                "title": "Sıcak–soğuk: soğuk, ılık, sıcak, çok sıcak",
                "description": "Soğuk, uzak veya zayıf; ılık ve sıcak, yakınsa; çok sıcak, cihaz elinize çok yakın. Sinyal gücüne dayanır, cetvelle ölçüm değil; doğru yöne gidip gitmediğini aşamalar fark ettirir.",
            },
            {
                "number": "3",
                "title": "Yakınlık (%)",
                "description": "Daha büyük sayı, tipik sinyal şartında genelde ‘daha yakınsa’ fikrini verir; metre cinsine çevirme. Sayı, sıcak–soğuk aşamalarıyla aynı anda, birlikte oku.",
            },
            {
                "number": "4",
                "title": "Cihaz bilgisi",
                "description": "Listede marka, model veya ad görünüyorsa, kaybolan cihazı tanımlamak kolaylaşır: özellikle birkaç telefon veya kulaklık varken.",
            },
            {
                "number": "5",
                "title": "Evde, işte, toplu taşımada",
                "description": "Radyo açık ve menzildeyse aramaya uygundur. AirPods, kordon, hoparlör gibi cihazlarda 'her yeri arama' eğilimini azaltır; sonuç, sinyal ve ortam koşuluna bağlıdır.",
            },
        ],
    },
    "how_to": {
        "title": "Bluetooth Finder nasıl kullanılır",
        "description": "Uygulamayı aç, Bluetooth iznini onayla, taramanı bekle, aradığın kulaklık veya hoparlörü seç. Oda veya koridorda yürürken soğuk, ılık, sıcak, çok sıcak aşamaları ve yüzdeye bak. Çok sıcak ve yüksek yüzde, cihaz çok yakındasın. Kalabalıkta önce listede kendi cihazının adını doğrula.",
    },
    "why_love": {
        "title": "Buna neden gerek olsun",
        "description": "Rastgele aranmayı az; uygulama sinyale göre yön verir. Sıcak–soğuk anlaşılır, yüzde destek, içeride ve dışarı, Bluetooth açıkken. Hızlı arayüz, ofiste, tren, kanepe, küçük cihaz kaybettiğin için pratik.",
    },
    "who_should_use": {
        "title": "Kimin için",
        "description": "AirPods, in-ear kulaklık, bant, hoparlör, iş seyahati, ev, aile: önce alanı daralt, sonra el ve gözle yakala.",
    },
    "advanced_features": {
        "title": "Ek bilgi",
        "description": "Liste neredeyse canlı yenilenir; sıcak–soğuk ve yüzde birlikte okun; uygulama hafif. Batarya ve arka planda tüketim, kullanıma ve ortama bağlı. Bazı özellikler uygulama içi satın alma olabilir; her zaman App Store açıklamasına bakın.",
    },
    "final_cta": {
        "title": "Bluetooth Finder’ı bugün indir",
        "paragraph1": "Boş yere dolaşma. <a href=\"__APP_STORE_URL__\" rel=\"noopener noreferrer\">App Store’dan indir</a> ve «sıcak–soğuk» ile yüzde ipuçlarını kullan; AirPods, saat, hoparlör veya başka açık Bluetooth cihazını menzilde, gereksiz strese yol açmadan yakala.",
        "cta_text": "App Store’da indir",
        "cta_aria_label": "App Store’dan Bluetooth Finder’ı indir",
        "cta_img_alt": "App Store’da Bluetooth Finder’ı indir",
    },
    "footer": {
        "copyright": "© 2026 Bluetooth Finder. Tüm hakları saklıdır.",
    },
    "app_info": {
        "category": "Verimlilik",
        "languages": "Türkçe (bu sayfa), English",
        "compatibility": "iOS 17.1 veya üzeri gerekir",
    },
    "seo": _SEO,
}
