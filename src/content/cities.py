"""'How much is a pint in X' pages, from ontap's sourced price data
(Supabase pint_prices / pint_baselines, collected Oct 2026). Every number
links to where it came from. Re-run the queries and update these figures
when the data is refreshed."""
from .pages import Page


def cheap_table(rows, note=""):
    head = "<tr><th>Bar</th><th>Pint</th><th>Price</th><th>Seen</th></tr>"
    body = "".join(
        f'<tr><td>{v}</td><td>{d}</td><td>{p}</td><td><a href="{u}" rel="nofollow noopener">{s}</a></td></tr>'
        for v, d, p, s, u in rows)
    return f"<table>{head}{body}</table><p><small>{note}Prices change all the time; tap the date to see each source.</small></p>"


LONDON = Page(
    slug="price-of-a-pint-in-london",
    kind="city",
    keyword="price of a pint in london",
    title="How Much Is a Pint in London? (2026 Prices)",
    description="The average pint in London is about £6.50–£6.75 in 2026, against £4.74 for the UK as a whole. Real prices from 63 London pubs, plus where to find a cheap one.",
    lede="A pint in London typically costs <b>£6.50 to £6.75</b> in 2026. That's well above the UK average of about <b>£4.74</b> for a pint of lager. Here's what we found when we checked 63 London pubs and bars, and where the cheap ones are.",
    publish="2026-10-20",
    body="""
<h2>London pint prices at a glance</h2>
<table>
<tr><th></th><th>Price</th><th>Source</th></tr>
<tr><td>UK average, pint of lager</td><td>£4.74</td><td><a href="https://raw.githubusercontent.com/ONSdigital/cpi-items-actions/main/avgprice.csv" rel="nofollow noopener">ONS, Aug 2026</a></td></tr>
<tr><td>UK average, all pints (pubs)</td><td>£5.34</td><td><a href="https://www.morningadvertiser.co.uk/Article/2026/05/21/average-pint-price-rises-33-to-534-the-morning-advertiser-finds/" rel="nofollow noopener">Morning Advertiser, Apr 2026</a></td></tr>
<tr><td>London average</td><td>£6.55</td><td><a href="https://www.morningadvertiser.co.uk/Article/2026/05/21/average-pint-price-rises-33-to-534-the-morning-advertiser-finds/" rel="nofollow noopener">Morning Advertiser, Apr 2026</a></td></tr>
<tr><td>Middle of the London menus we checked</td><td><b>£6.75</b></td><td>ontap, Oct 2026 (half paid £5.00–£7.55)</td></tr>
<tr><td>Typical London happy-hour pint</td><td>£4.93</td><td>ontap, Oct 2026</td></tr>
</table>
<p>The gap between the ONS figure and what you pay in a central London pub is real: the ONS average covers the whole country and standard lager, while the London figures include premium lagers, craft and city-centre rents.</p>
<h2>What drives the price</h2>
<ul>
<li><b>The beer:</b> premium lagers like Peroni and Asahi run £7 or more in London (Peroni averaged £7.03 and Asahi £7.60 in <a href="https://www.morningadvertiser.co.uk/Article/2026/07/06/ma-beer-report-reveals-sharp-rise-in-uk-pint-prices/" rel="nofollow noopener">this summer's MA beer report</a>). Cask ale is usually the cheapest pint on the bar.</li>
<li><b>The postcode:</b> Soho, the City and Mayfair cost more than Zone 3 locals.</li>
<li><b>Who owns the pub:</b> Samuel Smith's and Wetherspoon pubs are famously cheaper; students' union bars cheaper still.</li>
</ul>
<h2>Where to find a cheaper pint in London</h2>
""" + cheap_table([
        ("Phineas (Students' Union UCL)", "Carling", "£3.80", "Oct 2026", "https://studentsunionucl.org/phineas/P25GS-240919"),
        ("Imperial College Union bars", "Carling", "£3.85", "May 2026", "https://www.imperialcollegeunion.org/blog/price-increases-at-icu-bars"),
        ("The Marian Anderson", "Guinness", "£4.00", "Aug 2026", "https://www.designmynight.com/london/blog/cheap-pints-of-guinness-in-london"),
        ("The Five Bells", "Guinness", "£4.15", "Aug 2026", "https://www.designmynight.com/london/blog/cheap-pints-of-guinness-in-london"),
        ("The Nags Head", "Guinness", "£4.30", "Aug 2026", "https://www.designmynight.com/london/blog/cheap-pints-of-guinness-in-london"),
        ("The Old Ale Emporium", "Guinness", "£4.30", "Aug 2026", "https://www.designmynight.com/london/blog/cheap-pints-of-guinness-in-london"),
        ("The William Morris", "Guinness", "£4.40", "Aug 2026", "https://www.designmynight.com/london/blog/cheap-pints-of-guinness-in-london"),
    ], "Students' union bars may need a student or guest card. ") + """
<h2>How we got these numbers</h2>
<p>In October 2026 we collected 92 pint prices from 63 London pubs and bars, using their own menus and recent articles, and recorded where each came from and when. Happy-hour prices are counted separately. We'll keep updating this page; ontap users will soon be able to add what they paid too.</p>
""",
    faq=[
        ("What's the average price of a pint in London?", "About £6.50–£6.75 in 2026. The Morning Advertiser put London at £6.55 in April 2026; the middle of the London menus we checked in October was £6.75."),
        ("What's the average price of a pint in the UK?", "The ONS average for a pint of lager was £4.74 in August 2026. The Morning Advertiser's pub survey put the average pint at £5.34 in April 2026."),
        ("Where's the cheapest pint in London?", "Students' union bars (around £3.80), Samuel Smith's pubs and some Wetherspoon pubs are usually cheapest. See the table above for spots we've confirmed."),
        ("Is a £10 pint in London normal?", "Not for a standard lager. £10+ pints exist (rooftops, hotels, strong craft), but most London pubs charge £5.50–£7.50."),
    ],
    related=["price-per-pint-calculator", "price-of-a-pint-in-new-york", "best-apps-for-finding-pubs-uk"],
)

