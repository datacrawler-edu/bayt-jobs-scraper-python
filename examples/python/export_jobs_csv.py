"""Run Bayt Jobs Actor and export job records to CSV."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path

from apify_client import ApifyClient

ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
OUTPUT_PATH = ROOT / "data" / "bayt-jobs-export.csv"
ACTOR_ID = "datascraperes/bayt-jobs-http-scraper"
FIELDS = [
    "jobId", "jobTitle", "jobCompany", "jobLocation", "jobSalary",
    "jobType", "jobCareerLevel", "jobLink", "jobApplyUrl",
    "jobCreatedAt", "jobValidThrough", "detailStatus", "jobSkills",
]


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8-sig") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            if item.get("recordType") != "job":
                continue
            row = {field: item.get(field) for field in FIELDS}
            row["jobSkills"] = "; ".join(item.get("jobSkills") or [])
            row["jobSalary"] = json.dumps(row["jobSalary"], ensure_ascii=False) if isinstance(row["jobSalary"], (dict, list)) else row["jobSalary"]
            writer.writerow(row)
    print(f"Exported job rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
