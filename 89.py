# Exercise 89
# Write a function named get_price that takes in a dictionary and returns the price
book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}

def get_price(book):
  return book.get('price')
assert get_price(book) == 36.99
print("Exercise 89 is complete.")