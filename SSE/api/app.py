from flask import Flask, request, jsonify
from books import get_books

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Book API</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                color: #555;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Book API!</h1>
        <p>Explore our books <a href="/books">here</a></p>
    </body>
    </html>
    """

@app.route("/books")
def books_route():
    # Retrieve query parameters for 'id' and 'genre'
    book_id = request.args.get('id')
    genre = request.args.get('genre')

    # Call get_books with the parameters to filter the books accordingly
    filtered_books = get_books(book_id=book_id, genre=genre)
    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
