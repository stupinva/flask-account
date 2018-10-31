#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request

import utils

# Создаём новое приложение Flask
app = Flask(__name__, instance_relative_config = True)

# Загружаем настройки приложения из файла конфигурации
app.config.from_pyfile('config.cfg')

# Генерация случайного пароля с использованием
# настроек из файла конфигурации
def random_password(length = app.config['PASS_LENGTH'],
                    chars = app.config['PASS_CHARS']):
    return utils.random_password(length, chars)

# Генерация логина, длина которого указана в файле конфигурации
def login(*args, **kwargs):
    if 'max_len' not in kwargs:
        kwargs['max_len'] = app.config['LOGIN_LENGTH']
    return utils.login(*args, **kwargs)

@app.route('/', methods = ['GET'])
def index_get():
    return render_template('index.html', ilogin = 0,
                                         password = random_password())

@app.route('/', methods = ['POST'])
def index_post():
    surname = request.form.get('surname', '')
    name = request.form.get('name', '')
    patronym = request.form.get('patronym', '')
    password = request.form.get('password', random_password())
    ilogin = int(request.form.get('ilogin', 0))

    # Если попросили предыдущий логин, уменьшаем номер логина на единицу
    if 'prevlogin' in request.form:
        ilogin = max(0, ilogin - 1)
    # Если попросили следующий логин, увеличиваем номер логина на единицу
    elif 'nextlogin' in request.form:
        ilogin = max(0, ilogin + 1)
    # Если попросили другой пароль, генерируем новый пароль
    elif 'nextpassword' in request.form:
        password = random_password()
    # Если попросили очистить форму, чистим
    elif 'reset' in request.form:
        surname = ''
        name = ''
        patronym = ''
        ilogin = 0

    return render_template('index.html', surname = surname,
                                         name = name,
                                         patronym = patronym,
                                         login = login(surname, name, patronym, ilogin),
                                         ilogin = ilogin,
                                         password = password)

# Запуск сервера, если этот модуль был запущен как программа
if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)
