print("Welcome to PizzaBot!")
print("What size pizza would you like? (small/medium/large)")
size = input("You: ").lower()

if size in ["small", "medium", "large"]:
    print(f"Great! A {size} pizza.")
else:
    print("Sorry, I can only take orders for small, medium, or large pizzas.")
    exit()

print("What toppings do you want? (cheese/pepperoni/veggies)")
topping = input("You: ").lower()

if topping in ["cheese", "pepperoni", "veggies"]:
    print(f"Adding {topping} topping.")
else:
    print("Sorry, we don't have that topping.")
    exit()
print(f"Thank you! Your {size} pizza with {topping} will be ready for pickup.")
print("Enjoy your pizza! 🍕")
