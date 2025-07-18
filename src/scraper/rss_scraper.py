import feedparser

RSS_FEEDS = [
    "https://feeds.bloomberg.com/markets/news.rss",
    "https://feeds.bloomberg.com/technology/news.rss",
    "https://feeds.bloomberg.com/economics/news.rss"
]

def get_rss_headlines() -> list[dict]:
    """
    Fetch and deduplicate headlines from all predefined RSS feed URLs.

    Returns:
        list[dict]: A list of dictionaries with 'title' and 'published' keys.
    """
    seen_titles = set()
    results = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = getattr(entry, 'title', '').strip()
            published = getattr(entry, 'published', None)

            if title and title not in seen_titles:
                seen_titles.add(title)
                results.append({
                    "title": title,
                    "published": published
                })

    return results
