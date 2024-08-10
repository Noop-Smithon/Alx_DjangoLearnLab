<h1>Deleting a Book Instance<h1>
<br>
<h4>from bookshelf.models import Book<h4>
<h4>book = Book.objects.get(id="Nineteen Eighty-Four")<h4>
<h4>book.delete()<h4>
<h4>Terminal returned: (1, {'bookshelf.Book': 1})<h4>
<br>
<h4>Book.objects.all()<h4>
<h4>Terminal returned: &ltQuerySet []&gt<h4>
