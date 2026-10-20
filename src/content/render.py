"""Renders guides, tools and listicles (see pages.py) with one template."""
import html
import json
import os
from datetime import date

SITE = "https://getontap.net"
APP_ID = "6788189977"


def esc(s):
    return html.escape(s, quote=True)


def store_link(campaign):
    return (f"https://apps.apple.com/app/ontap-beer-tracker/id{APP_ID}"
            f"?pt=129131724&ct={campaign}&mt=8")


ARTICLE_CSS = """
  body { background: var(--foam); }
  .topbar { background: var(--amber); border-bottom: 2.5px solid var(--brown); }
  .topbar .wrap { display: flex; align-items: center; gap: 18px; padding: 10px 24px; }
  .topbar img { height: 34px; width: auto; display: block; }
  .topbar nav { margin-left: auto; display: flex; gap: 16px; align-items: center; }
  .topbar nav a { color: var(--brown); font-weight: 600; text-decoration: none; font-size: 15px; }
  .topbar nav a.get { background: var(--brown); color: var(--cream); padding: 8px 14px; border-radius: 12px; }
  article { max-width: 760px; margin: 0 auto; padding: 34px 22px 60px; color: var(--brown); }
  .crumbs { font-size: 13px; color: var(--brown-soft); margin-bottom: 14px; }
  .crumbs a { color: var(--brown-soft); }
  article h1 { font-size: clamp(30px, 5vw, 44px); line-height: 1.1; margin-bottom: 12px; }
  .lede { font-size: 19px; line-height: 1.55; color: var(--brown-soft); font-weight: 500; }
  .meta { font-size: 13px; color: var(--brown-soft); margin: 14px 0 26px; opacity: .85; }
  article h2 { font-size: 26px; margin: 34px 0 10px; line-height: 1.2; }
  article h3 { font-size: 20px; margin: 22px 0 6px; }
  article p, article li { font-size: 17px; line-height: 1.65; font-weight: 500; color: #4a2c12; }
  article p { margin: 10px 0; }
  article ul, article ol { margin: 10px 0 10px 22px; }
  article li { margin: 6px 0; }
  article a { color: #9a4f0a; font-weight: 600; }
  article table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 15.5px; }
  article th, article td { text-align: left; padding: 9px 10px; border-bottom: 1.5px solid #ead9bd; vertical-align: top; }
  article th { background: var(--cream); font-weight: 700; }
  .note { background: var(--cream); border: 2px solid var(--brown); border-radius: 16px; padding: 14px 16px; margin: 18px 0; box-shadow: 3px 3px 0 var(--brown); }
  .appcard { border: 2.5px solid var(--brown); border-radius: 18px; padding: 16px 18px; margin: 18px 0; background: #fff; box-shadow: 4px 4px 0 var(--brown); }
  .appcard h3 { margin: 0 0 4px; }
  .appcard .tag { display: inline-block; font-size: 12px; font-weight: 700; background: var(--amber); border-radius: 999px; padding: 2px 10px; margin-bottom: 6px; }
  .appcard dl { display: grid; grid-template-columns: 110px 1fr; gap: 4px 10px; margin-top: 8px; font-size: 15px; }
  .appcard dt { font-weight: 700; }
  .appcard dd { margin: 0; color: #4a2c12; }
  .cta { background: var(--amber); border: 2.5px solid var(--brown); border-radius: 20px; padding: 20px; margin: 34px 0; box-shadow: 4px 4px 0 var(--brown); text-align: center; }
  .cta p { color: var(--brown); font-weight: 600; margin: 0 0 12px; }
  .cta a.btn { display: inline-block; background: var(--brown); color: var(--cream); text-decoration: none; padding: 13px 22px; border-radius: 14px; font-weight: 600; font-size: 17px; }
  .faq details { background: #fff; border: 2px solid var(--brown); border-radius: 14px; padding: 12px 16px; margin-top: 10px; }
  .faq summary { font-weight: 700; cursor: pointer; font-size: 17px; }
  .related { margin-top: 36px; }
  .related ul { list-style: none; margin-left: 0; display: grid; gap: 8px; }
  .related a { text-decoration: none; }
  .tool { background: #fff; border: 2.5px solid var(--brown); border-radius: 20px; padding: 18px; margin: 20px 0; box-shadow: 4px 4px 0 var(--brown); }
  .tool label { display: block; font-weight: 700; font-size: 15px; margin: 10px 0 4px; }
  .tool input, .tool select { width: 100%; font: inherit; font-size: 17px; padding: 10px 12px; border: 2px solid #d9c3a0; border-radius: 12px; background: var(--foam); color: var(--brown); }
  .tool .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .tool .out { margin-top: 16px; background: var(--cream); border-radius: 14px; padding: 14px; font-size: 18px; font-weight: 600; }
  .tool .out b { font-size: 26px; }
  .tool button { font: inherit; font-weight: 600; background: var(--brown); color: var(--cream); border: 0; border-radius: 12px; padding: 10px 16px; margin-top: 12px; cursor: pointer; }
  .hub { display: grid; gap: 12px; margin-top: 18px; }
  .hub a { display: block; background: #fff; border: 2px solid var(--brown); border-radius: 16px; padding: 14px 16px; text-decoration: none; color: var(--brown); box-shadow: 3px 3px 0 var(--brown); }
  .hub a span { display: block; font-size: 14px; color: var(--brown-soft); font-weight: 500; margin-top: 3px; }
  @media (max-width: 600px) { .topbar nav a:not(.get) { display: none; } .tool .row { grid-template-columns: 1fr; } .appcard dl { grid-template-columns: 1fr; } }
"""


def faq_html(faq):
    if not faq:
        return ""
    items = "\n".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faq)
    return f'<section class="faq"><h2>FAQ</h2>{items}</section>'


