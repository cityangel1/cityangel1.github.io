---
title: "Information Gathering"
categories: [lab]
tags: [recon, osint, nmap]
excerpt: "Recon is where every engagement actually starts — this is the workflow I use to map an attack surface before touching an exploit."
---

<!-- EDIT: replace with your real write-up -->

Information gathering is the foundation of any engagement. Before a single exploit runs, the goal is to build the most complete possible picture of the target: what's exposed, what it's running, and where the soft edges are.

## Passive recon

- WHOIS / DNS enumeration
- Certificate transparency logs
- Shodan / Censys for exposed services

## Active recon

- Host discovery
- Port and service scanning with Nmap
- Technology fingerprinting

## Takeaway

The quality of everything downstream — exploitation, privilege escalation, reporting — depends on how thorough this stage is. Rushing recon is the most common way to miss the actual way in.
