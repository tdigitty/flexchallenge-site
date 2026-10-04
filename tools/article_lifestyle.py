"""The challenge-based lifestyle essay. Every number below is tied to a numbered
source in SOURCES; keep them in sync if you edit."""

SOURCES = [
    ("bem", 'Bem, D. J. (1972). Self-perception theory. <em>Advances in Experimental Social Psychology</em>, 6, 1–62.', "https://doi.org/10.1016/S0065-2601(08)60024-6"),
    ("bodner", 'Bodner, R., & Prelec, D. (2003). Self-signaling and diagnostic utility in everyday decision making. In <em>The Psychology of Economic Decisions, Vol. 1</em>. Oxford University Press.', "https://nel.mit.edu/wp-content/uploads/2016/10/21prelecbodnercopy.pdf"),
    ("benabou", 'Bénabou, R., & Tirole, J. (2004). Willpower and personal rules. <em>Journal of Political Economy</em>, 112(4), 848–886.', "https://doi.org/10.1086/421171"),
    ("lally", 'Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6), 998–1009.', "https://doi.org/10.1002/ejsp.674"),
    ("locke", 'Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. <em>American Psychologist</em>, 57(9), 705–717.', "https://doi.org/10.1037/0003-066X.57.9.705"),
    ("shu", 'Shu, S. B., & Gneezy, A. (2010). Procrastination of enjoyable experiences. <em>Journal of Marketing Research</em>, 47(5), 933–944.', "https://doi.org/10.1509/jmkr.47.5.933"),
    ("kivetz", 'Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected: Purchase acceleration, illusionary goal progress, and customer retention. <em>Journal of Marketing Research</em>, 43(1), 39–58.', "https://doi.org/10.1509/jmkr.43.1.39"),
    ("koo", 'Koo, M., & Fishbach, A. (2012). The small-area hypothesis: Effects of progress monitoring on goal adherence. <em>Journal of Consumer Research</em>, 39(3), 493–509.', "https://doi.org/10.1086/663827"),
    ("dai", 'Dai, H., Milkman, K. L., & Riis, J. (2014). The fresh start effect: Temporal landmarks motivate aspirational behavior. <em>Management Science</em>, 60(10), 2563–2582.', "https://doi.org/10.1287/mnsc.2014.1901"),
    ("sheldon", 'Sheldon, K. M., & Elliot, A. J. (1999). Goal striving, need satisfaction, and longitudinal well-being: The self-concordance model. <em>Journal of Personality and Social Psychology</em>, 76(3), 482–497.', "https://doi.org/10.1037/0022-3514.76.3.482"),
    ("harkin", 'Harkin, B., Webb, T. L., Chang, B. P. I., Prestwich, A., Conner, M., Kellar, I., Benn, Y., & Sheeran, P. (2016). Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychological Bulletin</em>, 142(2), 198–229.', "https://doi.org/10.1037/bul0000025"),
    ("amabile", 'Amabile, T. M., & Kramer, S. J. (2011). The power of small wins. <em>Harvard Business Review</em>, May 2011. See also <em>The Progress Principle</em> (Harvard Business Review Press, 2011).', "https://hbr.org/2011/05/the-power-of-small-wins"),
    ("weick", 'Weick, K. E. (1984). Small wins: Redefining the scale of social problems. <em>American Psychologist</em>, 39(1), 40–49.', "https://doi.org/10.1037/0003-066X.39.1.40"),
    ("bandura", 'Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. <em>Psychological Review</em>, 84(2), 191–215.', "https://doi.org/10.1037/0033-295X.84.2.191"),
    ("herman", 'Herman, C. P., & Mack, D. (1975). Restrained and unrestrained eating. <em>Journal of Personality</em>, 43(4), 647–660.', "https://pubmed.ncbi.nlm.nih.gov/1206453/"),
    ("polivy", 'Polivy, J., & Herman, C. P. (1985). Dieting and binging: A causal analysis. <em>American Psychologist</em>, 40(2), 193–201.', "https://doi.org/10.1037/0003-066X.40.2.193"),
    ("marlatt", 'Marlatt, G. A., & Gordon, J. R. (Eds.). (1985). <em>Relapse Prevention: Maintenance Strategies in the Treatment of Addictive Behaviors</em>. Guilford Press.', None),
    ("sharif", 'Sharif, M. A., & Shu, S. B. (2021). Nudging persistence after failure through emergency reserves. <em>Organizational Behavior and Human Decision Processes</em>, 163, 17–29.', "https://ideas.repec.org/a/eee/jobhdp/v163y2021icp17-29.html"),
    ("milkman", 'Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. <em>Nature</em>, 600, 478–483.', "https://doi.org/10.1038/s41586-021-04128-4"),
    ("gollwitzer", 'Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. <em>Advances in Experimental Social Psychology</em>, 38, 69–119.', "https://doi.org/10.1016/S0065-2601(06)38002-1"),
    ("oscarsson", 'Oscarsson, M., Carlbring, P., Andersson, G., & Rozental, A. (2020). A large-scale experiment on New Year\'s resolutions: Approach-oriented goals are more successful than avoidance-oriented goals. <em>PLOS ONE</em>, 15(12), e0234097.', "https://doi.org/10.1371/journal.pone.0234097"),
    ("norcross", 'Norcross, J. C., Mrykalo, M. S., & Blagys, M. D. (2002). Auld lang syne: Success predictors, change processes, and self-reported outcomes of New Year\'s resolvers and nonresolvers. <em>Journal of Clinical Psychology</em>, 58(4), 397–405.', "https://pubmed.ncbi.nlm.nih.gov/11920693/"),
    ("clear", 'Clear, J. (2018). <em>Atomic Habits</em>. Avery.', "https://jamesclear.com/quotes"),
    ("durant", 'Durant, W. (1926). <em>The Story of Philosophy</em>. On the common misattribution to Aristotle, see Check Your Fact (2019).', "https://checkyourfact.com/2019/06/26/fact-check-aristotle-excellence-habit-repeatedly-do/"),
    ("core4", 'Wake Up Warrior. Core 4. warrioros.com.', "https://warrioros.com/core-4/"),
]
IDX = {k: i + 1 for i, (k, _, _) in enumerate(SOURCES)}


