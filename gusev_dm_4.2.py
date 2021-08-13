import xml.dom.minidom
from requests import get, utils

r = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(r.headers)
content = r.content.decode(encoding=encodings)

dom = xml.dom.minidom.parseString(content)
root = dom.getElementsByTagName("ValCurs")[0]
date = f"Текущий курс ЦБ РФ на {root.getAttribute('Date')}г."
currency = dom.getElementsByTagName('Value')


def currency_r():
    name = input('Введите интересующую валюту:')
    for rate in currency:
        chars = rate.getElementsByTagName("CharCode")[0]
        value = rate.getElementsByTagName("Value")[0]
        res = {chars.firstChild.data: value.firstChild.date}
        p = res.get(name)
        if p is not None:
            print(date, ':', p)
            break


if __name__ == '__main__':
    currency_r()
