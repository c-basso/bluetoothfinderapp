# GEO Audit: Bluetooth Finder Website

**Audit date:** February 6, 2026  
**Reference:** iOS app as described in `descr.txt`  
**Scope:** Landing page for Bluetooth Finder app (https://bluetoothfinderapp.com)  
**Goal:** Optimize for AI search visibility (ChatGPT, Perplexity, Claude, Google AI Overviews).

---

## App Summary (from descr.txt)

- **Bluetooth Finder** – iOS app to quickly locate lost Bluetooth devices (AirPods, smartwatches, headphones, etc.).
- **Features:** Hot & cold guidance, proximity percentage, detailed device info, works everywhere; free to download with optional in-app purchases.
- **Use case:** Find lost AirPods, smartwatches, headphones; for homes, offices, public transport.

---

## GEO Audit Checklist Score

| Category                | Score | Max | Notes |
|-------------------------|-------|-----|--------|
| 1. Entity Clarity       | 8     | 10  | Good definition; could be more neutral/Wikipedia-style. |
| 2. Quotable Facts       | 3     | 10  | Few specific numbers in body; no "by the numbers" section. |
| 3. FAQ Coverage         | 6     | 10  | FAQ in schema only—**not visible on page**; questions are LLM-friendly. |
| 4. Comparison Positioning | 0   | 10  | No comparison tables, no "alternative to" or competitor framing. |
| 5. Structural Clarity   | 5     | 10  | Good H1/H2; no tables, no TL;DR. |
| 6. Authority Signals   | 2     | 10  | Author in schema only; no "last updated" in content. |
| 7. Freshness            | 2     | 10  | No visible update date; year in footer only. |
| **Total**               | **26**| **70** | **Poor** – significant GEO improvements needed. |

**Target:** Raise to 45+ (Good) and ideally 60+ (Excellent) with the recommended changes.

---

## Detailed Findings

### 1. Entity Clarity (8/10)

- **Strengths:** First paragraph defines Bluetooth Finder clearly; name used consistently; category ("bluetooth finder app", "bluetooth device finder") is clear.
- **Gaps:** Relationship to other entities (e.g. "alternative to Find My for non-Apple devices") not stated; tone is slightly promotional ("ultimate", "best") rather than Wikipedia-style neutral.

### 2. Quotable Facts (3/10)

- **Strengths:** Some concrete details exist in `app_info` and schema (e.g. 50.9 MB, iOS 17.1, pricing).
- **Gaps:** No "by the numbers" or key-facts section in the main content; no specific statistics (e.g. "finds devices within X m", "supports X device types") that LLMs can quote. Numbers are not in standalone, easily extractable sentences.

### 3. FAQ Coverage (6/10)

- **Strengths:** FAQ exists in `en.json`; FAQPage schema is present; questions align with how users ask (What is, How does it work, AirPods, compatibility, etc.).
- **Critical gap:** The FAQ is **only in JSON-LD**. There is **no visible FAQ section** in `template.html`, so crawlers and users reading the HTML body do not see it. For GEO, the same Q&A should appear both in the page content and in FAQ schema.

### 4. Comparison Positioning (0/10)

- No comparison tables.
- No explicit competitor or "alternative to X" content (e.g. vs Find My, vs Tile, vs other finder apps).
- No "Bluetooth Finder vs …" framing that would help for comparison-style AI queries.

### 5. Structural Clarity (5/10)

- **Strengths:** Clear H1 and H2 hierarchy; short paragraphs.
- **Gaps:** No bullet lists for key facts; no comparison tables; no summary or TL;DR block at top or bottom.

### 6. Authority Signals (2/10)

- **Strengths:** Developer name (Vladimir Ivakhnenko) and app info in schema.
- **Gaps:** No author/credentials in visible body; no testimonials or customer names; no "Last updated" date in content (only in schema).

### 7. Freshness (2/10)

- **Strengths:** Footer shows 2026.
- **Gaps:** No "Last updated: [date]" in visible content; no changelog or news section; freshness not clearly signaled to LLMs.

---

## Technical Notes

- **Schema:** MobileApplication, Organization, WebSite, HowTo, FAQPage, BreadcrumbList are present—good.
- **llms.txt:** Not present. Adding `/llms.txt` is recommended for LLM discoverability.
- **Content vs descr.txt:** Page content aligns well with the iOS app description; no major factual mismatches.

---

## Recommendations (Priority Order)

1. **Add a visible FAQ section** — ✅ Done. Template shows FAQ from `seo.faq`; same Q&A in HTML and FAQPage schema.
2. **Add a "By the numbers" / Key facts section** — ✅ Done. `seo.key_facts` and section in template.
3. **Add a visible "Last updated" date** — ✅ Done. Footer shows `seo.last_updated`.
4. **Add `/llms.txt`** — ✅ Done. `llms.txt` at project root with description, key facts, and links.
5. **Add 1–2 comparison-style FAQs** — ✅ Done. Two comparison FAQs in `seo.faq` (vs Find My, alternative for non-Apple).
6. **Summary + comparison table** — ✅ Done. Summary/TL;DR at top of main (`content.summary_tldr`); comparison table section with Bluetooth Finder vs Find My vs generic scanner (`seo.comparison_title`, `seo.comparison_intro`, `seo.comparison_rows`).

---

## Test Queries for Monitoring

After implementing changes, test on Perplexity / ChatGPT / Claude:

- "What is Bluetooth Finder app?"
- "Best app to find lost AirPods"
- "Bluetooth finder app for iPhone"
- "How does Bluetooth Finder work?"
- "Bluetooth Finder vs Find My"
- "App to find lost Bluetooth devices iOS"

---

*Audit performed using the geo-optimization skill (GEO: Generative Engine Optimization).*
