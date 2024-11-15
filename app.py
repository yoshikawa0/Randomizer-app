
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def random_number():
    number = random.randint(1, 6)
    return f"<h1>Your random number is: {number}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
