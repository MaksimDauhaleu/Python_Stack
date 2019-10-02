from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("*" * 80)
    print("In the Hello function")
    return 'Hello World!'


@app.route('/<name>')
def hello_person(name):
    print("*" * 80)
    print("In the Person function")
    print(name)
    return f'{name}!'


@app.route('/say/<name>')
def say(name):
    print("*" * 80)
    print("In the Say function")
    print(name)
    return f'Hi {name}!'


@app.route('/repeat/<num>/<name>')
def print_num(name, num):
    print("*" * 80)
    print("In the print_num function")
    print(name)
    return (name + " ") * int(num)


if __name__ == "__main__":
    app.run(debug=True)
