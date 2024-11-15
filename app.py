
from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def random_number():
    number = random.randint(1, 6)
    return f"<h1>Your random number is: {number}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
