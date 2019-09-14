from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Joseph Francis",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2019"
    },
    {
        "author": "John Doe",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2019"
    }

]

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return "About page"


if __name__ == '__main__':
    app.run(debug=True)
