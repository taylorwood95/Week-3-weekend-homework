from flask import render_template, request, redirect
from app import app
from models.book_list import *


@app.route("/books")
def index():
    return render_template("index.html", title="Home", books=books)


@app.route("/add_book", methods=["POST"])
def add_book():
    print(request.form)
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]

    new_book = Book(title, author, genre)

    add_new_book(new_book)
    return render_template("index.html", title="Home", books=books)


@app.route("/remove_book", methods=["POST"])
def remove_book_list():

    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]

    remove_books = Book(title, author, genre)
    remove_book(remove_books)

    return render_template("index.html", title="Home", books=books)


@app.route("/books/<int:book_id>")
def show_book(book_id):
    new_books = return_book(book_id)

    return render_template("index.html", title="Home", books=new_books)
