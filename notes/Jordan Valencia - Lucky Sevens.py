import random

rounds_max_money = 0
money = 15
round = 0
max_money = 15
while money >0:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
  # print(dice_1, dice_2)

    round += 1

    money -= 1

    if dice_1 + dice_2 == 7:
        money += 5
        print("Congrat, you now have", money, "dollars now.")
        if money > max_money:
            max_money = money
            rounds_max_money = round
    elif dice_1 + dice_2 < 7:
        print("You lost. You now have", money, "dollars")
print("you lasted",round,"rounds")
print("you had",max_money,"dollars")
print("You had",rounds_max_money,"rounds with max money")