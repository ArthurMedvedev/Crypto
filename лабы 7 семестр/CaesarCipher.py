def Caesar(char=None, key = None):
    key=int(key)
    SYMBOL = 'ABCDEFGHLIKLMNOPQRSTUVWXYZabcdefghliklmnopqrstuvwxyz '
    #key = int(input('введите ключ из отрезка [61;70]: '))
    Cryptotext = ''
    if key >= 61 and key <= 71: 
        for symbol in char:
            if symbol in SYMBOL:
                currentindex = SYMBOL.find(symbol)
                #print(Cryptotext, key)
                cryptoindex = currentindex + key
                #print(cryptoindex)
            if cryptoindex >= len(SYMBOL):
                cryptoindex -= len(SYMBOL)
            Cryptotext += SYMBOL[cryptoindex]
        return Cryptotext
    else:
        a = input('введите открытый текст: ')
        Caesar(char=a, key=input('введите ключ, пренадлежащий отрезку [61;70]: '))
a = input('введите открытый текст: ')
print(Caesar(char=a, key=input('введите корректный ключ: ')))