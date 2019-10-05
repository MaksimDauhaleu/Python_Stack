from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key= "maks99080403"


@app.route('/', methods=['POST'])
def main():
    number = request.form['number']
    

    return render_template("game.html", number=number)




if __name__ == "__main__":
    app.run(debug=True)
   