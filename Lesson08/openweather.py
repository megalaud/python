
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import requests
import gzip
import json
import os
import sqlite3
import datetime



class Cities:
    city_file = 'city.list.json.gz'
    url = f'http://bulk.openweathermap.org/sample/{city_file}'

    def check_file(self):
        if not os.path.isfile(self.city_file):
            self.load_file()

    def load_file(self):
        response = requests.get(self.url)
        with open(self.city_file, 'wb') as zip:
            zip.write(response.content)

    def get_city_data(self, cityname):
        self.check_file()
        with gzip.open(self.city_file, 'r') as zip:
            data = json.loads(zip.read())
        return [x for x in data if x['name']==cityname]    

    def get_countries(self):
        self.check_file()
        with gzip.open(self.city_file, 'r') as zip:
            data = json.loads(zip.read())
        return sorted(set([x['country'] for x in data])) 

class Weather:
    db_filename='weather.db'
    def __init__(self):
        self.check_db_file()
        
    def check_db_file(self):
        if not os.path.isfile(self.db_filename):
            conn = sqlite3.connect(self.db_filename)
            try:
                conn.execute("""
                create table CITY_WEATHER (
                CITY_ID        INTEGER primary key,
                CITY        VARCHAR(255),
                DATE        DATE,
                TEMPERATURE  INTEGER,
                WEATHER_ID   INTEGER );
                """)
            except:
                pass
            conn.close()

    def check_data_exist(self, city_id):
        rows = self.select_data(city_id)
        return len(rows) != 0
            
    def execute_command(self, command, commit=False):
        with sqlite3.connect(self.db_filename) as conn:
            answer = list(conn.cursor().execute(command))
            if commit:
                conn.commit()
        return answer
    
    def select_data(self,city_id):
        command = f'SELECT * FROM CITY_WEATHER WHERE CITY_ID={city_id}'
        return self.execute_command(command, False)


    def set_data(self,data):
        if self.check_data_exist(data[0]):
            command = f'UPDATE CITY_WEATHER SET TEMPERATURE="{data[3]}", DATE="{data[2]}"' \
                    f' WHERE city_id="{data[0]}"'
        else:
            values = map(lambda x: f'"{str(x)}"', data)
            command = f'INSERT INTO CITY_WEATHER(CITY_ID,CITY,DATE,TEMPERATURE,WEATHER_ID)' \
                      f' VALUES({",".join(values)})'
        self.execute_command(command, True)        


class OpenApi:
    id_file = 'app.id'
    url = r'http://api.openweathermap.org/data/2.5/weather?'

    def __init__(self):
        with open(self.id_file, 'r') as file:
            self.appid = file.read()

    def get_data(self, city_id):
        request = f'{self.url}id={city_id}&appid={self.appid}&units=metric'
        response = requests.get(request)
        if response.status_code == 200:
            return json.loads(response.content)
        return None


def search_city(string):
    print('Ищем город по файлу')
    cities = Cities()
    result = cities.get_city_data(string)
    if len(result) == 0:
        print('Город {} не найден в списке'.format(string))
        return None
    if len(result) > 1:
        print('\n'.join(['{}. {} {} {}'.format(i,x['name'],x['country'],x['coord'])  for i, x in enumerate(result)]))
        index = int(input('Выберите индекс нужного города:\n'))
        return result[index]
    return result[0]

def get_json_data(city_json):
    api = OpenApi()
    json_data = api.get_data(city_json['id'])
    if not json_data:
        print('Сервер не отвечает')
        return None

    if json_data['cod'] != 200:
        print(json_data['message'])
        return None
    print('Данные о погоде получены')
    return json_data


def update_db(json_data):
    # Add/update data in sql db
    print('Обновляем БД')
    weather = Weather()
    dt=datetime.datetime.now()
    weather.set_data([json_data['id'],
                      json_data['name'],
                      dt.strftime('%Y-%m-%d'),
                      json_data['main']['temp'],
                      json_data['weather'][0]['id']])
    print('БД обновлена')


def main():
    print('Введите город:')
    city = input()
    city_json = search_city(city)
    if city_json:
        json_data = get_json_data(city_json)
        if json_data:
            update_db(json_data)

if __name__ == '__main__':
    main()