NEW_YORK = Page(
    slug="price-of-a-pint-in-new-york",
    kind="city",
    keyword="price of a beer in nyc",
    title="How Much Is a Beer in NYC? Pint Prices in New York (2026)",
    description="A 16 oz draft beer in Manhattan averages about $9 in 2026, against $6.52 nationally. Real prices from 60+ New York bars, plus happy hour and cheap spots.",
    lede="Expect to pay about <b>$9 for a 16 oz draft</b> in Manhattan in 2026, against a US average of <b>$6.52</b>. Happy hour brings that down to around <b>$6</b>. Here's what we found across more than 60 New York bars.",
    publish="2026-10-22",
    body="""
<h2>NYC beer prices at a glance</h2>
<table>
<tr><th></th><th>Price (16 oz)</th><th>Source</th></tr>
<tr><td>US average</td><td>$6.52</td><td><a href="https://vinepair.com/booze-news/new-report-names-new-york-most-expensive-beer-city" rel="nofollow noopener">VinePair, Mar 2025–Mar 2026</a></td></tr>
<tr><td>New York State average</td><td>$7.97</td><td><a href="https://vinepair.com/booze-news/beer-cost-each-state-map/" rel="nofollow noopener">VinePair</a></td></tr>
<tr><td>Manhattan average</td><td>$9.16</td><td><a href="https://vinepair.com/booze-news/new-report-names-new-york-most-expensive-beer-city" rel="nofollow noopener">VinePair</a></td></tr>
<tr><td>Middle of the NYC menus we checked</td><td><b>about $9</b></td><td>ontap, Oct 2026 (half paid $7.50–$10)</td></tr>
<tr><td>Brooklyn menus we checked</td><td>about $6.85</td><td>ontap, Oct 2026</td></tr>
<tr><td>Typical happy-hour beer</td><td>$6 (often a 12 oz can or bottle)</td><td>ontap, Oct 2026</td></tr>
</table>
<p>Watch the size: a lot of New York "pints" are 16 oz, some are 14 oz, and plenty of cheap deals are 12 oz cans. Our <a href="/price-per-pint-calculator/">price per pint calculator</a> makes it a fair fight.</p>
<h2>Where to find a cheaper beer in New York</h2>
""" + cheap_table([
        ("The Stumble Inn (UES)", "Can of beer, happy hour list", "$3", "Jun 2026", "https://www.theinfatuation.com/new-york/guides/happy-hour-nyc"),
        ("Jeremy's Ale House", "Coors Light, 32 oz", "$9", "Jun 2026", "https://www.theinfatuation.com/new-york/guides/cheap-drinks-nyc"),
        ("The Wingbar (Brooklyn)", "Coors Light pitcher", "$14", "Jul 2026", "https://www.theinfatuation.com/new-york/guides/best-sports-bars-nyc"),
        ("Standings", "Bud Light draft, 16 oz", "$6", "Jul 2026", "https://www.theinfatuation.com/new-york/guides/best-sports-bars-nyc"),
        ("The Kettle Black (Brooklyn)", "Miller Lite draft, 16 oz", "$6", "Oct 2026", "https://thekettleblack1.kwickmenu.com/"),
        ("Harlem Tavern", "Bud Light draft, 16 oz", "$7", "Oct 2026", "https://www.harlemtavern.com/new-york-harlem-tavern-harlem-tavern-drink-menu"),
        ("McSorley's Old Ale House", "Two mugs of light or dark ale", "$8", "Oct 2026", "https://mcsorleysoldalehouse.nyc/menu/"),
    ]) + """
<h2>Tips for drinking in NYC without the $12 pint</h2>
<ul>
<li>Happy hours (usually 4–7pm) are where the deals are, especially at sports bars and dives.</li>
<li>Outer-borough bars, especially in Brooklyn and Queens, usually beat Manhattan by a couple of dollars.</li>
<li>Domestic lagers and house beers are cheapest; IPAs and imports usually add $2–4.</li>
<li>Remember tax and tip: menu prices don't include the roughly $1–2 tip per drink.</li>
</ul>
<h2>How we got these numbers</h2>
<p>In October 2026 we collected over 60 New York beer prices from bar menus and recent guides, recorded the size, source and date for each, and counted happy hour separately.</p>
""",
    faq=[
        ("How much is a beer in NYC?", "Around $9 for a 16 oz draft in Manhattan in 2026 (VinePair measured $9.16), less in Brooklyn and Queens, and about $6 at happy hour."),
        ("Is New York the most expensive US city for beer?", "VinePair's 2026 report named New York (Manhattan) the most expensive beer city in the US."),
        ("Do I need to tip on beer in New York?", "Yes, $1–2 per drink at the bar is standard."),
    ],
    related=["price-per-pint-calculator", "price-of-a-pint-in-london", "best-social-apps-for-nights-out"],
)

