from datetime import date

import requests
from bs4 import BeautifulSoup

url_params = "?" \
             "UniDbQuery.Posted=True&" \
             "UniDbQuery.From=17.09.2013&" \
             "UniDbQuery.To=15.05.2023"


# zakupki_url = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?" \
#               "searchString=%D1%8E%D1%80%D0%B8%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5&" \
#               "morphology=on&" \
#               "search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&" \
#               "pageNumber=1&" \
#               "sortDirection=false&" \
#               "recordsPerPage=_10&" \
#               "showLotsInfoHidden=false&" \
#               "sortBy=UPDATE_DATE&" \
#               "fz44=on&" \
#               "fz223=on&" \
#               "af=on&" \
#               "ca=on&" \
#               "pc=on&" \
#               "pa=on&" \
#               "currencyIdGeneral=-1"

def today_human_date():
    today = date.today().strftime("%d.%m.%Y")
    return today


def get_page():
    url = f"https://www.cbr.ru/hd_base/KeyRate/?" \
          f"UniDbQuery.Posted=True&" \
          f"UniDbQuery.From=17.09.2013&" \
          f"UniDbQuery.To={today_human_date()}"
    r = requests.get(url)

    return r.text


def main():
    html = get_page()
    soup = BeautifulSoup(html, "html.parser")
    raw_data = [i.text for i in soup.find("table", {"class": "data"}).find_all("td")]
    print("stop")
    dates_1 = raw_data[::2]
    rates_1 = raw_data[1::2]
    dates_2 = [data for i, data in enumerate(raw_data) if i % 2 == 0]
    rates_2 = [data for i, data in enumerate(raw_data) if i % 2 != 0]
    data = zip(dates_1, rates_1)


if __name__ == "__main__":
    main()
    pass
