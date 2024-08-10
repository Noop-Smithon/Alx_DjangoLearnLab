<h1>Updating a Book Instance<h1>
<br>
<h4>from bookshelf.models import Book<h4>
<h4>book = Book.objects.get(title="1984")<h4>
<h4>Terminal Outputs: &ltBook:  Title: 1984, Author: George Orwell, Publication Date: 1949&gt<h4>
<br>
<h4>book.title = "Nineteen Eighty-Four"<h4>
<h4>book.save()<h4>
<h4>Book.objects.all()<h4>
<br>
<h4>Terminal returned: &ltQuerySet [&ltBook:  Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949>]&gt<h4>
