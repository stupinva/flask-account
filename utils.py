#!/usr/bin/python
# -*- coding: UTF-8 -*-

from random import randrange
import re

ru2en_map = ((u'ъб', 'b'),
             (u'ъв', 'v'),
             (u'ъг', 'g'),
             (u'ъд', 'd'),
             (u'ъж', 'zh'),
             (u'ъз', 'z'),
             (u'ък', 'k'),
             (u'ъл', 'l'),
             (u'ъм', 'm'),
             (u'ън', 'n'),
             (u'ъп', 'p'),
             (u'ър', 'r'),
             (u'ъс', 's'),
             (u'ът', 't'),
             (u'ъф', 'f'),
             (u'ъх', 'kh'),
             (u'ъц', 'ts'),
             (u'ъч', 'ch'),
             (u'ъш', 'sh'),
             (u'ъщ', 'sch'),
             (u'ьб', 'b'),
             (u'ьв', 'v'),
             (u'ьг', 'g'),
             (u'ьд', 'd'),
             (u'ьж', 'zh'),
             (u'ьз', 'z'),
             (u'ьк', 'k'),
             (u'ьл', 'l'),
             (u'ьм', 'm'),
             (u'ьн', 'n'),
             (u'ьп', 'p'),
             (u'ьр', 'r'),
             (u'ьс', 's'),
             (u'ьт', 't'),
             (u'ьф', 'f'),
             (u'ьх', 'kh'),
             (u'ьц', 'ts'),
             (u'ьч', 'ch'),
             (u'ьш', 'sh'),
             (u'ьщ', 'sch'),
             (u'ъа', 'ia'),
             (u'ъе', 'ie'),
             (u'ъё', 'ie'),
             (u'ъи', 'ii'),
             (u'ъй', 'ij'),
             (u'ъо', 'io'),
             (u'ъу', 'iu'),
             (u'ъы', 'iy'),
             (u'ъэ', 'ie'),
             (u'ъю', 'iyu'),
             (u'ъя', 'iya'),
             (u'ия', 'ya'),
             (u'ий', 'y'),
             (u'ый', 'y'),
             (u'ая', 'aya'),
             (u'яя', 'aya'),
             (u'ья', 'ya'),
             (u'ьи', 'ii'),
             (u'ью', 'ju'),
             (u'ье', 'ie'),
             (u'ие', 'ie'),
             (u'ь', ''),
             (u'Ия', 'Ya'),
             (u'Ий', 'Y'),
             (u'Ый', 'Y'),
             (u'Ая', 'Aya'),
             (u'Яя', 'Aya'),
             (u'Ие', 'Ie'),
             (u'а', 'a'),
             (u'б', 'b'),
             (u'в', 'v'),
             (u'г', 'g'),
             (u'д', 'd'),
             (u'е', 'e'),
             (u'ё', 'e'),
             (u'ж', 'zh'),
             (u'з', 'z'),
             (u'и', 'i'),
             (u'й', 'j'),
             (u'к', 'k'),
             (u'л', 'l'),
             (u'м', 'm'),
             (u'н', 'n'),
             (u'о', 'o'),
             (u'п', 'p'),
             (u'р', 'r'),
             (u'с', 's'),
             (u'т', 't'),
             (u'у', 'u'),
             (u'ф', 'f'),
             (u'х', 'kh'),
             (u'ц', 'ts'),
             (u'ч', 'ch'),
             (u'ш', 'sh'),
             (u'щ', 'sch'),
             (u'ы', 'y'),
             (u'э', 'e'),
             (u'ю', 'yu'),
             (u'я', 'ya'),
             (u'А', 'A'),
             (u'Б', 'B'),
             (u'В', 'V'),
             (u'Г', 'G'),
             (u'Д', 'D'),
             (u'Е', 'E'),
             (u'Ё', 'E'),
             (u'Ж', 'Zh'),
             (u'З', 'Z'),
             (u'И', 'I'),
             (u'Й', 'J'),
             (u'К', 'K'),
             (u'Л', 'L'),
             (u'М', 'M'),
             (u'Н', 'N'),
             (u'О', 'O'),
             (u'П', 'P'),
             (u'Р', 'R'),
             (u'С', 'S'),
             (u'Т', 'T'),
             (u'У', 'U'),
             (u'Ф', 'F'),
             (u'Х', 'Kh'),
             (u'Ц', 'Ts'),
             (u'Ч', 'Ch'),
             (u'Ш', 'Sh'),
             (u'Щ', 'Sch'),
             (u'Ы', 'Y'),
             (u'Э', 'E'),
             (u'Ю', 'Yu'),
             (u'Я', 'Ya'))

# Транслитерация кириллицы в латиницу
def ru2en(s):
    s = re.sub(ur'ия(\W+|$)', r'ia\1', s, flags = re.U)
    for row in ru2en_map:
        s = s.replace(row[0], row[1])
    return s

# Логин из фамилии и первых букв имени и отчества
def login1(surname, name, patronym, max_len):
    login = ''
    if len(name) > 0: login += name[0]
    if len(patronym) > 0: login += patronym[0]
    surname_length = max([max_len - len(login), len(surname) - len(login)])
    if surname_length < 0: raise exception(u'login1: login_max_length too short!')
    login = surname[0:surname_length] + login
    return login

# Логин из фамилии и порядкового номера
def loginn(surname, num, max_len):
    num = str(num)
    surname_length = max([max_len - len(num), len(surname) - len(num)])
    if surname_length < 0: raise exception(u'login1: login_max_length too short!')
    login = surname[0:surname_length] + num
    return login

# Генератор логинов указанной длинны для указанных ФИО
def logins(surname, name = '', patronym = '', max_len = 12):
    surname = ru2en(surname)
    name = ru2en(name)
    patronym = ru2en(patronym)

    # Если указано имя, используем его для генерации логинов
    if len(name) > 0:
        # Первый логин использует фамилию и первые буквы имени и отчества
        yield login1(surname, name, patronym, max_len)

        # Последующие логины используют фамилию, первую букву имени
        # и одну из последующих букв имени
        used_chars = set()
        if len(patronym) > 0: used_chars.add(patronym[0].lower())
        for char in name[1:].lower():
            if char in used_chars: continue
            used_chars.add(char)
            yield login1(surname, name[0], char, max_len)
    # Если имени нет, используем только фамилию
    else:
        yield login1(surname, '', '', max_len)

    # Если все возможные логины, образованные из фамилии и букв имени и отчества закончились,
    # то генерируем логины, образованные из фамилии и порядкового номера
    i = 1
    while True: 
        yield loginn(surname, i, max_len)
        i += 1

# Генератор логина, порядковый номер которого указан
def login(surname, name = '', patronym = '', n = 0, max_len = 12):
    for login in logins(surname, name, patronym, max_len):
        if n == 0:
            return login
        n -= 1

# Генератор случайного пароля
def random_password(length = 8, chars = 'abcdefhkmnopqrstuvwxyzABCDEFHKMNOPQRSTUVWXYZ0123456789'):
    password = ''
    for i in xrange(0, length):
        password += chars[randrange(0, len(chars))]

    return password
