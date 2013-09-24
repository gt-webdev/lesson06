import random

class Book:
  books = {}

  @staticmethod
  def findById(id):
    return Book.books.get(id, None)


  @staticmethod
  def add(book):
    if isinstance(book, Book):
      Book.books[book.id] = book
      return True
    return False


  @staticmethod
  def find(criteria={}):
    result =[book 
        for id, book in Book.books.items()
        if all(
          [book.__dict__.get(field)==value 
            for field, value in criteria.items()]
          )]
    return result


  @staticmethod
  def genNewId():
    test_id = random.randint(0, 10000)
    while Book.books.get(test_id, None):
      test_id = random.randint(0, 10000)
    return test_id

  @staticmethod
  def clear():
    Book.books = {}


  def __init__(self, title="Harry Potter and Webdev", 
      year=2025, author="Atom", desc="This book is about Webdev!"):
    self.title = title
    self.year = year
    self.author = author
    self.description = desc
    self.id = Book.genNewId()


  def save(self):
    return Book.add(self)


  def delete(self):
    return Book.books.pop(self.id, None)


  def __repr__(self):
    return u'<Book(%i); title=%s, author=%s, year=%i>' % (self.id, self.title,
        self.author, self.year)
