---
title: "Skills & Work"
permalink: /skills-work/
layout: single
author_profile: true
---

## Toolkit

**Recon & Scanning** — Nmap, Amass, Shodan, Nuclei, Gobuster
**Web Exploitation** — Burp Suite, SQLmap, OWASP ZAP, ffuf
**Exploitation & C2** — Metasploit, Cobalt Strike, Sliver, Impacket
**Scripting** — Python, Bash, PowerShell

## Interests

- API Testing
- Cloud Security
- Web Application Testing
- Malware Analysis
- Reverse Engineering
- Incident Response

## Write-ups & Work

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url | relative_url }})** — {{ post.date | date: "%b %-d, %Y" }}
{% endfor %}
