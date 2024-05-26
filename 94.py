# Run this cell in order to have some setup data for the next exercises
books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]

# Exercise 94
# Write a function called highest_price_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the highest priced book.
# Hint: Much like sometimes start functions with a variable set to zero, you may want to create a dictionary with the price set to zero to compare to each dictionary's price in the list
def highest_price_book(books):
    if not books:
        return None  # Return None if the list is empty

    highest_priced_book = None
    highest_price = float('-inf')  # Initialize to negative infinity to ensure any price is higher

    for book in books:
        if 'price' in book and book['price'] > highest_price:
            highest_price = book['price']
            highest_priced_book = book

    return highest_priced_book

assert highest_price_book(books) == {
    "title": "The Visual Display of Quantitative Information",
    "price": 38.00,
    "author": "Edward Tufte"
}

print("Exercise 94 is complete")