from flask import Flask, render_template, request, session, redirect

import random

app = Flask(__name__)
app.secret_key= "maks"


@app.route('/')
def main():
    if "number"not in session:
        session['number'] = random.randint(1,100)
    return render_template("game.html")

@app.route('/getNumb', methods=['POST'])         
def getNumb():
    print("*"*80)
    print(session["number"])
    print("*"*80)
    print(request.form)
    session["guess"]=int(request.form["guess"])
    return redirect("game.html")



if __name__ == "__main__":
    app.run(debug=True)
   