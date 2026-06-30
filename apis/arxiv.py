import feedparser
import requests
from schemas.search_dataclass import Paper

async def arxiv_search(query: str) -> list[Paper]:
    papers = []

    responses = requests.get(url=f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=10")
    feed = feedparser.parse(responses.text)
    for entry in feed.entries:
        papers.append(
            Paper(
                title=entry.title,
                authors=[a.name for a in entry.authors],
                abstract=entry.summary,
                year=entry.published_parsed.tm_year,
                source="arXiv",
                url=entry.link,
                pdf_url=entry.links[1].href
            )
        )

    return papers