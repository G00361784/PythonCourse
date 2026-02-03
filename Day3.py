size = input("enter the size of the pizza s, m or l:")
pepperoini = input("do you want pepperoini, y or n:")
extraCheese = input("do you want extra cheese y or n:")

#size logic
bill = 0
small = 7
med = 10
large = 13

if size == "s":
    bill = bill + small
elif size == "m":
    bill = bill + med
elif size == "l":
    bill = bill + large
#pepperoini logic
if pepperoini == "y":
    bill = bill + 3
#cheese logic
if extraCheese == "y":
    bill = bill + 4
print(bill)
