def get_books(book_id=None, genre=None):
    filtered_books = []

    if book_id:
        try:
            book_id = int(book_id)  # Ensure that book_id is an integer
            filtered_books = [book for book in books if book['id'] == book_id]
        except ValueError:
            raise ValueError("Invalid book ID")  # Handle case where book_id is not an integer

    elif genre:
        genre = genre.lower()  # Case-insensitive match for genre
        filtered_books = [book for book in books if genre in book['genre'].lower()]

    else:
        filtered_books = books  # No filtering applied, return all books

    return filtered_books

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]
