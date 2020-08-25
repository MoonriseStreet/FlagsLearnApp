import pymysql.cursors
import urllib.request
import random
import string


def sequence():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


countries = []
pictures = []
capitals = []

f = open('data.txt', 'r')
for line in f:
    if len(line) == 0:
        continue
    countries.append(line.split('\t')[1])
    pictures.append(line.split('\t')[2])
    capitals.append(line.split('\t')[3])

connection = pymysql.connect(host='127.0.0.1',
                             user='...',
                             password='...',
                             db='...',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = '''DROP TABLE Countries;''' # if nessesary, like when u have bugs and run this many times

    cursor.execute(sql)
    connection.commit()

    sql = '''CREATE TABLE Countries ( \
        country_id INT UNSIGNED NOT NULL AUTO_INCREMENT, \
        name VARCHAR(128), \
        picture VARCHAR(128), \
        capital VARCHAR(128), \
        PRIMARY KEY (country_id) \
    );'''

    cursor.execute(sql)
    connection.commit()

    for i in range(len(countries)):
        name = "pic/" + sequence() + ".svg"
        flag = urllib.request.urlopen(pictures[i]).read()
        file = open(name, "wb")
        file.write(flag)
        file.close()
        sql = "INSERT INTO Countries (name, picture, capital) \
             VALUES (%(name)s, %(picture)s, %(capital)s);"

        cursor.execute(sql, {'name': countries[i],
                             'picture': name,
                             'capital': capitals[i]})
        connection.commit()

connection.close()
