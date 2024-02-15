#Three menu options: Pizza, Caesar Salad, and Chicken Sandwich
#Operational from 11am to 5pm or 6 hrs. One order every 30 minutes or 12 orders per day.

def Restaurant():

    #Welcome Message
    print("Welcome to the Restaurant, today our menu options are Pizza, Caesar Salad, and a Chicken Sandwich")

    #Variables to keep track of total order numbers
    RunningPizza = 0
    RunningCaesar = 0
    RunningChicken = 0

    #Loop which asks for order from user and documents new total for each item (12 times or once every 30 minutes)
    for x in range(12):
        Pizza = int(input("How Many Pizzas would you like to order"))
        Caesar = int(input("How Many Caesar Salads would you like to order"))
        Chicken = int(input("How Many Chicken Sandwiches would you like to order"))
        RunningPizza += Pizza
        RunningChicken += Chicken
        RunningCaesar += Caesar
    #End Display total count of all Menu Items
    print("Today,", RunningPizza, "Pizzas were ordered,", RunningCaesar, "Caesar Salads were ordered, and", RunningChicken, "Chicken Sandwiches were ordered")
Restaurant()
