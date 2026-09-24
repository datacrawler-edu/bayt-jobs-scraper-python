# Output reference

The default Dataset contains job records and may contain safe `run_status` records.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `recordType` | string | Yes | `job` for a delivered listing or `run_status` for target-status output. |
| `success` | boolean | Yes | Whether the target operation completed successfully. |
| `status` | string | Yes | Public target status such as `ok`, `exhausted` or a safe partial-state status. |
| `source` | string | Yes | Source site identifier (`bayt`). |
| `searchUrl` | string | Yes | Generated Bayt search page for the target. |
| `jobId` | string or null | For jobs | Source job identifier when available. |
| `jobTitle` | string or null | For jobs | Listing title. |
| `jobLink` | string or null | For jobs | Canonical public job page. |
| `jobSalary` | string, object or null | For jobs | Salary text/data if Bayt exposes it. |
| `jobType`, `jobCareerLevel` | string or null | For jobs | Employment type and career level where available. |
| `jobCompany`, `jobCompanyLogo` | string or null | For jobs | Employer name and logo URL. |
| `jobLocation` | string or null | For jobs | Source-provided location. |
| `jobDescription` | string or null | For jobs | Plain-text description from the public detail page. |
| `jobDescriptionHtml` | string or null | For jobs | HTML description when available. |
| `jobSkills` | array | Yes | Listed requirements/skills; may be empty when unavailable. |
| `preferredCandidate` | object or null | For jobs | Structured candidate information when present. |
| `jobCreatedAt`, `jobValidThrough` | string or null | For jobs | Source posting and expiry values where available. |
| `jobApplyUrl` | string or null | For jobs | Application URL when Bayt exposes one. |
| `detailStatus` | string | Yes | Outcome of optional detail enrichment. |
| `scrapedAt` | string | Yes | UTC timestamp for the item. |
| `errorType` | string or null | Yes | Safe error category when relevant. |
| `page` | integer or null | Yes | Source page index where relevant. |
| `message` | string or null | Yes | Safe status explanation where relevant. |

Nullable values mean the source did not provide a value. See [`data/sample-output.json`](../data/sample-output.json) for one complete real job row.
