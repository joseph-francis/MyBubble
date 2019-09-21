from flask import render_template, flash, redirect, url_for
from mybubble import app
from mybubble.registration_form import RegistrationForm, LoginForm

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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "josephfrancis100@gmail.com" and form.password.data == "dec131997":
            flash("You have logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful", "danger")

    return render_template("login.html", title="Login", form=form)