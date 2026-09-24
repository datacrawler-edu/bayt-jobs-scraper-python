# Run Bayt Jobs Scraper without code

Open [Bayt Jobs Scraper](https://apify.com/datascraperes/bayt-jobs-data-scraper?fpr=edudata) and use its **Input** tab.

## Step-by-step

1. Add one to 25 job searches. Each search needs a keyword, such as `data analyst` or `Python developer`.
2. Choose a country slug, such as `uae`, `saudi-arabia` or `qatar`; add a city if needed.
3. Set `maxItems`, the total unique-job limit for the run, and choose whether to fetch full details.
4. Click **Start** and wait for the run to finish.
5. Open **Dataset**. Filter on `recordType=job` for job rows; review `run_status` rows to understand target coverage.
6. Export as JSON, CSV or Excel.

## First test

Use [`data/sample-input.json`](../data/sample-input.json), which requests up to five Dubai software-engineering jobs. A source search can return fewer jobs than the cap.

## Apify monthly free usage

The Free plan includes $5 of monthly prepaid usage and does not require a credit card. It is a finite platform credit, not unlimited free Actor runs. Unused credit expires at the end of the billing cycle. See [current Apify pricing](https://apify.com/pricing?fpr=edudata).

## Read the output

A job row has `recordType=job`. Check `jobTitle`, `jobCompany`, `jobLocation` and `jobLink`. If `fetchDetails` is true, `detailStatus` indicates whether detail data was available; descriptions and skill lists may still be unavailable at the source. A `run_status` item reports safe collection status and should be read when a target returns no jobs or coverage is partial.

## Larger runs and billing

You can enter up to 25 searches and set a global cap up to 1,000 unique jobs. The Actor charges per unique job row delivered; the per-item price varies with Apify tier. Consult the live [Actor pricing page](https://apify.com/datascraperes/bayt-jobs-data-scraper?fpr=edudata). Source availability varies by search and time, so the requested cap is a maximum, not a promise that every run will return that many rows.