def c(*keys):
    return "".join(f'<sup><a href="#src-{IDX[k]}" aria-label="Source {IDX[k]}">[{IDX[k]}]</a></sup>' for k in keys)


INK, BLUE, VOLT, MUTED, RULE, PAPER = "#16150F", "#0A72CD", "#C8F222", "#55524A", "rgba(22,21,15,0.25)", "#FBF9F4"
FONT = "font-family:Archivo,-apple-system,sans-serif"

FIG_LEDGER = f"""
        <figure>
            <svg viewBox="0 0 640 300" role="img" aria-labelledby="fl-t fl-d"><title id="fl-t">The self-trust ledger</title><desc id="fl-d">Two paths over time. Each kept promise moves self-trust up; each broken promise moves it down, and the downward path gets easier to follow.</desc>
                <g style="{FONT}">
                <line x1="50" y1="150" x2="610" y2="150" stroke="{RULE}" stroke-width="2"/>
                <text x="50" y="140" font-size="13" fill="{MUTED}">Today</text>
                <polyline points="50,150 120,140 190,130 260,119 330,108 400,96 470,84 540,72 600,60" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linejoin="round"/>
                <g fill="{BLUE}">{''.join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x, y in [(120, 140), (190, 130), (260, 119), (330, 108), (400, 96), (470, 84), (540, 72)])}</g>
                <text x="604" y="22" font-size="15" font-weight="700" fill="{INK}" text-anchor="end">Kept promises</text>
                <text x="604" y="40" font-size="13" fill="{MUTED}" text-anchor="end">"I'm someone who follows through"</text>
                <polyline points="50,150 120,160 190,172 260,186 330,202 400,218 470,234 540,250 600,264" fill="none" stroke="#B91C1C" stroke-width="5" stroke-dasharray="2 10" stroke-linecap="round" stroke-linejoin="round"/>
                <text x="604" y="288" font-size="15" font-weight="700" fill="{INK}" text-anchor="end">Quietly broken promises</text>
                <text x="50" y="288" font-size="13" fill="{MUTED}">"I'll start Monday" … again</text>
                </g>
            </svg>
            <figcaption>An illustration, not data. Self-perception and self-signaling research suggest we read our own actions as evidence about who we are{c('bem','bodner')}. Every promise to yourself adds to one line or the other.</figcaption>
        </figure>"""

