from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()