MONTREAL = Page(
    slug="price-of-a-pint-in-montreal",
    kind="city",
    keyword="price of a pint in montreal",
    title="How Much Is a Pint in Montréal? Beer Prices (2026)",
    description="A pint in a Montréal bar usually costs $8–$12 CAD in 2026, depending on size. Real prices from 45 Montréal bars and brewpubs, plus the cheapest spots.",
    lede="In Montréal a pint usually costs <b>$8 to $12 CAD</b> in 2026. Where you land depends a lot on whether it's a 16 oz or a 20 oz <i>pinte</i>. We checked menus at 45 bars and brewpubs; here's what you'll actually pay.",
    publish="2026-10-24",
    body="""
<h2>Montréal beer prices at a glance</h2>
<table>
<tr><th></th><th>Price</th><th>Source</th></tr>
<tr><td>Average local beer, 500 ml</td><td>$9 CAD</td><td><a href="https://www.combien-coute.net/biere-locale/quebec/montreal/" rel="nofollow noopener">combien-coute.net, Oct 2026</a></td></tr>
<tr><td>Middle of the menus we checked, per 20 oz (568 ml)</td><td><b>$11.35 CAD</b></td><td>ontap, Oct 2026 (half paid $10–$12)</td></tr>
<tr><td>Same, for a 16 oz (473 ml) pint</td><td>about $9.45 CAD</td><td>ontap, Oct 2026</td></tr>
<tr><td>Typical happy-hour pint (usually 16 oz)</td><td>about $6.70 CAD</td><td>ontap, Oct 2026</td></tr>
</table>
<p>Menu prices in Québec usually don't include the two sales taxes (about 15% together) or the tip (15–20%), so a $9 pint really costs about $12.50 by the time you've paid.</p>
<h2>Good-value pints we found in Montréal</h2>
""" + cheap_table([
        ("Pub McCarold", "Bitburger, 1 litre <i>bock</i>", "$12.50", "Oct 2026", "https://pubmccarold.com/wp-content/uploads/2026/07/menu-mccarold-24-jun-fr_compressed.pdf"),
        ("La Terrasse St-Ambroise", "St-Ambroise pitcher", "$22.50", "Oct 2026", "https://mcauslan.com/la-terrasse/"),
        ("Bishop &amp; Bagg", "Burgundy Lion Ale, 20 oz", "$8.50", "Oct 2026", "https://www.bishopandbagg.com/en/menus"),
        ("Bar Suzanne", "Pretty Bastard stout, 16 oz", "$7.25", "Oct 2026", "https://barsuzanne.ca/menus/menu-bieres"),
        ("Les Sans-Taverne", "House beers, 20 oz", "from $8.75", "Oct 2026", "https://sans-taverne.coop/bieres-2/"),
        ("Dieu du Ciel! (Laurier)", "House beer pitcher", "$27.50", "Oct 2026", "https://dieuduciel.com/en/montreal-brewpub/"),
        ("Brasserie Chez Baptiste", "Blonde à Baptiste, 16 oz", "$7.50", "Oct 2026", "https://www.chezbaptiste.com/_files/ugd/5a0b4a_62b88e41422641a0bf1df276e13ab7fd.pdf"),
    ], "Before tax and tip. ") + """
<h2>Tips for drinking well in Montréal</h2>
<ul>
<li>Brewpubs like Dieu du Ciel! and the McAuslan terrace pour excellent local beer for the price of an import elsewhere.</li>
<li><i>5 à 7</i> (happy hour) is the cheapest time to drink: $6–$7 pints are common.</li>
<li>Pitchers (<i>pichets</i>) work out cheapest per glass if your group finishes them while they're cold.</li>
<li>Always ask the size: a <i>pinte</i> can mean 16 oz or 20 oz depending on the bar.</li>
</ul>
<h2>How we got these numbers</h2>
<p>In October 2026 we collected 99 Montréal beer prices from 45 bars, brewpubs and recent guides, recorded size, source and date for each, and counted happy hour separately. ontap started in Montréal, so this one's personal.</p>
""",
    faq=[
        ("How much is a pint in Montréal?", "Usually $8–$12 CAD before tax and tip in 2026: about $9.45 for a 16 oz and $11.35 for a 20 oz in the middle of the menus we checked."),
        ("Is beer cheaper in Montréal than Toronto?", "Close. Montréal brewpubs are good value, but Toronto's cheap spots can beat them; see our <a href=\"/price-of-a-pint-in-toronto/\">Toronto page</a>."),
        ("What is 5 à 7?", "Québec's happy hour, roughly 5pm to 7pm, when many bars cut drink prices."),
    ],
    related=["price-of-a-pint-in-toronto", "price-per-pint-calculator", "best-apps-for-craft-beer-lovers"],
)

