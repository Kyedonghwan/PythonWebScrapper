import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://www.indeed.com/jobs?q=python&limit=50&vjk=84a541c104b5b24c')

# indeed_result.text = 추출된 html

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

# class 속성이 pagination 인 div element를 추출

pages = pagination.find_all("a")

spans = []

for page in pages:
    spans.append(page.find("span"))

spans = spans[:-1]

print(spans)
