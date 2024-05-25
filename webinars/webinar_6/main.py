import requests

kirill_inn = '263411857320'
token = '4123saedfasedfsadf4324234f223ddf23'


# nasdaq_url = f"https://api.nasdaq.com/api/quote/{NVDA}/chart?" \
#              f"assetclass={stocks}&" \
#              f"fromdate={}&" \
#              f"todate={}"


class LegalAPI:
    BASE_URL = "https://legal-api.sirotinsky.com"

    def __init__(self, token):
        self.token = token

    def efrsb_traders_all(self):
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_manager_by_inn(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/manager/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    # def efrsb_traders_all(self):
    #     url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
    #     r = requests.get(url)
    #     r.raise_for_status()
    #     return r.json()
    #
    # def efrsb_traders_all(self):
    #     url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
    #     r = requests.get(url)
    #     r.raise_for_status()
    #     return r.json()
    #
    # def efrsb_traders_all(self):
    #     url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
    #     r = requests.get(url)
    #     r.raise_for_status()
    #     return r.json()


def main():
    api = LegalAPI(token)
    traders = api.efrsb_traders_all()
    kirill = api.efrsb_manager_by_inn(kirill_inn)
    print('stop')


if __name__ == '__main__':
    main()
