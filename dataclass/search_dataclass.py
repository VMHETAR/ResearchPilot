from dataclasses import dataclass

@dataclass
class Paper:
    title:str
    authors:list[str]
    abstract:str
    year:int
    source:str
    url:str
    pdf_url:str | None = None
    doi:str | None = None