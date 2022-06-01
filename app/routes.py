from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt

from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
# app folder is a package

posts = [
    {
        'author': 'Carla Cairns',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    # is user is logged in, take them back to the homepage on this route
    if current_user.is_authenticated:
        flash("You are already logged in...", "danger")

        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to login.","success")
        return redirect(url_for("login"))
        # home is the name of the function for that route, not the route itself
    
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    # is user is logged in, take them back to the homepage on this route
    if current_user.is_authenticated:
        flash("You are already logged in...", "danger")

        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # if user exsists and password matches with the database, then log user in
            # remeber will be a true or false
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # after login with no other params, redirect to home page. else rediecxt to next_page
            flash("You are succesfully logged in.", "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check email and password.", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout" )
def logout():
    # already knows which user is logged in
    logout_user()
    flash("You have succesfully logged out.", "success")
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    if not current_user.is_authenticated:
        # flash("Please login to view this page.", "danger")
        return app.login_manager.unauthorized()
    else:
        return render_template("account.html", title="Account")