FIG_LALLY = f"""
        <figure>
            <svg viewBox="0 0 640 300" role="img" aria-labelledby="lc-t lc-d"><title id="lc-t">How long habits take to form</title><desc id="lc-d">Automaticity rises quickly at first then levels off. In Lally and colleagues' study the median time to reach the plateau was 66 days, with a range of 18 to 254 days.</desc>
                <g style="{FONT}">
                <line x1="60" y1="240" x2="610" y2="240" stroke="{INK}" stroke-width="2"/>
                <line x1="60" y1="240" x2="60" y2="30" stroke="{INK}" stroke-width="2"/>
                <text x="70" y="40" font-size="13" fill="{MUTED}">How automatic it feels</text>
                <text x="610" y="268" font-size="13" fill="{MUTED}" text-anchor="end">Days of repetition →</text>
                <path d="M60,240 C120,120 200,80 300,68 S520,58 610,56" fill="none" stroke="{BLUE}" stroke-width="5"/>
                <rect x="79" y="40" width="{(254-18)*2.0:.0f}" height="200" fill="{BLUE}" opacity="0.07"/>
                <line x1="79" y1="240" x2="79" y2="226" stroke="{INK}" stroke-width="2"/><text x="79" y="286" font-size="13" fill="{INK}" text-anchor="middle">18</text>
                <line x1="175" y1="240" x2="175" y2="70" stroke="{INK}" stroke-width="2" stroke-dasharray="4 5"/>
                <circle cx="175" cy="89" r="7" fill="{VOLT}" stroke="{INK}" stroke-width="2"/>
                <text x="185" y="120" font-size="15" font-weight="800" fill="{INK}">66 days</text><text x="185" y="138" font-size="13" fill="{MUTED}">median</text>
                <line x1="551" y1="240" x2="551" y2="226" stroke="{INK}" stroke-width="2"/><text x="551" y="286" font-size="13" fill="{INK}" text-anchor="middle">254</text>
                <text x="315" y="286" font-size="13" fill="{MUTED}" text-anchor="middle">range across participants</text>
                </g>
            </svg>
            <figcaption>Shape is illustrative. Figures from Lally et al. (2010): median 66 days to reach a habit plateau, ranging from 18 to 254 days. Missing one day did not materially affect the process{c('lally')}.</figcaption>
        </figure>"""

FIG_FINISH = f"""
        <figure>
            <svg viewBox="0 0 640 230" role="img" aria-labelledby="ff-t ff-d"><title id="ff-t">Forever vs a finish line</title><desc id="ff-d">A habit promise is an arrow with no end. A challenge has Day 1, a visible midpoint, and a finish line, and motivation tends to rise as the finish gets close.</desc>
                <g style="{FONT}">
                <text x="40" y="34" font-size="15" font-weight="800" fill="{INK}">"I'll do this forever"</text>
                <line x1="40" y1="62" x2="580" y2="62" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
                <polygon points="580,52 600,62 580,72" fill="{MUTED}"/>
                <text x="40" y="92" font-size="13" fill="{MUTED}">No end date. No midpoint. No day when you're done.</text>
                <text x="40" y="140" font-size="15" font-weight="800" fill="{INK}">"75 days, starting Monday"</text>
                <rect x="40" y="158" width="540" height="18" rx="9" fill="{RULE}" opacity=".5"/>
                <rect x="40" y="158" width="360" height="18" rx="9" fill="{BLUE}"/>
                <rect x="580" y="146" width="8" height="42" fill="{INK}"/>
                <text x="40" y="206" font-size="13" fill="{INK}">Day 1</text>
                <text x="400" y="206" font-size="13" fill="{INK}" text-anchor="middle">Day 50: "only 25 left"</text>
                <text x="600" y="206" font-size="13" font-weight="800" fill="{INK}" text-anchor="end">Finish</text>
                </g>
            </svg>
            <figcaption>A finish line gives you a goal gradient: people speed up as a goal gets closer{c('kivetz')}, and late in a goal, focusing on what's left keeps them going{c('koo')}. An open-ended habit has no "closer".</figcaption>
        </figure>"""

