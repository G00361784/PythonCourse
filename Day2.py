# def greet(name):
#     return name

# def length_of_greeting(name):
#     greeting = greet(name)
#     return len(greeting)

# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     print(greet(name))
#     print(f"The length of the greeting is: {length_of_greeting(name)}")
totalBill = float(input("Enter the total bill"))

percentageTip = int(input("Enter the percentage tip"))

splitWays = int(input("Enter the total split"))

print((totalBill+(totalBill*percentageTip/100))/splitWays)