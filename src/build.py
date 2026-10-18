#!/usr/bin/env python3
"""Builds the landing page in every language from one template.

Edit the strings below (or src/base.css), then run:

    python3 src/build.py

It writes index.html (English), fr/index.html, es/index.html and
sitemap.xml. Don't edit those by hand; they get overwritten.
"""
import html
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://getontap.net"
APP_ID = "6788189977"


def app_store(campaign):
    return (f"https://apps.apple.com/app/ontap-beer-tracker/id{APP_ID}"
            f"?pt=129131724&ct={campaign}&mt=8")


# Path on the site for each language. English is the root.
LANGS = {
    "en": {"path": "/", "locale": "en_GB", "name": "English"},
    "fr": {"path": "/fr/", "locale": "fr_CA", "name": "Français"},
    "es": {"path": "/es/", "locale": "es_ES", "name": "Español"},
}

T = {
    "en": {
        "title": "ontap: Beer Tracker & Beer Log App for iPhone",
        "description": "Log a beer in one tap, see which friends are out, earn badges, become Mayor of your local and race your squad. A free beer tracker for iPhone.",
        "og_title": "ontap: Log beers. See who's out.",
        "tagline": "Log beers. See who's out.",
        "subline": "One tap on your home screen logs a beer and the spot you're at. See which friends are out, earn badges and race your squad to the top.",
        "cta": "Download on the App Store",
        "free": "Free on iPhone · 18+",
        "iab": "Button not opening? Tap ••• (top right) → Open in Browser",
        "alt_widget": "ontap home screen widget logging a beer in one tap",
        "alt_friends": "ontap friends map showing who's out",
        "alt_lastcall": "ontap Last Call monthly recap",
        "features_title": "Made for nights out, not spreadsheets.",
        "features": [
            ("🍺", "One tap to log", "A home screen and lock screen widget logs a beer, with the venue you're at, in a single tap. No opening the app."),
            ("📍", "See who's out", "Add your mates and see who's already out and where on a shared map. Skip the group chat, just go."),
            ("🏅", "Badges and Mayors", "Earn 30+ badges for your nights out. Log the most at your local and you're its Mayor 👑"),
            ("🏁", "Squad races", "Start a squad with your crew and race week by week or month by month. Share the recap when you win."),
            ("🌍", "Taps from everywhere", "Watch taps roll in from around the world and see which bars and cities top the charts this month."),
            ("✨", "Last Call", "Every month, your beers, your spots and your nights out, wrapped up like a recap worth screenshotting."),
        ],
        "showcase_title": "Your month, wrapped.",
        "showcase_body": "ontap keeps a quiet tally of where you drink and who you're with, then hands it back at the end of the month: your top spots, your go-to night, your map filling up over time. You didn't keep a diary. You just tapped a button.",
        "faq_title": "Questions",
        "faq": [
            ("What is ontap?", "ontap is a beer tracker and beer log for iPhone. Tap once to log a beer and where you are, keep a diary of every pint, and get your stats and a recap every month."),
            ("Is ontap free?", "Yes. ontap is free to download and use on iPhone."),
            ("Who can see where I am?", "Only friends you've added see where you've logged a beer. You can turn off location sharing at any time in the app, and you only appear on the Global tab if you choose to."),
            ("Can I use it with my friends?", "Yes. Add friends to see who's out, tag them in your taps and start a squad to race each other each week or month."),
            ("How do I become Mayor of a bar?", "Log the most beers at a spot over the last 60 days, across at least two nights, and you're its Mayor until someone takes it."),
        ],
        "footer_line": "Log beers. See who's out.<br>For beer lovers of legal drinking age. Please drink responsibly.",
        "privacy": "Privacy", "terms": "Terms", "contact": "Contact",
    },
    "fr": {
        "title": "ontap : appli pour suivre tes bières sur iPhone",
        "description": "Note une bière en un tap, vois quels amis sont sortis, gagne des badges, deviens maire de ton bar et affronte ton équipe. Appli gratuite sur iPhone.",
        "og_title": "ontap : note tes bières. Vois qui est sorti.",
        "tagline": "Note tes bières. Vois qui est sorti.",
        "subline": "Un tap sur ton écran d'accueil note une bière et l'endroit où tu es. Vois quels amis sont sortis, gagne des badges et mène ton équipe au sommet.",
        "cta": "Télécharger sur l'App Store",
        "free": "Gratuit sur iPhone · 18+",
        "iab": "Le bouton ne s'ouvre pas ? Touche ••• (en haut à droite) → Ouvrir dans le navigateur",
        "alt_widget": "Widget ontap sur l'écran d'accueil qui note une bière en un tap",
        "alt_friends": "Carte ontap montrant quels amis sont sortis",
        "alt_lastcall": "Last Call, le bilan mensuel d'ontap",
        "features_title": "Fait pour les sorties, pas pour les tableurs.",
        "features": [
            ("🍺", "Un tap pour noter", "Un widget sur l'écran d'accueil et l'écran verrouillé note une bière, avec le bar où tu es, en un seul tap. Pas besoin d'ouvrir l'appli."),
            ("📍", "Vois qui est sorti", "Ajoute tes amis et vois qui est déjà sorti, et où, sur une carte partagée. Oublie le groupe de discussion, vas-y."),
            ("🏅", "Badges et maires", "Gagne plus de 30 badges pour tes soirées. Note le plus de bières dans ton bar et tu en deviens le maire 👑"),
            ("🏁", "Courses entre amis", "Crée une équipe avec ta gang et affrontez-vous chaque semaine ou chaque mois. Partage le bilan quand tu gagnes."),
            ("🌍", "Des taps partout", "Regarde les taps arriver du monde entier et découvre les bars et les villes en tête ce mois-ci."),
            ("✨", "Last Call", "Chaque mois, tes bières, tes endroits et tes soirées, réunis dans un bilan qui mérite une capture d'écran."),
        ],
        "showcase_title": "Ton mois, en résumé.",
        "showcase_body": "ontap garde un compte discret de là où tu bois et avec qui, puis te le rend à la fin du mois : tes endroits préférés, ton soir de sortie, ta carte qui se remplit. Tu n'as pas tenu de journal. Tu as juste touché un bouton.",
        "faq_title": "Questions",
        "faq": [
            ("C'est quoi, ontap ?", "ontap est une appli iPhone pour suivre et noter tes bières. Un tap note une bière et l'endroit où tu es, tu gardes un journal de chaque pinte et tu reçois tes stats et un bilan chaque mois."),
            ("ontap est-elle gratuite ?", "Oui. ontap est gratuite à télécharger et à utiliser sur iPhone."),
            ("Qui peut voir où je suis ?", "Seuls les amis que tu as ajoutés voient où tu as noté une bière. Tu peux désactiver le partage de position à tout moment dans l'appli, et tu n'apparais dans l'onglet Global que si tu le choisis."),
            ("Je peux l'utiliser avec mes amis ?", "Oui. Ajoute tes amis pour voir qui est sorti, identifie-les dans tes taps et crée une équipe pour vous affronter chaque semaine ou chaque mois."),
            ("Comment devenir maire d'un bar ?", "Note le plus de bières dans un endroit sur les 60 derniers jours, sur au moins deux soirées, et tu en es le maire jusqu'à ce que quelqu'un te le prenne."),
        ],
        "footer_line": "Note tes bières. Vois qui est sorti.<br>Pour les amateurs de bière ayant l'âge légal. À consommer avec modération.",
        "privacy": "Confidentialité", "terms": "Conditions", "contact": "Contact",
    },
    "es": {
        "title": "ontap: app para registrar tus cervezas en iPhone",
        "description": "Registra una cerveza con un toque, mira qué amigos han salido, gana insignias, conviértete en alcalde de tu bar y compite con tu grupo. Gratis en iPhone.",
        "og_title": "ontap: registra cervezas. Mira quién ha salido.",
        "tagline": "Registra cervezas. Mira quién ha salido.",
        "subline": "Un toque en tu pantalla de inicio registra una cerveza y el sitio donde estás. Mira qué amigos han salido, gana insignias y lleva a tu grupo a lo más alto.",
        "cta": "Descargar en el App Store",
        "free": "Gratis en iPhone · 18+",
        "iab": "¿No se abre el botón? Toca ••• (arriba a la derecha) → Abrir en el navegador",
        "alt_widget": "Widget de ontap en la pantalla de inicio registrando una cerveza con un toque",
        "alt_friends": "Mapa de ontap que muestra qué amigos han salido",
        "alt_lastcall": "Last Call, el resumen mensual de ontap",
        "features_title": "Hecha para salir, no para hojas de cálculo.",
        "features": [
            ("🍺", "Un toque para registrar", "Un widget en la pantalla de inicio y de bloqueo registra una cerveza, con el bar donde estás, con un solo toque. Sin abrir la app."),
            ("📍", "Mira quién ha salido", "Añade a tus amigos y mira quién ha salido ya y dónde en un mapa compartido. Olvídate del grupo, simplemente ve."),
            ("🏅", "Insignias y alcaldes", "Gana más de 30 insignias por tus noches. Registra más cervezas que nadie en tu bar y serás su alcalde 👑"),
            ("🏁", "Carreras en grupo", "Crea un grupo con tus amigos y competid semana a semana o mes a mes. Comparte el resumen cuando ganes."),
            ("🌍", "Cervezas de todo el mundo", "Mira cómo llegan cervezas de todo el mundo y descubre qué bares y ciudades lideran este mes."),
            ("✨", "Last Call", "Cada mes, tus cervezas, tus sitios y tus noches, en un resumen que merece una captura."),
        ],
        "showcase_title": "Tu mes, resumido.",
        "showcase_body": "ontap lleva la cuenta de dónde bebes y con quién, y te la devuelve a final de mes: tus sitios favoritos, tu noche de salir, tu mapa llenándose. No llevaste un diario. Solo tocaste un botón.",
        "faq_title": "Preguntas",
        "faq": [
            ("¿Qué es ontap?", "ontap es una app para iPhone para registrar tus cervezas. Un toque registra una cerveza y dónde estás, guardas un diario de cada pinta y recibes tus estadísticas y un resumen cada mes."),
            ("¿ontap es gratis?", "Sí. ontap es gratis para descargar y usar en iPhone."),
            ("¿Quién puede ver dónde estoy?", "Solo los amigos que has añadido ven dónde has registrado una cerveza. Puedes desactivar la ubicación compartida cuando quieras en la app, y solo apareces en la pestaña Global si tú lo eliges."),
            ("¿Puedo usarla con mis amigos?", "Sí. Añade amigos para ver quién ha salido, etiquétalos en tus cervezas y crea un grupo para competir cada semana o cada mes."),
            ("¿Cómo me convierto en alcalde de un bar?", "Registra más cervezas que nadie en un sitio en los últimos 60 días, en al menos dos noches, y serás su alcalde hasta que alguien te lo quite."),
        ],
        "footer_line": "Registra cervezas. Mira quién ha salido.<br>Para amantes de la cerveza mayores de edad. Bebe con moderación.",
        "privacy": "Privacidad", "terms": "Términos", "contact": "Contacto",
    },
}

