# Use cases

## Recruit for a city and role

Search a specific role within one city, then review employer, location, listing and application links.

```json
{"searches":[{"keywords":"software engineer","country":"uae","city":"Dubai"}],"maxItems":30,"fetchDetails":true}
```

Inspect `jobTitle`, `jobCompany`, `jobLocation`, `jobDescription` and `jobSkills`.

## Compare countries

Use several searches for the same role in different locations. `maxItems` is a global cap shared by all definitions.

```json
{"searches":[{"keywords":"data analyst","country":"uae","city":"Dubai"},{"keywords":"data analyst","country":"qatar","city":"Doha"}],"maxItems":50,"fetchDetails":true}
```

Compare `jobLocation`, `jobCompany`, `jobSkills` and `jobCreatedAt` when exposed.

## Build an export for analysis

Set a bounded result cap, run the Actor and use the Python CSV example to download a tabular file. Descriptions and skill values are public source data and can be missing for some listings.
