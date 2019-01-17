import random
import string
win = False
guess_total = 8
db_info = True;
word_bank = ["Please", "jannet", "give", "me", "back", "the", "kids", "screw", "draw", "driver"]
chosen_word = random.choice(word_bank)
list_word = list(chosen_word)
guessed_letters = []
correct_guesses = []
for i in range(0, len(list_word)):
    correct_guesses.append("*")

while guess_total > 0 and win == False:
    print("You have %d guesses left" % guess_total)
    print(correct_guesses)

    letter = input("Guess a letter: ")
    guessed_letters.append(letter)

    # debug info
    if db_info == True:
        print("----DEBUG----")
        print(guessed_letters)
        print(list_word)
        print("-------------")

    for i in range(len(list_word)):
        if list_word[i] in guessed_letters:
            correct_guesses.pop(i)
            correct_guesses.insert(i, list_word[i])

    if letter not in list_word:
        guess_total -= 1

    if correct_guesses == list_word:
        print("You got a victory royale!!!")

        win = True





