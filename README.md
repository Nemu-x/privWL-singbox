# privWL-singbox

Auto-updating whitelist rule-set for **sing-box**.

This repository provides a remote rule-set for running sing-box in **whitelist mode** — only selected domains are routed through the proxy, while everything else goes **DIRECT**.

The domain list is automatically synchronized with the Clash version of this project.

---

![build](https://github.com/Nemu-x/privWL-singbox/actions/workflows/build-srs.yml/badge.svg)
![last commit](https://img.shields.io/github/last-commit/Nemu-x/privWL-singbox)
![repo size](https://img.shields.io/github/repo-size/Nemu-x/privWL-singbox)
![license](https://img.shields.io/github/license/Nemu-x/privWL-singbox)

---

## Features

- Automatic updates via GitHub Actions
- Remote binary rule-set for sing-box
- Whitelist routing based on Clash `DOMAIN-SUFFIX` rules
- Minimal and transparent setup
- Human-readable `privwl.json` included
- Fully open source

---

## Source list

The source domain list is maintained in the
[privWL-clash repository](https://github.com/Nemu-x/privWL-clash).

---

## How it works

```text
Clash whitelist (YAML)
        ↓
GitHub Actions
        ↓
Convert to sing-box source rule-set
        ↓
Compile to privwl.srs
        ↓
Use as remote rule-set in sing-box
