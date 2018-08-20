import requests
import re
from bs4 import BeautifulSoup


def require(requirement, error_message):
    if requirement == False:
        raise ValueError(error_message)


def is_yes_no_value(value):
    return value in ['ДА', 'НЕ', '-']


def validate_heating(value):
    return is_yes_no_value(value) or value == 'Лок.отопл.'


def validate_building_material(material):
    return material.upper() in ['ТУХЛА', 'ЕПК', 'ПАНЕЛ', 'ГРЕДОРЕД', 'ПК']


def validate_floor(floor):
    return floor.isdigit() or floor.strip().upper() == 'ПАРТЕР'


class Estate:
    def __init__(self, price, currency, square_meters, floor, max_floor, phone, tec, building_material, description, url, estate_id, build_year, estate_type, town, neighb):
        self.price = price
        self.currency = currency
        self.square_meters = square_meters
        self.floor = floor
        self.max_floor = max_floor
        self.phone = phone
        self.tec = tec
        self.building_material = building_material
        self.description = description
        self.url = url
        self.estate_id = estate_id
        self.build_year = build_year
        self.estate_type = estate_type
        self.town = town
        self.neighb = neighb

    def __repr__(self):
        return "price={}, currency={}, square_meters={}, floor={}, max_floor={}, phone={}, tec={}, building_material={}, " \
               "description={}, url={}, estate_id={}, build_year={}, estate_type={}, town={}, neighb={}".format(
            self.price, self.currency, self.square_meters, self.floor, self.max_floor, self.phone, self.tec, self.building_material, self.description[:20], self.url, self.estate_id, self.build_year, self.estate_type, self.town, self.neighb
        )


def scrape_estate(link):
    r = requests.get(link)
    r.encoding = 'windows-1251'
    bs = BeautifulSoup(r.text, 'html.parser')
    table_info = bs.find_all('table')[4]
    try:
        price, currency = bs.find('span', {'id': 'cena'}).get_text().split(' ')
    except AttributeError:
        print('Invalid property')
        return None
    require(price.isdigit(), 'Price must be a number, found {}'.format(price))
    require(len(currency) == 3, 'Invalid currency value, found {}'.format(currency))


    detailed_info_table = table_info.find_all('table')[3]
    square_meters = detailed_info_table.find_all('td')[1].get_text().split(' ')[0]
    require(square_meters.isdigit(), 'Square meters is not number, found {}'.format(square_meters))

    floor_node = detailed_info_table.find_all('td')[4].get_text()
    floor = floor_node.split('-')[0].split(' ')[0]
    require(validate_floor(floor), 'Floor is not valid, found {}'.format(floor))

    max_floor = None
    floor_info =  floor_node.split(' от ')
    if len(floor_info) == 2:
        max_floor = floor_info[1]

    phone = detailed_info_table.find_all('td')[6].get_text()
    require(is_yes_no_value(phone), 'phone is not yes/no, found {}'.format(phone))

    tec = detailed_info_table.find_all('td')[8].get_text()
    require(validate_heating(tec), 'tec is not valid, found {}'.format(tec))

    building_information = detailed_info_table.find_all('td')[10].get_text().split(',')
    building_material = building_information[0]
    require(validate_building_material(building_material),
            'invalid building_material, found {}'.format(building_material))

    build_year = None
    if len(building_information) > 1:
        build_year = re.sub('\D', '', building_information[1])


    # TODO: Add checks of labels

    description = bs.find('div', {'id': 'description_div'}).get_text()
    url = bs.find('input', {'class': 'w340'}).get('value')
    estate_id = url.split('/')[-1]

    estate_info_node = table_info.find('tr', recursive=False).find_all('td', recursive=False)[2]
    estate_type = estate_info_node.find('span').get_text()
    town, neighb = estate_info_node.find_all('span', recursive=False)[1].get_text().split(',')

    # print('price', price)
    # print('currency', currency)
    # print('square_meters', square_meters)
    # print('floor', floor)
    # print('max_floor', max_floor)
    # print('phone', phone)
    # print('tec', tec)
    # print('building_material', building_material)
    # print('text', description)
    # print('url', url)
    # print('id', estate_id)
    # print('build_year', build_year)
    # print('estate_type', estate_type)
    # print('town', town)
    # print('neighb', neighb)
    return Estate(price, currency, square_meters, floor, max_floor, phone, tec, building_material, description, url, estate_id, build_year, estate_type, town, neighb)


def test_single():
    res = scrape_estate('https://www.imot.bg/1c152475812917029')
    print(res)


def batch_test():
    validate_estates = ['https://www.imot.bg/1c152475812917029', 'https://www.imot.bg/1b152706683086429',
                        'https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1e152121570995803',
                        'https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1c151969701374315&slink=3xjeef&f1=1',
                        'https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1c153295081281418&slink=3xjeef&f1=1',
                        'https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1c153310031733621&slink=3xjeef&f1=1']
    for estate in validate_estates:
        print(scrape_estate(estate))


# batch_test()