def cta_html(campaign, text=None):
    text = text or "ontap is the free iPhone app for logging beers in one tap and seeing which friends are out."
    return (f'<div class="cta"><p>{esc(text)}</p>'
            f'<a class="btn" href="{store_link(campaign)}">Get ontap free on the App Store</a></div>')


def page_html(p, all_published):
    """p: a Page from pages.py. all_published: published pages, for related links."""
    base_css = open(os.path.join(os.path.dirname(__file__), "..", "base.css")).read()
    url = f"{SITE}/{p.slug}/"
    crumb_name = {"tool": "Tools", "best": "Guides", "alt": "Guides", "city": "Pint prices", "page": "ontap"}[p.kind]
    crumb_url = {"tool": "/tools/", "best": "/guides/", "alt": "/guides/", "city": "/pint-prices/", "page": "/"}[p.kind]

    related = [r for r in all_published if r.slug in p.related] or \
              [r for r in all_published if r.kind == p.kind and r.slug != p.slug][:4]
    related_html = ""
    if related:
        related_html = '<section class="related"><h2>Keep reading</h2><ul>' + "".join(
            f'<li><a href="/{r.slug}/">{esc(r.title)}</a></li>' for r in related[:5]) + "</ul></section>"

    ld = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": p.title,
        "description": p.description,
        "datePublished": p.publish,
        "dateModified": p.updated or p.publish,
        "author": {"@type": "Organization", "name": "ontap", "url": SITE},
        "publisher": {"@type": "Organization", "name": "ontap", "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.png"}},
        "mainEntityOfPage": url,
        "image": f"{SITE}/og-image.jpg",
    }, {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ontap", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb_name, "item": SITE + crumb_url},
            {"@type": "ListItem", "position": 3, "name": p.title, "item": url},
        ],
    }]
    if p.faq:
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}}
                           for q, a in p.faq],
        })
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    updated = f" · Updated {_nice(p.updated)}" if p.updated and p.updated != p.publish else ""

    return f"""<!DOCTYPE html>
<!-- Generated by src/build.py from src/content/. Edit those, not this file. -->
<html lang="{p.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p.title)}</title>
<meta name="description" content="{esc(p.description)}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta name="theme-color" content="#FBB615">
<link rel="icon" type="image/png" href="/logo.png">
<meta property="og:title" content="{esc(p.title)}">
<meta property="og:description" content="{esc(p.description)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:site_name" content="ontap">
<meta name="twitter:card" content="summary_large_image">
{ld_html}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap" rel="stylesheet">
<style>
{base_css}{ARTICLE_CSS}</style>
</head>
<body>
<div class="topbar"><div class="wrap">
  <a href="/"><img src="/logo.png" alt="ontap" width="784" height="320"></a>
  <nav><a href="/guides/">Guides</a><a href="/tools/">Free tools</a><a href="/pint-prices/">Pint prices</a>
  <a class="get" href="{store_link('site-' + p.slug)}">Get the app</a></nav>
</div></div>
<article>
  <div class="crumbs"><a href="/">ontap</a> › <a href="{crumb_url}">{crumb_name}</a></div>
  <h1>{esc(p.h1 or p.title)}</h1>
  <p class="lede">{p.lede}</p>
  <div class="meta">By the ontap team · {_nice(p.publish)}{updated}</div>
  {p.body}
  {cta_html('site-' + p.slug, p.cta)}
  {faq_html(p.faq)}
  {related_html}
</article>
<footer>
  <div class="flogo">ontap</div>
  <p>Log beers. See who's out.<br>For beer lovers of legal drinking age. Please drink responsibly.</p>
  <div class="footer-links">
    <a href="/guides/">Guides</a> <a href="/tools/">Free tools</a> <a href="/pint-prices/">Pint prices</a>
    <a href="https://lucapreston.github.io/ontap-legal/privacy/">Privacy</a>
    <a href="mailto:luca@getontap.net">Contact</a>
  </div>
  <p style="margin-top:18px;opacity:0.6;font-size:13px;">© 2026 ontap · Montréal</p>
</footer>
</body>
</html>
"""


def hub_html(slug, title, description, intro, pages):
    """A listing page (/guides/, /tools/, /pint-prices/)."""
    base_css = open(os.path.join(os.path.dirname(__file__), "..", "base.css")).read()
    items = "".join(f'<a href="/{p.slug}/">{esc(p.title)}<span>{esc(p.description)}</span></a>' for p in pages)
    url = f"{SITE}/{slug}/"
    return f"""<!DOCTYPE html>
<!-- Generated by src/build.py. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="icon" type="image/png" href="/logo.png">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap" rel="stylesheet">
<style>
{base_css}{ARTICLE_CSS}</style>
</head>
<body>
<div class="topbar"><div class="wrap">
  <a href="/"><img src="/logo.png" alt="ontap" width="784" height="320"></a>
  <nav><a href="/guides/">Guides</a><a href="/tools/">Free tools</a><a href="/pint-prices/">Pint prices</a>
  <a class="get" href="{store_link('site-' + slug)}">Get the app</a></nav>
</div></div>
<article>
  <h1>{esc(title)}</h1>
  <p class="lede">{intro}</p>
  <div class="hub">{items}</div>
  {cta_html('site-' + slug)}
</article>
<footer>
  <div class="flogo">ontap</div>
  <p>Log beers. See who's out.<br>For beer lovers of legal drinking age. Please drink responsibly.</p>
  <p style="margin-top:18px;opacity:0.6;font-size:13px;">© 2026 ontap · Montréal</p>
</footer>
</body>
</html>
"""


def _nice(iso):
    d = date.fromisoformat(iso)
    return d.strftime("%-d %B %Y")


def _strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)
