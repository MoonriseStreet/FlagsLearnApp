import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='...',
                             password='...',
                             db='...',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:


    sql = '''SELECT name FROM Countries;'''

    cursor.execute(sql)
    countries = cursor.fetchall()

    sql_true = '''INSERT INTO Complexity (level) VALUES (TRUE)'''
    sql_false = '''INSERT INTO Complexity (level) VALUES (FALSE)'''
    for country in countries:
        print('Is ' + country['name'] + ' complex?')
        cursor.execute(sql_true if int(input()) else sql_false)
        connection.commit()
