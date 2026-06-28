from dataclasses import dataclass

@dataclass
class SearchPapers:
    title:str
    authors:list[str]
    abstract:str
    year:int
    source:str
    url:str
    pdf_url:str | None
    doi:str | None