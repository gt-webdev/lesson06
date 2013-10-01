<div>
  <h1>Library of WebDev</h1>
  <h2>Books List</h2>
</div>
<div>
  <ul>
  %for book in books:
    <li>
      <a href="/books/{{book.id}}">
        <p>{{book.title}}</p>
      </a>
    </li>
  %end
  </ul>
</div>
<div>
  <form method='POST' action='/books'>
    <input type='text' placeholder="Book Title" name="title" />
    <br />
    <input type='text' placeholder="Book Publication Year" name="year" />
    <br />
    <input type='text' placeholder="Book Author" name="author" />
    <br />
    <textarea type='text' placeholder="Book Description" name="desc">
    </textarea>
    <br />
    <input type="submit" value="Add Book" />
  </form>
  <form method="GET" action="/books">
    <input type="hidden" name="_method" value="DELETE" />
    <input type="submit" value="Clear Library" />
  </form>
</div>
<div>
  <h6>Copyright 2025, gt: webdev, inc.</h6>
</div>
