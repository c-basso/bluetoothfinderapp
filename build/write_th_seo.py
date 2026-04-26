#!/usr/bin/env python3
# Regenerate th_seo.json (valid JSON; Thai copy + pl.json-shaped structured_data).
import json
from pathlib import Path

B = Path(__file__).parent

# 10 Q&A — avoid mai yamok (U+0E2F) immediately before ASCII " in any hand-written JSON; here we use json.dumps.
FAQ = [
    {
        "question": "Bluetooth Finder คืออะไร?",
        "answer": "แอปบน iPhone สำหรับมองหาอุปกรณ์ Bluetooth รอบตัวที่ยังออกอากาศ โดยใช้ ร้อน-เย็น สี่ขั้น (เย็น, อุ่น, ร้อน, ร้อนมาก) กับเปอร์เซ็นต์ ช่วยบีบมุมก่อน แล้วค่อยหาแบบมอง-มือ แทนเดาไปมั่ว",
    },
    {
        "question": "มันทำงานยังไง?",
        "answer": "แอปสแกน แสดงรายชื่อที่ออกอากาศ อัปเดตตามเวลา อ่านขั้น เย็น, อุ่น, ร้อน, ร้อนมาก กับเปอร์เซ็นต์ ถ้ามี — ยี่ห้อ รุ่น ชื่อ",
    },
    {
        "question": "เจอ AirPods หาย ได้มั้ย?",
        "answer": "ถ้าหูหรือกล่องยังส่งสัญญาณ เปิดทำงาน และปรากฏในรายชื่อ ก็เดินไล่ตาม ร้อน-เย็น รู้มุมก่อน แล้วมอง-มือ-สายตา. นี่บอกกำลังสัญญาณ ไม่รับประกันห่างกี่เมตร แต่ลดพื้นที่กว้าง ก่อนไปมอง ค้น ตัวจริง ๆ",
    },
    {
        "question": "ยี่ห้ออื่น นอก Apple ก็เจอได้มั้ย?",
        "answer": "ได้ — อะไรก็ตามที่เปิดและปรากฏใน Bluetooth นาฬิกา, รัดข้อ, ลำโพง, หูฟัง. แต่ละยี่ห้อออกเวกอัป-ชื่อ-สัญญาณ ไม่เท่ารุ่นกัน ผลอาจต่าง",
    },
    {
        "question": "แอปฟรีมั้ย?",
        "answer": "ดาวน์โหลดใน App Store มักไม่เสียค่าเริ่ม บางส่วนเสริมอาจซื้อในแอป — อ่านรายละเอียดและราคาใน App Store ทุกครั้ง",
    },
    {
        "question": "มือถือต้องใช้อะไร?",
        "answer": "ต้อง iPhone ที่ iOS 17.1 หรือใหม่กว่า ตามรุ่นนี้ของแอป เปิด Bluetooth และอนุญาตแอป; เวลาใช้, แบต, การทำงานเบื้องหลัง ขึ้นกับการใช้",
    },
    {
        "question": "ตัวเลขเปอร์เซ็นต์ บอกเหลือกี่เมตร?",
        "answer": "ไม่ — เป็นสัมพัทธ์จากกำลังรับ แปรตาม กำแพง, ฝูงคน, ร่าง, แบต. อ่านรวมกับ ร้อน-เย็น มากกว่าเลขเฉย ๆ",
    },
    {
        "question": "ฝูงแอ สถานี ห้าง ใช้ได้มั้ย?",
        "answer": "ใช้ แต่รายชื่ออาจยาว — เลือกตามป้าย อุปกรณ์, เข้าใกล้, มองเปอร์เซ็นต์, อ่านขั้น-ก่อน. ยิ่งหูหลายคู่ ยิ่งสำคัญที่ตรงชื่อในรายชื่อ",
    },
    {
        "question": "ต่างจาก ค้นหา (Find My) ยังไง?",
        "answer": "Find My ใช้ ecosystem Apple อุปกรณ์ที่ลงทะเบียน-ผูกบัญชี. Bluetooth Finder เน้นอะไรที่ออกอากาศ ณ นั้น อาจเติมกัน แต่ไม่แทนกันครบทุกกรณี",
    },
    {
        "question": "เครื่องไม่อยู่ใน Find My ก็ยังดีมั้ย?",
        "answer": "บางที ถ้าเปิดอยู่ ใกล้ และปรากฏในสแกน แอปจะบีบมุมหาได้. กรณีห่าง ขโมย ปิดเครื่อง ตามขั้นของเจ้าของหรือเจ้าหน้าที่ ยังต้องวิธีนอกนี้ด้วย",
    },
]

