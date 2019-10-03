from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("*"*80)
    print("In the Hello function")
    return render_template('index.html')


@app.route("/<name>/<times>")
def hello_person(name, times):
    print("*"*80)
    print("In the person function")
    print(name)
    return render_template('name.html', some_name=name, num_times=int(times))


if __name__=="__main__":
    app.run(debug=True)


var = (1, 2, 3, 4)



