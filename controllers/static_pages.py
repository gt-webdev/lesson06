from bottle import *

@route('/test')
def test():
  return 'testing'


@route('/books')
def listBooks():
  return 'hammer' #Book.find()
