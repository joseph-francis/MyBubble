from flask import Flask, render_template
from app_models.registration_form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ce3d6168915c2a48dcee679cbe2ac49a"

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
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
