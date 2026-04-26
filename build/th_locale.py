# Thai copy for build/th.json (keys match pl.json top-level).
import json
from pathlib import Path

B = Path(__file__).parent
_SEO = json.loads((B / "th_seo.json").read_text(encoding="utf-8"))

TH = {
    "meta": {
        "lang": "th",
        "title": "Bluetooth Finder - อุปกรณ์ Bluetooth หาย | AirPods, นาฬิกา, หูฟัง",
        "description": "Bluetooth Finder ช่วยตามหา AirPods, นาฬิกา, หูฟัง, ลำโพง Bluetooth ที่เปิดทำงานรอบตัว: คำแนะนำ «ร้อน-เย็น» สี่ขั้น (เย็น, อุ่น, ร้อน, ร้อนมาก) และตัวบ่งใกล้แบบเปอร์เซ็นต์ ต้อง iOS 17.1+ ดาวน์โหลดฟรีจาก App Store อาจซื้อเพิ่มในแอป",
        "keywords": "ค้นหา Bluetooth, หา AirPods, อุปกรณ์ Bluetooth, สแกน Bluetooth, iPhone, ตัวติดตาม, อุปกรณ์ใกล้ ๆ, ลำโพง Bluetooth, นาฬิกา, แอปหาเครื่อง",
        "author": "Bluetooth Finder",
        "og_url": "https://bluetoothfinderapp.com/th/",
        "og_title": "Bluetooth Finder - อุปกรณ์ Bluetooth รอบตัว",
        "og_description": "สแกน, ร้อน-เย็น, ตัวเลขเปอร์เซ็นต์. AirPods, หูฟังหรือนาฬิกา หากยังอยู่ในสัญญาณ. iOS 17.1+; iPhone; ดาวน์โหลดฟรี อาจมีการซื้อเพิ่มในแอป",
        "og_image": "https://bluetoothfinderapp.com/site_preview.png",
        "og_image_alt": "Bluetooth Finder - ค้นหาอุปกรณ์",
        "og_image_width": "1140",
        "og_image_height": "599",
        "og_locale": "th_TH",
        "twitter_url": "https://bluetoothfinderapp.com/th/",
        "twitter_title": "Bluetooth Finder - รู้ว่าใกล้หรือยัง",
        "twitter_description": "AirPods, นาฬิกา, หูฟัง. สี่ขั้น: เย็น-อุ่น-ร้อน-ร้อนมาก กับเปอร์เซ็นต์",
        "twitter_image": "https://bluetoothfinderapp.com/site_preview.png",
        "twitter_image_alt": "Bluetooth Finder",
        "twitter_image_width": "1140",
        "twitter_image_height": "599",
        "canonical": "https://bluetoothfinderapp.com/th/",
        "og_type": "website",
        "twitter_card": "summary_large_image",
        "theme_color": "#0A0E27",
        "apple_mobile_web_app_status_bar_style": "default",
    },
    "header": {
        "application_name": "Bluetooth Finder – ค้นหาอุปกรณ์ Bluetooth",
        "app_name_suffix": "เครื่องมือหาอุปกรณ์ Bluetooth",
        "logo_alt": "โลโก้ Bluetooth Finder: AirPods, นาฬิกา, หูฟัง",
        "app_name": "Bluetooth Finder",
        "title": "Bluetooth Finder",
        "tagline": "เอาเครื่องที่ลืม กลับมาใช้ง่ายขึ้น",
        "download_text": "ดาวน์โหลดบน App Store",
        "download_aria_label": "ดาวน์โหลด Bluetooth Finder จาก App Store",
        "download_img_alt": "ดาวน์โหลด Bluetooth Finder จาก App Store",
    },
    "screenshots": {
        "items": [
            {
                "src": "/img/1_cover_12_framed.webp",
                "alt": "Bluetooth Finder - หน้าหลัก",
            },
            {
                "src": "/img/2_scan_12_framed.webp",
                "alt": "Bluetooth Finder - สแกน",
            },
            {
                "src": "/img/3_track_12_framed.webp",
                "alt": "Bluetooth Finder - ตามหา",
            },
            {
                "src": "/img/4_info_12_framed.webp",
                "alt": "Bluetooth Finder - ข้อมูล",
            },
        ]
    },
    "content": {
        "summary_label": "สรุป",
        "summary_tldr": "Bluetooth Finder เป็นแอปบน iPhone (iOS) สำหรับตามหา AirPods, นาฬิกา, ลำโพง, อุปกรณ์ Bluetooth อื่น ๆ ที่ยังส่งสัญญาณ ใกล้ ๆ: ร้อน-เย็น สี่ขั้น (เย็น, อุ่น, ร้อน, ร้อนมาก) กับตัวบ่งแบบเปอร์เซ็นต์. ต่างจาก ค้นหา (Find My) ของ Apple มักไม่ต้องลงทะเบียนล่วงหน้า ดาวน์โหลดฟรี; ต้อง iOS 17.1 หรือใหม่กว่า",
        "intro1": 'เผลอ <strong>ลืมหูฟัง</strong> สาย <strong>รัดข้อมือ</strong> หรือ <strong>ลำโพง</strong> บ้างไหม? <strong>Bluetooth Finder</strong> คือ <em>ตัวช่วยหา Bluetooth รอบตัว</em>: สแกน, เลือกรายการ, ดูระดับร้อน-เย็น กับเปอร์เซ็นต์ ว่าเดินใกล้หรือห่าง',
        "intro2": "รายชื่ออัปเดตกับสัญญาณ; กำแพง ฝูงคน แบต มีผล. อ่านทุกบ่งชี้รวม ๆ กัน อย่าดูเฉพาะเปอร์เซ็นต์ แล้วเทียบ “เมตร” ลวง ๆ",
    },
    "features": {
        "title": "ทำไม Bluetooth Finder โดดเด่น",
        "subtitle": "สิ่งที่คุณได้รับจริง ๆ",
        "items": [
            {
                "number": "1",
                "title": "สแกนเร็ว",
                "description": "เมื่ออนุญาต Bluetooth แอปจะรับอุปกรณ์ที่ยังออกอากาศ อยู่รอบ ๆ แล้วแสดงในรายชื่อ มักไม่ต้องตั้งค่าซับซ้อน — ผลขึ้นตามที",
            },
            {
                "number": "2",
                "title": "ร้อน-เย็น: เย็น, อุ่น, ร้อน, ร้อนมาก",
                "description": "เย็น = ห่าง/อ่อน, อุ่น-ร้อน = กำลังใกล้, ร้อนมาก = ใกล้พอจะหยิบได้ นี่อิงกำลังสัญญาณ ไม่ใช่เอาเมตรวัด แต่รู้ได้ว่ากำลังกระชิดลงหรือถอย",
            },
            {
                "number": "3",
                "title": "ค่าเปอร์เซ็นต์ความใกล้ (%)",
                "description": "โดยทั่วไปค่ายิ่งสูงยิ่ง “ใกล้” ตามสัญญาณ ไม่ใช่ตัวแทนเมตร. อ่านคู่กับขั้น ร้อน-เย็น ดีกว่าเลขเดี่ยว",
            },
            {
                "number": "4",
                "title": "ข้อมูลอุปกรณ์",
                "description": "หากมียี่ห้อ รุ่น หรือชื่อในรายการ จะง่ายต่อการมองหา โดยเฉพาะเวลาโทรศัพท์-หลายอุปกรณ์มีหูฟังคู่",
            },
            {
                "number": "5",
                "title": "วันนี้ที่บ้าน พรุ่งนี้นอกบ้าน",
                "description": "ดีได้เมื่อวิทยุอุปกรณ์เปิดและอยู่บริเวณ. ตาม AirPods, นาฬิกา, ลำโพง ฯลฯ มักลด “ค้นสำรวจ” กว้าง ๆ — ขึ้นกับสัญญาณและบรรยากาศ",
            },
        ],
    },
    "how_to": {
        "title": "วิธีใช้งาน Bluetooth Finder",
        "description": "เปิดแอป, อนุญาต Bluetooth, รอสแกน, แล้วแตะรายการที่ตรงกับหูฟังหรือลำโพง. เดินในห้องหรือทางเดิน มอง ร้อน-เย็น (เย็น, อุ่น, ร้อน, ร้อนมาก) พร้อม % เมื่อถึง ร้อนมาก กับตัวเลขสูง แสดงว่าใกล้พอค้น แล้วเช็กจุดนั้น. ฝูงแออัด: เลือกก่อนให้ตรงชื่อในรายชื่อ",
    },
    "why_love": {
        "title": "ช่วยอะไร",
        "description": "ลดการ “เดาแล้วค้น” — แอปบอกทิศจากสัญญาณ: ร้อน-เย็น อ่านง่าย เปอร์เซ็นต์ช่วยเสริม ใช้ได้ทั้งในห้องและกลางแจ้งเมื่ออุปกรณ์ยังออกอากาศ Bluetooth อินเทอร์เฟซเร็ว สำหรับคนหูฟัง/แกดเจ็ตหาย ที่ออฟฟิศ รถไฟ หรือโซฟา",
    },
    "who_should_use": {
        "title": "เหมาะกับใคร",
        "description": "เจ้าของ AirPods/หูฟังอินเอียร์, นาฬิกา-สายรัดข้อมือ, ลำโพงพก หรือหูฟังครอบหู ทั้งเวลาเดินทางหรือบ้านที่วุ่นวาย ทุกวันที่ต้องรู้เรื่องเร็ว: รู้ “พื้นที่แคบ” ก่อน ค่อยใช้มือกับสายตาตาม",
    },
    "advanced_features": {
        "title": "ข้อมูลเพิ่มเติม",
        "description": "รายชื่ออัปเดตแทบตามเวลาจริง; รวมขั้น ร้อน-เย็น กับเปอร์เซ็นต์ ช่วยให้จับอาการได้ไว แอปออกแบบเบา-เร็ว แบตลดขึ้นกับเวลาใช้-พื้นหลัง-สิ่งกีดขวาง บางฟีเจอร์อาจเสียเงินในแอป — ดูคำอธิบายใน App Store ทุกครั้ง",
    },
    "final_cta": {
        "title": "ดาวน์โหลด Bluetooth Finder วันนี้",
        "paragraph1": "อย่าเสียเวลาไปกับการเดาเสีย ๆ <a href=\"__APP_STORE_URL__\" rel=\"noopener noreferrer\">ดาวน์โหลดจาก App Store</a> แล้วใช้คำแนะนำ ร้อน-เย็น กับตัวบ่งความใกล้ เพื่อเอา AirPods, นาฬิกา, ลำโพง หรืออุปกรณ์ Bluetooth อื่น ๆ ที่ยังออกอากาศ กลับมา โดยไม่เครียดจนเกินไป",
        "cta_text": "ดาวน์โหลดจาก App Store",
        "cta_aria_label": "ดาวน์โหลด Bluetooth Finder จาก App Store",
        "cta_img_alt": "ดาวน์โหลด Bluetooth Finder จาก App Store",
    },
    "footer": {
        "copyright": "© 2026 Bluetooth Finder. สงวนลิขสิทธิ์",
        "privacy_link": "นโยบายความเป็นส่วนตัว",
        "terms_link": "ข้อกำหนด",
    },
    "app_info": {
        "category": "ผลิตภาพ",
        "languages": "ไทย (หน้านี้), English",
        "compatibility": "ต้องใช้ iOS 17.1 หรือใหม่กว่า",
    },
    "seo": _SEO,
}
