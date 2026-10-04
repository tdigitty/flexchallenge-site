"""Content for the keyword guide pages. Competitor facts were checked against
App Store listings and vendor pricing pages in October 2026; re-verify before editing."""

APP = "https://apps.apple.com/us/app/flexchallenge/id6757351926"
DISCLAIMER = ('<p class="note">75 Hard is a trademark of Andy Frisella. FlexChallenge is not affiliated with, '
              'endorsed by, or sponsored by Andy Frisella or 75 Hard. Other product names belong to their owners. '
              'Check with a physician before starting any fitness or nutrition program.</p>')
PRICE_NOTE = ('<p class="note">Prices are US App Store prices as listed in October 2026 and can change; '
              'check each app\'s listing for current pricing in your region.</p>')

soft = dict(
    slug="75-soft-challenge",
    title="75 Soft Challenge Rules: The Full List and How to Track It",
    desc="The 75 Soft challenge rules explained: daily 45-minute workout, eating well, 3 liters of water, 10 pages of reading. How it compares to 75 Hard, and how to track all 75 days on iPhone.",
    eyebrow="Guide",
    h1="75 Soft Challenge Rules (and How to Track Every Day)",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "75 Soft challenge"},
    body="""
        <p class="lede">75 Soft is a 75-day self-improvement challenge built as a gentler, more sustainable version of 75 Hard. Four daily rules, one rest day a week, and no restarting from Day 1 when you slip.</p>

        <div class="tldr">
            <p><strong>The 75 Soft rules at a glance:</strong></p>
            <ul>
                <li><strong>Exercise 45 minutes a day</strong>, with one active-recovery day each week.</li>
                <li><strong>Eat well</strong> and only drink alcohol on social occasions.</li>
                <li><strong>Drink 3 liters of water</strong> (about 101 oz) every day.</li>
                <li><strong>Read 10 pages</strong> of any book.</li>
                <li>Do it for <strong>75 days in a row</strong>.</li>
            </ul>
        </div>

        <h2>Where 75 Soft comes from</h2>
        <p>75 Soft started on social media as a response to 75 Hard, Andy Frisella's strict 75-day program. People liked the idea of a long, defined challenge but wanted rules they could keep while working, parenting and recovering properly. There is no single official 75 Soft rulebook, so the version above is the most commonly shared one. Treat it as a starting point and adjust it to your own life.</p>

        <h2>The rules in detail</h2>
        <h3>1. A 45-minute workout every day</h3>
        <p>Any training counts: lifting, running, cycling, a fitness class, a long walk. One day a week is active recovery, such as yoga, stretching or an easy walk. Unlike 75 Hard, there is no second workout and no outdoor requirement.</p>
        <h3>2. Eat well, with alcohol only on social occasions</h3>
        <p>There is no prescribed diet. The rule is to make deliberate, healthy choices and keep drinking to social events. Many people define this up front, for example "home-cooked dinners on weekdays" or "no fast food", so it is clear on Day 40 what counts.</p>
        <h3>3. Drink 3 liters of water</h3>
        <p>That is roughly 101 oz or 12–13 glasses. 75 Hard asks for a full gallon (128 oz).</p>
        <h3>4. Read 10 pages</h3>
        <p>Any book works: fiction, nonfiction, audiobooks if you choose to count them. 75 Hard limits reading to nonfiction and excludes audiobooks.</p>
        <h3>Progress photos (optional)</h3>
        <p>75 Soft does not require a daily progress photo, but many people take one on Day 1 and Day 75, or once a week, to see the change.</p>

        <h2>75 Soft vs 75 Hard</h2>
        <div class="table-scroll"><table>
            <thead><tr><th scope="col">Rule</th><th scope="col">75 Soft</th><th scope="col">75 Hard</th></tr></thead>
            <tbody>
                <tr><th scope="row">Workouts</th><td>One 45-minute workout a day; one active-recovery day a week</td><td>Two 45-minute workouts a day; one must be outdoors</td></tr>
                <tr><th scope="row">Diet</th><td>Eat well; alcohol only on social occasions</td><td>Follow a diet with no cheat meals and no alcohol</td></tr>
                <tr><th scope="row">Water</th><td>3 liters (about 101 oz)</td><td>1 gallon (128 oz)</td></tr>
                <tr><th scope="row">Reading</th><td>10 pages of any book</td><td>10 pages of a nonfiction book; no audiobooks</td></tr>
                <tr><th scope="row">Progress photo</th><td>Optional</td><td>Every day</td></tr>
                <tr><th scope="row">Miss a day</th><td>Keep going</td><td>Start over at Day 1</td></tr>
            </tbody>
        </table></div>
        <p>Choose 75 Soft if you want a challenge you can keep up alongside a busy schedule, or as a lead-in to 75 Hard. Choose 75 Hard if the all-or-nothing restart rule is the point for you.</p>

        <h2>Tips for finishing all 75 days</h2>
        <ul>
            <li><strong>Write your rules down on Day 1.</strong> Decide exactly what "eat well" means before you are tired and hungry.</li>
            <li><strong>Plan your recovery day.</strong> Pick the same weekday each week so it is a plan, not an excuse.</li>
            <li><strong>Front-load the water.</strong> A liter before lunch makes the last liter easy.</li>
            <li><strong>Track every day, in one place.</strong> A checklist you open every morning keeps the challenge in front of you, and a calendar of finished days is motivating around Day 30, when most people quit.</li>
            <li><strong>Plan what comes after Day 75.</strong> Some people move on to 75 Hard; others start another 30- or 90-day challenge so they don't lose momentum.</li>
        </ul>

        <h2>How to track 75 Soft on iPhone with FlexChallenge</h2>
        <p><a href="/">FlexChallenge</a> includes a 75 Soft template, so setup takes about a minute:</p>
        <ul>
            <li><strong>Start from the 75 Soft template</strong> (75 days, five daily tasks) and edit any task to match your version of the rules, for example setting the water goal to 101 oz.</li>
            <li><strong>Water</strong> is a water task with visual progress; <strong>reading</strong> is a counter that tracks pages.</li>
            <li><strong>Pick flexible mode</strong> so a missed day is logged and the challenge keeps going, which is how 75 Soft works.</li>
            <li><strong>Schedule your recovery day</strong> as a rest day so it never breaks your streak.</li>
            <li><strong>Add an optional progress photo task</strong>; photos are saved day by day and stay on your phone.</li>
            <li><strong>Check the calendar</strong> to see every finished day, and use the Home Screen widget to keep today's tasks in sight.</li>
        </ul>
        <p>FlexChallenge is $3.99/month or $24.99/year after a 14-day free trial, with no account and no ads. Your data stays on your device.</p>
""" + "\n        " + DISCLAIMER,
    faqs=[
        ("What are the 75 Soft rules?", "For 75 days in a row: exercise for 45 minutes a day with one active-recovery day each week, eat well and only drink alcohol on social occasions, drink 3 liters of water, and read 10 pages of any book."),
        ("Do you have to restart 75 Soft if you miss a day?", "No. Unlike 75 Hard, the commonly shared 75 Soft rules don't require starting over at Day 1. You log the miss and keep going."),
        ("How much water is 75 Soft?", "3 liters a day, which is about 101 fluid ounces or 12–13 glasses. 75 Hard requires a gallon (128 oz)."),
        ("Is 75 Soft easier than 75 Hard?", "Yes. 75 Soft has one workout a day instead of two, a weekly recovery day, no outdoor-workout or strict-diet rule, less water, any book for reading, and no restart penalty."),
        ("What is the best app to track 75 Soft?", "FlexChallenge for iPhone. It includes a ready-made 75 Soft template with water and page counters, flexible mode for missed days, scheduled rest days and a calendar of finished days."),
    ],
)