EXTRA_CSS = """
  /* ---------- Added by src/build.py ---------- */
  /* width/height attributes are only there to reserve space; keep the ratio. */
  .phones img, .showcase img { height: auto; }
  .faq { max-width: 760px; margin: 80px auto 0; }
  .faq h2 { text-align: center; font-size: clamp(26px, 4vw, 38px); font-weight: 700; margin-bottom: 20px; }
  .faq details {
    background: var(--cream);
    border: 2.5px solid var(--brown);
    border-radius: 16px;
    box-shadow: 3px 3px 0 var(--brown);
    padding: 16px 20px;
    margin-top: 14px;
  }
  .faq summary { font-size: 18px; font-weight: 600; cursor: pointer; list-style: none; }
  .faq summary::-webkit-details-marker { display: none; }
  .faq summary::after { content: "+"; float: right; font-weight: 700; }
  .faq details[open] summary::after { content: "–"; }
  .faq details p { margin-top: 10px; font-size: 16px; font-weight: 500; line-height: 1.55; color: var(--brown-soft); }
  .langs { margin-top: 14px; font-size: 14px; }
  .langs a { margin: 0 8px; }
  .langs .here { margin: 0 8px; opacity: 0.6; }
"""


def esc(s):
    return html.escape(s, quote=True)


