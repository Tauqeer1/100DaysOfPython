from flask import Flask
import random

app = Flask(__name__)

global random_number

@app.route('/')
def index():
    global random_number
    random_number = random.randint(0, 9)
    # print(random_number)
    return ('<p>Guess a number between 0 and 9</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />')

@app.route('/guess/<int:number>')
def guess(number):
    # random_number = random.randint(0, 9)
    if number < random_number:
        message = f"{number} is too low"
    elif number > random_number:
        message = f"{number} is too high"
    else:
        message = f"{number} is just right"
    return message

if __name__ == '__main__':
    app.run(debug=True)