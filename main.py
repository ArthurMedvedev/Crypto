from datetime import datetime
from flask import Flask, render_template, request, session
# Импорты наших скриптов после импортов скаченых пакетов
from app.lib.code import Caesar


# Создание входной точки сервера
app = Flask(__name__)
# Создание сессии
app.permanent_session_lifetime = datetime.timedelta(days=365)
global app_session

app_session = session
# Функция маршрутизации на главную страницу
@App.route('/', methods=['GET', 'POST'])
def index():
    # Отслеживаем отправку формы ПОСТ запросом
    if request.method == 'POST':
        char = request.form['find']
        C = Caesar(char)
    else:
        C = None
    # Возрвращаем .html страницу
    return render_template(
        template_name_or_list="index.html", 
        name='index', 
        code=C
    )


# Функция маршрутизации на страницу входа/регистрации
@App.route('/login/', methods=['GET', 'POST'])
def login():
    # Возрвращаем .html страницу
    return render_template(
        template_name_or_list='login.html', 
        name='login'
    )


# Запуск веб сервера
if __name__ == '__main__':
    App.run(host='localhost', port=8000)