def page(lang):
    t = T[lang]
    meta = LANGS[lang]
    url = SITE + meta["path"]
    store = app_store("website" if lang == "en" else f"website-{lang}")
    css = open(os.path.join(ROOT, "src", "base.css")).read() + EXTRA_CSS

    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{m["path"]}">' for l, m in LANGS.items()
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'

    ld_app = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "ontap",
        "operatingSystem": "iOS",
        "applicationCategory": "LifestyleApplication",
        "description": t["description"],
        "url": url,
        "downloadUrl": f"https://apps.apple.com/app/id{APP_ID}",
        "image": f"{SITE}/og-image.jpg",
        "inLanguage": lang,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in t["faq"]
        ],
    }

    cards = "\n".join(
        f"""      <div class="card">
        <span class="icon">{icon}</span>
        <h3>{esc(h)}</h3>
        <p>{esc(p)}</p>
      </div>""" for icon, h, p in t["features"]
    )
    faqs = "\n".join(
        f"""      <details>
        <summary>{esc(q)}</summary>
        <p>{esc(a)}</p>
      </details>""" for q, a in t["faq"]
    )
    langs = " ".join(
        f'<span class="here">{m["name"]}</span>' if l == lang else f'<a href="{m["path"]}" hreflang="{l}">{m["name"]}</a>'
        for l, m in LANGS.items()
    )

    return f"""<!DOCTYPE html>
<!-- Generated by src/build.py. Edit that, not this file. -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["description"])}">
<link rel="canonical" href="{url}">
{alternates}
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta name="theme-color" content="#FBB615">
<link rel="icon" type="image/png" href="/logo.png">

<!-- Link previews in group chats / socials -->
<meta property="og:title" content="{esc(t["og_title"])}">
<meta property="og:description" content="{esc(t["description"])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{meta["locale"]}">
<meta property="og:site_name" content="ontap">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">{json.dumps(ld_app, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap" rel="stylesheet">

<style>
{css}</style>
</head>
<body>

<!-- ===== HERO ===== -->
<header>
  <span class="bubble" style="width:90px;height:90px;top:60px;left:8%;"></span>
  <span class="bubble" style="width:50px;height:50px;top:140px;left:82%;"></span>
  <span class="bubble" style="width:120px;height:120px;top:220px;left:74%;opacity:0.09;"></span>
  <span class="bubble" style="width:40px;height:40px;top:100px;left:24%;"></span>
  <span class="bubble" style="width:64px;height:64px;top:280px;left:12%;opacity:0.10;"></span>

  <div class="wrap">
    <img class="logo-img" src="/logo.png" alt="ontap" width="784" height="320">
    <h1 class="tagline">{esc(t["tagline"])}</h1>
    <p class="subline">{esc(t["subline"])}</p>

    <a class="cta" href="{store}">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M17.05 12.04c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.48.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.75 2.28-1.6 2.78-.41 6.89 1.15 9.14.76 1.1 1.67 2.34 2.86 2.29 1.15-.05 1.58-.74 2.97-.74 1.39 0 1.78.74 3 .72 1.24-.02 2.02-1.12 2.78-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.65zM14.77 5.3c.64-.78 1.07-1.86.95-2.94-.92.04-2.03.61-2.69 1.38-.59.69-1.11 1.79-.97 2.85 1.02.08 2.07-.52 2.71-1.29z"/></svg>
      {esc(t["cta"])}
    </a>
    <span class="comingsoon">{esc(t["free"])}</span>
    <span class="iab-hint">{esc(t["iab"])}</span>

    <div class="phones">
      <img src="/ss_widget.webp" alt="{esc(t["alt_widget"])}" width="600" height="1300">
      <img src="/ss_friends.webp" alt="{esc(t["alt_friends"])}" width="600" height="1300">
    </div>
  </div>
  <div class="foam"></div>
</header>

<!-- ===== FEATURES ===== -->
<section class="features below-foam">
  <div class="wrap">
    <h2 class="section-title">{esc(t["features_title"])}</h2>

    <div class="feature-grid">
{cards}
    </div>

    <div class="showcase">
      <img src="/ss_lastcall.webp" alt="{esc(t["alt_lastcall"])}" width="600" height="1300" loading="lazy">
      <div class="copy">
        <h2>{esc(t["showcase_title"])}</h2>
        <p>{esc(t["showcase_body"])}</p>
      </div>
    </div>

    <div class="faq">
      <h2>{esc(t["faq_title"])}</h2>
{faqs}
    </div>
  </div>
</section>

<!-- ===== FOOTER ===== -->
<footer>
  <div class="flogo">ontap</div>
  <p>{t["footer_line"]}</p>
  <div class="footer-links">
    <a href="https://lucapreston.github.io/ontap-legal/privacy/">{esc(t["privacy"])}</a>
    <a href="https://lucapreston.github.io/ontap-legal/terms/">{esc(t["terms"])}</a>
    <a href="mailto:luca@getontap.net">{esc(t["contact"])}</a>
  </div>
  <div class="langs">{langs}</div>
  <p style="margin-top:18px;opacity:0.6;font-size:13px;">© 2026 ontap · Montréal</p>
</footer>

</body>
</html>
"""


def sitemap():
    today = date.today().isoformat()
    entries = []
    for l, m in LANGS.items():
        alts = "\n".join(
            f'    <xhtml:link rel="alternate" hreflang="{l2}" href="{SITE}{m2["path"]}"/>'
            for l2, m2 in LANGS.items()
        )
        entries.append(f"""  <url>
    <loc>{SITE}{m["path"]}</loc>
    <lastmod>{today}</lastmod>
{alts}
  </url>""")
    return ("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
""" + "\n".join(entries) + "\n</urlset>\n")


if __name__ == "__main__":
    for lang, meta in LANGS.items():
        out = os.path.join(ROOT, meta["path"].strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(page(lang))
        print("wrote", os.path.relpath(out, ROOT))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print("wrote sitemap.xml")
