from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = '!#$*G)@#)$(F#%@#)O!_#!FO#RG$%H@'


@app.route('/')
def home():
    session['number_of_question'] = 1
    session['correct_answers'] = 0
    return render_template('home.html', url=url_for('quiz'))


@app.route('/quiz', methods=['POST', 'GET'])
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
        return render_template('checked.html', right=right, answer=right_answer)

    countries = new_question()
    names = []
    for country in countries:
        names.append(country.split('\t')[1])
    correct = random.randrange(100) % 4
    flag = countries[correct].split('\t')[2]
    session['correct'] = names[correct]
    return render_template('quiz.html', names=names, flag=flag, correct=correct)


@app.route('/nextquestion', methods=['POST'])
def nextquestion():
    if session.get('number_of_question') < 10:
        session['number_of_question'] += 1
        return redirect(url_for('quiz'))
    else:
        session['number_of_question'] += 0
        return redirect(url_for('results'))


@app.route('/results')
def results():
    return render_template('results.html', right=session.get('correct_answers'), url=url_for('home'))


def new_question() -> []:
    random_numbers = []
    while len(random_numbers) < 4:
        number = random.randrange(202)
        while number in random_numbers:
            number = random.randrange(202)
        random_numbers.append(number)
    f = open('data.txt', 'r')
    lines = f.readlines()
    countries = []
    for i in range(4):
        countries.append(lines[random_numbers[i]])
    return countries


if __name__ == '__main__':
    app.run(debug=True)
