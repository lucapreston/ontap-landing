from .pages import Page
from .apps import card, DISCLOSURE, APPS


def table(rows):
    head = "<tr><th>App</th><th>Best for</th><th>Price</th><th>Platforms</th></tr>"
    return "<table>" + head + "".join(
        f"<tr><td>{APPS[k]['name']}</td><td>{b}</td><td>{APPS[k]['price']}</td><td>{APPS[k]['platforms']}</td></tr>"
        for k, b in rows) + "</table>"


TRACKING = Page(
    slug="best-beer-tracking-apps",
    kind="best",
    keyword="best beer tracking app",
    title="The 6 Best Beer Tracking Apps in 2026",
    description="We compared the best beer tracker apps in 2026: Untappd, ontap, MyDrinkaware, BeerMenus, Pint Please and Swarm. What each tracks, what it costs and who it's for.",
    lede="\"Tracking beer\" means different things: rating every beer you try, counting what you drink, or remembering where you went and who with. These are the six best apps for each, as of 2026.",
    publish="2026-10-21",
    body=DISCLOSURE + """
<h2>The quick answer</h2>
""" + table([
        ("ontap", "Fast logging and friends"),
        ("untappd", "Rating every beer"),
        ("drinkaware", "Counting units, cutting down"),
        ("beermenus", "Finding a beer nearby (US)"),
        ("pintplease", "Rating beers, smaller community"),
        ("swarm", "Remembering every place"),
    ]) + """
<h2>How we chose</h2>
<p>We looked at how fast it is to log a beer on a night out, what the app does with that log (stats, recaps, ratings, friends), whether it's free, and whether it's still actively maintained in 2026. RateBeer would once have made this list, but it shut down in February 2025.</p>
<h2>The best beer tracking apps</h2>
""" + card("ontap", 1, "Best for nights out with friends") + """
<p>ontap's trick is the widget: tap once on your home or lock screen and the beer is logged with the bar you're at, without opening the app. Everything else is built on that log: a map of which friends are out, squads that race each other week by week, badges, Mayors for the person who logs most at a spot, and a monthly Last Call recap.</p>
""" + card("untappd", 2, "Best for rating beers") + """
<p>If you care about the difference between two hazy IPAs, Untappd is still the standard. You search for the exact beer, rate it out of five, and build up a record of every style you've tried. It's slower to log than a tap, which is why many people use Untappd for interesting beers and something quicker for everything else.</p>
""" + card("drinkaware", 3, "Best for keeping count") + card("beermenus", 4) + card("pintplease", 5) + card("swarm", 6) + """
<h2>Which one should you use?</h2>
<ul>
<li><b>You go out with the same group most weekends:</b> ontap.</li>
<li><b>You want a record of every beer and how good it was:</b> Untappd.</li>
<li><b>You want to drink less:</b> MyDrinkaware.</li>
<li><b>You want all of the above:</b> plenty of people use ontap for the night and Untappd for the special ones.</li>
</ul>
""",
    faq=[
        ("What's the best free beer tracker app?", "ontap, Untappd, MyDrinkaware, BeerMenus and Swarm are all free to use. Which is best depends on whether you want speed and friends (ontap), ratings (Untappd) or unit counting (MyDrinkaware)."),
        ("Is there a beer tracker that works from the home screen?", "Yes. ontap's home and lock screen widget logs a beer, with the venue, in one tap."),
        ("What happened to RateBeer?", "RateBeer shut down on 3 February 2025 after announcing its closure in December 2024. See our <a href=\"/ratebeer-alternatives/\">RateBeer alternatives</a>."),
    ],
    related=["untappd-alternatives", "best-beer-apps", "best-drink-tracker-apps", "beer-tracker-app"],
)

