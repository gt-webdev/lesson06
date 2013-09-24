from bottle import *
from models.books import Book

books_app = Bottle()

test = Book(title="Hitchhiker's guide to the Webdev")
test.save()
test2 = Book(title="Lord of the Webdev")
test2.save()
test3 = Book(title="Webdev: the Good Parts")
test3.save()

@books_app.route('/')
def listBooks():
  # DELETE Method Override
  if request.query.get('_method') == "DELETE":
    clear_library()
  return template('books_list', books=Book.find())

@books_app.route('/author/<author_name>')
def showFromAuthor(author_name):
  return template('books_list', books=Book.find({"author":author_name}))

@books_app.route('/year/<pub_year:int>')
def showFromAuthor(pub_year):
  return template('books_list', books=Book.find({"year":pub_year}))

@books_app.route('/<book_id:int>')
def getBook(book_id):
  book = Book.findById(book_id)
  # DELETE Method Override
  if request.query.get('_method') == "DELETE":
    delete_book(book_id)
  if book:
    return template('show_book', book=book)
  abort(404)

@books_app.route('/', method="POST")
def add_book():
  title = request.forms.get("title")
  author = request.forms.get("author")
  year = request.forms.get("year")
  desc = request.forms.get("desc")
  new_book_dict = {}
  if (title):
    new_book_dict["title"] = title
  if (author):
    new_book_dict["author"] = author
  if (year):
    new_book_dict["year"] = int(year)
  if (desc):
    new_book_dict["desc"] = desc
  new_book = Book(**new_book_dict)
  new_book.save()
  redirect('/')

@books_app.route('/', method="DELETE")
def clear_library():
  Book.clear()
  redirect('/')

@books_app.route('/<book_id:int>', method="DELETE")
def delete_book(book_id):
  book = Book.findById(book_id)
  if book:
    book.delete()
    redirect('/')
  abort(404)

@books_app.route('/<book_id:int>/check_out', method="POST")
def check_out(book_id):
  username = request.forms.get("username")
  book = Book.findById(book_id)
  if (username and book):
    book.check_out(username)
    redirect('/books/%i'%book_id)
  if (book):
    abort(403)
  abort(404)

@books_app.route('/<book_id:int>', method=["POST","PUT"])
def edit_book(book_id):
  book = Book.findById(book_id)
  if book:
    title = request.forms.get("title")
    author = request.forms.get("author")
    year = request.forms.get("year")
    desc = request.forms.get("desc")
    new_book_dict = {}
    if (title):
      new_book_dict["title"] = title
    if (author):
      new_book_dict["author"] = author
    if (year):
      new_book_dict["year"] = int(year)
    if (desc):
      new_book_dict["desc"] = desc
    for field, value in new_book_dict.items():
      book.__dict__[field] = value
      book.save()
    redirect('/books/%i' % book_id)
  abort(404)
      

