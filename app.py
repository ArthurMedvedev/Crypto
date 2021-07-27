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