BEER_APPS = Page(
    slug="best-beer-apps",
    kind="best",
    keyword="best beer apps",
    title="The Best Beer Apps in 2026 (for Drinkers, Not Brewers)",
    description="The best beer apps of 2026 for finding pubs, tracking pints, rating beers and going out with friends. Free picks for iPhone and Android.",
    lede="There's an app for every part of a night out: finding the pub, picking the beer, remembering it afterwards and getting your friends there. Here are the ones worth keeping on your phone in 2026.",
    publish="2026-10-22",
    body=DISCLOSURE + """
<h2>At a glance</h2>
""" + table([
        ("ontap", "Logging pints and seeing who's out"),
        ("untappd", "Rating and discovering beers"),
        ("beermenus", "Finding a specific beer (US)"),
        ("camra", "Finding real-ale pubs (UK)"),
        ("drinkaware", "Keeping an eye on units"),
        ("beli", "Ranking bars and restaurants"),
    ]) + """
<h2>For logging and going out: ontap</h2>
""" + card("ontap") + """
<h2>For rating and discovering beer: Untappd</h2>
""" + card("untappd") + """
<h2>For finding a beer: BeerMenus</h2>
""" + card("beermenus") + """
<h2>For finding a proper pub in the UK: CAMRA Good Beer Guide</h2>
""" + card("camra") + """
<h2>For drinking less: MyDrinkaware</h2>
""" + card("drinkaware") + """
<h2>For ranking your favourite bars: Beli</h2>
""" + card("beli") + """
<h2>Free tools that help too</h2>
<ul>
<li><a href="/alcohol-units-calculator/">How many units in a pint?</a> Units and standard drinks for any beer.</li>
<li><a href="/price-per-pint-calculator/">Price per pint calculator</a>: is the pitcher actually cheaper?</li>
<li><a href="/round-splitter/">Round splitter</a>: settle up after a night of rounds.</li>
</ul>
""",
    faq=[
        ("What app do beer lovers use?", "Untappd is the most widely used beer rating app. For logging nights out with friends, ontap is a quicker, more social option."),
        ("Is there an app that tells you where a beer is on tap?", "BeerMenus does this well in the US. Untappd also shows menus for venues that use Untappd for Business."),
    ],
    related=["best-beer-tracking-apps", "best-beer-rating-apps", "best-apps-for-finding-pubs-uk"],
)

DRINK_TRACKER = Page(
    slug="best-drink-tracker-apps",
    kind="best",
    keyword="drink tracker app",
    title="The Best Drink Tracker Apps in 2026: Count, Cut Down or Just Remember",
    description="The best drink tracking apps in 2026, from unit counters like MyDrinkaware to social trackers like ontap. How they differ and which to pick.",
    lede="Drink trackers fall into two camps: apps that help you <b>drink less</b> and apps that help you <b>remember nights out</b>. Both are useful, and they're very different. Here are the best of each.",
    publish="2026-10-24",
    body=DISCLOSURE + """
<h2>If you want to drink less</h2>
""" + card("drinkaware", None, "Best for cutting down") + """
<p>MyDrinkaware is made by the UK alcohol charity Drinkaware, it's free, and it's built around units, calories, goals and drink-free days. If your aim is fewer drinks, start here. In the US, the NIAAA's free <a href="https://www.rethinkingdrinking.niaaa.nih.gov/" rel="nofollow noopener">Rethinking Drinking</a> site has similar calculators.</p>
<h2>If you want to remember nights out</h2>
""" + card("ontap", None, "Best for nights out with friends") + """
<p>ontap tracks where you were, who you were with and what the month looked like, and turns it into a recap and a bit of friendly competition with your friends. It's about the night, not the number.</p>
""" + card("untappd", None, "Best for remembering specific beers") + """
<h2>A note on drinking sensibly</h2>
<p>The UK guideline is no more than 14 units a week, spread over several days. That's about six pints of 4% lager. Use our <a href="/alcohol-units-calculator/">units calculator</a> to check any drink. Whichever app you use, a tracker is most useful when it's honest.</p>
""",
    faq=[
        ("Is there a free app to track alcohol units?", "Yes. MyDrinkaware is free and counts units and calories, with goals and drink-free days."),
        ("Can a drink tracker help me cut down?", "Tracking makes your drinking visible, which helps many people cut down. Apps built for it, like MyDrinkaware, add goals and reminders. If you're worried, talk to your GP or doctor."),
    ],
    related=["alcohol-units-calculator", "best-beer-tracking-apps", "best-beer-journal-apps"],
)

