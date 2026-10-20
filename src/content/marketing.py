from .pages import Page

SHOT = ('<p style="text-align:center"><img src="/{src}" alt="{alt}" width="600" height="1300" loading="lazy" '
        'style="width:min(280px,70%);height:auto;border-radius:28px;box-shadow:0 20px 40px #3d1e0033"></p>')

TRACKER = Page(
    slug="beer-tracker-app",
    kind="page",
    keyword="beer tracker app",
    title="ontap: The Beer Tracker App That Logs a Pint in One Tap",
    h1="A beer tracker that takes one tap",
    description="ontap is a free beer tracker for iPhone: log a beer and the bar from your home screen in one tap, see which friends are out, and get a monthly recap.",
    lede="Most beer trackers make you search for the beer, pick the bar and type a note. ontap does it in <b>one tap</b> from your home or lock screen, so you actually keep it up.",
    publish="2026-10-23",
    body=SHOT.format(src="ss_widget.webp", alt="ontap widget logging a beer in one tap") + """
<h2>How it works</h2>
<ol>
<li><b>Add the widget</b> to your home or lock screen.</li>
<li><b>Tap it</b> when you order. ontap logs the beer and the bar you're at.</li>
<li><b>That's it.</b> Add a photo or tag friends later if you want.</li>
</ol>
<h2>What you get back</h2>
<ul>
<li><b>Your nights, mapped:</b> every spot you've been, filling up over time.</li>
<li><b>Friends who are out:</b> a shared map and a live list of who's out right now.</li>
<li><b>Squads:</b> race your group week by week, month by month.</li>
<li><b>30+ badges and Mayors:</b> log the most at your local and you're its Mayor.</li>
<li><b>Last Call:</b> a monthly recap of your nights out, made for sharing.</li>
</ul>
<h2>Private by default</h2>
<p>Only friends you add see where you've logged. Turn location sharing off whenever you like, and you only appear on the Global feed if you choose to.</p>
<h2>How ontap compares</h2>
<p>Want detailed ratings? See how ontap fits next to <a href="/untappd-alternatives/">Untappd</a>, or browse the <a href="/best-beer-tracking-apps/">best beer tracking apps</a>.</p>
""",
    faq=[
        ("Is ontap free?", "Yes, ontap is free on iPhone. An optional ontap Pro with extras is on the way."),
        ("Is ontap on Android?", "Not yet; ontap is iPhone only for now."),
        ("Does ontap work on the lock screen?", "Yes. The lock screen widget logs a beer without unlocking into the app."),
    ],
    related=["best-beer-tracking-apps", "untappd-alternatives", "squads"],
    cta="Log your next pint in one tap. ontap is free on iPhone.",
)

SQUADS = Page(
    slug="squads",
    kind="page",
    keyword="app for friend group nights out",
    title="ontap Squads: Your Friend Group's Weekly Nights-Out Race",
    h1="Squads: your group chat, with a leaderboard",
    description="Start a squad with your friends on ontap: see who's out, race week by week or month by month, and share the squad recap.",
    lede="A squad is your friend group inside ontap. Everyone logs their nights, and the squad page keeps score: who's out tonight, who's leading this week, and the recap at the end of the month.",
    publish="2026-10-28",
    body=SHOT.format(src="ss_friends.webp", alt="ontap friends map showing who's out") + """
<h2>What's in a squad</h2>
<ul>
<li><b>Who's out:</b> squad members out right now, at the top of your feed.</li>
<li><b>Week, Month or All time:</b> switch the leaderboard view.</li>
<li><b>The race:</b> a chart of the month, lead changes and all.</li>
<li><b>Squad Last Call:</b> a shareable recap card for the group chat or your story.</li>
</ul>
<h2>Start one in a minute</h2>
<ol>
<li>Get ontap and add your friends.</li>
<li>Create a squad and share the invite code.</li>
<li>Go out. The squad page does the rest.</li>
</ol>
<p>It's about nights out together, not about who drinks most: squads count nights, spots and moments as much as pints. Please drink responsibly.</p>
""",
    faq=[
        ("How many people can be in a squad?", "Squads work best for a friend group; invite everyone you go out with."),
        ("Do squads cost anything?", "No, squads are free."),
    ],
    related=["best-social-apps-for-nights-out", "beer-tracker-app", "last-call"],
    cta="Get your friends on ontap and start a squad. It's free.",
)

LAST_CALL = Page(
    slug="last-call",
    kind="page",
    keyword="beer wrapped",
    title="Last Call: Your Month in Beer, Wrapped (ontap)",
    h1="Last Call: your month in beer, wrapped",
    description="Like Spotify Wrapped, but for your nights out. ontap's Last Call recaps your month: top spots, go-to night, your map and more.",
    lede="You didn't keep a diary. You just tapped a button. At the start of every month, ontap hands it back as <b>Last Call</b>, a recap of your month in beer that's actually worth sharing.",
    publish="2026-10-31",
    body=SHOT.format(src="ss_lastcall.webp", alt="ontap Last Call monthly recap") + """
<h2>What's in your Last Call</h2>
<ul>
<li>Your top spots and how often you were there</li>
<li>Your go-to night of the week</li>
<li>Every night out on a calendar strip</li>
<li>New spots you tried this month</li>
<li>How your month compared with last month</li>
<li>A story card to share</li>
</ul>
<h2>When it drops</h2>
<p>Last Call goes live on the 1st of every month and stays open for five days. In December you also get the year's recap.</p>
<h2>Squad Last Call</h2>
<p>Your <a href="/squads/">squad</a> gets one too: the podium, the race and the biggest night together.</p>
""",
    faq=[
        ("Is there a Spotify Wrapped for beer?", "ontap's Last Call is exactly that: a monthly (and yearly) recap of your nights out, free on iPhone."),
    ],
    related=["squads", "beer-tracker-app", "best-beer-journal-apps"],
    cta="Your first Last Call starts with your first tap. ontap is free on iPhone.",
)

PAGES = [TRACKER, SQUADS, LAST_CALL]
