import random as rand

magic_number = rand.randint(1, 100)
num_rounds = input("How many rounds do you want to play?")

while not num_rounds.isnumeric():
    num_rounds = input("How many rounds do you want to play?")

num_rounds = int(num_rounds)

for i in range(num_rounds):
    print(f"Round {i+1}")
    guess = input("Give me a number (1-100)")

    while not guess.isnumeric():
        guess = input("Give me a number (1-100)")

    guess = int(guess)

    if guess == magic_number:
        print("Hooray!!! U are correct!!!")
        break
    elif guess > magic_number:
        print("Oops! You guessed wrong. Number should be lower.")
    else:
        print("Oops! You guessed wrong. Number should be higher.")
print(f"The secret number is {magic_number}")
