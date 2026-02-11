userInput = input("What would you like? (espresso/latte/cappuccino): ")

currentWater = 300
currentMilk = 200
currentCoffee = 100

coins = 0
def coinsFunction():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    totalCoins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return totalCoins

if userInput == "report":
    print(f"Water: {currentWater}ml")
    print(f"Milk: {currentMilk}ml")
    print(f"Coffee: {currentCoffee}g")


if userInput == "quit":
    print("Goodbye!")
    exit()

if userInput == "espresso":
    coins = coinsFunction()
    while coins < 1.50:
        print("Sorry, that's not enough money. Money refunded.")
        print("Coins Returned: " + str(coins))
        exit()
    if currentWater < 50:
        print("Sorry, not enough water.")
    elif currentCoffee < 18:
        print("Sorry, not enough coffee.")
    else:
        print("Here is your espresso. Enjoy!")
        currentWater -= 50
        currentCoffee -= 18

if userInput == "latte":
    coins = coinsFunction()
    while coins < 2.50:
        print("Sorry, that's not enough money. Money refunded.")
        print("Coins Returned: " + str(coins))
        exit()
    if currentWater < 200:
        print("Sorry, not enough water.")
    elif currentMilk < 150:
        print("Sorry, not enough milk.")
    elif currentCoffee < 24:
        print("Sorry, not enough coffee.")
    else:
        print("Here is your latte. Enjoy!")
        currentWater -= 200
        currentMilk -= 150
        currentCoffee -= 24

if userInput == "cappuccino":
    coins = coinsFunction()
    while coins < 3.00:
        print("Sorry, that's not enough money. Money refunded.")
        print("Coins Returned: " + str(coins))
        exit()
    if currentWater < 250:
        print("Sorry, not enough water.")
    elif currentMilk < 100:
        print("Sorry, not enough milk.")
    elif currentCoffee < 24:
        print("Sorry, not enough coffee.")
    else:
        print("Here is your cappuccino. Enjoy!")
        currentWater -= 250
        currentMilk -= 100
        currentCoffee -= 24