Y = '<span class="y">✓</span> '
N = '<span class="n">✗</span> '

hard = dict(
    slug="best-75-hard-apps",
    title="Best 75 Hard Tracker App for iPhone (2026): FlexChallenge vs 75 HARD, Streaks, Habitify",
    desc="Comparing 75 Hard tracker apps for iPhone: FlexChallenge vs the official 75 HARD app, Streaks and Habitify. Templates, custom challenges, progress photos, privacy and price.",
    eyebrow="Comparison",
    h1="The Best 75 Hard Tracker App for iPhone in 2026",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "75 Hard tracker apps"},
    body="""
        <p class="lede">75 Hard is simple on paper: five daily tasks for 75 days, and you restart if you miss one. Doing it every day is the hard part, and the right tracker makes the difference. Here's how FlexChallenge compares with the official 75 HARD app, Streaks and Habitify.</p>

        <div class="tldr">
            <p><strong>Why FlexChallenge comes out on top:</strong></p>
            <ul>
                <li><strong>75 Hard ready to go:</strong> the 75 Days: Phase I template sets up the full day in a minute, with Phases II and III to follow.</li>
                <li><strong>Not just 75 Hard:</strong> 75 Soft, six more templates, or any custom challenge from 1 to 365 days with your own tasks.</li>
                <li><strong>Proof of progress:</strong> daily photos, video clips and voice notes in one gallery.</li>
                <li><strong>Your rules:</strong> strict mode for the 75 Hard restart rule, or flexible mode for everything else.</li>
                <li><strong>Private:</strong> no account, no ads, nothing uploaded. And at $24.99 a year, it costs less than the official app.</li>
            </ul>
        </div>

        <h2>Comparison table</h2>
        <div class="table-scroll"><table class="compare">
            <thead><tr><th scope="col"></th><th scope="col"><span class="badge">Best pick</span>FlexChallenge</th><th scope="col">75 HARD (official)</th><th scope="col">Streaks</th><th scope="col">Habitify</th></tr></thead>
            <tbody>
                <tr><th scope="row">75 Hard template</th><td>""" + Y + """75 Days Phase I, II and III</td><td>""" + Y + """75 Hard and its phases</td><td>""" + N + """Build it yourself</td><td>""" + N + """Build it yourself</td></tr>
                <tr><th scope="row">Custom challenges</th><td>""" + Y + """Any tasks, any length from 1 to 365 days</td><td>""" + N + """75 Hard only</td><td>""" + N + """Open-ended habits, no end date</td><td>""" + N + """Open-ended habits, no end date</td></tr>
                <tr><th scope="row">Other ready-made programs</th><td>""" + Y + """75 Soft, Core 4, Habit Stacking, Mindful Living, Creative Sprint, Revenue Growth</td><td>""" + N + """</td><td>""" + N + """</td><td>""" + N + """</td></tr>
                <tr><th scope="row">Countdown to Day 75</th><td>""" + Y + """Day X of 75, with a finish-line date</td><td>""" + Y + """</td><td>""" + N + """Streak count only</td><td>""" + N + """Streak count only</td></tr>
                <tr><th scope="row">Progress photos</th><td>""" + Y + """Plus video clips and voice notes</td><td>""" + Y + """Photos</td><td>""" + N + """</td><td>""" + N + """</td></tr>
                <tr><th scope="row">Restart rule on a miss</th><td>""" + Y + """Strict or flexible, your choice per challenge</td><td>Strict only</td><td>Streak resets</td><td>Streak resets</td></tr>
                <tr><th scope="row">Water and page tracking</th><td>""" + Y + """Water in oz or glasses; page counter</td><td>Checkbox per task</td><td>Count-style tasks</td><td>Goal amounts</td></tr>
                <tr><th scope="row">Calendar, stats and gallery</th><td>""" + Y + """All three</td><td>Photo timeline</td><td>Stats</td><td>Stats</td></tr>
                <tr><th scope="row">No account, data on device</th><td>""" + Y + """</td><td>&ndash;</td><td>iCloud sync</td><td>""" + N + """Account required to sync</td></tr>
                <tr><th scope="row">Price</th><td><strong>$24.99/year</strong> or $3.99/month; 14-day free trial</td><td>$39.99/year or $4.99/month</td><td>$5.99 one-time</td><td>Free for 3 habits; Premium from about $2.49/month billed yearly</td></tr>
            </tbody>
        </table></div>
        """ + PRICE_NOTE + """

        <h2>FlexChallenge vs the official 75 HARD app</h2>
        <p>The official app tracks one program: 75 Hard and its later phases. FlexChallenge tracks that too, with the 75 Days: Phase I template setting up two workouts, a gallon of water, ten pages, a progress photo and your diet as one daily checklist. It also tracks whatever you want to do next.</p>
        <ul>
            <li><strong>Any challenge you can think of.</strong> 75 Soft when you need a lighter round, a 30-day reading sprint, a 90-day business push, or a custom challenge with your own tasks and length.</li>
            <li><strong>More ways to log a day.</strong> Seven task types, including water, counters, Apple Health steps, photos, video and voice notes.</li>
            <li><strong>Your call on misses.</strong> Strict mode enforces the 75 Hard restart; flexible mode logs the miss and keeps going.</li>
            <li><strong>Lower price.</strong> $24.99 a year versus $39.99, with a 14-day free trial.</li>
            <li><strong>Private.</strong> Your 75 progress photos stay on your iPhone. No account, no ads, no tracking.</li>
        </ul>

        <h2>FlexChallenge vs Streaks</h2>
        <p>Streaks is a general habit tracker built around open-ended streaks. There's no 75 Hard template, no countdown to Day 75 and no progress photos, so you'd be setting up the program and counting days yourself. FlexChallenge is built for exactly this: a challenge with a start, a finish line and proof of every day in between. See the <a href="/flexchallenge-vs-streaks/">full FlexChallenge vs Streaks comparison</a>.</p>

        <h2>FlexChallenge vs Habitify</h2>
        <p>Habitify's free plan stops at three habits, fewer than 75 Hard's five tasks, so you'll need Premium. Even then there's no 75 Hard template, no progress photos and no finish line, and syncing needs an account. FlexChallenge gives you the full program on day one, with nothing to sign up for.</p>

        <h2>What to look for in a 75 Hard tracker</h2>
        <ul>
            <li><strong>All five tasks in one checklist</strong>, so the day is done when the list is.</li>
            <li><strong>A clear restart rule</strong> that matches how you're running the challenge.</li>
            <li><strong>Private progress photos.</strong> You'll take 75 of them; know where they're stored.</li>
            <li><strong>A late day-end time</strong> if you train after midnight, so the workout counts for the right day.</li>
            <li><strong>Something for Day 76.</strong> The best app is one you keep using after the challenge ends. FlexChallenge lets you start the next challenge straight away.</li>
        </ul>
""" + "\n        " + DISCLAIMER,
    faqs=[
        ("What is the best 75 Hard tracker app for iPhone?", "FlexChallenge. It includes a 75 Days: Phase I template for the full 75 Hard routine, plus 75 Soft, other programs and fully custom challenges, with progress photos, strict or flexible mode, and no account. It costs $24.99/year after a 14-day free trial."),
        ("Is there an official 75 Hard app?", "Yes. The official 75 HARD app costs $4.99/month or $39.99/year on the US App Store (October 2026) and tracks only the 75 Hard program. FlexChallenge covers 75 Hard and any other challenge you set up, for $24.99/year."),
        ("Can I make my own challenge after 75 Hard?", "With FlexChallenge, yes. Start another template such as 75 Soft or Core 4, or build a custom challenge with your own tasks and any length from 1 to 365 days."),
        ("Which 75 Hard app keeps my progress photos private?", "FlexChallenge stores photos, videos and voice notes only on your iPhone, with no account and no cloud upload. You choose where any backup goes."),
    ],
)

