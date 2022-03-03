import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")
print(results)

job_elements = results.find_all("div",class_="card-content")

for temp in job_elements:
    title_name = temp.find("h2",class_="title")
    print(title_name.text)
