---
title: "Active Directory Lab Notes"
categories: [profession]
tags: [active-directory, red-team]
excerpt: "Building a disposable AD range to practice enumeration and lateral movement without touching anything real."
---

<!-- EDIT: replace with your real write-up -->

Most of what shows up in real engagements against enterprise networks eventually touches Active Directory. Practicing against a disposable, self-hosted range makes it possible to break things safely and repeatedly.

## What the lab covers

- Domain enumeration (BloodHound, PowerView)
- Kerberoasting and AS-REP roasting
- Lateral movement and privilege escalation paths

## Takeaway

AD attack paths are rarely a single vulnerability — they're a chain of small misconfigurations. The lab is as much about learning to read that chain as it is about any one technique.
