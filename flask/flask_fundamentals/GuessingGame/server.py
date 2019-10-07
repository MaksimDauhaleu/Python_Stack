from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'candycane'
@app.route('/')
def index():
    import random
    if 'num' not in session:
        session['num'] = random.randint(1, 100) 
    print(session['num'])
    return render_template('game.html')
@app.route('/guess', methods =['POST'])
def make_guess():
    userguess = request.form['guess']
    if int(userguess) == int(session['num']):
        return render_template('success.html')
    if int(userguess) < int(session['num']):
        return render_template('too_low.html')
    else:
        return render_template('too_high.html')
@app.route('/reset', methods=['POST'])
def reset_user():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

   