STRUCTURED = {
    "software_application": {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Bluetooth Finder",
        "alternateName": "แอปสำหรับตามหา Bluetooth อุปกรณ์รอบตัว",
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "iOS",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "THB",
            "availability": "https://schema.org/InStock",
        },
        "description": "แอปบน iPhone (iOS 17.1 ขึ้นไป) ช่วยมองหา AirPods, ลำโพง, นาฬิกา และอื่น ๆ ที่ยังเปิดและอยู่ใกล้: กับ ร้อน-เย็น สี่ขั้น (เย็น, อุ่น, ร้อน, ร้อนมาก) และตัวเลขเปอร์เซ็นต์ความใกล้ พร้อม ยี่ห้อ รุ่น ชื่อ หากมียืนยันจากอุปกรณ์",
        "image": {
            "@type": "ImageObject",
            "url": "https://bluetoothfinderapp.com/img/logo.webp",
            "width": 140,
            "height": 140,
            "caption": "Logo Bluetooth Finder",
        },
        "screenshot": {
            "@type": "ImageObject",
            "url": "https://bluetoothfinderapp.com/img/1_cover_12_framed.webp",
            "width": 390,
            "height": 844,
        },
        "url": "https://bluetoothfinderapp.com/th/",
        "author": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "publisher": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "keywords": "bluetooth, ตามหา, AirPods, หูฟัง, iOS, สแกน, อุปกรณ์ Bluetooth",
        "inLanguage": "th",
        "datePublished": "2024-12-31",
        "dateModified": "2026-04-26",
        "softwareVersion": "1.3",
        "fileSize": "25.3MB",
        "softwareRequirements": "ต้องใช้ iOS 17.1 หรือใหม่กว่า",
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
        "url": "https://bluetoothfinderapp.com/th/",
        "logo": "https://bluetoothfinderapp.com/img/logo.webp",
        "description": "Bluetooth Finder — iPhone, ค้นหาอุปกรณ์ Bluetooth บนหน้าไทย",
    },
    "website": {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Bluetooth Finder",
        "url": "https://bluetoothfinderapp.com/th/",
        "description": "เวอร์ชันไทย: อธิบาย, ตาราง, คำถาม, ลิงก์ App Store",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://bluetoothfinderapp.com/th/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    },
    "howto": {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "วิธีหาเครื่อง Bluetooth ใกล้ ๆ ด้วย Bluetooth Finder",
        "description": "ดาวน์โหลด, อนุญาตสแกน, เลือกรายการ, ตาม ร้อน-เย็น (เย็น, อุ่น, ร้อน, ร้อนมาก) อ่านเปอร์เซ็นต์, มองหาในจุดแคบ ด้วยตาและมือ",
        "step": [
            {
                "@type": "HowToStep",
                "position": 1,
                "name": "ดาวน์โหลด",
                "text": "จาก App Store, ต้อง iOS 17.1 หรือใหม่กว่า, มักลงทะเบียนได้โดยไม่เสียเงิน, ไฟล์ประมาณ 25.3 MB",
            },
            {
                "@type": "HowToStep",
                "position": 2,
                "name": "สแกน",
                "text": "เปิดแอป, อนุญาต Bluetooth, รอให้รายชื่ออุปกรณ์รอบตัวเติม",
            },
            {
                "@type": "HowToStep",
                "position": 3,
                "name": "เลือก",
                "text": "จากรายชื่อ แตะ หูฟัง ลำโพง นาฬิกา หรือรายการที่ตรง — อ่านชื่อ ยี่ห้อ รุ่น หากมองเห็น",
            },
            {
                "@type": "HowToStep",
                "position": 4,
                "name": "ร้อน-เย็น",
                "text": "เคลื่อนตัวให้ขั้น ขยับจากเย็น ไป อุ่น ร้อน ร้อนมาก — ยิ่งออกอากาศมาก ยิ่งน่าใกล้",
            },
            {
                "@type": "HowToStep",
                "position": 5,
                "name": "เปอร์เซ็นต์",
                "text": "อ่านเปอร์เซ็นต์เสริม ไม่เท่ากับเมตร, อ่านคู่กับทุกขั้น-สัญญาณ-สภาพ",
            },
            {
                "@type": "HowToStep",
                "position": 6,
                "name": "รับเอง",
                "text": "พอรู้ว่า ใกล้มาก ก็ก้มมอง โซฟา กระเป๋า กระเป๋าเสื้อ ช่องวาง, ฯลฯ ด้วยมือกับสายตา",
            },
        ],
    },
    "faqpage": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Bluetooth Finder ทำอะไร",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "สแกน เลือกจากรายชื่อ แล้วเดินหาตาม ร้อน-เย็น สี่ขั้น (เย็น, อุ่น, ร้อน, ร้อนมาก) กับเปอร์เซ็นต์ — บีบมุมก่อน ไม่ใช่เดาไปรอบ ๆ ลำพัง",
                },
            },
            {
                "@type": "Question",
                "name": "ต่างจาก ค้นหา ของ Apple ยังไง",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Find My ผูก account และฝั่ง cloud; Bluetooth Finder เน้นสิ่งที่ออกอากาศ Bluetooth รอบตัว ณ นี้. อาจใช้คู่กัน แต่ไม่แทนกันทุกกรณี",
                },
            },
            {
                "@type": "Question",
                "name": "เปอร์เซ็นต์ แทนระยะหรือยัง",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "ไม่ — มาจากกำลังรับ กำแพง ฝูง ร่าง แบต ก็เปลี่ยนค่า อ่านรวมกับ ร้อน-เย็น",
                },
            },
            {
                "@type": "Question",
                "name": "ดาวน์โหลดเสียเงินไหม",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "มักลง App Store ได้ก่อนโดยไม่เสียค่า; ออปชัน ใน-แอป อาจเสียเงิน — ดูใน App Store",
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
                "name": "หน้าแรก",
                "item": "https://bluetoothfinderapp.com/th/",
            }
        ],
    },
}