TORONTO = Page(
    slug="price-of-a-pint-in-toronto",
    kind="city",
    keyword="price of a pint in toronto",
    title="How Much Is a Pint in Toronto? Beer Prices (2026)",
    description="A pint in a Toronto bar usually costs $9.50–$12 CAD in 2026. Real prices from 38 Toronto bars, plus the cheapest pints we found.",
    lede="In Toronto, a pint usually costs <b>$9.50 to $12 CAD</b> before tax and tip in 2026. Happy hour knocks a few dollars off, and a few places still pour under $8. Here's what we found across 38 bars.",
    publish="2026-10-26",
    body="""
<h2>Toronto beer prices at a glance</h2>
<table>
<tr><th></th><th>Price</th><th>Source</th></tr>
<tr><td>Typical pint, Toronto</td><td>about $11.50 CAD</td><td><a href="https://citiesinsider.com/country/canada/toronto/nightlife/en" rel="nofollow noopener">Cities Insider, Jun 2026</a></td></tr>
<tr><td>Typical pint in a major Canadian city</td><td>about $10 CAD</td><td><a href="https://www.insauga.com/torontos-cheapest-beer-may-be-tucked-away-in-this-ramen-shop/" rel="nofollow noopener">insauga, Jul 2026</a></td></tr>
<tr><td>Middle of the menus we checked, per 20 oz (568 ml)</td><td><b>$10.13 CAD</b></td><td>ontap, Oct 2026 (half paid $9.45–$12)</td></tr>
<tr><td>Typical happy-hour pint (usually 16 oz)</td><td>about $6.50 CAD</td><td>ontap, Oct 2026</td></tr>
</table>
<p>Like elsewhere in Canada, menu prices exclude 13% HST and the tip, so budget about a third more than the menu says.</p>
<h2>Cheap pints we found in Toronto</h2>
""" + cheap_table([
        ("Tondou Ramen", "House pilsner, 12 oz mug", "$3.95", "Jul 2026", "https://www.insauga.com/torontos-cheapest-beer-may-be-tucked-away-in-this-ramen-shop/"),
        ("Sneaky Dee's", "Select beers, 16 oz", "$6", "Oct 2026", "https://www.sneakydees.com"),
        ("Madison Avenue Pub", "Amsterdam Blonde / 3-Speed, 20 oz", "$7.96", "Oct 2026", "https://madisonavenuepub.com/our-menu/"),
        ("The Bedford Academy", "Steam Whistle / Mill St Organic, 20 oz", "$8", "Oct 2026", "https://www.thebedfordacademy.com/drinks-menu.php"),
        ("The Harbord House", "Great Lakes IPA, 20 oz", "$9", "Oct 2026", "https://harbordhouse.ca/craft-beer/"),
        ("Hemingway's", "Amsterdam 3 Speed, 20 oz", "$9.25", "Oct 2026", "https://www.hemingways.to/menu/drinks"),
        ("Crafty Coyote Ale House", "House lager, 16 oz", "$7.75", "Oct 2026", "https://www.craftycoyote.ca/toronto-crafty-coyote-drink-menu"),
    ], "Before HST and tip. ") + """
<h2>Tips for a cheaper night in Toronto</h2>
<ul>
<li>Student-area pubs around U of T and the Annex keep prices lower than King West or the Entertainment District.</li>
<li>Ontario beers (Steam Whistle, Amsterdam, Mill Street, Great Lakes) are usually the cheapest taps.</li>
<li>Check the size: 20 oz pints are common in Toronto pubs and are better value than they look next to 16 oz.</li>
</ul>
<h2>How we got these numbers</h2>
<p>In October 2026 we collected 65 Toronto beer prices from 38 bars and recent guides, recorded size, source and date for each, and counted happy hour separately.</p>
""",
    faq=[
        ("How much is a pint in Toronto?", "Usually $9.50–$12 CAD before tax and tip in 2026; about $10 for a 20 oz in the middle of the menus we checked."),
        ("What's the cheapest beer in Toronto?", "We found a $3.95 house pilsner at Tondou Ramen and $6 select beers at Sneaky Dee's; see the table above."),
        ("Is tax included in Toronto bar prices?", "Usually not. Add 13% HST plus a 15–20% tip."),
    ],
    related=["price-of-a-pint-in-montreal", "price-per-pint-calculator", "best-beer-apps"],
)

PAGES = [LONDON, NEW_YORK, MONTREAL, TORONTO]
