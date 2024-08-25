<h1>Retrieving a Book Instance<h1>
<br>
<h4>from bookshelf.models import Book<h4>
<h4>book = Book.objects.get(title="1984")<h4>
<h4>print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")<h4>
<br>
<h4>Terminal returned: Title: 1984, Author: George Orwell, Publication Year: 1949<h4>
