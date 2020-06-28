from flask import render_template, request, redirect, url_for, session
from question_generator import new_question
import random


def quiz():
    answer = request.form.to_dict()
    if answer:
        answer = request.form.to_dict()
        right_answer = session.get('correct')
        right = False
        for value in answer.values():
            if value == right_answer:
                right = True
        if right:
            session['correct_answers'] += 1
        return render_template('country_checked.html', right=right,
                               answer=right_answer)

    level = str(session.get('level'))
    countries = new_question(level)
    flags = []
    for country in countries:
        flags.append(country.split('\t')[2])
    correct = random.randrange(100) % 4
    country = countries[correct].split('\t')[1]
    session['correct'] = flags[correct]
    return render_template('country_quiz.html', flags=flags, country=country)


def question():
    if session.get('number_of_question') < 10:
        session['number_of_question'] += 1
        return redirect(url_for('country_quiz'))
    else:
        session['number_of_question'] += 0
        return redirect(url_for('results'))
