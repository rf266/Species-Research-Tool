import arxiv 
from urllib.request import urlretrieve
import os


client_search = arxiv.Client()

search = arxiv.Search(
    query="Endangered animals OR species", 
    max_results=200,
    sort_by= arxiv.SortCriterion.Relevance
)

results = client_search.results(search)
os.mkdir("./docs")
print("arxiv\n")
for result in results:
    print("result ", result.title)
    urlretrieve(result.pdf_url, f"./docs/{result.title}.pdf")

