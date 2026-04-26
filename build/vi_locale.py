# Vietnamese copy for build/vi.json (keys match pl.json top-level).
import json
from pathlib import Path

B = Path(__file__).parent
_SEO = json.loads((B / "vi_seo.json").read_text(encoding="utf-8"))

VI = {
    "meta": {
        "lang": "vi",
        "title": "Bluetooth Finder - Tìm thiết bị Bluetooth thất lạc | AirPods, đồng hồ, tai nghe",
        "description": "Bluetooth Finder giúp tìm AirPods, đồng hồ, tai nghe, loa Bluetooth đang bật gần bạn. Cặp nóng–lạnh bốn bước (lạnh, ấm, nóng, rất nóng) và phần trăm gần. Cần iOS 17.1 trở lên. Tải trên App Store thường miễn phí; mua trong ứng dụng theo mô tả tại store.",
        "keywords": "tìm bluetooth, tìm airpod, ứng dụng tìm tai nghe, quét bluetooth, iPhone, thiết bị gần, tìm đồ bluetooth, theo dõi bluetooth, loa bluetooth",
        "author": "Bluetooth Finder",
        "og_url": "https://bluetoothfinderapp.com/vi/",
        "og_title": "Bluetooth Finder - Tìm thiết bị Bluetooth gần bạn",
        "og_description": "Quét, nóng–lạnh, %: AirPods, đồng hồ, tai nghe khi còn trong tầm. iOS 17.1+; iPhone; tải thường miễn phí, có thể mua thêm trong app.",
        "og_image": "https://bluetoothfinderapp.com/site_preview.png",
        "og_image_alt": "Bluetooth Finder - tìm thiết bị",
        "og_image_width": "1140",
        "og_image_height": "599",
        "og_locale": "vi_VN",
        "twitter_url": "https://bluetoothfinderapp.com/vi/",
        "twitter_title": "Bluetooth Finder - Tìm nhanh thiết bị Bluetooth",
        "twitter_description": "AirPods, đồng hồ, loa. Bốn bước: lạnh, ấm, nóng, rất nóng, và %.",
        "twitter_image": "https://bluetoothfinderapp.com/site_preview.png",
        "twitter_image_alt": "Bluetooth Finder",
        "twitter_image_width": "1140",
        "twitter_image_height": "599",
        "canonical": "https://bluetoothfinderapp.com/vi/",
        "og_type": "website",
        "twitter_card": "summary_large_image",
        "theme_color": "#0A0E27",
        "apple_mobile_web_app_status_bar_style": "default",
    },
    "header": {
        "application_name": "Bluetooth Finder – tìm thiết bị Bluetooth",
        "app_name_suffix": "Tìm thiết bị Bluetooth",
        "logo_alt": "Logo Bluetooth Finder: AirPods, smartwatch, tai nghe",
        "app_name": "Bluetooth Finder",
        "title": "Bluetooth Finder",
        "tagline": "Lấy lại đồ bị mất dễ hơn.",
        "download_text": "Tải trên App Store",
        "download_aria_label": "Tải Bluetooth Finder từ App Store",
        "download_img_alt": "Tải Bluetooth Finder trên App Store",
    },
    "screenshots": {
        "items": [
            {"src": "/img/1_cover_12_framed.webp", "alt": "Bluetooth Finder - màn hình chính"},
            {"src": "/img/2_scan_12_framed.webp", "alt": "Bluetooth Finder - quét"},
            {"src": "/img/3_track_12_framed.webp", "alt": "Bluetooth Finder - theo dõi"},
            {"src": "/img/4_info_12_framed.webp", "alt": "Bluetooth Finder - thông tin"},
        ],
    },
    "content": {
        "summary_label": "Tóm tắt",
        "summary_tldr": "Bluetooth Finder là ứng dụng trên iPhone (iOS) hỗ trợ tìm AirPods, đồng hồ, loa và thiết bị Bluetooth đang bật gần. Cặp nóng–lạnh bốn bước (lạnh, ấm, nóng, rất nóng) cùng phần trăm ước lượng. Khác với Find My — không thay mọi kịch bản một-một, mà hướng tới tìm theo tín hiệu trong vùng phủ. Tải thường miễn phí, cần iOS 17.1+.",
        "intro1": "Bạn từng bỏ quên <strong>tai nghe in-ear</strong>, <strong>vòng đeo</strong> hay <strong>loa</strong> không? <strong>Bluetooth Finder</strong> là công cụ <em>quét và tìm Bluetooth gần</em>: mở danh sách, chọn đúng dòng, đi theo cặp bước và %, biết bạn đang tới gần hay rời — tiện khi vội ra khỏi phòng hoặc lục tìm cả gian phòng.",
        "intro2": "Danh sách gần cập nhật nhanh, bớt phải tìm từng nơi mù. Chỉ số mang tính gợi ý: tường, kim loại, đám đông và pin làm tín hiệu đổi — đọc tổng hợp, đừng tách một con số mà tưởng tượng từng mét.",
    },
    "features": {
        "title": "Tại sao Bluetooth Finder nổi bật",
        "subtitle": "Bạn nhận được thực tế",
        "items": [
            {
                "number": "1",
                "title": "Quét nhanh",
                "description": "Sau khi bật quyền, ứng dụng bắt thiết bị đang phát trong tầm và lấp danh sách, thường không cần cài đặt phức tạp: kết quả hiện sớm.",
            },
            {
                "number": "2",
                "title": "Nóng–lạnh: lạnh, ấm, nóng, rất nóng",
                "description": "Các bước mô tả: lạnh tức tín hiệu yếu hoặc xa; ấm và nóng — bạn tới gần; rất nóng — tầm tới tay. Dựa cường độ, không bằng thước, nhưng cảm nhận tới gần hay lùi xa hơn.",
            },
            {
                "number": "3",
                "title": "Phần trăm gần (%)",
                "description": "Cao hơn thường gợi ý gần hơn theo tín hiệu, nhưng không tương đương bảng đo. Đọc cùng cặp nóng–lạnh, không tách số lẻ.",
            },
            {
                "number": "4",
                "title": "Thông tin thiết bị",
                "description": "Có tên, hãng, mẫu trên danh sách thì dễ tách cả chục tai nghe trong cùng phòng hay văn phòng.",
            },
            {
                "number": "5",
                "title": "Hôm nay ở nhà, mai trên tàu",
                "description": "Hiệu quả khi sóng bật và còn trong tầm. Tìm AirPods, vòng, loa giúp bớt lục từng hộc khi tín hiệu và cảnh quan hợp, không bảo đảm mọi tình.",
            },
        ],
    },
    "how_to": {
        "title": "Cách dùng Bluetooth Finder",
        "description": "Mở app, cho quyền Bluetooth, đợi quét, chạm dòng đúng tai nghe hoặc loa. Bước quanh phòng, xem: lạnh, ấm, nóng, rất nóng và %; khi rất nóng và % cao, thiết bị rất gần, kiểm tra thử điểm. Chỗ đông, chọn tên bạn ở danh sách trước.",
    },
    "why_love": {
        "title": "Dùng để làm gì",
        "description": "Ít đi vòng, nhiều tín hiệu: cặp nóng–lạnh, % hỗ trợ, trong phòng, ngoài sân, thiết bị vẫn phát Bluetooth, giao diện mau. Phù hợp mất thứ nhỏ: văn phòng, tàu, sofa.",
    },
    "who_should_use": {
        "title": "Dành cho ai",
        "description": "Người dùng AirPods, in-ear, đồng hồ, dây đeo, loa, đi làm, đi học, ồn ào: trước hết thu hẹp vùng, sau đó tìm bằng tay và mắt.",
    },
    "advanced_features": {
        "title": "Thông tin thêm",
        "description": "Danh sách gần cập nhật trực tiếp, bước + % tóm nhanh hơn, ứng dụng nhẹ. Một số tính năng mua thêm, luôn xem App Store. Tải, pin, nền, phụ thuộc cách dùng.",
    },
    "final_cta": {
        "title": "Tải Bluetooth Finder hôm nay",
        "paragraph1": "Đừng tốn thời gian đi vòng. <a href=\"__APP_STORE_URL__\" rel=\"noopener noreferrer\">Mở App Store</a> dùng cặp nóng–lạnh và % để lấy lại AirPods, đồng hồ, loa hoặc thiết bị Bluetooth đang bật trong tầm, bớt căng thay vì tìm mò.",
        "cta_text": "Tải trên App Store",
        "cta_aria_label": "Tải Bluetooth Finder từ App Store",
        "cta_img_alt": "Tải Bluetooth Finder trên App Store",
    },
    "footer": {
        "copyright": "© 2026 Bluetooth Finder. Bảo lưu mọi quyền.",
    },
    "app_info": {
        "category": "Hiệu suất",
        "languages": "Tiếng Việt (trang này), English",
        "compatibility": "Cần iOS 17.1 trở lên",
    },
    "seo": _SEO,
}
