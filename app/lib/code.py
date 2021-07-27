def Caesar(char):
    SYMBOL = 'ABCDEFGHLIKLMNOPQRSTUVWXYZabcdefghliklmnopqrstuvwxyz1234567890 '
    key = 13
    Cryptotext = ''

    for symbol in char:
        if symbol in SYMBOL:
            currentindex = SYMBOL.find(symbol)
            cryptoindex = currentindex + key
        if cryptoindex >= len(SYMBOL) - 1:
            cryptoindex -= len(SYMBOL)
        Cryptotext += SYMBOL[cryptoindex]
    return Cryptotext