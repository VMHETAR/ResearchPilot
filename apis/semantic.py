from schemas.search_dataclass import Paper

async def semantic_search(query: str) -> list[Paper]:


    papers = []

    for item in response["data"]:
        papers.append(
            Paper(
                title=item["title"],
                authors=[a["name"] for a in item["authors"]],
                abstract=item.get("abstract", ""),
                year=item["year"],
                source="Semantic Scholar",
                url=item["url"],
                doi=item.get("externalIds", {}).get("DOI")
            )
        )

    return papers