FIG_STACK = f"""
        <figure>
            <svg viewBox="0 0 640 350" role="img" aria-labelledby="fs-t fs-d"><title id="fs-t">Stacking challenges</title><desc id="fs-d">Four challenges climb like stairs, each in a different life area. Each leaves a few habits behind that carry forward into the next.</desc>
                <g style="{FONT}">
                {''.join(f'''<rect x="{40+i*140}" y="{256-i*60}" width="132" height="{90+i*60}" fill="{col}" stroke="{INK}" stroke-width="2"/>
                <text x="{48+i*140}" y="{278-i*60}" font-size="12" font-weight="800" fill="{tc}" letter-spacing="1">{area}</text>
                <text x="{48+i*140}" y="{298-i*60}" font-size="15" font-weight="800" fill="{tc}">{name}</text>
                <text x="{48+i*140}" y="{316-i*60}" font-size="12" fill="{tc}">{days}</text>''' for i, (area, name, days, col, tc) in enumerate([
                    ("BODY", "75 Soft", "75 days", PAPER, INK),
                    ("BUSINESS", "Revenue push", "90 days", PAPER, INK),
                    ("BEING", "Calm mornings", "30 days", PAPER, INK),
                    ("BALANCE", "Family dinners", "60 days", BLUE, "#fff")]))}
                <text x="40" y="34" font-size="13" fill="{MUTED}">Habits that stick carry forward:</text>
                <g font-size="12" fill="{INK}">
                <rect x="40" y="46" width="140" height="24" rx="12" fill="{VOLT}" stroke="{INK}"/><text x="110" y="62" text-anchor="middle">daily workout</text>
                <rect x="188" y="46" width="130" height="24" rx="12" fill="{VOLT}" stroke="{INK}"/><text x="253" y="62" text-anchor="middle">morning plan</text>
                <rect x="326" y="46" width="130" height="24" rx="12" fill="{VOLT}" stroke="{INK}"/><text x="391" y="62" text-anchor="middle">10 min quiet</text>
                </g>
                </g>
            </svg>
            <figcaption>An example of four challenges stacked over a year, each focused on a different area of life (the Body, Business, Being and Balance areas come from Garrett J White's Core 4 framework{c('core4')}). Some of each challenge sticks as habit; the rest is the starting point for a harder or different challenge.</figcaption>
        </figure>"""

