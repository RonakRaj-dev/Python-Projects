import random
random_number = int(random.randrange(0,100))
print("Random Number has been guessed it's your time to guess..")
while(True):
    user_input = int(input("Enter your number: "))
    if user_input == (random_number):
        print("Congratulations you have won the game!")
        break
    elif user_input < (random_number):
        print("Your number is less than the guess number.")
    elif user_input > (random_number):
        print("Your number is greater than the guess number.")
    else:
        print("Sorry You Lose The Game.")
        break
