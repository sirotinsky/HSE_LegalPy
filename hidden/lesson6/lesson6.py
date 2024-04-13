from datetime import date, timedelta
import requests

file_url = "https://opendata.fssp.gov.ru/7709576929-tolist/data-20230413-structure-20160729.csv"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "api.nasdaq.com",
    "Origin": "https://www.nasdaq.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
}


from_date = (date.today() - timedelta(days=90)).isoformat()
to_date = (date.today() - timedelta(days=1)).isoformat()
limit = 50


nasdaq_quete = f"https://api.nasdaq.com/api/quote/ZM/historical?" \
               f"assetclass=commodities&" \
               f"fromdate={from_date}&" \
               f"limit={limit}&" \
               f"todate={to_date}"

raw_nasdaq = "https://api.nasdaq.com/api/quote/indices?symbol=indu&symbol=ndx&symbol=comp&symbol=rut&symbol=spx"

zakup_url = "https://zakupki.gov.ru/epz/contract/search/results.html?" \
            "searchString=%D1%8E%D1%80%D0%B8%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8&" \
            "morphology=on&" \
            "search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&" \
            "fz44=on&" \
            "contractStageList_0=on&" \
            "contractStageList_1=on&" \
            "contractStageList_2=on&" \
            "contractStageList_3=on&" \
            "contractStageList=0%2C1%2C2%2C3&" \
            "contractCurrencyID=-1&" \
            "budgetLevelsIdNameHidden=%7B%7D&" \
            "sortBy=UPDATE_DATE&" \
            "pageNumber=1&" \
            "sortDirection=false&" \
            "recordsPerPage=_10&" \
            "showLotsInfoHidden=false"

nasdaq_url = "https://api.nasdaq.com/api/quote/indices?" \
             "symbol=kold&" \
             "symbol=ndx&" \
             "symbol=comp&" \
             "symbol=rut&" \
             "symbol=spx"

def make_a_req(url):
    r = requests.get(url, headers=headers)
    html = r.text
    pass


class SirotinskyAPI:
    BASE_URL = "https://api.sirotinsky.com"
    auth = {
        "username": "HSE_student",
        "password": "123123123"
    }

    def __init__(self):
        self.__get_token()

    def __get_token(self):
        url = f"{self.BASE_URL}/token"
        r = requests.post(url, data=self.auth)
        result = r.json()["access_token"]
        self.token = result

    def __request(self):
        # Перенести HTTP запрос сюда
        pass

    def get_organisation(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/organisation/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_person(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/person/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_trader(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_manager(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/manager/{inn}"
        r = requests.get(url)
        result = r.json()
        return result


def main():
    s_api = SirotinskyAPI()
    org = s_api.get_organisation("7701272485")
    pass


if __name__ == "__main__":
    # main()
    make_a_req(zakup_url)
    print("stop")
