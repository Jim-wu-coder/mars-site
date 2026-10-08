"""Build the four static pages of the MARS site into the repository root.

    python3 tools/build.py

Copy lives in tools/content.py and tools/content_more.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import EN  # noqa: E402
from content_more import COMPARE, FAQ, SECURITY  # noqa: E402

EXTRA = {
    "en": dict(
        nav=[("how", "How it works"), ("why", "Why MARS"), ("product", "Product"), ("security", "Security"), ("faq", "FAQ")],
        home="Home",
        h1=("AI triage", "your SOC", "can check."),
        shot_hero=("A real MARS screen. The email is a synthetic example.", "MARS AI verdict card for a phishing email"),
        shots_h="The console, on real output",
        shots_p="Captured from a local MARS instance analysing synthetic emails and synthetic XDR incidents with a Claude model. No real mail, devices or accounts appear.",
        shots=[
            ("ledger", "", "Analysis history: three synthetic emails and the verdict MARS published for each."),
            ("verdict-full", "crop", "One analysis in full: who sent it, the AI's verdict and reasoning, recommended steps, cautions, and questions for the reporter."),
            ("ioc", "", "Indicators extracted from the email, ready to copy or export."),
            ("xdr-queue", "", "The XDR incident queue: three synthetic incidents, each with the evidence for and against, the data gaps and the next step. In all three the AI's confidence was under the threshold, so MARS left the final decision to an analyst. This instance had no connection to Defender for Endpoint, so hunting queries could not run; the data gaps shown include everything those queries would have answered."),
            ("xdr-summary", "", "One incident in detail: what happened, why it matters, the next steps and the key evidence, with every gap stated."),
        ],
        problem_e="The problem",
        more_h="Keep exploring",
        more=[
            ("how", "How it works", "The four steps from a new case to a published answer, and what MARS checks in mail and in XDR incidents."),
            ("why", "Why MARS", "How MARS keeps the model inside a pipeline it controls, so the AI's answers can be checked."),
            ("product", "Product", "The console pages, the services MARS connects to, and how it runs on your own host."),
            ("security", "Security", "The controls at each boundary hostile input crosses, and the limits MARS states openly."),
            ("faq", "FAQ", "Short answers on setup, models, what is sent to the AI and what MARS will not do alone."),
        ],
        go="Open",
        next="Next",
        how_e="How it works",
        arch_h="Where the data goes",
        arch_p="Everything MARS keeps stays on your host. Two kinds of traffic leave it, and you decide whether either does.",
        arch_note='The controls on each of these paths are on the <a href="security.html">Security</a> page.',
        ai_e="AI",
        product_e="Product",
        pages_h="Console pages",
        integ_h="Connected services",
        cli=("Command line", "The same analyses run from a terminal."),
        deploy_e="Deployment and data",
        titles=dict(
            index="MARS · AI phishing analysis and incident response",
            how="How it works · MARS",
            why="Why MARS · MARS",
            product="Product · MARS",
            security="Security · MARS",
            faq="FAQ · MARS",
        ),
    ),
}

HREF = {"index": "./", "how": "how.html", "why": "why.html", "product": "product.html", "security": "security.html", "faq": "faq.html"}
NEXT = {"how": "why", "why": "product", "product": "security", "security": "faq"}

ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
TICK = '<svg class="tick" width="22" height="22" viewBox="0 0 22 22" fill="none" aria-hidden="true"><circle cx="11" cy="11" r="10" fill="var(--ok-soft)"/><path d="M6.5 11.5l3 3 6-6.5" stroke="var(--ok)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PROBLEM_ICONS = [
    '<path d="M3 7l9 6 9-6M4 5h16a1 1 0 011 1v12a1 1 0 01-1 1H4a1 1 0 01-1-1V6a1 1 0 011-1z"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 114 2c-.9.6-1.5 1.1-1.5 2.2M12 17h.01"/>',
    '<path d="M12 3l9 16H3L12 3zM12 10v4M12 17h.01"/>',
    '<rect x="5" y="11" width="14" height="9" rx="1.5"/><path d="M8 11V8a4 4 0 018 0v3"/>',
]

CSS = """
:root{--bg:#F4F7F6;--surface:#FFFFFF;--line:#D5DEDD;--line-2:#E6ECEB;--ink:#0E1D23;--ink-2:#46575F;--ink-3:#24353D;--accent:#0A6B7C;--accent-soft:#DBEEF1;
--band:#0B1F26;--band-2:#12303A;--band-line:#24444F;--band-ink:#EAF2F3;--band-ink-2:#A9C0C6;--band-ink-3:#8FA9B0;--cyan:#5FD0E0;--on-cyan:#06181D;
--ok:#1C7748;--ok-ink:#14592F;--ok-soft:#DFF1E6;--warn:#7A4F00;--warn-ink:#6A4400;--warn-soft:#F8EBCF;--bad:#B02F29;--bad-soft:#F8E1DF;--mute-soft:#E6ECEB;
--display:'Bricolage Grotesque','PingFang TC','Microsoft JhengHei',sans-serif;--ui:'IBM Plex Sans','PingFang TC','Microsoft JhengHei',system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#0F1A1F;--surface:#15242B;--line:#28393F;--line-2:#22323A;--ink:#E5EDEF;--ink-2:#A9B8BF;--ink-3:#C9D5D9;--accent:#5FD0E0;--accent-soft:#12333C;
--ok:#62D097;--ok-ink:#8BE0B2;--ok-soft:#12301F;--warn:#E9B85A;--warn-ink:#F2C56B;--warn-soft:#33270C;--bad:#F1887F;--bad-soft:#3A1A18;--mute-soft:#22323A;color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased}
[hidden]{display:none!important}h1,h2,h3,p,ol,ul{margin:0}h1,h2,h3{text-wrap:balance}ol,ul{list-style:none;padding:0}a{color:var(--accent)}
:focus-visible{outline:2px solid var(--cyan);outline-offset:3px;border-radius:4px}
.wrap{max-width:1200px;margin-inline:auto;padding-inline:32px}
.band{background:var(--band);color:var(--band-ink)}
.bar{display:flex;flex-wrap:wrap;align-items:center;gap:16px 36px;padding-block:22px}
.mark{font-family:var(--mono);font-weight:600;font-size:20px;letter-spacing:.26em;color:var(--band-ink);text-decoration:none}
.bar nav{display:flex;flex-wrap:wrap;gap:8px 32px;margin-left:auto;font-size:15px}
.bar nav a{color:var(--band-ink-2);text-decoration:none;padding:10px 0;border-bottom:2px solid transparent}
.bar nav a:hover{color:var(--band-ink)}.bar nav a[aria-current]{color:var(--band-ink);font-weight:600;border-bottom-color:var(--cyan)}
.eyebrow{font-size:14px;font-weight:600;letter-spacing:.08em;color:var(--accent)}.band .eyebrow{color:var(--cyan)}
.display{font-family:var(--display);font-weight:800}
.hero{display:flex;flex-direction:column;gap:56px;padding-block:64px 88px}
.hero-copy{min-width:0;display:flex;flex-direction:column;gap:26px;max-width:820px}
.hero .eyebrow{display:flex;align-items:center;gap:10px}.hero .eyebrow::before{content:"";width:28px;height:2px;background:var(--cyan)}
.hero h1{font-size:clamp(38px,5.4vw,72px);line-height:1.08;letter-spacing:-.02em}
.hero h1 em{font-style:normal;color:var(--cyan)}
.lead{font-size:19px;line-height:1.6;color:var(--band-ink-2);max-width:34em}
.cta{display:flex;flex-wrap:wrap;gap:14px}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:0 26px;border-radius:999px;background:var(--cyan);color:var(--on-cyan);font-weight:600;text-decoration:none}
.btn.ghost{background:transparent;color:var(--band-ink);border:1px solid #3A5B66}
.facts{display:flex;flex-wrap:wrap;gap:8px 10px;font-family:var(--mono);font-size:13px;color:var(--band-ink-2)}
.facts span{border:1px solid var(--band-line);border-radius:6px;padding:2px 10px}
.mock{flex:1 1 420px;min-width:0;display:flex;flex-direction:column;gap:14px}
.card{background:#FFFFFF;color:#0E1D23;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px -24px rgba(0,0,0,.6);--ok:#1C7748;--ok-soft:#DFF1E6}
.card-head{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;padding:18px 22px;border-bottom:1px solid #D5DEDD}
.card-head b{font-size:15px}.card-head .count{margin-left:auto;font-family:var(--mono);font-size:12px;color:#46575F}.card-head .subj{flex-basis:100%;font-size:14px;color:#46575F;overflow-wrap:anywhere}
.claim{display:flex;align-items:flex-start;gap:14px;padding:16px 22px;border-bottom:1px solid #E6ECEB}.claim:last-child{border-bottom:0}
.claim .tick{flex:none;margin-top:2px}.claim div{min-width:0;display:flex;flex-direction:column;gap:4px;font-size:15.5px;line-height:1.5}
.claim small{align-self:flex-start;font-family:var(--mono);font-size:12px;color:#0A6B7C;background:#DBEEF1;border-radius:4px;padding:1px 8px}
.card-foot{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;padding:14px 22px;background:#EEF3F2;font-size:14px;color:#46575F}
.card-foot span:last-child{margin-left:auto;font-size:12.5px;font-weight:600;border:1px solid #B9C6C5;border-radius:999px;padding:1px 10px}
.held{display:flex;align-items:center;gap:14px;background:var(--band-2);border:1px solid var(--band-line);border-radius:12px;padding:14px 20px;font-size:14.5px;color:var(--band-ink-2)}
.held b{flex:none;font-size:13px;color:#F2C56B;border:1px solid #F2C56B;border-radius:999px;padding:1px 12px}
.mock .note{font-size:12px;color:var(--band-ink-3);text-align:right}
.shot{margin:0;display:flex;flex-direction:column;gap:10px;min-width:0}
.shot a{display:block;border:1px solid var(--band-line);border-radius:14px;overflow:hidden;background:#0B161C;box-shadow:0 30px 60px -28px rgba(0,0,0,.55)}
.shot img{display:block;width:100%;height:auto}.shot.crop img{aspect-ratio:16/10;object-fit:cover;object-position:top}
.shot figcaption{font-size:14px;color:var(--ink-2);line-height:1.6}.band .shot figcaption{color:var(--band-ink-3);font-size:12.5px;text-align:right}
.hero .shot a{border-radius:16px}
.shots{display:flex;flex-direction:column;gap:40px}
.pagehead{display:flex;flex-direction:column;gap:20px;padding-block:64px 88px}
.pagehead h1{font-size:clamp(34px,4.6vw,62px);line-height:1.12;max-width:16em}
.sec{padding-block:104px}.sec.tight{padding-block:88px}.alt{background:var(--surface);border-block:1px solid var(--line)}
.stack{display:flex;flex-direction:column;gap:48px}
.split{display:flex;flex-wrap:wrap;gap:48px 72px}.split>.head{flex:1 1 340px;min-width:0}.split>.body{flex:1.4 1 520px;min-width:0}
.head{display:flex;flex-direction:column;gap:16px;max-width:760px}
h2.display{font-size:clamp(28px,3.4vw,44px);line-height:1.18}
.head p{font-size:17px;color:var(--ink-2)}.band .head p{color:var(--band-ink-2)}
h2.plain{font-size:22px;font-weight:700}
.cells{display:flex;flex-wrap:wrap;gap:0 40px}
.cell{flex:1 1 220px;min-width:0;display:flex;flex-direction:column;gap:6px;padding:22px 0;border-top:1px solid var(--line)}
.cell h3{font-size:18.5px;font-weight:700;line-height:1.4}.cell span{font-size:15.5px;color:var(--ink-2);line-height:1.65}
.cell svg{color:var(--accent);margin-bottom:2px}
.band .cell{border-top-color:var(--band-line);flex-basis:300px}.band .cell span{color:var(--band-ink-2)}
.tiles{display:flex;flex-wrap:wrap;gap:16px}
.tile{flex:1 1 320px;min-width:0;background:var(--band-2);border:1px solid var(--band-line);border-radius:14px;padding:28px;display:flex;flex-direction:column;gap:10px}
.tile h2{font-size:20px;font-weight:700;line-height:1.4}.tile span{font-size:15.5px;color:var(--band-ink-2);line-height:1.65}
.steps{display:flex;flex-wrap:wrap;gap:16px}
.step{flex:1 1 230px;min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:26px;display:flex;flex-direction:column;gap:10px}
.step .n{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}.step h2{font-size:21px;font-weight:700;line-height:1.35}.step span:last-child{font-size:15.5px;color:var(--ink-2);line-height:1.6}
.step.gate{background:var(--band);border-color:var(--band-line);color:var(--band-ink)}.step.gate .n{color:var(--cyan)}.step.gate span:last-child{color:var(--band-ink-2)}
.outcomes{display:flex;flex-wrap:wrap;gap:16px;margin-top:-28px}
.outcome{flex:1 1 320px;min-width:0;border-radius:14px;padding:24px 26px;display:flex;align-items:flex-start;gap:16px}
.outcome svg{flex:none}.outcome div{display:flex;flex-direction:column;gap:2px}.outcome b{font-size:19px}.outcome span{font-size:15.5px;color:var(--ink)}
.outcome.pass{background:var(--ok-soft)}.outcome.pass b{color:var(--ok-ink)}.outcome.hold{background:var(--warn-soft)}.outcome.hold b{color:var(--warn-ink)}
.pipes{display:flex;flex-wrap:wrap;gap:20px}
.pipe{flex:1 1 420px;min-width:0;background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:32px;display:flex;flex-direction:column;gap:18px}
.pipe h3{font-size:24px;font-weight:700}.pipe>p{font-size:15.5px;color:var(--ink-2)}
.pipe li{padding:13px 0;border-top:1px solid var(--line);font-size:14.5px;color:var(--ink-2)}.pipe li b{display:block;font-size:16px;font-weight:600;color:var(--ink)}.pipe li:last-child b{color:var(--accent)}
.pills{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:13.5px;color:var(--ink-2);margin-top:auto}
.pill{font-weight:700;border-radius:999px;padding:2px 12px}.pill.bad{color:var(--bad);background:var(--bad-soft)}.pill.warn{color:var(--warn);background:var(--warn-soft)}.pill.ok{color:var(--ok);background:var(--ok-soft)}.pill.neutral{color:var(--ink-2);background:var(--mute-soft)}
.gets{display:flex;flex-wrap:wrap;gap:24px 56px;align-items:flex-start}.gets h3{flex:0 1 240px;font-size:22px;font-weight:700;line-height:1.4}
.gets ul{flex:1 1 520px;min-width:0;display:flex;flex-wrap:wrap;gap:0 40px}.gets li{flex:1 1 260px;padding:12px 0;border-top:1px solid var(--line);font-size:15.5px;color:var(--ink-3)}
.more{display:flex;flex-wrap:wrap;gap:16px}
.more a{flex:1 1 300px;min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:30px;display:flex;flex-direction:column;gap:10px;color:var(--ink);text-decoration:none}
.more a:hover{border-color:var(--accent)}.more b{font-size:23px}.more span{font-size:15.5px;color:var(--ink-2);line-height:1.65}
.more .go{margin-top:14px;display:inline-flex;align-items:center;gap:8px;font-weight:600;color:var(--accent)}
.grid{display:flex;flex-wrap:wrap;gap:12px}
.grid div{flex:1 1 260px;min-width:0;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 20px;font-size:14.5px;color:var(--ink-2)}
.grid b{display:block;font-size:16px;color:var(--ink)}.grid .dashed{background:transparent;border-style:dashed}
.integ{display:flex;flex-wrap:wrap;gap:28px 48px}.integ>div{flex:1 1 220px;min-width:0;display:flex;flex-direction:column;gap:12px}
.integ h3{font-size:13px;font-weight:600;letter-spacing:.08em;color:var(--ink-2)}
.chips{display:flex;flex-wrap:wrap;gap:6px;font-size:13.5px;color:var(--ink-3)}.chips span{background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:3px 10px}
.bounds{display:flex;flex-direction:column}
.bound{display:flex;flex-wrap:wrap;gap:16px 56px;padding:36px 0;border-top:1px solid var(--line)}
.bound .n{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}
.bound>div{flex:1 1 300px;min-width:0;display:flex;flex-direction:column;gap:8px}.bound h3{font-size:23px;font-weight:700;line-height:1.35}.bound>div>p{font-size:16px;color:var(--ink-2)}
.bound ul{flex:1.5 1 460px;min-width:0;display:flex;flex-direction:column;gap:12px}
.bound li{position:relative;padding-left:22px;font-size:15.5px;line-height:1.65;color:var(--ink-3)}.bound li::before{content:"";position:absolute;left:0;top:.72em;width:10px;height:2px;background:var(--accent)}
.report{display:flex;flex-wrap:wrap;gap:12px 56px;align-items:baseline}.report h2{flex:0 1 300px}.report p{flex:1.5 1 460px;min-width:0;font-size:16px;color:var(--ink-2)}
.qgroup{display:flex;flex-wrap:wrap;gap:20px 56px;padding:44px 0;border-top:1px solid var(--line)}.qgroup:first-child{border-top:0;padding-top:0}
.qgroup>h2{flex:0 1 220px;font-size:22px;font-weight:700}
.qa{flex:1.8 1 520px;min-width:0;display:flex;flex-direction:column;gap:30px}.qa h3{font-size:18.5px;font-weight:700;line-height:1.45;margin-bottom:6px}.qa p{font-size:16px;color:var(--ink-2);max-width:44em}
.arch{display:grid;grid-template-columns:minmax(0,1fr) 28px minmax(0,1.9fr) 28px minmax(0,1fr);gap:20px 0;align-items:start}
.arch h3{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);margin-bottom:2px}
.arch-col{display:flex;flex-direction:column;gap:10px;min-width:0}
.node{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:14.5px;line-height:1.5;color:var(--ink-2);min-width:0}
.alt .node{background:var(--bg)}.node b{display:block;font-size:15.5px;color:var(--ink)}
.arch-arrow{align-self:center;justify-self:center;width:14px;height:14px;border-top:2px solid var(--accent);border-right:2px solid var(--accent);transform:rotate(45deg)}
.arch-host{position:relative;border:2px dashed var(--accent);border-radius:16px;padding:30px 18px 18px;display:flex;flex-direction:column;gap:12px;min-width:0}
.arch-tag{position:absolute;top:-13px;left:18px;background:var(--accent);color:var(--surface);font-size:12.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:2px 12px}
.arch-core{background:var(--band);color:var(--band-ink);border:1px solid var(--band-line);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:12px}
.arch-core>b{font-family:var(--mono);letter-spacing:.24em;font-size:15px}
.arch-stages{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;counter-reset:st}
.arch-stages span{counter-increment:st;background:var(--band-2);border:1px solid var(--band-line);border-radius:8px;padding:10px;font-size:13.5px;line-height:1.4;color:var(--band-ink)}
.arch-stages span::before{content:counter(st,decimal-leading-zero);display:block;font-family:var(--mono);font-size:11.5px;color:var(--cyan);margin-bottom:2px}
.arch-mid{display:flex;flex-direction:column;gap:6px;min-width:0}
.arch-ext{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.arch-ext .node{position:relative;margin-top:30px}
.arch-ext .node::before{content:"\\2195";position:absolute;left:50%;top:-31px;transform:translateX(-50%);font-size:26px;line-height:1;color:var(--accent)}
.node small{display:block;margin-top:6px;font-size:13px;color:var(--ink-2)}.node small i{font-style:normal;font-weight:600;color:var(--accent)}
@media (max-width:900px){.arch{grid-template-columns:minmax(0,1fr)}.arch-arrow{transform:rotate(135deg);margin:2px 0}.arch-ext{grid-template-columns:minmax(0,1fr)}.arch-stages{grid-template-columns:repeat(2,minmax(0,1fr))}}
.cmp-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.cmp{border-collapse:collapse;width:100%;min-width:760px;font-size:15px;line-height:1.55}
.cmp th,.cmp td{text-align:left;vertical-align:top;padding:14px 18px;border-bottom:1px solid var(--line)}
.cmp tr:last-child th,.cmp tr:last-child td{border-bottom:0}
.cmp thead th{font-size:14px;font-weight:700;color:var(--ink);border-bottom:2px solid var(--line)}
.cmp tbody th{font-weight:600;color:var(--ink);width:22%}.cmp td{color:var(--ink-2);width:24%}
.cmp .us{background:var(--accent-soft);color:var(--ink);width:30%}.cmp thead .us{color:var(--accent)}
.cmp-note{font-size:14px;color:var(--ink-2);max-width:60em}
.closing{padding-block:104px 0}.closing h2.display{font-size:clamp(32px,4.4vw,60px)}
footer.band{color:var(--band-ink-3)}
.next{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;padding-block:64px 44px;color:var(--band-ink);text-decoration:none}
.next span{display:flex;flex-direction:column;gap:4px}.next small{font-size:14px;font-weight:600;letter-spacing:.08em;color:var(--cyan)}.next b{font-size:clamp(26px,3vw,40px);line-height:1.3}
.foot{display:flex;flex-wrap:wrap;align-items:center;gap:12px 32px;font-size:14px;padding-block:28px 48px;border-top:1px solid var(--band-line)}
.foot.first{border-top:0;padding-top:40px}.foot .mark{font-size:14px;letter-spacing:.2em}.foot a{color:var(--band-ink-2);text-decoration:none}.foot a:hover{color:var(--band-ink)}.foot span:last-child{margin-left:auto}
@media (max-width:640px){.wrap{padding-inline:18px}.bar nav{order:3;flex-basis:100%;margin-left:0;gap:4px 22px}.hero{padding-block:44px 64px}.pagehead{padding-block:40px 56px}.sec,.sec.tight{padding-block:60px}.closing{padding-block:60px 0}.stack{gap:32px}.outcomes{margin-top:-12px}.pipe{padding:22px}.foot span:last-child{margin-left:0}}
"""

def bar(X, lang, page):
    links = "".join(
        f'<a href="{HREF[k]}"{" aria-current=page" if k == page else ""}>{t}</a>' for k, t in X["nav"]
    )
    return (
        f'<header class="wrap bar"><a class="mark" href="./">MARS</a><nav aria-label="{X["home"]}">{links}</nav>'
        '</header>'
    )


def footer(L, X, page):
    nxt = ""
    if page in NEXT:
        k = NEXT[page]
        label = dict(X["nav"])[k]
        nxt = (
            f'<a class="next" href="{HREF[k]}"><span><small>{X["next"]}</small><b class="display">{label}</b></span>'
            '<svg width="44" height="44" viewBox="0 0 44 44" fill="none" stroke="var(--cyan)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="22" cy="22" r="21"/><path d="M14 22h16M24 16l6 6-6 6"/></svg></a>'
        )
    links = "".join(
        f'<a href="{HREF[k]}">{t}</a>' for k, t in [("index", X["home"]), *X["nav"]] if k != page
    )
    return (
        f'<div class="wrap">{nxt}<div class="foot{"" if nxt else " first"}"><span class="mark">MARS</span>{links}'
        f'<span>Mail Analysis &amp; Response System · {L["footer"]}</span></div></div>'
    )


def cells(items, tag="h3", icons=None):
    out = ""
    for i, (k, v) in enumerate(items):
        icon = (
            f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icons[i]}</svg>'
            if icons
            else ""
        )
        out += f'<div class="cell">{icon}<{tag}>{k}</{tag}><span>{v}</span></div>'
    return out


def pagehead(L, X, lang, page, eyebrow, h1, lead):
    return (
        f'<div class="band">{bar(X, lang, page)}<div class="wrap pagehead"><span class="eyebrow">{eyebrow}</span>'
        f'<h1 class="display">{h1}</h1><p class="lead">{lead}</p></div>'
    )


def shot(name, lang, alt, caption, cls=""):
    src = f"img/{name}-{lang}.webp"
    return (
        f'<figure class="shot {cls}"><a href="{src}"><img src="{src}" alt="{alt}" loading="lazy" decoding="async"></a>'
        f"<figcaption>{caption}</figcaption></figure>"
    )


def home(L, X, lang):
    more = "".join(
        f'<a href="{HREF[k]}"><b>{t}</b><span>{d}</span><span class="go">{X["go"]} {ARROW}</span></a>'
        for k, t, d in X["more"]
    )
    a, b, c = X["h1"]
    return f"""<div class="band">{bar(X, lang, "index")}
<div class="wrap hero"><div class="hero-copy"><span class="eyebrow">{L["eyebrow"]}</span>
<h1 class="display">{a}<br>{b}<br><em>{c}</em></h1><p class="lead">{L["lead"]}</p>
<div class="cta"><a class="btn" href="how.html">{L["cta"][0]} {ARROW}</a><a class="btn ghost" href="why.html">{L["cta"][1]}</a></div>
<div class="facts">{"".join(f"<span>{x}</span>" for x in L["facts"])}</div></div>
{shot("verdict", lang, X["shot_hero"][1], X["shot_hero"][0])}</div></div>
<section class="alt"><div class="wrap sec split"><div class="head"><span class="eyebrow">{X["problem_e"]}</span><h2 class="display">{L["problem_h"]}</h2><p>{L["problem_p"]}</p></div>
<div class="body cells">{cells(L["problem"], icons=PROBLEM_ICONS)}</div></div></section>
<section><div class="wrap sec stack" style="gap:36px"><h2 class="display">{X["more_h"]}</h2><div class="more">{more}</div></div></section>
<footer class="band">{footer(L, X, "index")}</footer>"""


def how(L, X, lang):
    steps = "".join(
        f'<li class="step{" gate" if i == 3 else ""}"><span class="n">{i + 1:02d}</span><h2>{k}</h2><span>{v}</span></li>'
        for i, (k, v) in enumerate(L["rail"])
    )

    def pipe(h, p, items, label, pills):
        li = "".join(f"<li><b>{k}</b>{v}</li>" for k, v in items)
        ps = "".join(f'<span class="pill {c}">{t}</span>' for c, t in pills)
        return f'<article class="pipe"><h3>{h}</h3><p>{p}</p><ul>{li}</ul><div class="pills"><span>{label}</span>{ps}</div></article>'

    gets = "".join(f"<li>{x}</li>" for x in L["gets"])
    return f"""{pagehead(L, X, lang, "how", X["how_e"], L["how_h"], L["how_p"])}</div>
<section><div class="wrap sec tight stack"><ol class="steps">{steps}</ol>
<div class="outcomes"><div class="outcome pass"><svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true"><circle cx="14" cy="14" r="13" fill="#1C7748"/><path d="M8.5 14.5l3.8 3.8 7.2-8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><div><b>{L["pass"][0]}</b><span>{L["pass"][1]}</span></div></div>
<div class="outcome hold"><svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true"><circle cx="14" cy="14" r="13" fill="#7A4F00"/><path d="M10 9.5v9M18 9.5v9" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></svg><div><b>{L["hold"][0]}</b><span>{L["hold"][1]}</span></div></div></div></div></section>
<section class="alt"><div class="wrap sec stack"><div class="head"><h2 class="display">{L["cases_h"]}</h2><p>{L["cases_p"]}</p></div>
<div class="pipes">{pipe(L["mail_h"], L["mail_p"], L["mail"], L["verdict"], L["mail_pills"])}{pipe(L["xdr_h"], L["xdr_p"], L["xdr"], L["klass"], L["xdr_pills"])}</div>
<div class="gets"><h3>{L["gets_h"]}</h3><ul>{gets}</ul></div></div></section>
<section><div class="wrap sec stack"><div class="head"><h2 class="display">{X["arch_h"]}</h2><p>{X["arch_p"]}</p></div>
<div class="arch">
<div class="arch-col"><h3>Comes in</h3>
<div class="node"><b>Reporting mailbox</b>Mail your employees report, read from Microsoft 365.</div>
<div class="node"><b>Uploaded files</b>Message files an analyst submits by hand.</div>
<div class="node"><b>Defender XDR</b>Incidents and their alerts.</div>
<div class="node"><b>Defender for Endpoint and Entra ID</b>Device, email and sign-in activity MARS looks up for a case.</div></div>
<span class="arch-arrow" aria-hidden="true"></span>
<div class="arch-mid"><div class="arch-host"><span class="arch-tag">Your host</span>
<div class="arch-core"><b>MARS</b><div class="arch-stages"><span>Gather evidence</span><span>Ask the model</span><span>Check the answer</span><span>Publish or hold for review</span></div></div>
<div class="node"><b>Local database</b>Analysis records, the signed audit log and settings. Nothing here is stored anywhere else.</div></div>
<div class="arch-ext">
<div class="node"><b>Threat intelligence</b>Only the sources you configure.<small><i>Sends</i> indicators such as domains, URLs and file hashes.</small><small><i>Returns</i> reputation and context.</small></div>
<div class="node"><b>AI model</b>A hosted model, a company gateway or a local model. The host sets which endpoints are allowed.<small><i>Sends</i> the evidence for one case, with internal names replaced if you choose.</small><small><i>Returns</i> a structured answer, which MARS then checks.</small></div></div></div>
<span class="arch-arrow a2" aria-hidden="true"></span>
<div class="arch-col out"><h3>Goes out</h3>
<div class="node"><b>Analyst console</b>Verdicts, evidence and recommended steps, in the browser.</div>
<div class="node"><b>Notifications</b>Email, Teams or Slack, if you set them up.</div>
<div class="node"><b>Approved actions</b>Response steps a person has approved, sent through Microsoft's own interfaces.</div></div>
</div><p style="font-size:15px;color:var(--ink-2)">{X["arch_note"]}</p></div></section>
<footer class="band">{footer(L, X, "how")}</footer>"""


def why(L, X, lang):
    tiles = "".join(f'<div class="tile"><h2>{k}</h2><span>{v}</span></div>' for k, v in L["why"])
    C = COMPARE
    rows = "".join(
        f'<tr><th scope="row">{r[0]}</th><td>{r[1]}</td><td>{r[2]}</td><td class="us">{r[3]}</td></tr>' for r in C["rows"]
    )
    return f"""{pagehead(L, X, lang, "why", L["why_e"], L["why_h"], L["why_p"])}
<div class="wrap tiles" style="padding-bottom:104px">{tiles}</div></div>
<section><div class="wrap sec stack" style="gap:32px"><div class="head"><h2 class="display">{C["h"]}</h2><p>{C["p"]}</p></div>
<div class="cmp-wrap"><table class="cmp"><thead><tr><th scope="col"></th><th scope="col">{C["cols"][0]}</th><th scope="col">{C["cols"][1]}</th><th scope="col" class="us">{C["cols"][2]}</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cmp-note">{C["note"]}</p></div></section>
<section class="alt"><div class="wrap sec split"><div class="head"><span class="eyebrow">{X["ai_e"]}</span><h2 class="display">{L["ai_h"]}</h2><p>{L["ai_p"]}</p></div>
<div class="body cells">{cells(L["ai"])}</div></div></section>
<footer class="band">{footer(L, X, "why")}</footer>"""


def product(L, X, lang):
    grid = "".join(f"<div><b>{k}</b>{v}</div>" for k, v in L["pages"])
    grid += f'<div class="dashed"><b>{X["cli"][0]}</b>{X["cli"][1]}</div>'
    integ = "".join(
        f'<div><h3>{k}</h3><div class="chips">{"".join(f"<span>{x}</span>" for x in v)}</div></div>'
        for k, v in L["integ"]
    )
    shots = "".join(shot(n, lang, c, c, cls) for n, cls, c in X["shots"])
    return f"""{pagehead(L, X, lang, "product", X["product_e"], L["product_h"], L["product_p"])}</div>
<section class="alt"><div class="wrap sec tight stack" style="gap:28px"><div class="head"><h2 class="display">{X["shots_h"]}</h2><p>{X["shots_p"]}</p></div><div class="shots">{shots}</div></div></section>
<section><div class="wrap sec tight stack" style="gap:28px"><h2 class="plain">{X["pages_h"]}</h2><div class="grid">{grid}</div></div></section>
<section class="alt"><div class="wrap sec tight stack" style="gap:28px"><h2 class="plain">{X["integ_h"]}</h2><div class="integ">{integ}</div></div></section>
<section class="band"><div class="wrap closing stack"><div class="head"><span class="eyebrow">{X["deploy_e"]}</span><h2 class="display">{L["deploy_h"]}</h2><p>{L["deploy_p"]}</p></div>
<div class="cells" style="gap:0 48px;padding-bottom:20px">{cells(L["deploy"])}</div></div></section>
<footer class="band">{footer(L, X, "product")}</footer>"""


def security(L, X, lang):
    S = SECURITY[lang]
    bounds = "".join(
        f'<li class="bound"><div><span class="n">{i + 1:02d}</span><h3>{h}</h3><p>{p}</p></div><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></li>'
        for i, (h, p, items) in enumerate(S["bounds"])
    )
    return f"""{pagehead(L, X, lang, "security", S["eyebrow"], S["h1"], S["lead"])}</div>
<section><div class="wrap sec tight stack" style="gap:28px"><h2 class="display">{S["bounds_h"]}</h2><ol class="bounds">{bounds}</ol></div></section>
<section class="band"><div class="wrap sec stack"><div class="head"><span class="eyebrow">{S["limits_e"]}</span><h2 class="display">{S["limits_h"]}</h2><p>{S["limits_p"]}</p></div>
<div class="cells" style="gap:0 48px">{cells(S["limits"])}</div></div></section>
<section class="alt"><div class="wrap sec tight report"><h2 class="plain">{S["report_h"]}</h2><p>{S["report_p"]}</p></div></section>
<footer class="band">{footer(L, X, "security")}</footer>"""


def faq(L, X, lang):
    F = FAQ[lang]
    groups = "".join(
        f'<div class="qgroup"><h2>{g}</h2><div class="qa">{"".join(f"<div><h3>{q}</h3><p>{a}</p></div>" for q, a in qs)}</div></div>'
        for g, qs in F["groups"]
    )
    return f"""{pagehead(L, X, lang, "faq", F["eyebrow"], F["h1"], F["lead"])}</div>
<section><div class="wrap sec tight">{groups}</div></section>
<footer class="band">{footer(L, X, "faq")}</footer>"""


PAGES = {"index": home, "how": how, "why": why, "product": product, "security": security, "faq": faq}
ICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230B1F26'/%3E%3Cpath d='M8 23V9h3l5 8 5-8h3v14h-3v-9l-5 8-5-8v9z' fill='%235FD0E0'/%3E%3C/svg%3E"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap"
DESC = "MARS reads reported mail and Microsoft Defender XDR incidents, gathers the evidence, asks an AI model for a judgement, and publishes only the answers that evidence supports."


def render(page):
    X = EXTRA["en"]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{X["titles"][page]}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{X["titles"][page]}">
<meta property="og:description" content="Self-hosted AI phishing analysis and incident response whose answers are checked against evidence.">
<meta property="og:type" content="website">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{CSS}</style>
</head>
<body>
{PAGES[page](EN, X, "en")}
</body>
</html>
"""


def main():
    for page in PAGES:
        (ROOT / f"{page}.html").write_text(render(page), encoding="utf-8")
        print(f"wrote {page}.html")


if __name__ == "__main__":
    main()
