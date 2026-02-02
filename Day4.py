import random

listOfNames = ["Alice", "Bob", "Charlie"]
randomint = random.randint(0, 3)
print(listOfNames[randomint-1])
# if randomint == 0:
#     print(listOfNames[0])
# elif randomint == 1:
#     print(listOfNames[1])
# elif randomint == 2:
#     print(listOfNames[2])


print(random.choice(listOfNames))
#print("Hello, World!")

useraction=input("Enter your choice (Rock, Paper, Scissors): ")
listofactions=["Rock","Paper","Scissors"]
print("I picked "+random.choice(listofactions))

if random.choice(listofactions)=="Rock" and useraction=="Scissors":
    print("Rock crushes Scissors. You lose!")
elif random.choice(listofactions)=="Scissors" and useraction=="Paper":
    print("Scissors cut Paper. You lose!")
elif random.choice(listofactions)=="Paper" and useraction=="Rock":
    print("Paper covers Rock. You lose!")
elif random.choice(listofactions)==useraction:
    print("It's a tie!")
else:
    print("You win!")   