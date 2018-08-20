import estate_parser
import requests
import re
from bs4 import BeautifulSoup

def get_links(search_result_page_url):
    r = requests.get(search_result_page_url)
    r.encoding = 'windows-1251'
    bs = BeautifulSoup(r.text, 'html.parser')
    result = None
    try:
        links = bs.find_all('a', attrs={'class':'lnk2'}, href=True)
        result = ['http://' + a['href'].strip('//') for a in links]
        print(result)
        print(len(result))
    except Exception:
        print('Exception ')
    return result


def get_all_result_pages(first_page_link):
    r = requests.get(first_page_link)
    r.encoding = 'windows-1251'
    bs = BeautifulSoup(r.text, 'html.parser')
    pages = int(bs.find('span', {'class': 'pageNumbersInfo'}).get_text().split(' ')[-1])
    if pages == 25:
        print("WARNING: pages = 25, it's possible to miss some estates")
    main_link = first_page_link[:-1]
    result = [main_link + str(page) for page in range(1, pages + 1)]
    print(result)
    return result


# TEST
def test_parse_page():
    lozenets_3room_120_to_140 = "https://www.imot.bg/pcgi/imot.cgi?act=3&slink=3ykm2m&f1=1"
    result = get_links(lozenets_3room_120_to_140)
    for link in result:
        print(estate_parser.scrape_estate(link))


def test_get_all_result_pages():
    simeonovo_3room_link = 'https://www.imot.bg/pcgi/imot.cgi?act=3&slink=3yks1m&f1=3'
    get_all_result_pages(simeonovo_3room_link)


test_get_all_result_pages()