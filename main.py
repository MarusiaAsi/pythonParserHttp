import json
import urllib
import requests
from bs4 import BeautifulSoup


def get_data():
    # Переход по ссылке для получения IP адреса
    url = 'https://2ip.ru/'
    response = requests.get(url)
    html = response.content

    # создаем парсер
    soup = BeautifulSoup(html, 'html.parser')

    # ищем и выводим IP
    ip_address = soup.find('div', class_="ip").find('span')
    print("IP-адрес: " + ip_address.text)

    # Переходим по ссылке вводим API ключ и с помощью найденного ip получаем таймзону
    url = f"https://api-bdc.net/data/timezone-by-ip?ip={ip_address.text}"
    response = requests.get(url, params={'key': 'bdc_f1833abd83544401ba467f24bfd51a11'})
    response = response.json()
    current_timezone = response['ianaTimeId']
    print("Текущая таймзона:", current_timezone)

    # Записываем таймзону в файл
    with open('timezones_data.txt', 'w', encoding='utf-8') as f:
        f.write(current_timezone + '\n')
    f.close()

    # Переходим на гитхаб и для удобного извлечения данных добавляем raw
    url = 'https://gist.githubusercontent.com/salkar/19df1918ee2aed6669e2' + '/raw'

    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    # Конвертируем данные в json
    regions_timezones = json.loads(data)
    regions = []
    # Получаем и записываем список регионов, входящих в полученную таймзону
    for element in regions_timezones:
        if element[1] == current_timezone:
            regions.append(element[0])
            print(element[0])

    # Записываем данные в текстовый файл
    with open("timezones_data.txt", "a", encoding='utf-8') as f:
        f.write(", ".join(regions))
    f.close()


if __name__ == '__main__':
    get_data()
