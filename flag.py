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
        return render_template('flag_checked.html', right=right,
                               answer=right_answer)

    level = str(session.get('level'))
    countries = new_question(level)
    names = []
    for country in countries:
        names.append(country.split('\t')[1])
    correct = random.randrange(100) % 4
    flag = countries[correct].split('\t')[2]
    session['correct'] = names[correct]
    return render_template('flag_quiz.html', names=names, flag=flag)


def question():
    if session.get('number_of_question') < 10:
        session['number_of_question'] += 1
        return redirect(url_for('flag_quiz'))
    else:
        session['number_of_question'] += 0
        return redirect(url_for('results'))
