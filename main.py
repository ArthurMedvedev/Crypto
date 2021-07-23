from flask import Flask, render_template, request


App = Flask(__name__)

@App.route('/', methods=['GET', 'POST'])
def main():

    #Основная логика
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
        
    if request.method == 'POST':
        char = request.form['find']
        C = Caesar(char)
    else:
        C = None
        
    return render_template(template_name_or_list="index.html", code=C)


@App.route('/voyajer/', methods=['GET', 'POST'])
def voyaj():
    return render_template(template_name_or_list='voyaj.html')


if __name__ == '__main__':
    App.run(host='localhost', port=8000)


