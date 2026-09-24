# cURL request

Set `APIFY_API_TOKEN` in your environment first. This synchronous request posts the exact input JSON and returns default Dataset items when the run completes.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~bayt-jobs-data-scraper/run-sync-get-dataset-items" \
  --header "Authorization: Bearer $APIFY_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

For Windows PowerShell, use `Invoke-RestMethod` with the same endpoint, a bearer authorization header and `Get-Content -Raw` as the JSON body.
