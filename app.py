import random
from flask import Flask, render_template, request

app = Flask(__name__)
wsgi_app = app.wsgi_app

global number_to_guess
global count_number_of_tries
number_to_guess = random.randint(1, 10)
# Initialise the number of tries the player has made 
count_number_of_tries = 0


@app.route("/", methods=["GET", "POST"])
def guess():
    global number_to_guess, count_number_of_tries
    message = ''
    if request.method == "POST":
        count_number_of_tries += 1
        form = request.form

        # Obtain their initial guess 
        user_guess = int(form["guess"])

        # Check to see if they did guess the correct number 
        if number_to_guess == user_guess:
            message = 'Well done you won!', 'You took', count_number_of_tries, 'goes to complete the game'
            return render_template("gameover.html", message=message)

        elif user_guess < number_to_guess:
            message = 'Your guess was lower than the number'

        else:
            message = 'Your guess was higher than the number'
        if count_number_of_tries == 4:
            message = 'Game Over'
            return render_template("gameover.html", message=message)

    return render_template("guess.html", message=message)


if __name__ == '__main__':
    import os

    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))

    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