BODY = f"""
        <p class="lede">You set the alarm for 5:30. You told yourself this is the week. The alarm goes off, you hit snooze, and nobody else ever knows. You know, though. This article is about that gap between what we tell ourselves we'll do and what we actually do, and why committing to finite, self-chosen challenges is one of the most practical ways to close it.</p>

        <div class="tldr">
            <p><strong>The short version</strong></p>
            <ul>
                <li>We judge ourselves by what we do, not what we intend{c('bem','bodner')}. Quietly broken promises to yourself add up.</li>
                <li>"Forever" is a vague goal. Specific, challenging goals with a deadline get more follow-through{c('locke','shu')}.</li>
                <li>A challenge has a finish line, a fresh start and a daily record, three things the research says help people persist{c('kivetz','dai','harkin')}.</li>
                <li>Finishing builds self-efficacy, the belief that you can do hard things{c('bandura')}.</li>
                <li>When one challenge ends, stack the next. Programs that just stop tend to fade{c('milkman')}.</li>
            </ul>
        </div>

        <h2>The promises nobody else hears</h2>
        <p>Think about a friend who cancels on you. Once is fine. By the fifth time, you've stopped expecting them to show up, and they haven't said a word about it. You just watched what they did.</p>
        <p>Psychologists think we treat ourselves much the same way. Daryl Bem's <em>self-perception theory</em> proposes that people partly work out their own attitudes and traits by observing their own behavior, much as an outsider would{c('bem')}. Economists have built on the same idea: Ronit Bodner and Drazen Prelec describe "self-signaling", choosing actions partly for what they tell us about ourselves{c('bodner')}, and Roland Bénabou and Jean Tirole model personal rules as a kind of reputation you hold with yourself, where each lapse or success is evidence about your own willpower{c('benabou')}.</p>
        <p>That gives a reasonable reading of something most of us have felt. A promise only you know about is easy to break: no one is disappointed, no one asks. But you notice. Do it often enough and you start to expect it of yourself, which makes the next one easier to break. Over time it costs you something hard to name: confidence that when you decide to do something, it will happen.</p>
{FIG_LEDGER}

        <blockquote><p>"Every action you take is a vote for the type of person you wish to become. No single instance will transform your beliefs, but as the votes build up, so does the evidence of your new identity."</p><cite>James Clear, <em>Atomic Habits</em> (2018){c('clear')}</cite></blockquote>

        <h2>Why "forever" is a hard promise to keep</h2>
        <p>The usual advice is to build a habit: do the thing every day until it's automatic. It's good advice with a hidden problem. Nobody knows how long that will take, and the commitment has no end.</p>
        <p>In the best-known study of habit formation, Phillippa Lally and colleagues followed 96 volunteers who each picked a daily behavior, such as eating fruit at lunch or running before dinner. The median time to reach a plateau of automaticity was 66 days, but the range ran from 18 to 254 days{c('lally')}. "Until it's a habit" might be three weeks or eight months.</p>
{FIG_LALLY}
        <p>Open-ended commitments are also vague by nature, and vague goals underperform. Edwin Locke and Gary Latham's review of 35 years of goal-setting research found that specific, difficult goals consistently led to higher performance than urging people to "do your best"{c('locke')}. "Work out more" is a do-your-best goal. "Train 45 minutes a day for 75 days" is a specific one.</p>
        <p>Deadlines matter too, sometimes in counter-intuitive ways. When Suzanne Shu and Ayelet Gneezy gave people a voucher for a free pastry and coffee, 31% redeemed it when it expired in three weeks, but only 6% did when they had two months, even though people expected the longer window to make redeeming more likely{c('shu')}. Without a deadline, "later" has a way of never arriving.</p>

        <div class="stat">
            <div><b>66 days</b><span>median time to form a habit; the range was 18–254 days{c('lally')}</span></div>
            <div><b>31% vs 6%</b><span>follow-through with a 3-week deadline vs a 2-month one{c('shu')}</span></div>
            <div><b>58.9% vs 47.1%</b><span>success for "start doing" vs "stop doing" resolutions after a year{c('oscarsson')}</span></div>
        </div>

        <h2>What a challenge gives you that a habit doesn't</h2>
        <p>A personal challenge is a promise with edges: a start date, an end date and a short list of things you'll do every day. Those edges line up with several well-studied drivers of follow-through.</p>

        <h3>1. A finish line pulls you forward</h3>
        <p>In a study of a real café loyalty program, Ran Kivetz, Oleg Urminsky and Yuhuang Zheng found that customers bought coffee more often as they got closer to a free one. Customers whose 12-stamp card came with two stamps already filled in finished the ten required purchases faster than customers with a plain 10-stamp card. Feeling closer to the goal was enough to speed them up{c('kivetz')}. Later research found that early in a goal, focusing on progress made motivates people, while near the end, focusing on what's left keeps them going{c('koo')}. Both effects need an end point, and "forever" doesn't have one.</p>
{FIG_FINISH}

        <h3>2. Day 1 is a fresh start</h3>
        <p>Hengchen Dai, Katherine Milkman and Jason Riis found that people are more likely to pursue goals right after "temporal landmarks", such as a new week, month, year or birthday. Google searches for "diet", gym visits and goal commitments all rose after those dates{c('dai')}. A challenge creates landmarks on purpose: every new challenge gives you a new Day 1.</p>

        <h3>3. You chose it</h3>
        <p>Goals that come from your own interests and values get more sustained effort. Kennon Sheldon and Andrew Elliot found that these "self-concordant" goals were more likely to be reached, and reaching them did more for well-being{c('sheldon')}. A challenge you design yourself, around what you want to change right now, is self-concordant by default.</p>

        <h3>4. Every day is recorded</h3>
        <p>A meta-analysis by Benjamin Harkin and colleagues covering 138 studies and nearly 20,000 people found that interventions that increased progress monitoring improved goal attainment (d = 0.40). The effect was larger when progress was physically recorded or reported to someone{c('harkin')}. A daily checklist with a calendar of finished days is exactly that kind of record.</p>

        <h3>5. Small wins add up</h3>
        <p>Teresa Amabile and Steven Kramer analyzed nearly 12,000 daily diary entries from 238 people and found that making progress in meaningful work, even small progress, was associated with people's best days for emotion and motivation{c('amabile')}. Karl Weick argued decades earlier that a series of small, concrete wins builds momentum that big abstract goals don't{c('weick')}. A checked-off day is a small win you can see.</p>

        <blockquote><p>"You do not rise to the level of your goals. You fall to the level of your systems."</p><cite>James Clear, <em>Atomic Habits</em> (2018){c('clear')}</cite></blockquote>

        <h2>Finishing is how confidence is built</h2>
        <p>Albert Bandura's work on self-efficacy, the belief that you can carry out what you set out to do, identified four sources of it: performance accomplishments, watching others succeed, encouragement, and your physical and emotional state. The more dependable the source, the bigger the change in belief, and personal accomplishments are the most dependable of the four{c('bandura')}. Self-efficacy in turn predicts whether people start, how hard they try and how long they persist when it gets difficult.</p>
        <p>This is where the self-trust ledger turns around. Finishing a 30-day challenge is direct evidence that you keep your word to yourself. The next challenge can be a little harder because you have proof. People who believed in their ability to change before New Year were among the most likely to keep their resolutions six months later{c('norcross')}.</p>

        <div class="story">
            <p><strong>An analogy: the rope bridge.</strong> Picture crossing a canyon on a rope bridge you built yourself. The first crossing is terrifying because you've never tested your own knots. Every crossing after that is a little easier. Not because the canyon got smaller, but because you have evidence the knots hold. A finished challenge is a tested knot.</p>
        </div>

        <h2>When you slip (because you will)</h2>
        <p>All-or-nothing rules have a known failure mode. In a classic study, dieters who had been given a milkshake went on to eat <em>more</em> ice cream afterwards, while non-dieters ate less{c('herman')}: once the diet felt broken, there seemed no point holding back. Janet Polivy and Peter Herman linked this pattern of rigid restraint to binge eating{c('polivy')}, and in addiction research Alan Marlatt described a similar "abstinence violation effect", where a single slip turns into a full relapse when people blame themselves globally and lose confidence they can recover{c('marlatt')}.</p>
        <p>The fix isn't to abandon structure. It's to decide up front what a miss means:</p>
        <ul>
            <li><strong>One missed day isn't fatal.</strong> In Lally's study, missing a single opportunity didn't materially affect habit formation{c('lally')}.</li>
            <li><strong>Planned slack helps.</strong> Goals framed with a few "emergency reserve" skips led people to persist more after a miss{c('sharif')}.</li>
            <li><strong>Strict can still be right</strong>, if the restart rule is the point of the challenge and you've chosen it on purpose. What hurts is a rule you never really agreed to, broken quietly.</li>
        </ul>
        <p>Either way, you set the rule before Day 1, so a miss is handled by a decision you already made, not by a 10 p.m. negotiation with yourself.</p>

        <h2>Finish, then stack the next one</h2>
        <p>Finite programs have a weakness, and the research is honest about it. In a megastudy of 61,293 gym members testing 54 different four-week programs, 45% of programs significantly increased gym visits while they ran, by 9% to 27%. But only 8% had a significant effect after the four weeks were over{c('milkman')}. When the program ends and nothing replaces it, behavior tends to slide back.</p>
        <p>That's the case for a challenge-based <em>lifestyle</em> rather than a single challenge. When one challenge ends, you choose the next, using the fresh start of a new Day 1{c('dai')}. Some of what you practiced sticks as a habit; the rest becomes the base for a harder or different challenge.</p>
        <p>Over time, the challenges change because you do. A useful lens is Garrett J White's Core 4, from his Wake Up Warrior program, which splits life into four areas: Body, Being, Balance and Business{c('core4')}. A year of challenges might move from your body to your business, then to your relationships, as different parts of your life need attention and different habits.</p>
{FIG_STACK}

        <blockquote><p>"We are what we repeatedly do. Excellence, then, is not an act, but a habit."</p><cite>Will Durant, <em>The Story of Philosophy</em> (1926), summarizing Aristotle. Often misattributed to Aristotle himself{c('durant')}.</cite></blockquote>

        <h2>How to design your next challenge</h2>
        <ol>
            <li><strong>Pick one area of life.</strong> Body, mind, relationships or work. One area keeps the challenge focused.</li>
            <li><strong>Choose a length you can see the end of.</strong> 30 days for a first challenge, 75 or 90 when you've built some proof.</li>
            <li><strong>Write 3–7 specific daily tasks.</strong> "45-minute workout", not "exercise more"{c('locke')}. Phrase them as things to do rather than things to avoid{c('oscarsson')}.</li>
            <li><strong>Attach each task to a when and where.</strong> "After I make coffee, I read 10 pages." If-then plans like this had a medium-to-large effect on goal attainment across 94 tests (d = 0.65){c('gollwitzer')}.</li>
            <li><strong>Decide what a miss means</strong> before you start: restart, or log it and keep going{c('sharif')}.</li>
            <li><strong>Record every day</strong> where you'll see it{c('harkin')}.</li>
            <li><strong>Before the last day, pick the next challenge.</strong> Don't let the finish line become a cliff{c('milkman')}.</li>
        </ol>

        <h2>Is this approach for everyone?</h2>
        <p>No. Some people do well with quiet, open-ended routines, and the studies above describe averages, not guarantees. No study we know of directly compares a fixed-term challenge with an open-ended habit commitment. The case here is built from related findings on deadlines, goal gradients, fresh starts, self-chosen goals, monitoring and self-efficacy. But if you've started the same habit five Mondays in a row, or you've stopped believing yourself when you say "this time", a challenge with a finish line is worth a try. Keep one promise to yourself, then the next, until keeping them is normal for you.</p>

        <h2>How FlexChallenge fits in</h2>
        <p><a href="/">FlexChallenge</a> is built around this loop. Pick a template or build your own challenge from 1 to 365 days. Check off each day's tasks, with progress photos and voice notes as proof. Choose strict or flexible mode before you start. When you finish, start the next one. The calendar fills in one finished day at a time.</p>

        <h2 id="sources">Sources</h2>
        <ol class="sources">
{chr(10).join(f'            <li id="src-{i+1}">{t}' + (f' <a href="{u}">{u}</a>' if u else '') + '</li>' for i, (_, t, u) in enumerate(SOURCES))}
        </ol>
        <p class="note">FlexChallenge is not affiliated with Wake Up Warrior, Garrett J White, James Clear, or any researcher cited here.</p>"""

