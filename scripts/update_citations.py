"""Refresh _data/citations.json from OpenAlex for every {% include cite.html id="W..." %} in _pages."""
import glob, json, re, urllib.request
from datetime import date

ids = sorted({i for f in glob.glob("_pages/*.html") for i in re.findall(r'include cite\.html id="(W\d+)"', open(f).read())})
url = "https://api.openalex.org/works?per-page=200&select=id,cited_by_count,counts_by_year&filter=openalex:" + "|".join(ids)
req = urllib.request.Request(url, headers={"User-Agent": "kimjongwoo-cell.github.io (mailto:kimjongwoo-cell@users.noreply.github.com)"})
works = json.load(urllib.request.urlopen(req, timeout=60))["results"]
out = {}
for w in works:
    years = {c["year"]: c["cited_by_count"] for c in w["counts_by_year"]}
    first = min(years, default=date.today().year)
    out[w["id"].rsplit("/", 1)[1]] = {"total": w["cited_by_count"],
        "years": [{"year": y, "n": years.get(y, 0)} for y in range(first, date.today().year + 1)]}
json.dump({"updated": date.today().isoformat(), "works": out}, open("_data/citations.json", "w"), indent=1)
print(len(out), "of", len(ids), "works")
