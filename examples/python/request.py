"""Run the hosted Bayt Jobs Actor and print its Dataset rows."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient

ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
ACTOR_ID = "datascraperes/bayt-jobs-data-scraper"


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
