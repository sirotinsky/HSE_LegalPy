from datetime import date

import requests
from bs4 import BeautifulSoup

url_params = "?" \
             "UniDbQuery.Posted=True&" \
             "UniDbQuery.From=17.09.2013&" \
             "UniDbQuery.To=15.05.2023"


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
    data = list(zip(dates_1, rates_1))


if __name__ == "__main__":
    main()
    pass
