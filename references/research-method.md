# Research method (how this skill's knowledge was built + how to refresh it)

Scenario: user wants you to "study all videos / guides / reddit / forums" and act as a
companion. The naive path (browser_navigate YouTube search → snapshot) FAILS: the
accessibility snapshot does NOT expose clean video URLs or IDs, and clicking results
doesn't yield IDs reliably. Use this pipeline instead.

## 1. Discover videos by scraping YouTube search HTML
The browser tool can't give you IDs; curl+regex on the search HTML can.

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
q="Palworld+1.0+progression+guide"
curl -s "https://www.youtube.com/results?search_query=$q" -A "$UA" -o /tmp/yt.html
python3 - <<'PY'
import re, glob
for f in glob.glob("/tmp/yt_*.html"):
    html=open(f,encoding='utf-8',errors='ignore').read()
    for m in re.finditer(r'"videoId":"([A-Za-z0-9_-]{11})".*?"title":\{"runs":\[\{"text":"(.*?)"\}', html):
        print(m.group(1), "|", m.group(2)[:80])
PY
```
This prints `videoId | title` so you can pick authoritative videos (favour
KhrazeGaming / Moxsy-IGN for Palworld; look for current-version wording and high
view counts).

## 2. Transcribe the chosen videos
Run the youtube-content helper (it IS available to run, just not editable by you):
```bash
uv run python3 "C:/Users/DOSe/AppData/Local/hermes/skills/media/youtube-content/scripts/fetch_transcript.py" "https://youtube.com/watch?v=VIDEO_ID" --text-only
```
Transcripts are the real information density; you don't need to "watch" the video.

## 3. Cross-check version currency
- Wikipedia infobox ("Release" date) confirms the current full/early-access version.
- Steam news API for live patch/content confirmation:
  `curl -s "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1623730&count=8&format=json"`
- SteamDB and palworld.wiki.gg often BLOCK automated access (Cloudflare / ban) — skip them.

## 4. Compile into the roadmap
Synthesize the transcripts into the phased Lv1→Lv80 roadmap in SKILL.md. Keep
coords, exact levels, and named Pals verbatim (they're the actionable payload).

Note: model training cutoff is nov-2024, so ALL post-cutoff game version content
must be researched live, never recalled. If asked something 1.0-specific not in
SKILL.md, re-run steps 1-3 rather than guessing.
