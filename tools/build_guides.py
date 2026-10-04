"""Generates the keyword guide pages (75-soft-challenge, best-75-hard-apps,
flexchallenge-vs-streaks) from the content below. Run: python3 tools/build_guides.py"""
import html, json, os, re

SITE = "https://flexchallenge.app"
APP = "https://apps.apple.com/us/app/flexchallenge/id6757351926"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = open(os.path.join(ROOT, "faq/index.html")).read()
CSS = re.search(r'(<style>[\s\S]*?)\n\s*@media \(max-width: 540px\)', CSS).group(1)
CSS += """
        .fc-legal .lede { font-size: 19px; color: #3E3B33; margin: 0 0 32px; }
        .fc-legal .prose h2 { font-size: 26px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.2; margin: 48px 0 12px; }
        .fc-legal .prose h3 { font-size: 19px; font-weight: 700; letter-spacing: -0.01em; margin: 28px 0 8px; }
        .fc-legal .tldr { background: var(--card); border: 2px solid var(--border); border-radius: 16px; padding: 20px 24px; }
        .fc-legal .tldr p:last-child, .fc-legal .tldr ul:last-child { margin-bottom: 0; }
        .fc-legal .table-scroll { overflow-x: auto; margin: 16px 0 8px; border: 2px solid var(--border); border-radius: 16px; background: var(--card); }
        .fc-legal table { border-collapse: collapse; width: 100%; min-width: 560px; font-size: 15px; }
        .fc-legal th, .fc-legal td { text-align: left; vertical-align: top; padding: 12px 14px; border-bottom: 1px solid var(--border); color: #3E3B33; }
        .fc-legal thead th { color: var(--text); font-weight: 700; background: rgba(22,21,15,0.04); }
        .fc-legal tbody th { color: var(--text); font-weight: 600; }
        .fc-legal tr:last-child th, .fc-legal tr:last-child td { border-bottom: 0; }
        .fc-legal .note { font-size: 14px; color: var(--muted); }
        .fc-legal .cta { margin: 48px 0 0; background: #16150F; color: #F2EFE7; border-radius: 16px; padding: 28px; }
        .fc-legal .cta h2 { color: #F2EFE7; margin: 0 0 8px; font-size: 24px; }
        .fc-legal .cta p { color: #D9D5CA; margin: 0 0 18px; }
        .fc-legal .cta a.btn { display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; background: #C8F222; color: #16150F; font-weight: 800; border-radius: 10px; }
        .fc-legal .cta a.btn:hover { text-decoration: none; }
        .fc-legal .related a { font-weight: 600; }
        .fc-legal table.compare th:nth-child(2), .fc-legal table.compare td:nth-child(2) { background: #E3F0FC; color: var(--text); border-left: 2px solid #0A72CD; border-right: 2px solid #0A72CD; font-weight: 600; }
        .fc-legal table.compare thead th:nth-child(2) { background: #0A72CD; color: #fff; font-size: 16px; }
        .fc-legal table.compare tbody tr:last-child td:nth-child(2) { border-bottom: 2px solid #0A72CD; }
        .fc-legal table.compare .badge { display: block; width: max-content; margin-bottom: 4px; padding: 1px 8px; border-radius: 999px; background: #C8F222; color: #16150F; font-size: 11px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
        .fc-legal table.compare.two { min-width: 0; }
        .fc-legal figure { margin: 28px 0; background: var(--card); border: 2px solid var(--border); border-radius: 16px; padding: 20px; }
        .fc-legal figure svg { display: block; width: 100%; height: auto; }
        .fc-legal figcaption { font-size: 14px; color: var(--muted); margin-top: 12px; line-height: 1.5; }
        .fc-legal blockquote { margin: 28px 0; padding: 4px 0 4px 22px; border-left: 4px solid #0A72CD; }
        .fc-legal blockquote p { font-size: 21px; line-height: 1.45; color: var(--text); font-weight: 600; letter-spacing: -0.01em; margin: 0 0 8px; }
        .fc-legal blockquote cite { font-style: normal; font-size: 14px; color: var(--muted); }
        .fc-legal .stat { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin: 24px 0; }
        .fc-legal .stat div { background: var(--card); border: 2px solid var(--border); border-radius: 14px; padding: 16px; }
        .fc-legal .stat b { display: block; font-size: 32px; font-weight: 800; letter-spacing: -0.02em; color: #0A72CD; line-height: 1.1; }
        .fc-legal .stat span { font-size: 14px; color: #3E3B33; line-height: 1.45; display: block; margin-top: 6px; }
        .fc-legal sup a { font-size: 12px; font-weight: 700; padding: 0 1px; }
        .fc-legal ol.sources { font-size: 14px; padding-left: 22px; }
        .fc-legal ol.sources li { font-size: 14px; color: var(--muted); margin-bottom: 8px; word-break: break-word; }
        .fc-legal .story { background: #16150F; color: #F2EFE7; border-radius: 16px; padding: 22px 24px; margin: 24px 0; }
        .fc-legal .story p { color: #E4E0D5; }
        .fc-legal .story p:last-child { margin-bottom: 0; }
        .fc-legal .y { color: #15803D; font-weight: 800; }
        .fc-legal .n { color: #B91C1C; font-weight: 800; }

        @media (max-width: 540px) {
            .fc-legal .legal-nav { flex-direction: column; gap: 12px; align-items: flex-start; }
            .fc-legal .legal-nav .nav-links { flex-wrap: wrap; gap: 4px 18px; }
            .fc-legal .legal-wrap { padding-top: 32px; }
            .fc-legal h1 { font-size: clamp(28px, 8vw, 36px); }
            .fc-legal .legal-footer { flex-direction: column; gap: 4px; }
            .fc-legal .prose h2 { font-size: 22px; }
            .fc-legal .cta { padding: 22px; }
        }
    </style>"""

