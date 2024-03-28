# GTIN Lookup CLI

Look up GTIN/UPC data from a configurable HTTP API and print JSON results.

## Install (from source)
```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

## Usage
```sh
export GTIN_LOOKUP_API_KEY=your-key

gtin-lookup 8712345678901
```

## Options
- `--base-url`: API base URL (default: `https://go-upc.com/api/v1/code/{code}`).
- `--api-key`: API key (or set `GTIN_LOOKUP_API_KEY`).
- `--pretty`: pretty-print JSON output.

## Development
```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```

## License
See `LICENSE`.
