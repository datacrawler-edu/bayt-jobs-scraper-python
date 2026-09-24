# Bayt Jobs Scraper API with Python

Run **Bayt Jobs Scraper | Full Details & Skills** from Apify's web interface without code, or call it with Python, JavaScript or cURL to collect structured public Bayt job listings with details when available.

This repository contains runnable API examples, a small input, one real Dataset row and a CSV export sample. The job record is copied from a successful run and retains its source values.

[Open Bayt Jobs Scraper on Apify](https://apify.com/datascraperes/bayt-jobs-http-scraper?fpr=edudata)

## What this repository helps you do

- Search Bayt jobs by role or skill, country and optional city.
- Collect descriptions, listed skills, employer and location details when Bayt exposes them.
- Compare hiring markets with several search definitions in one run.
- Export job records as JSON or CSV for recruiting research and analysis.

## Example result

The full Dataset item is in [`data/sample-output.json`](data/sample-output.json); [`data/sample-output.csv`](data/sample-output.csv) shows selected fields in table form. This excerpt is from that item:

```json
{
  "recordType": "job",
  "jobTitle": "Automation Tester",
  "jobCompany": "Cognizant",
  "jobLocation": "Dubai, UAE",
  "jobLink": "https://www.bayt.com/en/uae/jobs/automation-tester-5483309/",
  "detailStatus": "success"
}
```

## Run without code

1. Open [Bayt Jobs Scraper on Apify](https://apify.com/datascraperes/bayt-jobs-http-scraper?fpr=edudata).
2. In **Input**, add one or more job searches with keywords, country and optional city.
3. Set the maximum number of unique jobs and whether to fetch details, then click **Start**.
4. Open **Dataset** after the run and inspect the job rows and any run-status rows.
5. Export the Dataset as JSON, CSV or Excel.

See [`docs/no-code-guide.md`](docs/no-code-guide.md) and [`data/sample-input.json`](data/sample-input.json) for a small example.

## Try it with Apify's free plan

Apify's Free plan includes $5 in monthly prepaid usage for Store purchases or platform usage, with no credit card required. The credit is limited and unused credit expires at the end of the billing cycle. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) before a larger run.

## Quick start for developers

### Python

Install the Apify API client with `pip install -r examples/python/requirements.txt`, set `APIFY_API_TOKEN`, then run:

```bash
python examples/python/request.py
```

The script reads [`data/sample-input.json`](data/sample-input.json), calls the hosted Actor and prints Dataset items. On Windows PowerShell, set the token with `$env:APIFY_API_TOKEN = "your-token"`.

## Input example

```json
{
  "searches": [
    {
      "keywords": "AI",
      "country": "international",
      "city": ""
    }
  ],
  "maxItems": 3,
  "fetchDetails": true
}
```

See [`docs/input-reference.md`](docs/input-reference.md) for the full input contract and limits.

## Request examples

- cURL: [`examples/curl-request.md`](examples/curl-request.md)
- Python API call: [`examples/python/request.py`](examples/python/request.py)
- Download and export CSV: [`examples/python/export_jobs_csv.py`](examples/python/export_jobs_csv.py)
- JavaScript API call: [`examples/javascript/request.mjs`](examples/javascript/request.mjs)

These examples use the hosted Apify Actor. They do not include or expose its implementation.

## Output fields

| Field | Meaning |
| --- | --- |
| `recordType` | `job` for job records; `run_status` for safe target-status records. |
| `success`, `status` | Whether the source target completed and its public status. |
| `jobTitle`, `jobCompany`, `jobLocation` | Listing title, employer and location when available. |
| `jobLink`, `jobApplyUrl` | Public listing and application links when exposed. |
| `jobSalary`, `jobType`, `jobCareerLevel` | Optional listing attributes; null means unavailable. |
| `jobDescription`, `jobSkills` | Public detail-page description and listed skills when fetched. |
| `detailStatus` | Status of optional detail enrichment. |

See [`docs/output-reference.md`](docs/output-reference.md) for the full field guide.

## Common use cases

- Search a role in one city and review matching employers and descriptions.
- Compare the same role across several MENA countries in one Dataset.
- Export public job descriptions and listed skills for labor-market analysis.

See [`docs/use-cases.md`](docs/use-cases.md) for example inputs.

## Search Bayt jobs by location with Python

Put the role in `searches[].keywords`, the Bayt country slug in `country`, and an optional city in `city`. The sample [`data/sample-input.json`](data/sample-input.json) uses Dubai; country slugs such as `uae`, `saudi-arabia`, and `qatar` are supported.

## Export Bayt job listings to CSV

Run [`examples/python/export_jobs_csv.py`](examples/python/export_jobs_csv.py) to call the Actor and write the returned job records to a local CSV file. `run_status` rows are kept out of that job export.

## FAQ

See [`docs/faq.md`](docs/faq.md) for answers about input, results and pricing.

## Limits and pricing

The input accepts 1–25 search definitions and a global `maxItems` from 1 to 1,000. `fetchDetails` enables or disables detail-page enrichment. Output is deduplicated by job and can also contain `run_status` records for source coverage.

The Actor charges for each unique job row delivered to the default Dataset. Current per-job prices depend on Apify tier: FREE $0.00100, BRONZE $0.00090, SILVER $0.00080, and GOLD, PLATINUM and DIAMOND $0.00075. That is $1.00, $0.90, $0.80 and $0.75 per 1,000 jobs respectively. Run-status rows, duplicates and results not delivered as job rows are not charged. Check the live [Actor pricing page](https://apify.com/datascraperes/bayt-jobs-http-scraper?fpr=edudata) for the price that applies to your account.

## Hosted version

Use the hosted Actor to run repeatable keyword and location searches, store each Dataset on Apify and integrate results through the API:

[Open Bayt Jobs Scraper on Apify](https://apify.com/datascraperes/bayt-jobs-http-scraper?fpr=edudata)

## Responsible use

Use returned data lawfully and follow the terms and privacy obligations that apply to your work. This Actor collects public job listing information; it does not make the data unrestricted for every use. Keep API tokens in environment variables or a credential manager and never commit them.

## Support

For a problem with these examples, [open a GitHub issue](https://github.com/datacrawler-edu/bayt-jobs-scraper-python/issues) with the sanitized input and error message. For a run problem, include the Apify run ID but never include your API token.

## License

Released under the MIT License. See [`LICENSE`](LICENSE).
