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

# Exercise 100
# Write a function named get_average_spent_per_item that takes in the shopping cart and returns the average of summing each item's quanties times that item's price.
# Hint: You may need to set an initial total price and total total quantity to zero, then sum up and divide that total price by the total quantity
def get_average_spent_per_item(cart):
    total_price = 0
    total_quantity = 0
    
    for item in cart['items']:
        total_price += item['price'] * item['quantity']
        total_quantity += item['quantity']
    
    if total_quantity == 0:
        return 0  # To avoid division by zero error
    
    average_spent_per_item = total_price / total_quantity
    return average_spent_per_item
assert get_average_spent_per_item(shopping_cart) == 1.333529411764706
print("Exercise 100 is complete.")