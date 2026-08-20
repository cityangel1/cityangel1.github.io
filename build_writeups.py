import re, html

POSTS = [
    dict(
        slug="active-directory-lab-notes",
        title="Active Directory Lab Notes",
        date="Aug 3, 2026",
        cat="profession",
        cat_label="Profession",
        excerpt="Building a disposable AD range to practice enumeration and lateral movement without touching anything real.",
        tools=["BloodHound", "PowerView", "Active Directory"],
        body=[
            ("p", "Most of what shows up in real engagements against enterprise networks eventually touches Active Directory. Practicing against a disposable, self-hosted range makes it possible to break things safely and repeatedly."),
            ("h2", "What the lab covers"),
            ("ul", ["Domain enumeration with BloodHound and PowerView", "Kerberoasting and AS-REP roasting", "Lateral movement and privilege escalation paths"]),
            ("lesson", "AD attack paths are rarely a single vulnerability — they're a chain of small misconfigurations. The lab is as much about learning to read that chain as it is about any one technique."),
        ],
    ),
    dict(
        slug="port-scanning-workflow",
        title="Port Scanning — Workflow Notes",
        date="Jul 20, 2026",
        cat="lab",
        cat_label="Lab",
        excerpt="Knowing what's actually listening on a target is the difference between guessing and testing.",
        tools=["Nmap"],
        body=[
            ("p", "Port scanning tells you what services are running and, by extension, what attack surface is actually available. It's part of information gathering, but it deserves its own pass because the follow-up decisions — which service to target first — all come from here."),
            ("h2", "Workflow"),
            ("ul", ["Fast scan across all ports to find what's open", "Targeted service and version scan against the open ports", "Cross-reference versions against known CVEs"]),
            ("lesson", "Default scripts and timing templates are a starting point, not a finish line — tuning scan speed and script selection to the target matters more than people expect early on."),
        ],
    ),
    dict(
        slug="information-gathering-workflow",
        title="Information Gathering — Recon Workflow",
        date="Jul 5, 2026",
        cat="lab",
        cat_label="Lab",
        excerpt="Recon is where every engagement actually starts — this is the workflow I use to map an attack surface before touching an exploit.",
        tools=["WHOIS", "Shodan", "Censys"],
        body=[
            ("p", "Information gathering is the foundation of any engagement. Before a single exploit runs, the goal is to build the most complete possible picture of the target: what's exposed, what it's running, and where the soft edges are."),
            ("h2", "Passive recon"),
            ("ul", ["WHOIS and DNS enumeration", "Certificate transparency logs", "Shodan and Censys for exposed services"]),
            ("h2", "Active recon"),
            ("ul", ["Host discovery", "Service and version fingerprinting", "Mapping the results back to a prioritised target list"]),
            ("lesson", "Passive recon should always come first — it costs nothing and rarely trips a detection. Active recon is where you start spending some of your stealth budget, so it should be aimed, not sprayed."),
        ],
    ),
    dict(
        slug="social-engineering-attacks",
        title="Social Engineering Attacks",
        date="Jul 18, 2025",
        cat="lab",
        cat_label="Lab",
        excerpt="Evaluating how the weakest link in any system — people — can be exploited, and what that means for defenders.",
        tools=["Google Search", "SET (Social-Engineer Toolkit)"],
        body=[
            ("p", "Social engineering attacks are effective and, honestly, fascinating to study. In a lab exercise, I evaluated how humans — the weakest link in most systems — can cause significant harm if they aren't equipped with the right awareness of social engineering tactics."),
            ("h2", "Setup"),
            ("p", "Challenge: send a crafted malicious link to a company worker via email."),
            ("ul", ["Google search to gather information about the target company", "SET (Social-Engineer Toolkit) to build the delivery"]),
            ("img", "https://github.com/user-attachments/assets/d0f10134-000d-415e-8452-462c0c7a7339"),
            ("lesson", "It's very easy to compromise a company through a well-crafted malicious link. Regular, up-to-date training on emerging social engineering threats is one of the highest-leverage defenses an organisation has."),
        ],
    ),
    dict(
        slug="cybersecurity-mindset",
        title="Cybersecurity Mindset",
        date="Jul 17, 2025",
        cat="profession",
        cat_label="Profession",
        excerpt="Knowledge is power — and in this field, that power comes with a choice about how you use it.",
        tools=[],
        body=[
            ("p", "Knowledge is power. With cybersecurity knowledge, you have a choice: be the good guy, or be the bad guy. But here's the real question — do you want to spend your life looking over your shoulder because of one bad decision made with that knowledge?"),
            ("p", "I've settled on an answer: life is genuinely better spent building and protecting than exploiting for personal gain. That mindset shapes every engagement I take on."),
        ],
    ),
    dict(
        slug="cybersecurity-introduction",
        title="Cybersecurity Introduction",
        date="Jul 12, 2025",
        cat="profession",
        cat_label="Profession",
        excerpt="What most people picture when they hear 'cybersecurity' — and what it actually means to work in it.",
        tools=[],
        body=[
            ("p", "What comes to mind for most people when they hear \"cybersecurity\" is hacking and its illegal side. For me, cybersecurity is about something closer to the opposite: enhancing the security that even the world's most powerful systems depend on to function at all."),
            ("p", "Without that layer of defense, scale and sophistication become liabilities rather than strengths. That's the part of the field that keeps me interested."),
        ],
    ),
    dict(
        slug="my-cybersecurity-qualities",
        title="My Cybersecurity Qualities",
        date="Jun 25, 2025",
        cat="profession",
        cat_label="Profession",
        excerpt="The traits I try to bring to every engagement, lab, and CTF.",
        tools=[],
        body=[
            ("p", "As a cybersecurity practitioner, it helps to have a clear set of principles driving daily work. Mine are:"),
            ("ul", ["Analytical skills", "Ethical integrity", "A continuous-learning mindset", "Adaptability", "Curiosity", "Team collaboration", "Risk awareness"]),
        ],
    ),
    dict(
        slug="information-gathering-osint",
        title="Information Gathering — OSINT Lab",
        date="Jun 24, 2025",
        cat="lab",
        cat_label="Lab",
        excerpt="A hands-on OSINT pass using social platforms and passive recon tooling.",
        tools=["Instagram", "TikTok", "X", "YouTube", "Google Search", "Spiderfoot"],
        body=[
            ("p", "Information gathering is one of the most important parts of pentesting and adjacent fields. It's a wide discipline that requires building a real picture of the target before anything else happens."),
            ("p", "It starts with basic information pulled from social media platforms: name, date of birth, place of residence, job, relationships, and general living standard."),
            ("img", "https://github.com/user-attachments/assets/e378e40e-48b6-4058-b921-7604d8fc827c"),
            ("img", "https://github.com/user-attachments/assets/f04f9a46-1563-4fe8-b399-eb2f3f01118b"),
            ("p", "I used passive mode throughout to avoid detection, and came away with a meaningful amount of data — including IP addresses and subdomains. A solid starting point for further exploitation."),
            ("lesson", "Exposing personal details on social platforms can have a real impact on someone's safety — especially for public figures or people in high-ranking positions."),
        ],
    ),
    dict(
        slug="port-scanning-nmap",
        title="Port Scanning — Nmap Lab",
        date="Jun 20, 2025",
        cat="lab",
        cat_label="Lab",
        excerpt="A practical Nmap pass to map open ports and services on a lab target.",
        tools=["Nmap"],
        body=[
            ("p", "Port scanning is essential to knowing what services are running on a target system. It's part of information gathering and helps establish the attack surface."),
            ("img", "https://github.com/user-attachments/assets/ce55c1e2-7185-478a-b598-e1877cb29930"),
            ("img", "https://github.com/user-attachments/assets/acedb381-82bd-44fb-a66c-970a598e2104"),
            ("img", "https://github.com/user-attachments/assets/af2dc51e-4430-4bcd-9709-57287ded26cf"),
            ("img", "https://github.com/user-attachments/assets/9318bc63-75e6-4a30-87a2-e456c2227d34"),
            ("h2", "Challenges"),
            ("p", "Scanning takes time, and some ports may be shielded behind a firewall that prevents detection."),
            ("lesson", "Ports act as doors, and anyone can attempt to access them. It's good practice for any organisation to lock down port-level security proactively."),
        ],
    ),
    dict(
        slug="bug-bounty",
        title="Bug Bounty",
        date="Jun 10, 2025",
        cat="projects",
        cat_label="Projects",
        excerpt="Practicing offensive skills the right way — inside legal, structured bug bounty programs.",
        tools=[],
        body=[
            ("p", "Hacking is good — in the right environment. With the skills I've built, I try to put them to use in safe, structured environments: bug bounty programs."),
            ("p", "I'm not a seasoned pro, but I try my best to learn something new with every submission and understand how the broader world of cybersecurity actually operates. It doubles as a project in its own right, since a successful, responsibly disclosed finding can pay out."),
            ("p", "<strong>Consistency beats perfection every time.</strong>"),
        ],
    ),
    dict(
        slug="max-devices-wifi-router",
        title="Maximum Devices Connected to a WiFi Router",
        date="May 15, 2025",
        cat="projects",
        cat_label="Projects",
        excerpt="A hostel WiFi bottleneck turned into a small, hands-on networking experiment.",
        tools=[],
        body=[
            ("p", "When I joined campus, I was placed in a hostel with free WiFi. The connection was often slow, and it bothered me enough to investigate — especially since the connection was sometimes excellent."),
            ("p", "I teamed up with hostelmates to figure out the maximum number of devices a LAN WiFi setup could realistically support. We connected devices one at a time, watching the connection as each new device joined."),
            ("p", "As more devices came online, the connection lagged noticeably — until we hit roughly 10 connected devices, at which point performance dropped off sharply."),
            ("lesson", "For that specific LAN setup, around 10 devices appeared to be the practical ceiling before shared bandwidth became the bottleneck."),
        ],
    ),
    dict(
        slug="pentesting-a-website",
        title="Pentesting a Website",
        date="Dec 28, 2024",
        cat="projects",
        cat_label="Projects",
        excerpt="Taking ownership of a real club website's security — and turning it into a hands-on pentesting project.",
        tools=[],
        body=[
            ("p", "Tools are only useful if you actually put them to work. Alongside being a cybersecurity student, I had the chance to serve as Vice Chair of a university club — and with that came access to the source code of our website."),
            ("p", "I took on the job of making sure the site was secure and used it as a chance to practice my skills in a live, if low-stakes, setting. It was voluntary work, but it confirmed that I wanted to do this professionally — on systems where security actually carries weight."),
        ],
    ),
]


