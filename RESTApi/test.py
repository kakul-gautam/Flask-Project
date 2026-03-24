books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe"},
    {"id": 2, "title": "Flask for Beginners", "author": "Jane Smith"}
]

book_id = 1

result = [book for book in books if book["id"] == book_id]
print(result)