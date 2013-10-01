%rebase('layout.tpl', title=book.title + ' - Library of Webdev')
<div class="header">
  <h1>Library of WebDev</h1>
  <h2>{{book.title}}</h2>
</div>
<div class="books-details">
  <h1>{{book.title}} by {{book.author}}</h1>
  <h2>{{book.year}}</h2>
  <p>{{book.description}}</p>
</div>

<div class='actions'>
  <h3>Checked Out by</h3>
  <ul>
  %for username in book.checked_out:
    <li>{{username}}</li>
  %end
  </ul>
  <form method="POST" action="/books/{{book.id}}/check_out">
    <input type='text' placeholder="Username" name="username" />
    <br />
    <input type="submit" value="Check out Book" />
  </form>

  <form method='POST' action='/books/{{book.id}}'>
    <input type="hidden" name="_method" value="PUT" />
    <input type='text' placeholder="Book Title" name="title" />
    <br />
    <input type='text' placeholder="Book Publication Year" name="year" />
    <br />
    <input type='text' placeholder="Book Author" name="author" />
    <br />
    <textarea type='text' placeholder="Book Description" name="desc">
    </textarea>
    <br />
    <input type="submit" value="Edit Book" />
  </form>

  <form method="GET" action="/books/{{book.id}}">
    <input type="hidden" name="_method" value="DELETE" />
    <input type="submit" value="Delete Book" />
  </form>

  <div class='link'>
    <a href='/books'>GO BACK</a>
  </div>
</div>

<div class='footer'>
  <h6>Copyright 2025, gt: webdev, inc.</h6>
</div>
