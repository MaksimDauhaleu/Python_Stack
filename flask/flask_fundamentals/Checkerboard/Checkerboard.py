from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Checkerboard():
    print("*" * 80)
    print("In the Checker function")
    return render_template('Checkerboard.html')


@app.route('/<num>')
def times(num):
    print("*" * 80)
    print("In the times function")
    return render_template('Checkerboard.html', x = int(num))

if __name__=="__main__":
    app.run(debug=True)