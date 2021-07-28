def Caesar(char=None, key = None):
    key=int(key)
    SYMBOL = 'ABCDEFGHLIKLMNOPQRSTUVWXYZabcdefghliklmnopqrstuvwxyz '
    Cryptotext = ''
    if key >= 61 and key <= 71:
        for symbol in char:
            if symbol in SYMBOL:
                currentindex = SYMBOL.find(symbol)
                cryptoindex = currentindex + key
            if cryptoindex >= len(SYMBOL):
                cryptoindex -= len(SYMBOL)
                Cryptotext += SYMBOL[cryptoindex]
        return Cryptotext
    else:
        a = input('введите открытый текст: ')
        return Caesar(char=a, key=input('введите ключ, пренадлежащий отрезку [61;70]: '))
a = input('введите открытый текст: ')
print(Caesar(char=a, key=input('введите корректный ключ: ')))




def decrypt(for_decrypt, arr_decrypt_letters):
    encrypt = []
    arr_encrypt_letters = [' ', 'о', 'а', 'е', 'и', 'т', 'н', 'л',
                           'р', 'с', 'в', 'к', 'м', 'д', 'у', 'п',
                           'б', 'г', 'ы', 'ч', 'ь', 'з', 'я', 'й',
                           'х', 'ж', 'ш', 'ю', 'ф', 'э', 'щ',
                           'ё', 'ц', 'ъ']
    dictionary = dict(zip(arr_decrypt_letters, arr_encrypt_letters))
    for i in for_decrypt:
    encrypt.append(dictionary.get(i))
    for_decrypt = ''.join(encrypt)
    print(for_decrypt)