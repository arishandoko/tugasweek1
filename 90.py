# Exercise 90
# Write a function named get_book_author that takes in a dictionary (the above declared book variable) and returns the author's name

book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}

def get_book_author(book):
  return book.get('author')
assert get_book_author(book) == "Frances Buontempo"
print("Exercise 90 is complete.")
