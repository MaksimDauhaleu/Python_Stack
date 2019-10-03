from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("*"*80)
    print("In the Hello function")
    return render_template('playground.html')


@app.route("/threeBlocks")
def hello_person():
    print("*"*80)
    print("In the person function")
    return render_template('playground1.html')


if __name__=="__main__":
    app.run(debug=True)

