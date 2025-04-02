from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<name>')
@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
