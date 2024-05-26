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

# Exercise 101
# Write a function named most_spent_on_item that takes in the shopping cart as input and returns the dictionary associated with the item that has the highest price*quantity.
# Be sure to do this as programmatically as possible. 
# Hint: Similarly to how we sometimes begin a function with setting a variable to zero, we need a starting place:
# Hint: Consider creating a variable that is a dictionary with the keys "price" and "quantity" both set to 0. You can then compare each item's price and quantity total to the one from "most"
def most_spent_on_item(cart):
    max_spent_item = None
    max_spent_amount = 0
    
    for item in cart['items']:
        total_amount = item['price'] * item['quantity']
        if total_amount > max_spent_amount:
            max_spent_amount = total_amount
            max_spent_item = item
    
    return max_spent_item
assert most_spent_on_item(shopping_cart) == {
    "title": "chocolate",
    "price": 0.75,
    "quantity": 9
}
print("Exercise 101 is complete.")