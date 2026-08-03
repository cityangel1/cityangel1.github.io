---
title: "Port Scanning"
categories: [lab]
tags: [nmap, recon]
excerpt: "Knowing what's actually listening on a target is the difference between guessing and testing."
---

<!-- EDIT: replace with your real write-up -->

Port scanning tells you what services are running and, by extension, what attack surface is actually available. It's part of information gathering, but it deserves its own pass because the follow-up decisions — which service to target first — all come from here.

## Workflow

1. Fast scan across all ports to find what's open
2. Targeted service/version scan against the open ports
3. Cross-reference versions against known CVEs

## Notes

Default scripts and timing templates are a starting point, not a finish line — tuning scan speed and script selection to the target matters more than people expect early on.
