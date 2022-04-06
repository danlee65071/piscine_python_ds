#!hcharlsi/bin/python
import requests
from bs4 import BeautifulSoup
import sys
import time


def financial():
    if len(sys.argv) != 3:
        return
    url = f'https://www.finance.yahoo.com/quote/{sys.argv[1]}/financials'
    resp = requests.get(url, headers={'User-Agent': 'Custom'})
    bs = BeautifulSoup(resp.text, 'html.parser')
    title = bs.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticker')
    tags = bs.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if sys.argv[2] not in breakdowns:
        raise Exception('Not found breakdown')
    time.sleep(5)
    return tuple(t.get_text() for t in tags[breakdowns.index(sys.argv[2])].find_all('span'))


if __name__ == '__main__':
    print(financial())
