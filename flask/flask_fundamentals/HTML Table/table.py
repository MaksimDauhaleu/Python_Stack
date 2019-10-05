from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("*"*80)
    print("In the Hello function")
    return render_template('table.html')


@app.route('/user')
def render_lists():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("table.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)




from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "Durantula"

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/postRouteToMatchInServer', methods=['POST'])
def process():
    print("*"*80)
    print(request.form['postDataFromFormObjectBook'])
    print(request.form['postDataFromFormObjectAuthor'])

    book = request.form['postDataFromFormObjectBook']
    author = request.form['postDataFromFormObjectAuthor']

    print(book)
    print(author)

    return render_template('show.html', book=book, author=author)

if __name__ == "__main__":
    app.run(debug=True)