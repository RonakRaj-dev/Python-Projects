import random
import string
random_alpha = random.choice(string.ascii_lowercase)
print("Random Letter has been guessed it's your time to guess..")
while(True):
    user_input = input("Enter your alphabet: ")
    if user_input == (random_alpha):
        print("Congratulations you have won the game!")
        break
    elif user_input < (random_alpha):
        print("More to go...")
    elif user_input > (random_alpha):
        print("Go a little lower...")
    else:
        print("Sorry You Lose The Game.")
        break
