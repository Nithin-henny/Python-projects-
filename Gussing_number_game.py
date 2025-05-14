import random

number_to_guess=random.randint(1,100)

while True:
    try:
        Guess=int(input("Guss a number between 1 t0 100: "))
        if Guess < number_to_guess:
            print("Too Low!")
        elif Guess > number_to_guess:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number.")
            break            
    except ValueError:
        print('Please entre a valid number')
        