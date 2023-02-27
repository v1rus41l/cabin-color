from flask import Flask, url_for, request, render_template
import json

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('base.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=5)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/queue')
def queue():
    return render_template('queue.html')

@app.route('/training/<prof>', methods=['GET', 'POST'])
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<list>', methods=['GET', 'POST'])
def list_prof(list):
    professions = ['инженер-исследователь',
                   'пилот',
                   'строитель',
                   'экзобиолог',
                   'врач',
                   'инженер по терраформированию',
                   'климатолог',
                   'специалист по радиационной защите',
                   'астрогеолог',
                   'гляциолог',
                   'инженер',
                   'инженер жизнеобеспечения',
                   'метеоролог',
                   'оператор марсохода',
                   'киберинженер',
                   'штурман',
                   'пилот дронов']
    return render_template('professions.html', list=list, professions=professions)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profile = {}
    profile['surname'] = "Whatny"
    profile['name'] = "Pit"
    profile['education'] = "High School"
    profile['profession'] = "штурман"
    profile['sex'] = "Male"
    profile['motivation'] = "None"
    profile['ready'] = "True"
    return render_template('answer.html', title='Анкета', **profile)

@app.route('/login')
def login():
    return render_template('login.html', title='Аварийнный доступ')

@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт',
                  'Энди Уир',
                  'Марк Уотни',
                  'Венката Капур',
                  'Тедди Сандерс',
                  'Шон Бин']
    return render_template('distribution.html', title='По каютам!', astronauts=astronauts)

@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', title='Цвет каюты', sex=sex, age=int(age))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')