def esc(s):
    return html.escape(s, quote=False)


def render_body(blocks):
    out = []
    for kind, content in blocks:
        if kind == "p":
            out.append(f"<p>{content}</p>")
        elif kind == "h2":
            out.append(f"<h2>{esc(content)}</h2>")
        elif kind == "ul":
            items = "".join(f"<li>{esc(i)}</li>" for i in content)
            out.append(f"<ul>{items}</ul>")
        elif kind == "img":
            out.append(f'<img src="{content}" alt="Screenshot from the write-up" loading="lazy">')
        elif kind == "lesson":
            out.append(f'<div class="lesson"><strong>Lesson learned.</strong> {esc(content)}</div>')
    return "\n".join(out)


PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Brian Karaba Wachira</title>
<meta name="description" content="{excerpt}">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

<nav id="site-nav">
  <div class="nav-inner">
    <a href="../index.html#top" class="nav-mark"><span class="dot"></span>brian@offsec:~$</a>
    <ul class="nav-links" id="nav-links">
      <li><a href="../index.html#about">About</a></li>
      <li><a href="../index.html#skills">Skills</a></li>
      <li><a href="../index.html#experience">Experience</a></li>
      <li><a href="../index.html#writeups">Write-ups</a></li>
      <li><a href="../index.html#beyond">Beyond</a></li>
      <li><a href="../index.html#contact">Contact</a></li>
    </ul>
    <div class="nav-right">
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode">
        <span class="tt-track">
          <span class="tt-icon tt-sun">☀</span>
          <span class="tt-icon tt-moon">☾</span>
          <span class="tt-knob"></span>
        </span>
      </button>
      <button id="nav-toggle-btn" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>