JOURNAL = Page(
    slug="best-beer-journal-apps",
    kind="best",
    keyword="beer journal app",
    title="The Best Beer Journal and Beer Diary Apps in 2026",
    description="Want a beer diary? These are the best beer journal apps in 2026 for tasting notes, photos, places and monthly recaps.",
    lede="A beer journal used to be a notebook in your back pocket. Now your phone can do it, with photos, places and stats. Here are the best beer diary apps, depending on what you want to remember.",
    publish="2026-10-25",
    body=DISCLOSURE + """
<h2>What makes a good beer journal?</h2>
<ul>
<li><b>Fast to add to</b>, or you'll stop after a week.</li>
<li><b>Remembers the place</b>: half the memory is where you were.</li>
<li><b>Gives something back</b>: stats, recaps, maps.</li>
<li><b>Notes when you want them</b>: tasting notes for the special beers, not every lager.</li>
</ul>
<h2>The best beer journal apps</h2>
""" + card("untappd", 1, "Best for tasting notes") + """
<p>Untappd is the closest thing to a classic tasting journal: every check-in can have a rating, a note, a photo and the venue, and it's all searchable later.</p>
""" + card("ontap", 2, "Best automatic diary") + """
<p>ontap is a journal that writes itself. One tap logs the beer and the spot; add a photo and caption when the moment deserves it. At the end of each month Last Call turns it into a recap: your top spots, your go-to night and your map filling up.</p>
""" + card("pintplease", 3) + card("swarm", 4, "Best for every place, not just pubs") + """
<h2>Old school still works</h2>
<p>Plenty of beer fans keep a paper journal for tasting notes and use an app for the logging. There's no wrong answer, as long as you actually use it.</p>
""",
    faq=[
        ("What's the best beer diary app?", "Untappd for detailed tasting notes; ontap for an effortless diary of where and when, with monthly recaps."),
        ("Can I export my beer journal?", "Untappd offers data export to its paid Insiders tier (and in the EU/EEA). Check each app's settings for export options."),
    ],
    related=["best-beer-tracking-apps", "last-call", "untappd-alternatives"],
)

FRIENDS = Page(
    slug="best-apps-to-see-where-your-friends-are",
    kind="best",
    keyword="app to see where friends are",
    title="The Best Apps to See Where Your Friends Are (2026)",
    description="Since Zenly shut down, which apps show where your friends are? We compare Find My, Snap Map, Google Maps, Swarm and ontap for nights out.",
    lede="Zenly closed in 2023 and nothing quite replaced it. But if you mainly want to know <b>which friends are out tonight and where</b>, there are good options. Here's how they compare.",
    publish="2026-10-26",
    body=DISCLOSURE + """
<h2>Two kinds of "where are my friends"</h2>
<p><b>Live location</b> (a dot that follows your friend everywhere) is what Find My, Snap Map and Google Maps do. <b>Who's out</b> (friends share where they are when they're out, by logging at a bar) is what ontap and Swarm do. For nights out, the second is often what you actually want: you see who's at the pub without everyone tracking everyone all week.</p>
""" + card("ontap", 1, "Best for seeing who's out tonight") + card("findmy", 2, "Best private live location (iPhone)") + card("snapmap", 3) + card("gmaps", 4, "Best for mixed iPhone and Android") + card("swarm", 5) + """
<h2>Privacy tips</h2>
<ul>
<li>Share live location only with people you'd trust with your house keys.</li>
<li>Use time limits ("for one hour") on a night out.</li>
<li>In ontap, only friends you've added see where you've logged, and you can turn location sharing off at any time.</li>
</ul>
""",
    faq=[
        ("What replaced Zenly?", "Nothing exactly. Snap Map (from the same owner) took over its role inside Snapchat; Find My and Google Maps cover live sharing. See <a href=\"/zenly-alternatives/\">Zenly alternatives</a>."),
        ("Is there an app to see which friends are at the pub?", "Yes. ontap shows friends who've logged a beer recently on a shared map, so you can see who's out without constant tracking."),
    ],
    related=["zenly-alternatives", "snap-map-alternatives", "best-social-apps-for-nights-out"],
)

