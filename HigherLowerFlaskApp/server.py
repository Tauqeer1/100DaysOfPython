from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():

    random_number = random.randint(0, 9)


    return ('<p>Guess a number between 0 and 9</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />')


if __name__ == '__main__':
    app.run(debug=True)