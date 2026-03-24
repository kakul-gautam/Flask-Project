from flask import Flask, jsonify, request
app = Flask(__name__)
books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe"},
    {"id": 2, "title": "Flask for Beginners", "author": "Jane Smith"}
]

@app.route('/')
def home():
    return jsonify({'message':'Welcome to Home Page!!'})

@app.route("/books")
def all_books():
    all_books = [i for i in books]
    return jsonify(books)
@app.route("/books/<int:book_id>", methods=['GET'])
def one_book(book_id):
    one_book = [book for book in books if book["id"] == book_id]
    if one_book:
        return jsonify(one_book)
    else:
        return jsonify({'Error Message': 'Book Id not found'})
    
@app.route("/books", methods=['POST'])
def add_book():
    new_book = request.get_json()
    existing = [book for book in books if book["id"] == new_book["id"]]
    if existing:
        return jsonify({"error": "Book with this ID already exists"}), 400

    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201
@app.route("/books/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    existing_books = [book for book in books if book["id"] == book_id]

    if not existing_books:
        return jsonify({"error": "Book not found"}), 404

    book = existing_books[0]

    book["title"] = updated_data.get("title", book["title"])
    book["author"] = updated_data.get("author", book["author"])

    return jsonify({"message": "Book updated successfully", "book": book}), 200

@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    global books  # allow modification of global list

    # find the book(s) with matching id using list comprehension
    book_to_delete = [book for book in books if book["id"] == book_id]

    if not book_to_delete:
        return jsonify({"error": "Book not found"}), 404

    # create new list excluding the deleted book
    books = [book for book in books if book["id"] != book_id]

    return jsonify({"message": "Book deleted successfully", "remaining_books": books}), 200



if  __name__ == '__main__':
    app.run(debug=True)    