GUIDES = [
    ("75-soft-challenge", "75 Soft Challenge rules"),
    ("best-75-hard-apps", "Best 75 Hard tracker apps"),
    ("flexchallenge-vs-streaks", "FlexChallenge vs Streaks"),
    ("challenge-based-lifestyle", "The challenge-based lifestyle"),
]

CTA = f"""
        <div class="cta">
            <h2>Start your challenge today</h2>
            <p>FlexChallenge for iPhone: pick a template or build your own, then check off every day until you finish. 14-day free trial, no account.</p>
            <a class="btn" href="{APP}">Download on the App Store</a>
        </div>"""


def page(slug, title, desc, eyebrow, h1, updated, body, faqs, ld_extra):
    url = f"{SITE}/{slug}/"
    related = " · ".join(f'<a href="/{s}/">{t}</a>' for s, t in GUIDES if s != slug)
    graph = [{
        "@type": "Article", "headline": h1, "description": desc, "url": url,
        "mainEntityOfPage": url, "image": f"{SITE}/og-image.jpg",
        "datePublished": "2026-10-04", "dateModified": updated,
        "author": {"@type": "Organization", "name": "FlexChallenge", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "FlexChallenge", "url": SITE + "/",
                      "logo": {"@type": "ImageObject", "url": SITE + "/icons/icon-512.png"}},
        "about": ld_extra,
    }, {
        "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "FlexChallenge", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": h1, "item": url}],
    }]
    faq_html = ""
    if faqs:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]})
        faq_html = '\n        <h2>Frequently asked questions</h2>\n' + "\n".join(
            f'        <div class="faq-item">\n            <h3>{html.escape(q)}</h3>\n            <p>{a}</p>\n        </div>' for q, a in faqs)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    t, d = html.escape(title), html.escape(desc)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id=6757351926">
<meta name="theme-color" content="#F2EFE7">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="article">
<meta property="og:site_name" content="FlexChallenge">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<script type="application/ld+json">
{ld}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>

<div class="fc-legal">
    {CSS.strip()}

    <nav class="legal-nav">
        <a href="/" class="brand">FlexChallenge</a>
        <div class="nav-links">
            <a href="/">App</a>
            <a href="/faq">FAQ</a>
            <a href="/support">Help</a>
            <a href="{APP}">Download</a>
        </div>
    </nav>

    <main class="legal-wrap prose">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="effective">Updated {updated_human(updated)}</p>
{body}
{faq_html}
{CTA}

        <p class="related">More guides: {related}</p>
    </main>

    <footer class="legal-footer">
        <span>© 2026 FlexChallenge</span>
        <span>
            <a href="/privacy">Privacy Policy</a> &nbsp;·&nbsp;
            <a href="/terms">Terms of Service</a> &nbsp;·&nbsp;
            <a href="/faq">FAQ</a> &nbsp;·&nbsp;
            <a href="/support">Support</a>
        </span>
    </footer>
</div>

</body>
</html>
"""


def updated_human(iso):
    import datetime
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B ") + str(d.day) + d.strftime(", %Y")


def write(slug, content):
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    with open(os.path.join(ROOT, slug, "index.html"), "w") as f:
        f.write(content)


import guides_content as C  # noqa: E402  (content lives next to this script)

import article_lifestyle as A  # noqa: E402

for g in C.PAGES + [A.PAGE]:
    write(g["slug"], page(**g))
print("built", [g["slug"] for g in C.PAGES + [A.PAGE]])
