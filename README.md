# Nemu-x-WL-singbox

Auto-updating **whitelist rule-set for sing-box**.

This project provides a lightweight remote rule-set designed for **whitelist routing**:

• domains in the list → **proxy**  
• everything else → **direct**

The rule-set is automatically generated from the Clash whitelist and compiled into the optimized **sing-box `.srs` format**.

---

![build](https://github.com/Nemu-x/privWL-singbox/actions/workflows/build-srs.yml/badge.svg)
![maintained](https://img.shields.io/badge/maintained-by%20Nemu--x-purple)
![last commit](https://img.shields.io/github/last-commit/Nemu-x/privWL-singbox)

---

# Quick Install

### Import config (recommended)

Use this URL inside your sing-box client:



[https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/singbox-config.json](https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/singbox-config.json)



Most sing-box clients support **Import from URL**.

---

### Install button

[![Import Config](https://img.shields.io/badge/Import-sing--box-blue?style=for-the-badge)](https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/singbox-config.json)

---

### QR Code

Scan this QR code inside your sing-box client.

<p align="center">
<img src="qr.png" width="220">
</p>

---

# Manual setup

If you want to add the rule-set manually, use the following rule-set URL:



[https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/nemu-x-wl.srs](https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/nemu-x-wl.srs)


Example configuration:

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "nemu-x-wl",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/Nemu-x/privWL-singbox/main/nemu-x-wl.srs",
        "update_interval": "1d"
      }
    ],
    "rules": [
      {
        "rule_set": ["nemu-x-wl"],
        "outbound": "proxy"
      }
    ],
    "final": "direct"
  }
}
````

---

# Features

* Automatic rule updates via GitHub Actions
* Remote rule-set for sing-box
* Optimized `domain_suffix` rules
* Lightweight `.srs` binary format
* Transparent rule generation
* Minimal configuration
* Fully open source

---

# How it works

```
Clash whitelist (YAML)
        ↓
GitHub Actions
        ↓
Convert to sing-box rule-set
        ↓
Compile to nemu-x-wl.srs
        ↓
Use as remote rule-set in sing-box
```

---

# Source list

The domain list is maintained in:

[https://github.com/Nemu-x/privWL-clash](https://github.com/Nemu-x/privWL-clash)

---

# Repository structure

```
privWL-singbox
│
├ nemu-x-wl.srs
├ nemu-x-wl.json
├ singbox-config.json
│
├ scripts
│   └ clash2srs.py
│
└ .github/workflows
    └ build-srs.yml
```

---

# Related projects

| Project      | Description          |
| ------------ | -------------------- |
| [privWL-clash](https://github.com/Nemu-x/privWL-clash) | Clash rule provider  |
| [privWL-happ](https://github.com/Nemu-x/privWL-happ)  | Happ routing profile |
| [sing-box](https://github.com/sagernet/sing-box)     | Core proxy engine    |

---

# License

MIT

---

# Disclaimer

This repository only provides routing rules and a domain list.

It does **not** provide proxy servers or bypass censorship on its own.

---