streaks = dict(
    slug="flexchallenge-vs-streaks",
    title="FlexChallenge vs Streaks: The Streaks Alternative Built for Challenges",
    desc="FlexChallenge vs Streaks compared: challenges with a finish line vs open-ended streaks, ready-made programs like 75 Hard and 75 Soft, progress photos, strict mode and privacy.",
    eyebrow="Comparison",
    h1="FlexChallenge vs Streaks",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "FlexChallenge vs Streaks"},
    body="""
        <p class="lede">Streaks and FlexChallenge both put a daily checklist on your iPhone. The difference is what happens over time. Streaks counts up forever. FlexChallenge gives every goal a Day 1 and a finish line, plus the programs, task types and proof you need to get there.</p>

        <div class="tldr">
            <p><strong>Why people switch from Streaks to FlexChallenge:</strong></p>
            <ul>
                <li><strong>Challenges that end:</strong> commit to 30, 75 or 365 days and actually finish.</li>
                <li><strong>Ready-made programs:</strong> 75 Days Phase I–III, 75 Soft, Core 4 and more, set up in a minute.</li>
                <li><strong>Proof of progress:</strong> daily photos, video clips and voice notes.</li>
                <li><strong>Strict or flexible:</strong> choose whether a missed day means starting over.</li>
            </ul>
        </div>

        <h2>Side by side</h2>
        <div class="table-scroll"><table class="compare two">
            <thead><tr><th scope="col"></th><th scope="col"><span class="badge">Best pick</span>FlexChallenge</th><th scope="col">Streaks</th></tr></thead>
            <tbody>
                <tr><th scope="row">Challenges with an end date</th><td>""" + Y + """Any length from 1 to 365 days</td><td>""" + N + """Open-ended streaks</td></tr>
                <tr><th scope="row">Ready-made programs</th><td>""" + Y + """9 templates: 75 Days Phase I, II, III; 75 Soft; Core 4; Habit Stacking; Mindful Living; Creative Sprint; Revenue Growth</td><td>""" + N + """Build each task yourself</td></tr>
                <tr><th scope="row">Progress photos</th><td>""" + Y + """Saved per day, with a gallery</td><td>""" + N + """</td></tr>
                <tr><th scope="row">Video clips and voice notes</th><td>""" + Y + """</td><td>""" + N + """</td></tr>
                <tr><th scope="row">Water tracking</th><td>""" + Y + """Ounces or glasses, with visual progress</td><td>Count-style task</td></tr>
                <tr><th scope="row">Missed day</th><td>""" + Y + """Strict (restart or continue) or flexible, per challenge</td><td>Streak resets</td></tr>
                <tr><th scope="row">Scheduled rest days</th><td>""" + Y + """Never break your streak</td><td>Set which days each task is due</td></tr>
                <tr><th scope="row">Custom day-end time</th><td>""" + Y + """A 1 a.m. workout still counts for today</td><td>&ndash;</td></tr>
                <tr><th scope="row">Calendar of the whole challenge</th><td>""" + Y + """Every day, with tasks, notes and photos</td><td>History view</td></tr>
                <tr><th scope="row">Apple Health steps</th><td>""" + Y + """</td><td>""" + Y + """</td></tr>
                <tr><th scope="row">Widgets</th><td>""" + Y + """Home Screen and Lock Screen</td><td>""" + Y + """</td></tr>
                <tr><th scope="row">No account, private</th><td>""" + Y + """Data stays on your device</td><td>""" + Y + """iCloud sync</td></tr>
            </tbody>
        </table></div>

        <h2>Streaks never end. Challenges do.</h2>
        <p>A streak has no finish line. The longer it runs, the more it hurts to break, until keeping the number alive matters more than the habit. And there's never a day when you're done.</p>
        <p>A challenge is different. You commit to 30, 75 or 90 days and you know exactly when it ends. That makes harder goals easier to start, gives you a real win at the end, and lets you choose what comes next. FlexChallenge is built around that loop: start, finish, stack the next one.</p>

        <h2>What you get with FlexChallenge</h2>
        <ul>
            <li><strong>Structured programs.</strong> Start 75 Days Phase I, 75 Soft or Core 4 in a minute instead of building them task by task.</li>
            <li><strong>Any custom challenge.</strong> Your tasks, your length, your weekdays.</li>
            <li><strong>Seven task types</strong> in one checklist: yes/no, water, counter, Apple Health steps, photo, video and voice note.</li>
            <li><strong>Proof of progress</strong> in one gallery: see Day 1 next to Day 75.</li>
            <li><strong>Strict mode</strong> for 75 Hard-style rules, or <strong>flexible mode</strong> when life happens.</li>
            <li><strong>Stats that matter for a challenge:</strong> completion rate, streaks, personal bests and trends across every challenge you run.</li>
            <li><strong>Privacy:</strong> no account, no ads, no tracking, and no cloud copy of your photos.</li>
        </ul>
""" + "\n        " + DISCLAIMER,
    faqs=[
        ("Is FlexChallenge a good Streaks alternative?", "Yes. FlexChallenge does daily check-offs like Streaks, and adds challenges with a set end date, ready-made programs like 75 Hard-style Phase I and 75 Soft, progress photos and voice notes, and a choice of strict or flexible mode."),
        ("What's the difference between a habit tracker and a challenge tracker?", "A habit tracker counts an open-ended streak. A challenge tracker like FlexChallenge gives each goal a Day 1 and a final day, so you commit to a fixed period, see how far along you are, and finish."),
        ("Can Streaks track 75 Hard?", "You can create the five tasks in Streaks yourself, but it doesn't count down to Day 75, store progress photos, or ask you to restart when you miss a day. FlexChallenge does all three with its 75 Days: Phase I template."),
        ("How much does FlexChallenge cost?", "$3.99/month or $24.99/year, with a 14-day free trial on either plan. No account and no ads."),
    ],
)

PAGES = [soft, hard, streaks]
