# 1. Import necessary libraries
import asyncio
import os
import re
import zipfile
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
# from crawl4ai.content_scraping_strategy import PlaywrightWebScrapingStrategy  # optional


async def main():
    """
    Performs a 2-level BFS crawl on www.wikipedia.com
    and saves each scraped page as a markdown file.
    Finally compresses them into results.zip.
    """

    start_url = "https://www.wikipedia.com"
    max_depth = 2
    max_pages = 1000
    zip_name = "results.zip"

    # Ensure the output directory exists
    output_dir = "output_1000"
    os.makedirs(output_dir, exist_ok=True)
    print(f"--- Saving output to ./{output_dir}/ directory ---")

    # Configure the crawl
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        # scraping_strategy=PlaywrightWebScrapingStrategy(),  # if LXML fails
        user_agent="Mozilla/5.0 (compatible; MyCrawler/1.0; +https://example.com/bot)",
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        print(f"\n--- Starting BFS deep crawl on {start_url} ---")
        results = await crawler.arun(start_url, config=config)

        print(f"\n--- Crawling complete! Got {len(results)} pages in total. ---")

        # Debug sample of results
        for r in results[:5]:
            print(f"URL: {r.url}, Markdown length: {len(r.markdown) if r and r.markdown else 0}")

        # Save each result to a markdown file
        print("\n--- Saving files... ---")
        saved_files = []
        for result in results:
            if result and result.markdown:
                sanitized_name = re.sub(r'https?://|/|:', '_', result.url)
                filename = f"{sanitized_name}.md"
                filepath = os.path.join(output_dir, filename)

                try:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(result.markdown)
                    print(f"✅ Saved: {filepath}")
                    saved_files.append(filepath)
                except Exception as e:
                    print(f"❌ Failed to save {filepath}: {e}")

        print(f"\n--- Finished saving {len(saved_files)} files. ---")

        # Compress results into a zip file
        if saved_files:
            with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
                for file in saved_files:
                    zipf.write(file, os.path.basename(file))
            print(f"\n--- All files compressed into {zip_name} ---")
        else:
            print("\n⚠️ No files saved, skipping zip creation.")


# Run when executed from the terminal
if __name__ == "__main__":
    asyncio.run(main())
