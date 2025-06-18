from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_choice = ""
    computer_choice = ""
    if request.method == "POST":
        choices = ["rock", "paper", "scissors"]
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

    return render_template("rps.html", result=result, user_choice=user_choice, computer_choice=computer_choice)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ this makes it work on Render
    app.run(debug=True, host="0.0.0.0", port=port)

