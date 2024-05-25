import requests
from bs4 import BeautifulSoup


class CBRParser:
    BASE_URL = "https://cbr.ru"

    def __init__(self):
        self.soup = None

    def get_cbr_page_soup(self, from_date: str, to_date: str) -> BeautifulSoup:
        params = f"?UniDbQuery.Posted=True" \
                 f"&UniDbQuery.From={from_date}" \
                 f"&UniDbQuery.To={to_date}"
        url = f"{self.BASE_URL}/hd_base/KeyRate/{params}"
        r = requests.get(url)
        r.raise_for_status()
        return BeautifulSoup(r.text, 'html.parser')

    def parse_cbr_data(self, soup: BeautifulSoup):
        table_cells = soup.find('table').find_all('td')
        dates = [d.text for i, d in enumerate(table_cells) if i % 2 == 0]
        rates = [d.text for i, d in enumerate(table_cells) if i % 2 != 0]
        return list(zip(dates, rates))

    def start(self):
        cbr_soup = self.get_cbr_page_soup('17.09.2013', '17.05.2024')
        parsed_data = self.parse_cbr_data(cbr_soup)


def main():
    parser = CBRParser()
    parser.start()


if __name__ == '__main__':
    main()
