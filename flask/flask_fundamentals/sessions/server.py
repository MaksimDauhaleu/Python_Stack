from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = "Durantula"

@app.route("/")
def root():
    if 'count' not in session:
        session['count'] = 1
    else :
        session['count']+=1

    return render_template("firstpage.html", count = session['count'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

@app.route('/addTwo')
def addTwo():
    session['count'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)