import random
# '\x1B[4m' makes it underlined
# '\x1B[3m' makes it italic
# '\x1B[1m' makes it bold
# '\x1B[1;4m' makes it bold and underlined
# '\x1B[0m' is the closing tag

print("        \x1B[1;4m\x1B[3mGuess The Correct Number\x1B[0m\n\n\n")
difficulty_lvl = input("Enter the difficulty level [Hard/Easy]: ").lower()
if difficulty_lvl == 'hard':
    chance = 5
elif difficulty_lvl == 'easy':
    chance = 10
print(f"You've {chance} moves to guess the correct number.")

user_input = int(input("Enter your guess: "))
number = random.randint(1,100)

while (chance != 0 and user_input != number):
    if user_input != number:
        if user_input < number:
            print("Your guessed number is smaller.\n")
        elif user_input > number:
            print("Your guessed number is greater.\n")
        chance -= 1
        print(f"Only '{chance}' chance left\n\n")
        if chance >= 1:
            user_input = int(input("Enter your guess: "))

if user_input!= number:
     print(f"\nYou Lose!\nThe correct number was {number}.")
elif user_input == number:
    print(f"\nYou guessed the right number in just {chance} moves.\n     CONGRATULATIONS, YOU WON!") 