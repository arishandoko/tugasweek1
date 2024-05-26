shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}

# Exercise 98
# Write a function named total_number_of_items that takes in the shopping cart as input and returns the total number all item quantities.
# This should return the sum of all of the quantities from each item type
def total_number_of_items(cart):
    total_quantity = 0
    for item in cart['items']:
        total_quantity += item['quantity']
    return total_quantity
assert total_number_of_items(shopping_cart) == 17
print("Exercise 98 is complete.")
