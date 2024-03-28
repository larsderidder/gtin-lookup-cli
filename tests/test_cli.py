from gtin_lookup_cli.cli import build_url


def test_build_url_adds_query():
    url = build_url("https://example.test/{code}", "123", "k")
    assert url == "https://example.test/123?key=k"


def test_build_url_respects_existing_query():
    url = build_url("https://example.test/{code}?a=b", "123", "k")
    assert url == "https://example.test/123?a=b&key=k"
