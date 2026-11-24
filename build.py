import html
MAIL="mannyadspecialist@zohomail.com"
SUB="https://mannyads.substack.com/?utm_source=mannyads_site"
NAV=[("index.html","Home"),("offers.html","Offers & prices"),("agencies.html","For agencies"),("how-i-work.html","How I work"),("suspension-decoded.html","Suspension Decoded"),("about.html","About")]
def page(fn,title,desc,body):
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a>' for h,t in NAV)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Manny Ads</title><meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="assets/manny_ads_logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Serif:wght@500;600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"></head><body>
<header class="top"><div class="wrap"><a href="index.html" aria-label="Manny Ads home"><img src="assets/manny_ads_logo.svg" alt="Manny Ads"></a><nav>{nav}<a class="cta" href="work-with-me.html">Free triage</a></nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap"><p><b>Manny Ads</b> · Google Ads account recovery · <a href="mailto:{MAIL}">{MAIL}</a></p>
<p>Independent specialist. Not affiliated with, endorsed by or sponsored by Google. Nothing on this site guarantees any outcome with Google.</p>
<p><a href="{SUB}">Suspension Decoded</a> · <a href="legal.html#privacy">Privacy</a> · <a href="legal.html#terms">Terms</a></p></div></footer>
</body></html>'''
P={}
P["index.html"]=("Google Ads account recovery","Manny Ads helps businesses find why a Google Ads account was suspended, fix it and file the appeal. Free triage, no guarantees.",f'''
<section class="hero"><p class="lbl">Google Ads account recovery</p>
<h1>Suspended Google Ads account? I find the cause, fix it, and file the appeal.</h1>
<p class="lead">I handle suspensions for Circumventing Systems, Abuse of the Ad Network and Unacceptable Business Practices. Send me the suspension notice for a free triage and I will tell you honestly whether the case looks recoverable.</p>
<a class="btn" href="work-with-me.html">Get a free triage</a><a class="btn alt" href="offers.html">See offers and prices</a></section>
<h2>Who this is for</h2>
<p>Businesses with a real product or service that are willing to fix what Google flagged. I decline work that keeps cloaking, deceptive redirects or fake landing pages in place, creating replacement accounts to evade a suspension, or anything that needs a guaranteed result.</p>
<h2>What happens</h2>
<ol class="steps"><li><b>Free triage.</b> Send the suspension wording and your site URL. You get a straight answer within 1 business day.</li>
<li><b>Diagnosis and fix list.</b> I identify the likely trigger and list what must change in your site and ads before appealing.</li>
<li><b>Appeal.</b> I write and submit the appeal, and follow up. Google alone decides the result.</li></ol>
<div class="note"><b class="lbl">No guarantees</b><br>Google decides every appeal. My fee covers my work, not the outcome, and I never promise reinstatement.</div>
<h2>I also publish</h2>
<p><a href="suspension-decoded.html">Suspension Decoded</a> is my independent publication on how Google Ads suspensions work. Tagline: <i>Behind the suspension. Beyond the appeal.</i></p>
<p><a class="btn" href="work-with-me.html">Send me your case</a></p>''')
P["offers.html"]=("Offers and prices","Manny Ads offers and prices in naira: recovery, audits, setup and monitoring.",f'''
<p class="lbl">Offers and prices</p><h1>What I offer</h1>
<p>Prices are in naira and start from the figures below; I confirm a fixed price after the free triage. Dollar amounts are approximate at ₦1,500 per $1.</p>
<div class="tw"><table><tr><th>Service</th><th>What it covers</th><th>From</th></tr>
<tr><td><b>Free triage</b></td><td>Likely trigger, whether it looks recoverable, and what it would take. Reply within 1 business day.</td><td>Free</td></tr>
<tr><td><b>Account Recovery Package</b></td><td>Diagnosis, compliance fix list for your site and ads, written appeal strategy, submission, and one follow-up round. Paid 50% upfront, 50% on submission, not tied to the outcome.</td><td>₦150,000 (≈$100)</td></tr>
<tr><td><b>Additional appeal round</b></td><td>Further appeal after the included round.</td><td>₦30,000 (≈$20)</td></tr>
<tr><td><b>Policy Health Audit</b></td><td>Review of ads, landing pages and account setup for policy risk, with a prioritized written fix list. Paid upfront.</td><td>₦50,000 (≈$33)</td></tr>
<tr><td><b>Search or Performance Max setup</b></td><td>Campaign setup built around policy compliance.</td><td>₦100,000 (≈$67)</td></tr>
<tr><td><b>Compliance monitoring</b></td><td>Monthly checks and quick fixes so the same flag does not return.</td><td>₦350,000 / month (≈$233)</td></tr></table></div>
<div class="note"><b class="lbl">Read this</b><br>I do not guarantee reinstatement, approval, timing or ad performance. Google decides appeals. Work already delivered is not refundable; if I cannot begin work, the upfront payment is refunded. See the <a href="legal.html#terms">terms</a>.</div>
<p><a class="btn" href="work-with-me.html">Start with the free triage</a></p>''')
a=lambda n:f"₦{round(n*0.8):,}"
P["agencies.html"]=("For agencies","White-label Google Ads account recovery for agencies, 20% below standard prices.",f'''
<p class="lbl">For agencies</p><h1>White-label recovery under your brand</h1>
<p>If your clients' accounts get suspended, I can handle diagnosis, fix list and appeal under your agency's name. I start with a free triage on one live case so you can judge the work before committing.</p>
<div class="tw"><table><tr><th>Service</th><th>Agency price from</th></tr>
<tr><td>Account Recovery Package</td><td>{a(150000)}</td></tr><tr><td>Policy Health Audit</td><td>{a(50000)}</td></tr>
<tr><td>Search or Performance Max setup</td><td>{a(100000)}</td></tr><tr><td>Compliance monitoring</td><td>{a(350000)} / month</td></tr>
<tr><td>Additional appeal round</td><td>{a(30000)}</td></tr></table></div>
<p>Agency prices are 20% below standard. The same rules apply: no guarantees, no cloaking or deceptive practices, and no passwords, only Google Ads manager access.</p>
<p><a class="btn" href="work-with-me.html?utm_source=agency_page">Send one live case</a></p>''')
P["how-i-work.html"]=("How I work","How Manny Ads handles Google Ads suspensions: a six-step framework and how to judge the work.",f'''
<p class="lbl">Method</p><h1>How I work, and how to judge it</h1>
<p>I do not show case stories or results here. Any case I describe publicly will have a source record and written client permission first. Until then, judge the work by the method and by a free triage on your own case.</p>
<h2>The six-step framework</h2>
<ol class="steps"><li><b>Identify.</b> Read the exact notice and establish the policy cited.</li><li><b>Investigate.</b> Check the site, ads, payments and recent account changes against that policy.</li>
<li><b>Fix first.</b> Make the changes Google flagged before any appeal is sent.</li><li><b>Write the appeal.</b> A factual, policy-grounded account of the cause and the fixes.</li>
<li><b>Submit and track.</b> File through the proper channel and log every step.</li><li><b>Follow up.</b> Respond to Google's replies and decide on further rounds.</li></ol>
<h2>What you get to check</h2>
<ul><li>A written diagnosis tied to the wording of your notice.</li><li>A fix list you can verify on your own site.</li><li>The appeal text before it is submitted.</li><li>A clear statement of what is uncertain.</li></ul>
<div class="note"><b class="lbl">Limits</b><br>Some cases are not recoverable. If I think yours is not, the triage will say so.</div>
<p>For analysis of how suspensions work in general, read <a href="{SUB}">Suspension Decoded</a>.</p>
<p><a class="btn" href="work-with-me.html">Get a free triage</a></p>''')
P["suspension-decoded.html"]=("Suspension Decoded","Suspension Decoded is an independent publication about Google Ads suspensions by Manny Ads.",f'''
<p class="lbl">Publication</p><h1>Suspension Decoded</h1>
<p class="lead"><i>Behind the suspension. Beyond the appeal.</i></p>
<p>An independent publication about how Google Ads suspensions work: the policies, the evidence, and the limits of what anyone can know from outside Google.</p>
<p><a class="btn" href="{SUB}">Read on Substack</a></p>
<div class="note"><b class="lbl">Disclosure</b><br>Written by Manny Ads, a Google Ads specialist who offers Google Ads account recovery. Suspension Decoded is independent: not affiliated with, endorsed by or sponsored by Google. Nothing here guarantees any outcome with Google.</div>
<div class="note"><b class="lbl">AI assistance</b><br>Written with AI assistance for research and drafting. Every piece is checked and approved by me before it is published.</div>
<p>The publication does not sell inside articles. If you want help with your own account, <a href="work-with-me.html?utm_source=suspension_decoded">send a case</a>.</p>''')
P["about.html"]=("About","About Manny Ads, a Google Ads account recovery specialist and trading name of Immanuel Aziba.",f'''
<p class="lbl">About</p><h1>About Manny Ads</h1>
<p>Manny Ads is the trading name of Immanuel Aziba, a Google Ads specialist based in Nigeria who works remotely on account suspensions, appeals and policy compliance.</p>
<p>I also write Suspension Decoded, an independent publication on the same subject. The business and the publication are linked openly, and the publication never sells inside an article.</p>
<h2>Independence</h2>
<p>I am an independent specialist, not affiliated with or endorsed by Google, and I have no special channel to Google's decisions.</p>
<h2>Certifications</h2>
<p>Google Ads Search and Measurement certifications: in progress.</p>
<h2>What I will not do</h2>
<p>I will not keep cloaking, deceptive redirects or fake landing pages in place, create new accounts to evade a suspension, submit false statements to Google, post fake reviews, or ask for your password.</p>
<p><a class="btn" href="work-with-me.html">Get a free triage</a></p>''')
P["work-with-me.html"]=("Work with me","Send your Google Ads suspension for a free triage. Reply within 1 business day.",f'''
<p class="lbl">Free triage</p><h1>Tell me what happened</h1>
<p>I reply within 1 business day with whether the case looks recoverable. Send the suspension wording, your site URL and what the account advertised. <b>Never send passwords.</b> If I take the case, access is granted through Google Ads manager access. Please do not post account IDs publicly.</p>
<form action="https://formspree.io/f/xoederzl" method="POST">
<input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
<input type="hidden" name="utm_source" id="utm_source"><input type="hidden" name="utm_content" id="utm_content">
<label>Your name<input type="text" name="name" required autocomplete="name"></label>
<label>Email<input type="email" name="email" required autocomplete="email"></label>
<label>Website URL<input type="url" name="website" required placeholder="https://"></label>
<label>Google Ads customer ID (optional)<input type="text" name="customer_id" placeholder="123-456-7890"></label>
<label>Suspension type<select name="suspension_type" required><option value="">Choose one</option><option>Circumventing Systems</option><option>Abuse of the Ad Network</option><option>Unacceptable Business Practices</option><option>Other or not sure</option></select></label>
<label>Date suspended<input type="text" name="date_suspended" placeholder="e.g. 28 October 2026"></label>
<label>Paste the wording of the suspension notice<textarea name="notice" required></textarea></label>
<label>What changed recently (site, ads, payments, ownership, agency)?<textarea name="changes"></textarea></label>
<label class="check"><input type="checkbox" name="will_fix" value="yes" required><span>I understand recovery depends on fixing whatever Google flagged, and I am willing to make those changes. No result is guaranteed.</span></label>
<label class="check"><input type="checkbox" name="consent" value="yes" required><span>I consent to Manny Ads (Immanuel Aziba) using these details to assess my case, as described in the <a href="legal.html#privacy">privacy notice</a>.</span></label>
<p><button class="btn" type="submit" style="border:0;cursor:pointer;font:inherit;font-weight:600">Send for free triage</button></p></form>
<p>Prefer email? <a href="mailto:{MAIL}">{MAIL}</a></p>
<script>try{{var q=new URLSearchParams(location.search);document.getElementById("utm_source").value=q.get("utm_source")||"direct";document.getElementById("utm_content").value=q.get("utm_content")||"";}}catch(e){{}}</script>''')
for fn,(t,d,b) in P.items(): open(fn,"w").write(page(fn,t,d,b))
# legal: adapt old page
L=open("/mnt/user-data/uploads/legal.html").read()
import re
body=L[L.index('<h1>'):L.index('</main>')]
body=body.replace('<p class="m">Last updated: November 2026. Replace the bracketed items before publishing, and have a Nigerian lawyer review this page.</p>','<p class="mono">Last updated: November 2026</p>')
body=body.replace("Immanuel Aziba, Nigeria, is the data controller.","Immanuel Aziba, trading as Manny Ads, Nigeria, is the data controller.")
body=body.replace("the service providers I use to run the practice: Formspree, my email provider (zohomail), and cloud storage.","the service providers I use to run the practice: Formspree (which receives form submissions), my email provider (Zoho Mail), and cloud storage. This site is hosted on Vercel.")
body=body.replace('<h3>How long I keep it</h3>','<h3>Cookies and analytics</h3>\n<p>This site does not use analytics or advertising cookies. Links may carry a source tag (for example, which platform you came from) so I can see where an enquiry started; it is saved with your form only.</p>\n<h3>How long I keep it</h3>')
body=body.replace("Triage requests that do not become projects are deleted","Declined or lost leads and triage requests that do not become projects are deleted")
open("legal.html","w").write(page("legal.html","Privacy Notice and Terms of Service","Manny Ads privacy notice and terms of service.",body))
