import random

money = 15

while money >0:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(dice_1, dice_2)

    if dice_1 + dice_2 == 7:
        money += 4
        print("Congrat, you now have", money, "dollars now.")
    elif dice_1 + dice_2 < 7:
        money -= 1
        print("You lost. You now have", money, "dollars")