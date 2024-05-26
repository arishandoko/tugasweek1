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

# Exercise 99
# Write a function named get_average_item_price that takes in the shopping cart as an input and returns the average of all the item prices.
# Hint - This should determine the total price divided by the number of types of items. This does not account for each item type's quantity.
def get_average_item_price(cart):
    total_price = 0
    num_item_types = len(cart['items'])
    
    for item in cart['items']:
        total_price += item['price']
    
    if num_item_types == 0:
        return 0  # To avoid division by zero error
    
    average_price = total_price / num_item_types
    return average_price

assert get_average_item_price(shopping_cart) == 2.1420000000000003
print("Exercise 99 is complete.")