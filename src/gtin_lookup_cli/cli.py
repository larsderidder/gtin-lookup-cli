import argparse
import json
import os
from typing import Optional



DEFAULT_BASE = "https://go-upc.com/api/v1/code/{code}"


def build_url(base_url: str, code: str, api_key: str) -> str:
    """Build the request URL including the API key query parameter."""
    url = base_url.format(code=code)
    joiner = "&" if "?" in url else "?"
    return f"{url}{joiner}key={api_key}"


def fetch_payload(code: str, base_url: str, api_key: str, timeout: float) -> dict:
    """Fetch JSON payload for the given GTIN/UPC code."""
    import requests

    url = build_url(base_url, code, api_key)
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Lookup GTIN/UPC data")
    parser.add_argument("code", help="GTIN/UPC to query")
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--api-key", default=os.getenv("GTIN_LOOKUP_API_KEY"))
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--timeout", type=float, default=10)
    return parser.parse_args(argv)


def main(argv: Optional[list] = None) -> None:
    """CLI entry point."""
    args = parse_args(argv)
    if not args.api_key:
        raise SystemExit("Missing API key. Provide --api-key or GTIN_LOOKUP_API_KEY.")

    payload = fetch_payload(args.code, args.base_url, args.api_key, args.timeout)
    if args.pretty:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload))


if __name__ == "__main__":
    main()
