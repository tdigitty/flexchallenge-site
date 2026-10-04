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
        ("What is the best app to track 75 Soft?", "Any checklist app can work. FlexChallenge for iPhone includes a ready-made 75 Soft template with water and page counters, flexible mode for missed days, scheduled rest days and a calendar of finished days."),
    ],
)

hard = dict(
    slug="best-75-hard-apps",
    title="Best 75 Hard Tracker Apps for iPhone (2026): Compared",
    desc="An honest comparison of 75 Hard tracker apps for iPhone: the official 75 HARD app, FlexChallenge, Streaks and Habitify. Prices, features, privacy, and which one fits you.",
    eyebrow="Comparison",
    h1="The Best 75 Hard Tracker Apps for iPhone in 2026",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "75 Hard tracker apps"},
    body="""
        <p class="lede">75 Hard is simple on paper: five daily tasks for 75 days, and you restart if you miss one. The hard part is doing it every day, and a good tracker helps. Here is how the main iPhone options compare.</p>
        <p class="note">Full disclosure: we make FlexChallenge, so we're not neutral. We've tried to be fair about where the other apps do better.</p>

        <div class="tldr">
            <p><strong>Short answer:</strong></p>
            <ul>
                <li><strong>Only want 75 Hard, done the official way:</strong> the official 75 HARD app.</li>
                <li><strong>75 Hard plus other challenges (75 Soft, 30-day, custom), with photos and no account:</strong> FlexChallenge.</li>
                <li><strong>Ongoing daily habits with a great Apple Watch app, paid once:</strong> Streaks.</li>
                <li><strong>Habits on iPhone and Android, or a free plan:</strong> Habitify.</li>
            </ul>
        </div>

        <h2>Comparison table</h2>
        <div class="table-scroll"><table>
            <thead><tr><th scope="col"></th><th scope="col">75 HARD (official)</th><th scope="col">FlexChallenge</th><th scope="col">Streaks</th><th scope="col">Habitify</th></tr></thead>
            <tbody>
                <tr><th scope="row">Price</th><td>$4.99/month or $39.99/year</td><td>$3.99/month or $24.99/year; 14-day free trial</td><td>$5.99 one-time</td><td>Free for 3 habits; Premium from about $2.49/month billed yearly, or $59.99 lifetime</td></tr>
                <tr><th scope="row">Built for</th><td>75 Hard and its follow-on phases</td><td>Fixed-length challenges of 1–365 days</td><td>Ongoing daily habits</td><td>Ongoing daily habits</td></tr>
                <tr><th scope="row">75 Hard-style template</th><td>Yes (the official program)</td><td>Yes: 75 Days Phase I, II and III</td><td>No; set up tasks yourself</td><td>No; set up habits yourself</td></tr>
                <tr><th scope="row">Other programs</th><td>No</td><td>75 Soft, Core 4, Habit Stacking, Mindful Living, Creative Sprint, Revenue Growth, custom</td><td>Any habits you create, up to 24</td><td>Any habits you create</td></tr>
                <tr><th scope="row">Restart rule on a miss</th><td>Yes</td><td>Your choice: strict (restart or continue) or flexible</td><td>Streak resets</td><td>Streak resets</td></tr>
                <tr><th scope="row">Progress photos</th><td>Yes</td><td>Yes, plus video clips and voice notes</td><td>No</td><td>No</td></tr>
                <tr><th scope="row">Water and page counters</th><td>Checkbox per task</td><td>Water task in oz or glasses; page counter</td><td>Timed and count-style tasks</td><td>Goal amounts per habit</td></tr>
                <tr><th scope="row">Apple Health</th><td>&ndash;</td><td>Steps</td><td>Auto-completes Health-linked tasks</td><td>Health integrations</td></tr>
                <tr><th scope="row">Platforms</th><td>iPhone, Android</td><td>iPhone (iOS 17+)</td><td>iPhone, iPad, Apple Watch, Mac</td><td>iPhone, Android, web</td></tr>
                <tr><th scope="row">Account required</th><td>&ndash;</td><td>No; data stays on your device</td><td>No; iCloud sync</td><td>Account with cross-device sync</td></tr>
            </tbody>
        </table></div>
        """ + PRICE_NOTE + """

        <h2>1. The official 75 HARD app</h2>
        <p>Made by Andy Frisella's company, this is the one to pick if you want 75 Hard exactly as written. It gives you the five daily tasks (two workouts, diet, a gallon of water, ten pages, a progress photo), reminders and a photo timeline, and it continues into the later phases of the program. It does one thing: if you want to run a different challenge afterwards, you'll need another app. It moved from a one-time purchase to a subscription, which is the most common complaint in its reviews.</p>
        <p><strong>Best for:</strong> people who want the official program and nothing else.</p>

        <h2>2. FlexChallenge</h2>
        <p><a href="/">FlexChallenge</a> is a challenge tracker rather than a habit app: every challenge has a Day 1 and a finish line. The 75 Days: Phase I template sets up the full 75 Hard-style day (two workouts, a gallon of water, ten pages, a progress photo, strict diet), and Phases II and III follow on. Beyond 75 Hard it includes 75 Soft and six other templates, or you can build any challenge from 1 to 365 days.</p>
        <ul>
            <li><strong>Seven task types:</strong> yes/no, water, counter, Apple Health steps, photo, video and voice note, all in one daily checklist.</li>
            <li><strong>Strict or flexible mode:</strong> strict asks whether to restart from Day 1 when you miss a day, which is the 75 Hard rule; flexible logs the miss and carries on.</li>
            <li><strong>Calendar, stats and a media gallery</strong>, plus Home Screen and Lock Screen widgets.</li>
            <li><strong>Private by design:</strong> no account, no ads, no tracking; photos and data stay on your iPhone, with JSON backup and restore.</li>
        </ul>
        <p>It's iPhone-only, and there's no free tier after the 14-day trial.</p>
        <p><strong>Best for:</strong> people who want to do 75 Hard and then keep going with other challenges, with photos kept private on their phone.</p>

        <h2>3. Streaks</h2>
        <p>Streaks is one of the most popular habit trackers on iPhone and a former Apple Editor's Choice. You can track up to 24 tasks, many of which complete automatically from Apple Health, and its Apple Watch app is excellent. It's a one-time $5.99 purchase. It's designed for open-ended habits, though: there are no 75 Hard program templates or progress photos, and no built-in finish line, so you'll be counting to 75 yourself.</p>
        <p><strong>Best for:</strong> Apple Watch users who want ongoing habits and prefer to pay once. See our <a href="/flexchallenge-vs-streaks/">full FlexChallenge vs Streaks comparison</a>.</p>

        <h2>4. Habitify</h2>
        <p>Habitify is a cross-platform habit tracker with a free plan for up to three habits, which won't cover 75 Hard's five tasks. Premium unlocks unlimited habits. Its strengths are flexible schedules, analytics and sync across iPhone, Android and the web. Like Streaks, it has no 75 Hard template or progress photos, and it uses an account to sync.</p>
        <p><strong>Best for:</strong> people who switch between iPhone and Android or want habits on the web.</p>

        <h2>What to look for in a 75 Hard tracker</h2>
        <ul>
            <li><strong>All five tasks in one checklist</strong>, so the day is done when the list is.</li>
            <li><strong>A clear restart rule.</strong> 75 Hard resets on any miss; your app should either enforce that or let you choose.</li>
            <li><strong>Private progress photos.</strong> You'll take 75 of them; know where they're stored.</li>
            <li><strong>A late day-end time</strong> if you train after midnight, so the workout still counts for the right day.</li>
            <li><strong>Something for Day 76.</strong> The most useful app is one you'll keep using after the challenge ends.</li>
        </ul>
""" + "\n        " + DISCLAIMER,
    faqs=[
        ("Is there an official 75 Hard app?", "Yes. The official 75 HARD app is published by Andy Frisella's company and costs $4.99/month or $39.99/year on the US App Store (October 2026)."),
        ("What is the best free 75 Hard tracker?", "There's no fully free option among the apps compared here. Habitify's free plan allows only three habits, fewer than 75 Hard's five tasks. FlexChallenge offers a 14-day free trial, and a paper checklist is always free."),
        ("Can I track 75 Hard with a regular habit tracker?", "Yes, by creating the five tasks yourself. You'll be counting to 75 manually, and most habit trackers don't store progress photos or enforce the restart rule."),
        ("Which 75 Hard app keeps my progress photos private?", "FlexChallenge stores photos, videos and voice notes only on your iPhone, with no account and no cloud upload. You choose where any backup goes."),
    ],
)