NIGHTS_OUT = Page(
    slug="best-social-apps-for-nights-out",
    kind="best",
    keyword="best social apps for nights out",
    title="The Best Social Apps for Nights Out in 2026",
    description="The apps that make nights out better: seeing who's out, planning where to go, sharing the night and settling up. Our 2026 picks.",
    lede="The group chat does a lot of heavy lifting on a night out. These apps take some of the load: who's out, where to go, what happened and who owes what.",
    publish="2026-10-27",
    body=DISCLOSURE + """
<h2>Our picks by job</h2>
<table>
<tr><th>Job</th><th>App</th></tr>
<tr><td>See which friends are out</td><td>ontap</td></tr>
<tr><td>Live location for getting home</td><td>Find My / Google Maps</td></tr>
<tr><td>Rank the bars you love</td><td>Beli</td></tr>
<tr><td>Find a real-ale pub (UK)</td><td>CAMRA Good Beer Guide</td></tr>
<tr><td>Rate the beer</td><td>Untappd</td></tr>
<tr><td>Settle up the rounds</td><td><a href="/round-splitter/">Our round splitter</a></td></tr>
</table>
""" + card("ontap", 1, "Best all-round nights-out app") + """
<p>ontap was built for this: log a beer in one tap, see who's already out on the map, race your friends in squads and get a monthly recap of the nights. It's the thing your group chat was missing.</p>
""" + card("findmy", 2, "Best for getting everyone home") + card("beli", 3) + card("untappd", 4) + card("camra", 5) + """
<h2>One more thing</h2>
<p>The best nights-out app is the one your friends actually have. Pick one, get the group on it, and keep the group chat for the memes.</p>
""",
    faq=[
        ("What app shows which friends are out?", "ontap shows friends who've logged a beer recently on a shared map and in a live list."),
        ("Is there an app for planning a pub crawl?", "See our guide to <a href=\"/best-pub-crawl-apps/\">pub crawl apps</a>."),
    ],
    related=["best-apps-to-see-where-your-friends-are", "best-pub-crawl-apps", "squads"],
)

PUBS_UK = Page(
    slug="best-apps-for-finding-pubs-uk",
    kind="best",
    keyword="best app for finding pubs uk",
    title="The Best Apps for Finding a Good Pub in the UK (2026)",
    description="Looking for a proper pub? The best UK pub-finder apps in 2026: CAMRA's Good Beer Guide, Google Maps, Untappd, ontap and more.",
    lede="Finding a good pub in a town you don't know is a craft. These apps make it easier, whether you want real ale, a cheap pint or wherever your mates are.",
    publish="2026-10-28",
    body=DISCLOSURE + """
""" + card("camra", 1, "Best for real ale") + """
<p>CAMRA volunteers survey every pub in the Good Beer Guide, which makes it the most trusted list of proper pubs in the country.</p>
""" + card("gmaps", 2, "Best for 'what's open near me'") + card("ontap", 3, "Best for finding your friends' locals") + """
<p>ontap shows the pubs your friends actually go to, who the Mayor of each one is, and which spots are popular with ontap users nearby. It's a different kind of recommendation: people you know, not strangers' reviews.</p>
""" + card("untappd", 4, "Best for craft beer bars") + card("beli", 5) + """
<h2>Cheap pint?</h2>
<p>See <a href="/price-of-a-pint-in-london/">how much a pint costs in London</a>, with the cheapest pubs we found, and compare any deal with the <a href="/price-per-pint-calculator/">price per pint calculator</a>.</p>
""",
    faq=[
        ("What's the best app for real ale pubs?", "CAMRA's Good Beer Guide app, built from the printed Good Beer Guide."),
        ("Is there an app for cheap pints in the UK?", "ontap Pro's pint price finder is coming soon. For now, see our <a href=\"/price-of-a-pint-in-london/\">London pint price guide</a>."),
    ],
    related=["price-of-a-pint-in-london", "best-beer-apps", "best-pub-crawl-apps"],
)

RATING = Page(
    slug="best-beer-rating-apps",
    kind="best",
    keyword="beer rating app",
    title="The Best Beer Rating Apps in 2026 (Now RateBeer's Gone)",
    description="With RateBeer closed, these are the best beer rating apps in 2026: Untappd, Pint Please, BeerAdvocate's website and simpler options.",
    lede="RateBeer closed in February 2025, leaving Untappd as the clear leader for rating beers. But it's not the only option, and not every drinker needs star ratings at all.",
    publish="2026-10-29",
    body=DISCLOSURE + card("untappd", 1, "Best overall") + """
<p>The largest beer database and the biggest community. If you rate beers, you're probably on Untappd already.</p>
""" + card("pintplease", 2, "Best smaller alternative") + """
<h3>3. BeerAdvocate (website)</h3>
<p>BeerAdvocate's reviews and forums are still one of the deepest archives of beer opinion online. We couldn't confirm an active BeerAdvocate app in 2026, so treat it as a website you visit rather than an app you log in.</p>
""" + card("ontap", 4, "Best if you'd rather not rate at all") + """
<p>Not everyone wants to score every beer. ontap skips ratings entirely: log the beer and the place in one tap, and let the stats tell you which spots you love.</p>
""",
    faq=[
        ("Is RateBeer still working?", "No. RateBeer went offline on 3 February 2025. See <a href=\"/ratebeer-alternatives/\">RateBeer alternatives</a>."),
        ("Is Untappd free?", "Yes, with an optional paid tier called Untappd Insiders for extra stats and badges."),
    ],
    related=["ratebeer-alternatives", "untappd-alternatives", "beeradvocate-alternatives"],
)

