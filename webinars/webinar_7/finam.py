import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup


class CBRParser:
    BASE_URL = "https://www.finam.ru/"

    def __init__(self):
        self.soup = None

    def get_finam_soup(self) -> BeautifulSoup:
        headers = {
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "Accept-Encoding": 'gzip, deflate, br, zstd',
            "Accept-Language": 'en-US,en;q=0.9',
            "Cache-Control": 'max-age=0',
            "Connection": 'keep-alive',
            "Cookie": 'spid=1716034427316_d84213e59312284cac73c145c07b4480_ij7ua47dkvh797ij; spsc=1716034427316_54620d406913d6e961a08a7f7eae35ae_2dc4c47e5beb4aae25be080fa9d16c8093e7e989cef732b63b8bada59af3d7da; srv_id=ae728f13e40892822b53df39694f66af; tmr_lvid=d45c9785040a8e21a26447fa37727ec3; tmr_lvidTS=1716034427677; _gcl_au=1.1.434186915.1716034428; _ga=GA1.1.1527632047.1716034428; segmentsUserId=bb171825-1449-9efd-7497-f9eb23bd8931; segmentsData=puid1=; _ym_uid=1716034428313960007; _ym_d=1716034428; ClientTimezoneOffset=180; ASPSESSIONIDCSSQDBSS=FAEHLFOBJPHDPFFBKIAGEEPH; refreshPage=true; selectedAgency=1; _ym_isad=2; _ym_visorc=b; _pk_id.19.2ab2=ed3c508162169d44.1716034429.; _pk_ses.19.2ab2=1; offfyUserId=1716034239381-0160-179c13048851; displayResolution=desktop; _ga_P7V3S6WS35=GS1.1.1716034427.1.1.1716034502.0.0.0; tmr_detect=0%7C1716034504332',
            "Host": 'www.finam.ru',
            "Referer": 'https://www.finam.ru/',
            "Sec-Fetch-Dest": 'document',
            "Sec-Fetch-Mode": 'navigate',
            "Sec-Fetch-Site": 'same-origin',
            "Upgrade-Insecure-Requests": '1',
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": '"macOS"',

        }
        url = f"{self.BASE_URL}"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    @staticmethod
    def parse_finam_data(soup: BeautifulSoup):
        data = {}
        main_div = soup.find('div', {'class': 'HomeDesktop__newsListContainer--13P'})
        news_divs = main_div.find_all('div', {'class': 'Item__newsBlock--31I Item__newsWithImage--VDV'})
        news_titles = [i.find('p') for i in news_divs]
        return data

    def start(self):
        cbr_soup = self.get_finam_soup()
        parsed_data = self.parse_finam_data(cbr_soup)
        print(parsed_data)


def main():
    parser = CBRParser()
    parser.start()


if __name__ == '__main__':
    main()
