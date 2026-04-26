#!/usr/bin/env python3
# Regenerate vi_seo.json; pl.json shape; VND; four steps: lạnh, ấm, nóng, rất nóng.
import json
from pathlib import Path

B = Path(__file__).parent

FAQ = [
    {
        "question": "Bluetooth Finder là gì?",
        "answer": "Đây là ứng dụng trên iPhone giúp tìm thiết bị Bluetooth đang bật gần bạn — tai nghe, loa, đồng hồ — với cặp nóng–lạnh bốn bước (lạnh, ấm, nóng, rất nóng) và phần trăm gần. Trước hết thu hẹp vùng, rồi tìm bằng mắt và tay thay vì đoán bừa.",
    },
    {
        "question": "Cách hoạt động thế nào?",
        "answer": "Ứng dụng quét, liệt kê thiết bị đang phát, cập nhật theo tín hiệu. Có bước: lạnh, ấm, nóng, rất nóng, phần trăm, và nếu có thì tên hãng, mẫu, tên thiết bị.",
    },
    {
        "question": "Có tìm được AirPods bị mất không?",
        "answer": "Nếu hộp hoặc tai còn phát, đang bật và thấy trong danh sách, bạn có thể theo hướng dẫn nóng–lạnh rồi thu hẹp vùng, dùng mắt và tai. Đây không phải bảo đảm từng mét, mà thu hẹp thực tế trước khi tìm chính xác.",
    },
    {
        "question": "Hãng khác, không chỉ Apple?",
        "answer": "Có: mọi thiết bị bật và thấy trong Bluetooth có thể lên danh sách — đồng hồ, vòng tay, loa, tai nghe. Mỗi hãng bật và quảng bá khác nhau, kết quả khác nhau.",
    },
    {
        "question": "Ứng dụng có miễn phí không?",
        "answer": "Tải trên App Store thường miễn phí. Một số tính năng hoặc gói mở rộng có thể mua trong ứng dụng — luôn xem mô tả trong store.",
    },
    {
        "question": "Điện thoại cần gì?",
        "answer": "iPhone iOS 17.1 trở lên theo bản ứng dụng này, bật Bluetooth, cấp quyền. Thời lượng và pin phụ thuộc cách dùng và nền.",
    },
    {
        "question": "Phần trăm có nghĩa còn bao nhiêu mét?",
        "answer": "Không — đó là mức tương đối, phụ thuộc tường, kim loại, đám đông và nhiều yếu tố. Kết hợp với bước nóng–lạnh, đừng tin một con số.",
    },
    {
        "question": "Dùng được ở chỗ đông, ga, siêu thị không?",
        "answer": "Có, nhưng danh sách có thể dài: đọc nhãn thiết bị, lại gần, xem %, rồi tìm. Càng nhiều tai nghe lạ, càng cần đúng tên trên danh sách.",
    },
    {
        "question": "Khác gì với Find My của Apple?",
        "answer": "Find My thuộc hệ sinh thái Apple, cần tài khoản và nhiều khi đăng ký trước. Bluetooth Finder ưu tiên thiết bị đang phát Bluetooth gần điện thoại, không bắt ghép sẵn. Đó là tình huống khác, đôi khi bổ sung, không thay thế 1-1 mọi lúc.",
    },
    {
        "question": "Có ổn khi thiết bị không nằm trong Find My hoặc không phải Apple?",
        "answer": "Đôi khi, nếu bật, gần và thấy khi quét — ứng dụng thu hẹp vùng. Trộm xa, tắt nguồn, thủ tục khác: cần bước ngoài một app này.",
    },
]