CRAWL = Page(
    slug="best-pub-crawl-apps",
    kind="best",
    keyword="pub crawl app",
    title="The Best Pub Crawl Apps and Planners in 2026",
    description="How to plan a pub crawl with your phone in 2026: route planning, finding the pubs, keeping the group together and settling up after.",
    lede="A good pub crawl is a short walk between great pubs, with everyone still together at the end. Here's how to plan one with apps you probably already have, plus a new one on the way.",
    publish="2026-10-30",
    body=DISCLOSURE + """
<h2>Planning the route</h2>
""" + card("gmaps", None, "Best free route planner") + """
<p>Save the pubs to a list, then use walking directions between them. Keep walks under 10 minutes and plan 4–6 stops.</p>
""" + card("camra", None, "Best for picking great pubs (UK)") + """
<h2>Keeping the group together</h2>
""" + card("ontap", None, "Best for seeing who's where") + """
<p>On a crawl, ontap shows which pub everyone last logged at, so stragglers can catch up. A dedicated <b>pub crawl planner</b> is coming to ontap in November 2026: pick an area and a vibe, get a walking route built from where ontap users actually go, and tick off stops as you log.</p>
<h2>Settling up</h2>
<p>Use our free <a href="/round-splitter/">round splitter</a> the morning after.</p>
<h2>Crawl tips</h2>
<ul>
<li>Plan food and water stops, and alternate with soft drinks.</li>
<li>Halves are your friend on a long crawl.</li>
<li>Agree a meeting point in case phones die, and plan how everyone gets home.</li>
</ul>
""",
    faq=[
        ("Is there an app that plans a pub crawl for you?", "ontap's pub crawl planner arrives in November 2026. Until then, Google Maps lists with walking directions work well."),
        ("How many pubs should a pub crawl have?", "Four to six is plenty. Fewer, better pubs beat a long list."),
    ],
    related=["round-splitter", "best-social-apps-for-nights-out", "best-apps-for-finding-pubs-uk"],
)

CRAFT = Page(
    slug="best-apps-for-craft-beer-lovers",
    kind="best",
    keyword="apps for craft beer lovers",
    title="The Best Apps for Craft Beer Lovers in 2026",
    description="Untappd, BeerMenus, ontap and more: the apps craft beer fans actually use in 2026, plus a free ABV calculator for homebrewers.",
    lede="Craft beer fans want to find new beers, remember the good ones and share them with friends. These are the apps that do it best.",
    publish="2026-10-31",
    body=DISCLOSURE + card("untappd", 1, "Best for craft beer fans") + card("beermenus", 2, "Best for tracking down a beer (US)") + card("ontap", 3, "Best for brewery and taproom nights") + """
<p>Logging taproom visits in ontap fills your map with every brewery you've been to, and Last Call tells you which ones you keep going back to.</p>
""" + card("pintplease", 4) + card("camra", 5) + """
<h2>For homebrewers</h2>
<p>Use our free <a href="/abv-calculator/">ABV calculator</a> to turn your gravity readings into strength, and the <a href="/alcohol-units-calculator/">units calculator</a> to see what a pint of it means.</p>
""",
    faq=[
        ("What app do craft beer drinkers use?", "Untappd is the standard for rating craft beers. BeerMenus helps find them in the US, and ontap logs the taprooms and bars you visit."),
    ],
    related=["abv-calculator", "best-beer-rating-apps", "price-of-a-pint-in-montreal"],
)

PAGES = [TRACKING, BEER_APPS, DRINK_TRACKER, JOURNAL, FRIENDS, NIGHTS_OUT, PUBS_UK, RATING, CRAWL, CRAFT]
