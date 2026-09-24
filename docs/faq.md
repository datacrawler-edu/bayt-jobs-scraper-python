# FAQ

## Can I run the Actor without Python?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/bayt-jobs-data-scraper?fpr=edudata), enter searches in the **Input** tab, click **Start**, and inspect or export the **Dataset**.

## How do I search Bayt jobs by city?

Set `searches[].keywords`, a country slug such as `uae`, and the city name such as `Dubai`. See [`data/sample-input.json`](../data/sample-input.json).

## Can I search several markets in one run?

Yes. Add up to 25 entries to `searches`. `maxItems` is one global unique-job cap across all entries.

## Does the Actor always return descriptions, salary and skills?

No. `fetchDetails` requests detail enrichment, but each optional field depends on what the public Bayt listing exposes. Nullable values and empty skill arrays indicate unavailable data.

## What does a run-status row mean?

Rows with `recordType=run_status` describe the safe status of a target. Review them when the run returns fewer jobs than the cap; an Actor run can finish while some source coverage is partial.

## How is it priced?

Each unique job row delivered to the default Dataset is a billable event. The per-job price depends on your Apify tier. Run-status rows and duplicates are not billed; check the Actor's live Pricing tab before a run.

## Can I filter by salary, remote work or posting date?

Those filters are not part of the current input contract. The input supports keywords, country, optional city, a global cap and detail enrichment.
