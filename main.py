from flask import Flask, render_template, request
from crypto_lib.app import Caesar

App = Flask(__name__)

@App.route('/', methods=['GET', 'POST'])
def main():

    #Основная логика
        
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


