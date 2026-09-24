# Input reference

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `searches` | array | Yes | `[{"keywords":"AI","country":"international","city":""}]` | One to 25 search definitions. |
| `searches[].keywords` | string | Yes | `software engineer` | Role, skill or phrase; 1–120 characters. |
| `searches[].country` | string | No | `uae` | Bayt country slug. Defaults to `international`; see the Apify input selector for suggested values. |
| `searches[].city` | string | No | `Dubai` | Optional city within the selected country; up to 80 characters. Empty searches the country. |
| `maxItems` | integer | No | `30` | Global cap of 1–1,000 unique jobs across searches; default 30. |
| `fetchDetails` | boolean | No | `true` | Fetch public job detail pages after discovering listings; defaults to true. |

## Validation and limits

- Search definitions: 1–25.
- Each keyword: 1–120 characters.
- City: at most 80 characters.
- Country slug: 1–80 characters; select from the live input field's suggestions.
- Global result cap: 1–1,000, default 30.
- Details: enabled by default; set `false` for listing-card fields only.
- There are no URL, salary, remote-only, company-only or date-range input fields.