<main>
  <div class="wrap post-hero">
    <a class="back-link" href="../index.html#writeups">← All write-ups</a>
    <div class="post-meta" style="margin-top:1.2rem;">
      <span class="cat-tag">{cat_label}</span><span>·</span><span>{date}</span>
    </div>
    <h1>{title}</h1>
    {tools_html}
  </div>
  <div class="wrap">
    <article class="post-body">
      {body_html}
    </article>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;width:100%;">
    <span class="fmark mono">© 2026 Brian Karaba Wachira</span>
    <div class="flinks">
      <a href="mailto:cityangel111@gmail.com">Email</a>
      <a href="https://github.com/cityangel1" target="_blank" rel="noopener">GitHub</a>
      <a href="https://linkedin.com/in/brian-karaba-wachira" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </div>
</footer>

<button id="back-to-top" aria-label="Back to top">↑</button>
<script src="../assets/js/main.js"></script>
</body>
</html>
"""

CARD_TMPL = """<a class="card post-card" data-cat="{cat}" href="writeups/{slug}.html">
  <div class="post-meta"><span class="cat-tag">{cat_label}</span><span>·</span><span>{date}</span></div>
  <h3>{title}</h3>
  <p>{excerpt}</p>
  <span class="read-more">Read write-up →</span>
</a>"""

import os
os.makedirs("writeups", exist_ok=True)

cards = []
for post in POSTS:
    tools_html = ""
    if post["tools"]:
        tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in post["tools"])
        tools_html = f'<div class="interests-list" style="margin-top:1rem;">{tags}</div>'
    page = PAGE_TMPL.format(
        title=esc(post["title"]),
        excerpt=esc(post["excerpt"]),
        cat_label=post["cat_label"],
        date=post["date"],
        tools_html=tools_html,
        body_html=render_body(post["body"]),
    )
    with open(f"writeups/{post['slug']}.html", "w") as f:
        f.write(page)

    cards.append(CARD_TMPL.format(
        cat=post["cat"], cat_label=post["cat_label"], date=post["date"],
        title=esc(post["title"]), excerpt=esc(post["excerpt"]), slug=post["slug"],
    ))

with open("index.html") as f:
    idx = f.read()

idx = idx.replace("<!--WRITEUP_CARDS-->", "\n".join(cards))

with open("index.html", "w") as f:
    f.write(idx)

print(f"Generated {len(POSTS)} write-up pages and injected cards.")
