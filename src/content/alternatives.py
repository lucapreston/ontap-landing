from .pages import Page
from .apps import card, DISCLOSURE

UNTAPPD = Page(
    slug="untappd-alternatives",
    kind="alt",
    keyword="untappd alternatives",
    title="5 Untappd Alternatives in 2026 (Faster, Simpler or More Social)",
    description="Looking for an Untappd alternative? Compare ontap, Pint Please, BeerMenus, MyDrinkaware and Swarm: what they do better, and what you'd miss.",
    lede="Untappd is brilliant for rating beers, but searching for the exact beer every round gets old on a night out. If you want something <b>faster, simpler or more about your friends</b>, here are the best alternatives.",
    publish="2026-10-21",
    body=DISCLOSURE + """
<h2>Why people look for an Untappd alternative</h2>
<ul>
<li><b>Logging is slow:</b> finding the exact beer and rating it takes a minute you don't always have.</li>
<li><b>It's about the beer, not the night:</b> great for styles and breweries, less about where you went and who you were with.</li>
<li><b>The best extras are paid:</b> deeper stats and data export sit in the Untappd Insiders tier.</li>
</ul>
<h2>The alternatives</h2>
""" + card("ontap", 1, "Best for speed and friends") + """
<p><b>Compared with Untappd:</b> ontap logs in one tap from a widget instead of a search, and focuses on the night rather than the beer: which friends are out, squads, Mayors of your local and a monthly recap. You lose detailed ratings and tasting notes. Many people run both: ontap for every pint, Untappd for the special ones.</p>
""" + card("pintplease", 2, "Best like-for-like rating app") + card("beermenus", 3, "Best for finding beers (US)") + card("drinkaware", 4, "Best if you want to count, not rate") + card("swarm", 5, "Best for logging every place you go") + """
<h2>ontap vs Untappd at a glance</h2>
<table>
<tr><th></th><th>ontap</th><th>Untappd</th></tr>
<tr><td>Log a beer</td><td>One tap from a widget</td><td>Search for the beer, then check in</td></tr>
<tr><td>Ratings and tasting notes</td><td>No</td><td>Yes</td></tr>
<tr><td>See which friends are out now</td><td>Yes, on a map</td><td>Friends' activity feed</td></tr>
<tr><td>Friend group competitions</td><td>Squads, weekly and monthly</td><td>No</td></tr>
<tr><td>Badges</td><td>30+</td><td>Hundreds</td></tr>
<tr><td>Monthly recap</td><td>Last Call, every month</td><td>Stats (more with Insiders)</td></tr>
<tr><td>Platforms</td><td>iPhone</td><td>iPhone, Android, web</td></tr>
</table>
""",
    faq=[
        ("Is there a simpler app than Untappd?", "Yes. ontap logs a beer in one tap from your home screen, without searching for the exact beer."),
        ("Can I use ontap and Untappd together?", "Absolutely. They do different jobs: ontap for nights out and friends, Untappd for rating specific beers."),
        ("Is Untappd free?", "Yes, with an optional paid tier, Untappd Insiders, for extra stats, badges and data export."),
    ],
    related=["best-beer-tracking-apps", "ratebeer-alternatives", "best-beer-rating-apps"],
)

RATEBEER = Page(
    slug="ratebeer-alternatives",
    kind="alt",
    keyword="ratebeer alternative",
    title="RateBeer Alternatives: Where to Go Now RateBeer Has Shut Down",
    description="RateBeer went offline in February 2025. These are the best RateBeer alternatives in 2026 for rating beers, keeping a beer log and finding good bars.",
    lede="RateBeer announced its closure in December 2024 and went offline on <b>3 February 2025</b>, ending a 25-year run. If you were a RateBeer user, here's where to take your beer habit next.",
    publish="2026-10-23",
    body=DISCLOSURE + """
<h2>What happened to RateBeer?</h2>
<p>RateBeer announced on 18 December 2024 that it would stop operating, set an export deadline of 18 January 2025, and went fully offline on 3 February 2025 (<a href="https://www.beeradvocate.com/ratebeer/" rel="nofollow noopener">source</a>). Former users have reportedly still been able to request their old ratings by email.</p>
<h2>The best RateBeer alternatives</h2>
""" + card("untappd", 1, "Closest replacement") + """
<p>The obvious home for ex-RateBeer users: the biggest beer database, ratings out of five and a huge community. You won't get RateBeer's style-adjusted scores, but you'll find almost every beer.</p>
""" + card("pintplease", 2, "Best smaller community") + """
<h3>3. BeerAdvocate (website)</h3>
<p>The other long-running review site. Its reviews and forums are still active on the web; we couldn't confirm a current app, so use it in the browser. BeerAdvocate has a page explaining RateBeer's closure.</p>
""" + card("ontap", 4, "Best if you're done with ratings") + """
<p>If what you really enjoyed was the record of where you'd been and what you'd had, ontap logs it in one tap and gives it back as a monthly recap, without asking you to score anything.</p>
<h2>Bringing your history with you</h2>
<p>If you exported your RateBeer data before it closed, keep the file: most apps can't import it directly, but it's your record. Untappd's own export sits in its Insiders tier.</p>
""",
    faq=[
        ("Is RateBeer coming back?", "There's no sign of it. The site has been offline since 3 February 2025."),
        ("Can I still get my RateBeer ratings?", "BeerAdvocate's RateBeer page reports that former users who emailed after the deadline still received their old ratings."),
        ("What's the best RateBeer replacement?", "Untappd for ratings and community; Pint Please if you prefer a smaller app; ontap if you'd rather log nights than rate beers."),
    ],
    related=["untappd-alternatives", "beeradvocate-alternatives", "best-beer-rating-apps"],
)

