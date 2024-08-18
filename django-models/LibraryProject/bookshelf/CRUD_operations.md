<h1>Creating a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>new_book = Book(title="1984", author="George Orwell", publication_year=1949)<p>
<p>new_book.save()<p>
<br>
'''No output was shown on terminal - signifying a successful creation of the book'''

<h1>Retrieving a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>Book.objects.filter(title="1984", author="George Orwell")<p>
<br>
'''Terminal returned
<QuerySet [<Book:  Title: 1984, Author: George Orwell, Publication Date: 1949>]>'''

<h1>Updating a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>new_book.title = 'Nineteen Eighty-Four'<p>
<p>new_book.save()<p>
<p>Book.objects.all()<p>
<br>
'''Terminal returned
<QuerySet [<Book:  Title: The gods Cry Too, Author: John Doe, Publication Date: 2001>, <Book:  Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949>]>'''

<h1>Deleting a Book Instance<h1>
<br>
<p>from bookshelf.models import Book<p>
<p>Book.objects.filter(title="Nineteen Eighty-Four").delete()<p>
<br>
'''Terminal returned
(1, {'bookshelf.Book': 1})'''
Book.objects.all()
'''Terminal returned
<QuerySet [<Book:  Title: The gods Cry Too, Author: John Doe, Publication Date: 2001>]>'''
