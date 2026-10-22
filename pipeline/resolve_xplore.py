#!/usr/bin/env python3
"""Map DOIs to IEEE Xplore document numbers through doi.org redirects.

Only doi.org is queried (one request per DOI, no redirect following), so this
touches IEEE Xplore not at all. Results are cached in corpus/xplore_ids.csv.
"""
import argparse
import csv
import os
import re
import sys
import time
import urllib.error
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def resolve(doi):
    opener = urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(f"https://doi.org/{doi}", method="HEAD",
                                 headers={"User-Agent": "ieee-distillation-skills/0.1"})
    try:
        opener.open(req, timeout=30)
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location", "")
        m = re.search(r"/document/(\d+)", loc)
        return m.group(1) if m else ""
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selected", default="corpus/selected.csv")
    ap.add_argument("--out", default="corpus/xplore_ids.csv")
    args = ap.parse_args()
    known = {}
    if os.path.exists(args.out):
        known = {r["doi"]: r["arnumber"] for r in csv.DictReader(open(args.out, encoding="utf-8"))}
    rows = list(csv.DictReader(open(args.selected, encoding="utf-8")))
    for r in rows:
        if r["doi"] in known and known[r["doi"]]:
            continue
        known[r["doi"]] = resolve(r["doi"])
        print(r["doi"], known[r["doi"]] or "-", file=sys.stderr)
        time.sleep(0.5)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["doi", "arnumber"])
        w.writerows(sorted(known.items()))


if __name__ == "__main__":
    main()