STRUCTURED = {
    "software_application": {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Bluetooth Finder",
        "alternateName": "Ứng dụng tìm thiết bị Bluetooth gần bạn",
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "iOS",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "VND",
            "availability": "https://schema.org/InStock",
        },
        "description": "Ứng dụng trên iPhone (iOS 17.1 trở lên) tìm tai nghe, loa, đồng hồ Bluetooth đang bật gần: cặp nóng–lạnh bốn bước (lạnh, ấm, nóng, rất nóng) và % gần, cộng tên hãng, mẫu, tên khi có.",
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
        "url": "https://bluetoothfinderapp.com/vi/",
        "author": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "publisher": {"@type": "Person", "name": "Vladimir Ivakhnenko"},
        "keywords": "bluetooth, tìm, AirPods, tai nghe, iOS, quét, thiết bị Bluetooth",
        "inLanguage": "vi",
        "datePublished": "2024-12-31",
        "dateModified": "2026-04-26",
        "softwareVersion": "1.3",
        "fileSize": "25.3MB",
        "softwareRequirements": "Cần iOS 17.1 trở lên",
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
        "url": "https://bluetoothfinderapp.com/vi/",
        "logo": "https://bluetoothfinderapp.com/img/logo.webp",
        "description": "Bluetooth Finder — iPhone, tìm thiết bị Bluetooth, trang tiếng Việt.",
    },
    "website": {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Bluetooth Finder",
        "url": "https://bluetoothfinderapp.com/vi/",
        "description": "Bản tiếng Việt: mô tả, bảng, câu hỏi, liên kết App Store.",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://bluetoothfinderapp.com/vi/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    },
    "howto": {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "Cách tìm thiết bị Bluetooth gần bằng Bluetooth Finder",
        "description": "Cài, cho phép quét, chọn mục, theo cặp nóng–lạnh: lạnh, ấm, nóng, rất nóng, xem %, cuối cùng tìm trong vùng hẹp bằng mắt và tay.",
        "step": [
            {
                "@type": "HowToStep",
                "position": 1,
                "name": "Tải về",
                "text": "Từ App Store, cần iOS 17.1 trở lên, dung lượng khoảng 25,3 MB; tải thường miễn phí, chi tiết và mua trong app xem tại store.",
            },
            {
                "@type": "HowToStep",
                "position": 2,
                "name": "Quét",
                "text": "Mở ứng dụng, cấp quyền Bluetooth, đợi danh sách thiết bị gần lấp đầy.",
            },
            {
                "@type": "HowToStep",
                "position": 3,
                "name": "Chọn",
                "text": "Chạm dòng đúng tai nghe, loa hoặc đồng hồ, đọc tên, hãng, mẫu nếu hiện.",
            },
            {
                "@type": "HowToStep",
                "position": 4,
                "name": "Nóng–lạnh",
                "text": "Di chuyển sao bước tăng: lạnh, ấm, nóng, rất nóng — tín hiệu phát càng mạnh, càng gần hơn.",
            },
            {
                "@type": "HowToStep",
                "position": 5,
                "name": "Phần trăm",
                "text": "Xem % bổ sung, đừng coi như mét; gộp với mọi bước, không chỉ con số.",
            },
            {
                "@type": "HowToStep",
                "position": 6,
                "name": "Lấy thật",
                "text": "Khi tín hiệu rất gần, kiểm tra khu hẹp: sofa, túi, túi áo, ngăn, thực tế bằng tay và mắt.",
            },
        ],
    },
    "faqpage": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Bluetooth Finder làm gì?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Quét, chọn trong danh sách, bước tới tín hiệu mạnh hơn với bốn bước nóng–lạnh và % — thu hẹp vùng, không dò từng thử phòng, không tưởng tượng con số là thước dây.",
                },
            },
            {
                "@type": "Question",
                "name": "Khác Find My trên iPhone thế nào?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Find My nối thiết bị với tài khoản và mạng Apple. Bluetooth Finder ưu tiên thiết bị đang bật Bluetooth, thấy ngay quanh bạn, không phải tình huống 1-1 mọi lúc.",
                },
            },
            {
                "@type": "Question",
                "name": "Phần trăm thay cho mét à?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Không, % từ cường độ tín hiệu; tường, đám đông, tư thế, pin thay đổi. Đọc gộp cả cặp nóng–lạnh.",
                },
            },
            {
                "@type": "Question",
                "name": "Tải từ App Store có tính phí không?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Thường bắt đầu tải miễn phí; mua thêm có thể trong ứng dụng — xem mô tả và bảng giá trong store.",
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
                "name": "Trang chủ",
                "item": "https://bluetoothfinderapp.com/vi/",
            }
        ],
    },
}

TOP = {
    "breadcrumb_home": "Trang chủ",
    "last_updated_label": "Cập nhật",
    "key_facts_title": "Bluetooth Finder qua số liệu",
    "key_facts": [
        {"value": "25.3 MB", "label": "Dung lượng"},
        {"value": "iOS 17.1+", "label": "Hệ thống"},
        {"value": "4+", "label": "Độ tuổi"},
        {"value": "Miễn phí (IAP)", "label": "Tải về"},
        {"value": "ví dụ: AirPods, đồng hồ, tai nghe", "label": "Ví dụ"},
    ],
    "comparison_title": "Bluetooth Finder, Find My và trình quét thông thường",
    "comparison_intro": "So sánh công bằng, không nói quá:",
    "comparison_col_feature": "Tiêu chí",
    "comparison_col_bluetooth_finder": "Bluetooth Finder",
    "comparison_col_find_my": "Find My",
    "comparison_col_generic": "Quét chung",
    "comparison_rows": [
        {
            "feature": "Loại thiết bị",
            "bluetooth_finder": "Bật, thấy trong Bluetooth trong vùng phủ, nhiều hãng",
            "find_my": "Chủ yếu Apple, thường đã đăng ký trước với tài khoản",
            "generic": "Bất kỳ trên danh sách, thiếu cặp nóng–lạnh dẫn đường",
        },
        {
            "feature": "Chuẩn bị trước",
            "bluetooth_finder": "Hầu hết không cần thiết lập đặc biệt",
            "find_my": "Có, theo tình huống mạng Find My / iCloud",
            "generic": "Thường không bắt buộc",
        },
        {
            "feature": "Dẫn tới thiết bị",
            "bluetooth_finder": "Bốn bước nóng–lạnh + % gần",
            "find_my": "Hướng/khoảng cách ở máy hỗ trợ",
            "generic": "Nhiều khi chỉ danh sách, mức hỗ trợ khác nhau",
        },
        {
            "feature": "Nền tảng (ứng dụng này)",
            "bluetooth_finder": "iOS 17.1+ trên iPhone",
            "find_my": "Hệ sinh thái Apple",
            "generic": "Tùy ứng dụng",
        },
    ],
    "faq_title": "Câu hỏi thường gặp: Bluetooth Finder",
    "faq": FAQ,
    "structured_data": STRUCTURED,
}

out = json.dumps(TOP, ensure_ascii=False, indent=2) + "\n"
path = B / "vi_seo.json"
path.write_text(out, encoding="utf-8")
json.loads(out)
print("Wrote", path, path.stat().st_size)