BEERADVOCATE = Page(
    slug="beeradvocate-alternatives",
    kind="alt",
    keyword="beeradvocate alternatives",
    title="BeerAdvocate Alternatives in 2026: Apps for Rating and Logging Beer",
    description="Want BeerAdvocate on your phone? There's no confirmed current app, so here are the best mobile alternatives for rating, logging and sharing beers.",
    lede="BeerAdvocate is one of the oldest beer review communities online, but it lives on the web; we couldn't confirm a current BeerAdvocate app in 2026. If you want something in your pocket, these are the best alternatives.",
    publish="2026-10-29",
    body=DISCLOSURE + card("untappd", 1, "Best mobile alternative") + """
<p>Untappd has the mobile experience BeerAdvocate fans tend to miss: scan or search a beer, rate it and share it, with a database covering most beers you'll meet.</p>
""" + card("pintplease", 2) + card("ontap", 3, "Best for nights out rather than reviews") + card("beermenus", 4, "Best for finding beers nearby (US)") + """
<h2>Keep using BeerAdvocate for what it's best at</h2>
<p>The BeerAdvocate website is still a great place for long-form reviews and forum discussion. Use it alongside an app rather than instead of one.</p>
""",
    faq=[
        ("Does BeerAdvocate have an app?", "We couldn't confirm a current BeerAdvocate app in 2026. The website and forums remain active."),
        ("Which is better, Untappd or BeerAdvocate?", "Untappd for logging and rating on your phone; BeerAdvocate for in-depth reviews and forums on the web."),
    ],
    related=["ratebeer-alternatives", "untappd-alternatives", "best-beer-rating-apps"],
)

SWARM = Page(
    slug="swarm-alternatives",
    kind="alt",
    keyword="swarm app alternative",
    title="Swarm Alternatives in 2026: Check-in Apps for Nights Out",
    description="Looking for a Swarm (Foursquare) alternative? Compare ontap, Beli, Untappd, Find My and Google Maps for check-ins, nights out and location history.",
    lede="Swarm is still going in 2026, and it's the king of checking in everywhere. But if most of your check-ins are at bars, an app built for nights out might suit you better.",
    publish="2026-10-27",
    body=DISCLOSURE + """
<h2>Why look beyond Swarm?</h2>
<ul>
<li>It's built for every kind of place, so there's nothing specific to nights out: no beer counts, no recap of your month at the pub.</li>
<li>Your friends need to check in manually too, which a lot of groups stop doing.</li>
</ul>
<h2>The alternatives</h2>
""" + card("ontap", 1, "Best for bar check-ins") + """
<p>ontap is basically check-ins for nights out, made faster: tap a widget, the beer and bar are logged, and friends see you're out. Add Mayors of each bar, squads and a monthly recap, and you've got the bits of Swarm people loved, focused on going out.</p>
""" + card("beli", 2, "Best for ranking places") + card("untappd", 3, "Best for beer check-ins") + card("findmy", 4) + card("gmaps", 5, "Best for automatic location history") + """
<p>Google Maps Timeline can keep a private history of where you've been automatically, if you turn it on, with no check-ins needed.</p>
""",
    faq=[
        ("Is Swarm still around in 2026?", "Yes. Swarm is still available and took over Foursquare City Guide's features in 2024."),
        ("Is there a Swarm for bars?", "ontap is the closest: one-tap logging at bars, Mayors for each spot and friends on a map."),
    ],
    related=["best-apps-to-see-where-your-friends-are", "beli-alternatives", "best-social-apps-for-nights-out"],
)

