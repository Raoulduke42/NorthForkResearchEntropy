from scraper.rss_scraper import get_rss_headlines

def main():
    headlines = get_rss_headlines()

    print(f"Fetched {len(headlines)} headlines:\n")

    for item in headlines:
        print(f"[{item['published']}] {item['title']}")

if __name__ == "__main__":
    main()