streaks = dict(
    slug="flexchallenge-vs-streaks",
    title="FlexChallenge vs Streaks: Which iPhone Tracker Is Right for You?",
    desc="FlexChallenge vs Streaks compared: challenge tracker vs habit tracker, pricing, task types, progress photos, Apple Watch, privacy. An honest Streaks alternative guide.",
    eyebrow="Comparison",
    h1="FlexChallenge vs Streaks",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "FlexChallenge vs Streaks"},
    body="""
        <p class="lede">Streaks and FlexChallenge both put a daily checklist on your iPhone, but they're built on different ideas. Streaks helps you keep habits going indefinitely. FlexChallenge helps you finish a challenge with a set end date. Which one suits you depends on which of those you're after.</p>
        <p class="note">Full disclosure: we make FlexChallenge. Streaks is a well-made app, and for some people it's the better choice. We say which people below.</p>

        <div class="tldr">
            <p><strong>Pick Streaks</strong> if you want open-ended daily habits, a strong Apple Watch app, iPad and Mac support, and a one-time price.</p>
            <p><strong>Pick FlexChallenge</strong> if you want challenges with a finish line (75 Hard-style, 75 Soft, 30 or 90 days), progress photos and voice notes, ready-made programs, or a strict mode that makes you restart.</p>
        </div>

        <h2>Side by side</h2>
        <div class="table-scroll"><table>
            <thead><tr><th scope="col"></th><th scope="col">FlexChallenge</th><th scope="col">Streaks</th></tr></thead>
            <tbody>
                <tr><th scope="row">Core idea</th><td>Challenges with a Day 1 and a final day (1–365 days)</td><td>Ongoing habits and streaks</td></tr>
                <tr><th scope="row">Price</th><td>$3.99/month or $24.99/year; 14-day free trial</td><td>$5.99 one-time</td></tr>
                <tr><th scope="row">Templates</th><td>9: 75 Days Phase I, II, III; 75 Soft; Core 4; Habit Stacking; Mindful Living; Creative Sprint; Revenue Growth</td><td>Build your own from suggested tasks</td></tr>
                <tr><th scope="row">Task limit</th><td>&ndash;</td><td>Up to 24 tasks</td></tr>
                <tr><th scope="row">Task types</th><td>Yes/no, water, counter, Apple Health steps, photo, video, voice note</td><td>Yes/no, timed, negative ("don't do") and Health-linked tasks</td></tr>
                <tr><th scope="row">Progress photos and voice notes</th><td>Yes, saved per day with a gallery</td><td>No</td></tr>
                <tr><th scope="row">Missed day</th><td>Strict (restart or continue) or flexible, per challenge</td><td>Streak resets</td></tr>
                <tr><th scope="row">Rest days</th><td>Choose which weekdays count; scheduled rest days don't break the streak</td><td>Set which days each task is due</td></tr>
                <tr><th scope="row">Apple Health</th><td>Reads steps</td><td>Auto-completes many Health-linked tasks</td></tr>
                <tr><th scope="row">Devices</th><td>iPhone (iOS 17+), widgets</td><td>iPhone, iPad, Apple Watch, Mac, widgets</td></tr>
                <tr><th scope="row">Data</th><td>On device only; no account; JSON backup</td><td>iCloud sync; no account</td></tr>
            </tbody>
        </table></div>
        """ + PRICE_NOTE + """

        <h2>Habits vs challenges</h2>
        <p>A streak has no end. That works well for small, permanent habits such as flossing or taking vitamins. For bigger efforts it can turn into pressure: the longer the streak, the more breaking it hurts, and there's never a moment where you're done.</p>
        <p>A challenge has a finish line. You commit to 30, 75 or 90 days, and you know when it ends. That makes harder goals easier to start, gives you a clear win at the end, and lets you choose what comes next. FlexChallenge is built around that loop: start, finish, then start the next challenge.</p>

        <h2>Where Streaks is better</h2>
        <ul>
            <li><strong>Apple Watch, iPad and Mac.</strong> If you check things off from your wrist, Streaks is hard to beat.</li>
            <li><strong>Automatic Health tracking</strong> for many task types, not just steps.</li>
            <li><strong>One-time price.</strong> Pay once rather than subscribe.</li>
            <li><strong>Negative habits</strong>, such as "don't smoke", as a task type.</li>
        </ul>

        <h2>Where FlexChallenge is better</h2>
        <ul>
            <li><strong>Structured programs.</strong> Start 75 Days Phase I, 75 Soft or Core 4 in a minute instead of building them from scratch.</li>
            <li><strong>A real end date</strong>, with a calendar that shows the whole challenge and a summary when you finish.</li>
            <li><strong>Proof of progress:</strong> daily photos, video clips and voice notes, kept in one gallery on your phone.</li>
            <li><strong>Strict mode</strong> for 75 Hard-style rules: miss a day and the app asks whether you're starting over.</li>
            <li><strong>Water and page counters</strong> built for the usual challenge tasks.</li>
            <li><strong>Privacy:</strong> no account, no ads, no tracking, and no cloud copy of your photos.</li>
        </ul>

        <h2>Can you use both?</h2>
        <p>Yes, and some people do: Streaks for permanent daily habits on the Watch, and FlexChallenge for the 75-day or 30-day challenge they're working through right now.</p>
""" + "\n        " + DISCLAIMER,
    faqs=[
        ("Is FlexChallenge a good Streaks alternative?", "Yes, if you want challenges with a set end date, ready-made programs like 75 Soft, or progress photos and voice notes. If you mainly want open-ended habits on Apple Watch, Streaks is the better fit."),
        ("Is Streaks a subscription?", "No. Streaks is a one-time purchase ($5.99 on the US App Store as of October 2026). FlexChallenge is a subscription at $3.99/month or $24.99/year with a 14-day free trial."),
        ("Can Streaks track 75 Hard?", "You can create the five 75 Hard tasks in Streaks yourself, but it doesn't count down to Day 75, store progress photos, or ask you to restart when you miss a day."),
        ("Does FlexChallenge work on Apple Watch?", "FlexChallenge runs on iPhone (iOS 17 or later) with Home Screen and Lock Screen widgets. If an Apple Watch app is essential for you, Streaks has one."),
    ],
)

PAGES = [soft, hard, streaks]