# Top of file (same as previous valid keys) + faq + structured
TOP = {
    "breadcrumb_home": "หน้าแรก",
    "last_updated_label": "อัปเดต",
    "key_facts_title": "Bluetooth Finder ในตัวเลข",
    "key_facts": [
        {"value": "25.3 MB", "label": "ขนาด"},
        {"value": "iOS 17.1+", "label": "ระบบ"},
        {"value": "4+", "label": "อายุ"},
        {"value": "ฟรี (IAP)", "label": "ดาวน์โหลด"},
        {"value": "เช่น AirPods, นาฬิกา, หูฟัง", "label": "ตัวอย่าง"},
    ],
    "comparison_title": "Bluetooth Finder, ค้นหา (Find My) กับสแกนทั่วไป",
    "comparison_intro": "เทียบแบบเน้นการใช้ ไม่เอาโฆษณาเปล่า:",
    "comparison_col_feature": "หัวข้อ",
    "comparison_col_bluetooth_finder": "Bluetooth Finder",
    "comparison_col_find_my": "ค้นหา (Find My)",
    "comparison_col_generic": "สแกนทั่วไป",
    "comparison_rows": [
        {
            "feature": "ชนิดอุปกรณ์",
            "bluetooth_finder": "อุปกรณ์ที่เปิด — เห็นใน Bluetooth รอบตัว ตามเครื่องที่ออกอากาศ",
            "find_my": "ส่วนใหญ่เป็น Apple และมักลงทะเบียน/ผูกบัญชีมาก่อน",
            "generic": "อะไรก็ตามที่โผล่ในรายชื่อ แต่ไม่มีคู่ ร้อน-เย็น นำทาง",
        },
        {
            "feature": "เตรียมตั้งค่าล่วงหน้า",
            "bluetooth_finder": "มักไม่ต้องตั้งพิเศษ",
            "find_my": "ต้อง (เครือข่าย) ค้นหา / Find My",
            "generic": "มักไม่บังคับ",
        },
        {
            "feature": "พาใกล้เครื่อง",
            "bluetooth_finder": "ร้อน-เย็น: เย็น, อุ่น, ร้อน, ร้อนมาก กับเปอร์เซ็นต์",
            "find_my": "ทิศ/ระยะ บนรุ่นที่รองรับ",
            "generic": "มักแค่รายชื่อ บางตัวช่วยน้อยมาก",
        },
        {
            "feature": "แพลตฟอร์ม",
            "bluetooth_finder": "iOS 17.1 หรือใหม่กว่า",
            "find_my": "ระบบ Apple",
            "generic": "ขึ้นกับแอป",
        },
    ],
    "faq_title": "คำถามที่พบ: Bluetooth Finder",
    "faq": FAQ,
    "structured_data": STRUCTURED,
}

out = json.dumps(TOP, ensure_ascii=False, indent=2) + "\n"
path = B / "th_seo.json"
path.write_text(out, encoding="utf-8")
json.loads(out)
print("Wrote", path, path.stat().st_size)
