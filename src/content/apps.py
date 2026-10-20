"""One description per app, reused by every list and comparison so they never
contradict each other. Keep claims to things we checked (Oct 2026) and say
'check the App Store' rather than quote prices we couldn't confirm."""
from .render import esc, store_link

APPS = {
    "ontap": {
        "name": "ontap",
        "what": "Log a beer in one tap from a home or lock screen widget, with the bar you're at. See which friends are out on a shared map, race your friends in squads, earn 30+ badges and become Mayor of your local. Every month you get Last Call, a recap worth sharing.",
        "platforms": "iPhone",
        "price": "Free (an optional ontap Pro is coming)",
        "best": "Groups of friends who go out together and want logging to take one tap.",
        "missing": "No beer-by-beer ratings or tasting notes, and no Android app yet.",
        "url": None,
    },
    "untappd": {
        "name": "Untappd",
        "what": "The best-known beer check-in app: scan or search a specific beer, rate it, add notes and photos, and collect badges. Huge beer database and venue menus from bars that use Untappd for Business.",
        "platforms": "iPhone, Android, web",
        "price": "Free, with an optional paid tier (Untappd Insiders) for extra stats and badges",
        "best": "Beer geeks who want to rate every individual beer they try.",
        "missing": "Logging means finding the exact beer each time, which is slow on a night out. Less about seeing which friends are out right now.",
        "url": "https://untappd.com",
    },
    "drinkaware": {
        "name": "MyDrinkaware",
        "what": "The UK alcohol charity Drinkaware's free tracker: log drinks to see units and calories, set goals, mark drink-free days and see how your week compares.",
        "platforms": "iPhone, Android",
        "price": "Free",
        "best": "Anyone mainly trying to keep an eye on units or cut down.",
        "missing": "Not social, and nothing about where you were or who you were with.",
        "url": "https://www.drinkaware.co.uk/tools/mydrinkaware-app",
    },
    "swarm": {
        "name": "Swarm (Foursquare)",
        "what": "Check in to any place, from pubs to airports, keep a searchable history of everywhere you've been and see friends' check-ins. Took over Foursquare City Guide's features in 2024.",
        "platforms": "iPhone, Android",
        "price": "Free",
        "best": "People who want a diary of every place they go, not just bars.",
        "missing": "No beer counting, recaps or drinking-specific features.",
        "url": "https://www.swarmapp.com",
    },
    "beli": {
        "name": "Beli",
        "what": "Rank restaurants, bars, cafés and bakeries by comparing each new place with ones you've already been to. Builds a personal score and recommendations, with friends' lists in a feed.",
        "platforms": "iPhone, Android",
        "price": "Free",
        "best": "Food-first people who want a ranked list of favourite spots.",
        "missing": "Built around restaurants; no beer logging, counts or live 'who's out'.",
        "url": "https://beliapp.com",
    },
    "beermenus": {
        "name": "BeerMenus",
        "what": "Find which bars, restaurants and shops near you pour or sell a particular beer, follow beers and venues for alerts, and keep a simple log of what you drank. Strongest in the US.",
        "platforms": "iPhone, Android, web",
        "price": "Free",
        "best": "Hunting down a specific beer nearby (mainly US).",
        "missing": "Light on social features; coverage outside the US is thinner.",
        "url": "https://www.beermenus.com",
    },
    "pintplease": {
        "name": "Pint Please",
        "what": "A Finnish-born beer rating app: rate beers, note where you had them and discover new ones, with brewery and pub pages.",
        "platforms": "iPhone (check Google Play for Android)",
        "price": "Free (in-app purchases)",
        "best": "A smaller, Europe-flavoured alternative to Untappd for rating beers.",
        "missing": "Much smaller community than Untappd.",
        "url": "https://www.pintplease.com",
    },
    "camra": {
        "name": "CAMRA Good Beer Guide app",
        "what": "The Campaign for Real Ale's guide to thousands of UK pubs serving good real ale, with pub details and maps, from the people behind the printed Good Beer Guide.",
        "platforms": "iPhone, Android",
        "price": "Check the App Store for the current price",
        "best": "Real-ale fans looking for a proper pub anywhere in the UK.",
        "missing": "UK only and no social or logging features.",
        "url": "https://camra.org.uk",
    },
    "snapmap": {
        "name": "Snap Map (Snapchat)",
        "what": "See friends who share their location on a map inside Snapchat, plus public Stories from around you.",
        "platforms": "iPhone, Android",
        "price": "Free",
        "best": "Friend groups who already live in Snapchat.",
        "missing": "Location only, and not always real time; nothing about nights out, beers or recaps.",
        "url": None,
    },
    "findmy": {
        "name": "Find My (Apple)",
        "what": "Apple's built-in location sharing: share where you are with chosen friends or family, indefinitely or for an hour.",
        "platforms": "iPhone (built in)",
        "price": "Free",
        "best": "Simple, private location sharing with a few close people.",
        "missing": "No social feed, no venues, nothing beyond a dot on a map.",
        "url": None,
    },
    "gmaps": {
        "name": "Google Maps location sharing",
        "what": "Share your real-time location with chosen contacts from Google Maps, on iPhone or Android, and save lists of pubs to visit.",
        "platforms": "iPhone, Android",
        "price": "Free",
        "best": "Mixed iPhone/Android groups, and for saving lists of places.",
        "missing": "Not social; you have to set sharing up per person.",
        "url": None,
    },
}


def card(key, rank=None, tag=None, best=None):
    a = APPS[key]
    title = (f"{rank}. " if rank else "") + a["name"]
    link = ""
    if key == "ontap":
        link = f' · <a href="{store_link("site-card")}">App Store</a>'
    elif a["url"]:
        link = f' · <a href="{a["url"]}" rel="nofollow noopener">Website</a>'
    tag_html = f'<span class="tag">{esc(tag)}</span><br>' if tag else ""
    return f"""<div class="appcard">{tag_html}<h3>{esc(title)}</h3>
<p>{esc(a["what"])}</p>
<dl><dt>Platforms</dt><dd>{esc(a["platforms"])}{link}</dd>
<dt>Price</dt><dd>{esc(a["price"])}</dd>
<dt>Best for</dt><dd>{esc(best or a["best"])}</dd>
<dt>Watch out</dt><dd>{esc(a["missing"])}</dd></dl></div>"""


DISCLOSURE = ('<div class="note"><b>Full disclosure:</b> we make ontap, so it\'s on this list. '
              'We\'ve tried to be fair about what every app does well and where ours isn\'t the right fit.</div>')
