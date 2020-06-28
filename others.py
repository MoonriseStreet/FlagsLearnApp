from flask import render_template, request, session
import random


def country_list():
    f = open('data.txt', 'r')
    lines = f.readlines()
    f.close()
    countries = []
    flags = []
    for line in lines:
        countries.append(line.split('\t')[1])
        flags.append(line.split('\t')[2])
    return render_template('list_of_countries.html', countries=countries,
                           flags=flags)


def random_country():
    f = open('data.txt', 'r')
    line = f.readlines()[random.randrange(202)]
    f.close()
    country = line.split('\t')[1]
    flag = line.split('\t')[2]
    return render_template('random_country.html', country=country, flag=flag)


def settings():
    session['number_of_question'] = 1
    session['correct_answers'] = 0
    answer = request.form.to_dict()
    if answer:
        answer = request.form.to_dict()
        for key in answer.keys():
            session['level'] = int(key)
    return render_template('/settings.html')
