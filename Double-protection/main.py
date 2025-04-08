from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronaut = StringField('ID астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('ID капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/')
@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)


@app.route("/training/<prof>")
def training(prof):
    engineer = any(map(lambda x: x in prof,
                       ("инженер", "строитель")))
    return render_template("prof.html", engineer=engineer)


@app.route("/list_prof/<listt>")
def list_prof(listt):
    lst = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог", "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    return render_template("list_prof.html", list_type=listt, jobs=lst)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    data =\
        {
            'title': 'answer',
            'surname': 'Watny',
            'name': 'Mark',
            'education': 'Выше среднего',
            'profession': 'Штурман марсохода',
            'sex': 'male',
            'motivation': 'Всегда мечтал застрять на Марсе!',
            'ready': True
        }
    return render_template("auto_answer.html", **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
