from flask import Flask, request, render_template, redirect, url_for, json, make_response, abort
from models import books
from LibrForm import LibrForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET", "POST"])
@app.route("/books_index.html/", methods=["GET" , "POST"])
def books_list():
    form = LibrForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("books_list"))

    return render_template("books_index.html", form=form, books=books.all(), error=error)

@app.route("/delete/<int:book_id>", methods=["GET"])
def delete_book(book_id):
    form = LibrForm()
    error = ""
    book = books.delete(book_id-1)
    books.save_all()
    if not book:
        abort(404)

    return render_template("books_index.html", form=form, books=books.all(), error=error) 

@app.route("/update/<int:book_id>/", methods=["GET" , "POST"])
def update_book(book_id):
    book = books.get(book_id-1)
    form = LibrForm(data=book)
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
            books.save_all()
        return redirect(url_for("books_list"))

    return render_template("book_add.html", form=form, book_id=book_id, error=error)

@app.errorhandler(400)
def bad_request(error):
    return make_response(({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)