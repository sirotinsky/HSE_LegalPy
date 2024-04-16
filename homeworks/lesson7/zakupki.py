import time
from random import randint
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://zakupki.gov.ru"

search_url = "https://zakupki.gov.ru/epz/contract/search/results.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "zakupki.gov.ru",
    "Referer": "https://zakupki.gov.ru/epz/contract/search/results.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
}


def construct_url():
    pass


def search_request(page: int, price: int, search_string: str):
    search_url = f"https://zakupki.gov.ru/epz/contract/search/results.html?morphology=on&" \
                 f"searchString={search_string}&" \
                 f"strictEqual=true&" \
                 f"search-filter=Дате+размещения&" \
                 f"fz44=on&" \
                 f"contractStageList_0=on&" \
                 f"contractStageList=0%2C1%2C2%2C3&" \
                 f"contractPriceFrom={price}&" \
                 f"contractCurrencyID=-1&" \
                 f"sortBy=UPDATE_DATE&" \
                 f"pageNumber={page}&" \
                 f"sortDirection=false&" \
                 f"recordsPerPage=_50&" \
                 f"showLotsInfoHidden=false"

    new_url = f"https://zakupki.gov.ru/epz/contract/search/results.html?searchString=%D0%AE%D1%80%D0%B8%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8&strictEqual=true&fz44=on&contractStageList_0=on&contractStageList=0&contractCurrencyID=-1&budgetLevelsIdNameHidden=%7B%7D&sortBy=UPDATE_DATE&pageNumber=1&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false"

    r = requests.get(new_url, headers=headers)
    html = r.text
    return html


def page_request(url):
    r = requests.get(url, headers=headers, allow_redirects=True)
    html = r.text
    return html


def get_all_searched_links():
    result = []
    # for i in range(20):
    html = search_request(1, price=0, search_string="Юридические услуги")
    time.sleep(1)
    print(1)
    soup = BeautifulSoup(html, "html.parser")
    raw_links = [i.find("a")["href"] for i in soup.find_all("div", {"class": "registry-entry__header-mid__number"})]
    links = [BASE_URL + i for i in raw_links]
    result.extend(links)
    return result


def clean_price(raw_price):
    new_string = ""
    for char in raw_price:
        if char.isdigit():
            new_string += char
        if char == ",":
            new_string += "."
    return Decimal(new_string)


def start():
    data = []
    links = get_all_searched_links()
    for link in links:
        print(link)
        html = page_request(link)
        soup = BeautifulSoup(html, "html.parser")
        contract_price = clean_price(soup.find("div", "price").find_all("span")[1].text.strip())
        try:
            contract_subject = [i for i in soup.find_all("span", "section__title") if i.text == 'Предмет контракта'][
                0].find_next("span").text
        except IndexError:
            contract_subject = None
        contract_number = \
            [i for i in soup.find_all("span", "section__title") if i.text == 'Реестровый номер контракта'][0].find_next(
                "span").text
        contract_date_start = soup.find("div", "date mt-auto").find_all("span", "cardMainInfo__content")[0].text.strip()
        contract_date_end = soup.find("div", "date mt-auto").find_all("span", "cardMainInfo__content")[1].text.strip()
        buyer_inn = [i for i in soup.find_all("span", "section__title") if i.text == 'ИНН'][0].find_next("span").text
        data.append(
            (contract_price, contract_subject, contract_number, contract_date_start, contract_date_end, buyer_inn))
        print("stop")
    print(data)


if __name__ == "__main__":
    start()
    pass
