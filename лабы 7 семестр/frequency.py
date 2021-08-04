#импорт сторонних модулей
from requests import get
import json


def generate_frequency_dict_and_write_to_file():
    write_dict_to_file(generate_frequency_dict())

#функция записи словаря частот в json объект
def write_dict_to_file(d: dict):
    
    with open('freq.json', 'w', encoding='UTF-8') as file:
        json.dump(d, file, ensure_ascii=False)


#функция генерирования словаря частот 
def generate_frequency_dict(txt: str = None) -> dict:
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #если текст не передан явно, то используются данные с указанных сайтов
    if txt is None:
        
        response = get('https://www.weblitera.com/book/?id=19&lng=1&ch=7&l=ru')
        response1 = get('https://www.weblitera.com/book/?id=19&lng=1&ch=8&l=ru')
        response2 = get('https://www.weblitera.com/book/?id=19&lng=1&ch=12&l=ru')
        txt = response.text + response1.text + response2.text

    arr = [i.lower() for i in txt if i.lower() in alphabet]

    d: dict = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1
    d = d
    return d


def generate_list_for_frequency_analyse(d: dict = None):
    if d is None:
        with open('freq.json', encoding='UTF-8') as file:
            d = json.load(file)
            #print(d)

    return [[element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)], [d]]


if __name__ == '__main__':
    #print(generate_frequency_dict_and_write_to_file())
    print(generate_list_for_frequency_analyse())





    


