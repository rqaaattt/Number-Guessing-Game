import random

while True:
    print("Welcome to the Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.\n"
        "You have 5 chances to guess the correct number.\n") 
    print("Please select the difficulty level:\n"
        "1. Easy (10 chances)\n"
        "2. Medium (5 chances)\n"
        "3. Hard (3 chances)\n")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            attempt = 10
            level_is = "Easy"
            break
        elif choice == 2:
            attempt = 5
            level_is = "Medium"
            break
        elif choice == 3:
            attempt = 3
            level_is = "Hard"
            break
        else:
            print('You have a mistake, please, again.')

    print(f"Great! You have selected the {level_is} difficulty level.\n"
        "Let's start the game!\n")
    guess = random.randint(0, 100)
    guess_attempt = None
    n = 0
    while True:
        if guess_attempt == guess:
            print(f'Congratulations! You guessed the correct number in {n} attempts.\n')
            break
        else:
            if attempt==0:
                print(f'Losing, your number was {guess}\n')
                break
            else:
                attempt-=1
            guess_attempt = int(input('Enter your guess: '))
            n+=1
            if guess_attempt<guess:
                print(f"Incorrect! The number is greater than {guess_attempt}\n")
            elif guess_attempt>guess:
                print(f"Incorrect! The number is less than {guess_attempt}\n")

    play_again = input("If you want to play again, write something, but for leaving write 'leave': ")
    if play_again == 'leave':
        break
    else:
        continue