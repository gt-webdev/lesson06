from bottle import *

# Configure app
app = Bottle()
app.TEMPLATE_PATH = './views/'

import controllers.books as books_controller

app.mount('/books', books_controller.books_app)

@app.route('/')
def index():
  redirect('/books')

@app.route('/static/:path#.+#', name='static')
def static(path):
  return static_file(path, root='static')

# run app
run(app, host='localhost', port=8080)
