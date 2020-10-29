import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&vjk=84a541c104b5b24c"


def extract_indeed_pages():
    result = requests.get(URL)

    # indeed_result.text = 추출된 html

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    # class 속성이 pagination 인 div element를 추출

    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
