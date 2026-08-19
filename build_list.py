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
! Description: Converted third-party tracker list from EFF Privacy Badger's seed data (Badger Sett).
! Homepage: https://github.com/HeimD0S/uprivacy
! Source: https://github.com/EFForg/privacybadger
! Version: {version_str}
! Last modified: {last_modified_str}
! Expires: 2 days
! Total Rules: {len(blocked_domains) + len(cookieblock_domains)}
!
! ========================================================
! Section 1: Third-Party Blocked Domains ({len(blocked_domains)})
! Blocks third-party tracking while allowing direct site navigation
! ========================================================
"""

lines = [header.strip()]
for domain in blocked_domains:
    # Use $3p so direct first-party visits to sites like google.com still work
    lines.append(f"||{domain}^$3p")

lines.append("""
! ========================================================
! Section 2: Third-Party Cookie-Blocked Domains ({0})
! Restricts 3rd-party cookies/storage without canceling the request
! ========================================================
""".format(len(cookieblock_domains)).strip())

for domain in cookieblock_domains:
    lines.append(f"||{domain}^$3p,cookie")

# 4. Write output file
with open("privacybadger.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated privacybadger.txt with {len(blocked_domains) + len(cookieblock_domains)} rules.")
