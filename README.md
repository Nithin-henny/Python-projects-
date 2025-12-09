🎮 Python Mini Projects Collection

A collection of three beginner-friendly Python console-based games that demonstrate fundamental programming concepts like loops, conditionals, functions, input validation, and Python’s random module.
These projects are perfect for learning logic building and improving Python basics.

📌 Projects Included
1️⃣ Number Guessing Game
📖 Description

The computer randomly selects a number between 1 and 100, and the player must guess it.
The program provides hints like “Too Low!” or “Too High!” until the user guesses correctly.

🧠 Python Logic Used

random.randint(1, 100) to generate the secret number

Infinite while True loop for continuous guessing

Conditionals (if/elif/else) for comparison logic

Error handling using try–except for invalid inputs

✔ Key Features

Validates only integer inputs

Gives directional hints

Ends when correct number is guessed

2️⃣ Dice Rolling Simulator
📖 Description

Simulates rolling two dice.
The user decides whether to roll by entering y/n.
Each roll generates two random numbers between 1 and 6.

🧠 Python Logic Used

random.randint(1, 6) for dice values

Loop runs until user chooses to exit

Lowercasing input to handle case variations

Clean output like:
(3, 5)

✔ Key Features

Realistic dice roll simulation

Simple user interaction

Repeats until user enters n

3️⃣ Rock–Paper–Scissors Game
📖 Description

A classic game where the user chooses Rock (r), Paper (p), or Scissor (s) and plays against the computer.
Emojis make the output fun and easy to understand.

🧠 Python Logic Used

Dictionary:

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}


random.choice() to select computer’s move

Input validation loop to accept only r/p/s

Winner logic using conditions:

Rock beats Scissor

Scissor beats Paper

Paper beats Rock
