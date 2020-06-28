from flask import Flask, render_template, session
import country
import flag
import others

app = Flask(__name__)
app.secret_key = '!#$*G)@#)$(F#%@#)O!_#!FO#RG$%H@'


@app.route('/', methods=['POST', 'GET'])
def home():
    session['number_of_question'] = 1
    session['correct_answers'] = 0
    return render_template('home.html')


@app.route('/country_quiz', methods=['POST', 'GET'])
def country_quiz():
    return country.quiz()


@app.route('/next_country_question', methods=['POST'])
def next_country_question():
    return country.question()


@app.route('/flag_quiz', methods=['POST', 'GET'])
def flag_quiz():
    return flag.quiz()


@app.route('/next_flag_question', methods=['POST'])
def next_flag_question():
    return flag.question()


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/about')
def about():
    session['number_of_question'] = 1
    session['correct_answers'] = 0
    return render_template('about.html')


@app.route('/random_country')
def random_country():
    return others.random_country()


@app.route('/list')
def draw_list():
    return others.country_list()


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    return others.settings()


if __name__ == '__main__':
    app.run(debug=False)
