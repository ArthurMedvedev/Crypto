from flask import Flask, render_template, request


App = Flask(__name__)

@App.route('/', methods=['GET', 'POST'])
def main():
    #Основная логика
    def Caesar(char):
        SYMBOL = 'ABCDEFGHLIKLMNOPQRSTUVWXYZabcdefghliklmnopqrstuvwxyz1234567890 '
        key = 13
        Cryptotext = ''
        for symbol in SYMBOL:
            if symbol in SYMBOL:
                currentindex = SYMBOL.find(symbol)
                cryptoindex = currentindex + key
<<<<<<< HEAD
            if cryptoindex >= len(SYMBOL) - 1:
                cryptoindex -= len(SYMBOL)
            Cryptotext += SYMBOL[cryptoindex]
            print(cryptoindex)
=======
                if cryptoindex >= len(SYMBOL) - 1:
                    cryptoindex -= len(SYMBOL)

                    Cryptotext += SYMBOL[cryptoindex]
        print(Cryptotext)
>>>>>>> 26c28b5cce822b619b69946e3cb5281e196b95c3
        #return Cryptotext

                
    if request.method == 'POST':
        char = request.form['find']
        print(Caesar(char))
    return render_template(template_name_or_list="index.html")

if __name__ == '__main__':
    App.run(host='localhost', port=8000)


