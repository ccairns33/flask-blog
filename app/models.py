from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# DB MODELS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    # post attribute has a relationship to the Post Model
    # backref allows us to use author attr to get the posts 
    # lazy: aqlalchemy will load data as necessary in one go

    # how our object is printed when we print()
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow) #pass in without (), so it doesn't set default to our current time
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # id of the user who authored the post, ForeignKey is referencing the table and column name of user.id

    # how our object is printed when we print()
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

