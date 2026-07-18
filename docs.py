import arxiv 
from urllib.request import urlretrieve
import os
import requests
client_search = arxiv.Client()

search = arxiv.Search(
    query="Endangered animal species", 
    max_results=100,
    sort_by= arxiv.SortCriterion.Relevance
)

results = client_search.results(search)
os.mkdir("./docs")
print("arxiv\n")
for result in results:
    print("result ", result.title)
    urlretrieve(result.pdf_url, f"./docs/{result.title}.pdf")


print("now openalex\n")
oa_api = os.getenv("OA_API_KEY")

url = f"https://api.openalex.org/works?api_key={oa_api}"

payload = {"search": "endangered species research", "filter": "is_oa:true"}

r = requests.get(url, params=payload)

print(r.json())