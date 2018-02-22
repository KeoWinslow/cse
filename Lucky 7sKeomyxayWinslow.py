import random
# This is Lucky 7s
# This is a rigged game...
print("Roll the dices to get a sum of 7...")
money = 15
rounds = 0
Best_round = 0
High_score = 0

while money > 0:
    if High_score > money:
        High_score = money
        Best_round = money
    money -= 1
    print("You made a bet of one dollar...")
    rounds += 1
    print("You won back one dollar.")
    number1 = (random.randint(1,6))
    number2 = (random.randint(1,6))
    total = number1 + number2
    if total == 7:
       money += 5
       print("You got five additional dollars!")
    print("You won.")
    print("The total is %d" % total)
    if High_score == money:
        print("You've run out of money. You lost!")
        print("Your highest round number was %d and your balance of money was %d" % (Best_round, money))