from http.client import responses

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-films.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"



# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)





# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewer_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    reviewer = relationship("User", back_populates="movies")
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String, nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    email:Mapped[str] = mapped_column(String(100), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))
    movies = relationship("Movie", back_populates="reviewer")
    # CREATE DB

with app.app_context():
    db.create_all()


@app.route("/login",methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        result = db.session.execute(db.select(User).where(User.email == request.form.get("email")))
        user = result.scalar()

        #Email does not exist
        if not user:
            flash("That email does not exist, please try again.","login-error")
            # return render_template("all-movies.html")

        #Password does not exist

        elif not check_password_hash(user.password,password):
            flash('Password incorrect, please try again.',"login-error")
            # return render_template("all-movies.html")

        else:
            login_user(user)
            return redirect(url_for("all_movies"))

    return redirect(url_for("home"))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        if request.form.get("password") == request.form.get("confirm-password"):
            hash_and_salted_password = generate_password_hash(
                request.form.get("password"),
                method='pbkdf2:sha256',
                salt_length=8
            )

            new_user = User(
                email = request.form.get("email"),
                name = request.form.get("name"),
                password = hash_and_salted_password
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("all_movies", current_user=current_user))
    return render_template(url_for("all_movies", current_user=current_user))


@app.route("/")
def     home():
    return render_template("index.html")
@app.route("/all-movies")
@login_required
def all_movies():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("all-movies.html", movies=movies)



class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done", render_kw={"class": "btn-signup", "id": "addButton"})


@app.route("/edit" , methods = ["POST" , "GET"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('all_movies'))
    return render_template("edit.html", form=form, movie = movie_to_update)

@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    selected_movie = db.session.get(Movie, movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('all_movies'))



class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie",render_kw={"class": "btn-signup"})



@app.route('/add', methods=["GET", "POST"])
@login_required
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": "c1da5421745044499c12a47565f7662f", "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
@login_required
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": "c1da5421745044499c12a47565f7662f"})
        data = response.json()

        existing_movie = db.session.execute(
            db.select(Movie).where(Movie.title == data["title"], Movie.reviewer_id == current_user.id)
        ).scalar()

        if existing_movie:
            flash("This movie is already in your list!", "movies-error")
            return redirect(url_for("all_movies"))  # Redirectează înapoi la all-movies.html


        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            rating=0,
            ranking=data["popularity"],
            review="Write some",
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            reviewer_id=current_user.id
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True,port= 8081)
