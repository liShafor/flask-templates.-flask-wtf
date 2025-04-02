from flask import Flask, render_template


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
