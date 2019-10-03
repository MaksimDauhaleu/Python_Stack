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
    print
    return render_template('playground1.html')


@app.route("/play/<times>/<color>")
def block_times(times, color):
    print("*"*80)
    print("In the person function")
    print(times)
    return render_template('playground1.html', num_times = int(times), block_color = color)



if __name__=="__main__":
    app.run(debug=True)

