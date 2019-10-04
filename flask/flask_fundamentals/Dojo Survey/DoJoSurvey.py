from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("survey.html")


from flask import Flask, render_template, request, redirect # added request
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    name_from_form = request.form['name']
    locations_from_form = request.form['locations']
    language_from_form = request.form['language']
    comments_from_form = request.form['comments']
    return render_template("show.html", name=name_from_form, location=locations_from_form
    , language=language_from_form, comments=comments_from_form)






if __name__ == "__main__":
    app.run(debug=True)


