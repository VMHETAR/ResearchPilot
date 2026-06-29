from dataclass.search_dataclass import Paper

async def arxiv_search(query: str) -> list[Paper]:
    papers = []

    for entry in feed.entries:
        papers.append(
            Paper(
                title=entry.title,
                authors=[a.name for a in entry.authors],
                abstract=entry.summary,
                year=entry.published_parsed.tm_year,
                source="arXiv",
                url=entry.link,
                pdf_url=...
            )
        )

    return papers