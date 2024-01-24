import random

someWords = '''omm aliva pikun pritam pratikshya pratyasa parativa rakesh rojalin ronak rohit saroj roshni sandeep sreeja subham sushant smurti swati shurti saswati swagat srijan suraj shaktiman soumya
swadhin sonali sasmita subhasini purbasa sambit sourav srikant santanu ritesh'''

names = someWords.split(' ')
name = random.choice(names)

chance = len(name) + 2
ch = 0

# Initialize a list to store user's correct guesses
correct_guesses = ['_'] * len(name)

while ch != chance:
    # Display the current state of correct guesses
    print(' '.join(correct_guesses))
    user_guess = input("Guess a letter: ")

    # Check if the guessed letter is in the name
    if user_guess in name:
        # Update correct_guesses with the guessed letter at the correct positions
        for i in range(len(name)):
            if name[i] == user_guess:
                correct_guesses[i] = user_guess

        # Check if the entire name has been guessed
        if ''.join(correct_guesses) == name:
            print('Congratulations! You guessed the name:', name)
            break
    else:
        print('Wrong')
        print("You have", chance - ch - 1, "chances left")
    
    ch += 1

if ch == chance:
    print("Sorry, you've run out of chances. The correct answer was:", name)
else:
    print('You guessed the name in', ch + 1, 'attempts')