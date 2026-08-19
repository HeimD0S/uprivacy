import urllib.request
import json
from datetime import datetime, timezone

# 1. Fetch live Privacy Badger seed data
url = "https://raw.githubusercontent.com/EFForg/privacybadger/master/src/data/seed.json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

action_map = data.get("action_map", {})

# 2. Extract blocked and cookie-blocked domains
blocked_domains = sorted([d for d, v in action_map.items() if v.get("heuristicAction") == "block"])
cookieblock_domains = sorted([d for d, v in action_map.items() if v.get("heuristicAction") == "cookieblock"])

# 3. Format uBlock / Adblock Plus compliant metadata
now_utc = datetime.now(timezone.utc)
version_str = now_utc.strftime("%Y%m%d%H%M")
last_modified_str = now_utc.strftime("%d %b %Y %H:%M UTC")

header = f"""[Adblock Plus 2.0]
! Title: EFF Privacy Badger Blocklist
! Description: Automatically converted filter list from EFF Privacy Badger's seed data (Badger Sett).
! Homepage: https://github.com/HeimD0S/uprivacy
! Source: https://github.com/EFForg/privacybadger
! Version: {version_str}
! Last modified: {last_modified_str}
! Expires: 2 days
! Total Rules: {len(blocked_domains) + len(cookieblock_domains)}
!
! ========================================================
! Section 1: Hard Blocked Tracking Domains ({len(blocked_domains)})
! ========================================================
"""

lines = [header]
for domain in blocked_domains:
    lines.append(f"||{domain}^")

lines.append(f"""
! ========================================================
! Section 2: Cookie-Blocked Domains ({len(cookieblock_domains)})
! Blocks 3rd-party cookie & storage access
! ========================================================
""")

for domain in cookieblock_domains:
    lines.append(f"||{domain}^$3p,cookie")

# 4. Write output file
with open("privacybadger.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated privacybadger.txt with {len(blocked_domains) + len(cookieblock_domains)} rules.")
