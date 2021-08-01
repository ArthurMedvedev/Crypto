import requests

import json

def generate_frequency_dict():
    
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'


    #создаем запрос по указнной сслыке, выделяем из нее только текстовые значения
    
    response = requests.get('https://www.weblitera.com/book/?id=19&lng=1&ch=1&l=ru')
    responseAdd = requests.get('https://www.weblitera.com/book/?id=19&lng=1&ch=11&l=ru')
    responseAdd1 = requests.get('https://www.weblitera.com/book/?id=19&lng=1&ch=19&l=ru')
    s = response.text + responseAdd.text + responseAdd1.text
    
    #отсекаем лишние символы
    arr = [i.lower() for i in s if i.lower() in alphabet]
    #print(arr[0:1001])

    #создаем словарь, хранящий частоты символов
    frequency_dict = {}

    #цикл компонования словаря частот
    for i in arr:
        
        frequency_dict[i] = frequency_dict.get(i, 0) + 1
        
        '''if i not in frequency_dict:
            frequency_dict[i] = 1
        
        else:
            frequency_dict[i] += 1'''

    #сохранение словаря в json нотации
    with open('freq.json', 'w', encoding='UTF-8') as file:
        
        json.dump(frequency_dict, file, ensure_ascii=False)

    print(frequency_dict)

#функция сортировки
def generate_sort_list():

    with open('freq.json',  encoding='UTF-8') as file:
        
        d = json.load(file)

        return [element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)]
    
    print(d)

generate_frequency_dict()
print(generate_sort_list())

    





    


