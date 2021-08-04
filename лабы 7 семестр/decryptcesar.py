from frequency import generate_list_for_frequency_analyse
from CaesarCipher import text_caesar, decrypt_text_caesar
from requests import get


def generate_notepad_from_two_lists(lst1: list, lst2: list) -> dict:
    return {k: v for v, k in zip(lst1, lst2)}


T = get('https://www.weblitera.com/book/?id=19&lng=1&ch=7&l=ru').text
E = text_caesar(T, 1)
lst = generate_list_for_frequency_analyse()[0]
#print(lst)
lst_encrypt = [x for x in text_caesar(lst, shift=1)]
#print(lst_encrypt)

'''shablon = []

for i, v in enumerate(lst_encrypt):
    
    #lst_encrypt[i] = lst[i]
    shablon.append(lst[i])

#print(shablon)
#print(lst_encrypt)'''
D = generate_notepad_from_two_lists(lst_encrypt, shablon)


for key, value in D.items():

    
    if key == 'e':
        
        KEY = ord(key)
        VALUE = ord(value)


print(KEY, VALUE)

shift = VALUE - KEY
print(shift)





'''N = ''

for i in T:
    
    try:
        N += generate_notepad_from_two_lists(shablon, lst_encrypt)[i]
    except:
        pass
'''
print(decrypt_text_caesar(E, shift))
#print(N)