PAGE = dict(
    slug="challenge-based-lifestyle",
    title="The Challenge-Based Lifestyle: Why Finite Challenges Beat \"Forever\" Habits",
    desc="Why self-set, time-bound challenges help people follow through: the research on self-trust, deadlines, goal gradients, fresh starts, progress tracking and self-efficacy, and how to stack challenges over time.",
    eyebrow="Essay",
    h1="The Challenge-Based Lifestyle: Keep Promises to Yourself, One Challenge at a Time",
    updated="2026-10-04",
    ld_extra={"@type": "Thing", "name": "Personal challenges and habit formation"},
    body=BODY,
    faqs=[
        ("What is a challenge-based lifestyle?", "Living in a series of self-chosen, time-bound challenges, such as 30, 75 or 90 days with a few specific daily tasks, finishing each one and then starting the next, often focused on a different area of life."),
        ("How long does it take to form a habit?", "In Lally et al. (2010), the median time to reach a habit plateau was 66 days, but it ranged from 18 to 254 days depending on the person and behavior."),
        ("Why are challenges easier to stick to than habits?", "A challenge has a specific goal, a deadline, a fresh start and a finish line. Research links each of these to better follow-through: specific goals, shorter deadlines, temporal landmarks, and the goal-gradient effect, where people speed up as a goal gets closer."),
        ("What happens if I miss a day?", "In Lally et al. (2010), missing a single day didn't materially affect habit formation. Decide before you start whether a miss means restarting or logging it and continuing, so you're not negotiating with yourself in the moment."),
    ],
)