ZENLY = Page(
    slug="zenly-alternatives",
    kind="alt",
    keyword="zenly alternative",
    title="Zenly Alternatives That Actually Work in 2026",
    description="Zenly shut down in February 2023. The best Zenly alternatives in 2026: Snap Map, Find My, Google Maps and ontap for seeing which friends are out.",
    lede="Zenly closed on <b>3 February 2023</b> when Snap shut it down, and its fans have been looking for a replacement ever since. Here's what's closest in 2026, and what's better for nights out.",
    publish="2026-10-25",
    body=DISCLOSURE + """
<h2>What made Zenly special</h2>
<p>Zenly wasn't just location sharing; it was <i>fun</i> location sharing, showing where your friends were and what they were up to. Most replacements only do the dot on the map.</p>
<h2>The best Zenly alternatives</h2>
""" + card("snapmap", 1, "Closest to Zenly") + """
<p>Snap owned Zenly, and Snap Map is where its ideas went. If your friends are on Snapchat, it's the natural replacement.</p>
""" + card("findmy", 2, "Best for close friends (iPhone)") + card("gmaps", 3, "Best for mixed iPhone and Android") + card("ontap", 4, "Best for seeing who's out tonight") + """
<p>ontap brings back the fun part of Zenly for nights out: friends show up on a shared map when they log a beer, you can see who's out right now, and there's a monthly recap of everyone's nights. No 24/7 tracking: you're on the map when you're out.</p>
""",
    faq=[
        ("When did Zenly shut down?", "Zenly closed on 3 February 2023, as part of Snap's cost-cutting."),
        ("Is there a new Zenly?", "Nothing has replaced it exactly. Snap Map is closest; ontap covers the 'who's out' side for nights out."),
    ],
    related=["best-apps-to-see-where-your-friends-are", "snap-map-alternatives", "swarm-alternatives"],
)

BELI = Page(
    slug="beli-alternatives",
    kind="alt",
    keyword="beli app alternative",
    title="Beli Alternatives for Bars and Pubs (2026)",
    description="Love Beli for restaurants but want something for bars and pubs? Compare ontap, Untappd, Swarm and CAMRA's Good Beer Guide.",
    lede="Beli made ranking restaurants fun, and it covers bars too. But if your list is more pubs than plates, these apps are built around drinking spots and nights out.",
    publish="2026-10-30",
    body=DISCLOSURE + card("ontap", 1, "Best for pubs and bars") + """
<p>Where Beli ranks places by comparison, ontap ranks them by what you actually do: your most-logged spots, your go-to night and who's Mayor of each bar. Friends' favourite spots show up on the map, so recommendations come from people you know.</p>
""" + card("untappd", 2) + card("swarm", 3) + card("camra", 4, "Best curated list of UK pubs") + """
<h2>Keep Beli for food</h2>
<p>Beli is excellent for restaurants. Plenty of people use Beli for dinner and ontap for what happens after.</p>
""",
    faq=[
        ("Is there a Beli for bars?", "ontap is built around bars and pubs: one-tap logging, your top spots, Mayors of each bar and friends on a map."),
    ],
    related=["swarm-alternatives", "best-apps-for-finding-pubs-uk", "best-social-apps-for-nights-out"],
)

SNAPMAP = Page(
    slug="snap-map-alternatives",
    kind="alt",
    keyword="snap map alternative",
    title="Snap Map Alternatives in 2026 (Without Living in Snapchat)",
    description="Want to see where friends are without Snapchat? The best Snap Map alternatives: Find My, Google Maps, Swarm and ontap for nights out.",
    lede="Snap Map is handy if your whole group lives in Snapchat. If they don't, or you'd rather not be on a map all the time, these alternatives do the job.",
    publish="2026-11-01",
    body=DISCLOSURE + card("findmy", 1, "Best private alternative (iPhone)") + card("gmaps", 2, "Best for iPhone and Android groups") + card("ontap", 3, "Best for nights out") + """
<p>ontap only puts you on the map when you're out and log a beer, and only for friends you've added, so it's a lighter-touch way to see who's out tonight.</p>
""" + card("swarm", 4) + """
<h2>Privacy first</h2>
<p>Whatever you use, share your location only with people you trust, and use time-limited sharing on nights out.</p>
""",
    faq=[
        ("How do I see where my friends are without Snapchat?", "Apple's Find My (iPhone) or Google Maps location sharing for live location; ontap to see which friends are out at a bar."),
    ],
    related=["zenly-alternatives", "best-apps-to-see-where-your-friends-are"],
)

PAGES = [UNTAPPD, RATEBEER, BEERADVOCATE, SWARM, ZENLY, BELI, SNAPMAP]
