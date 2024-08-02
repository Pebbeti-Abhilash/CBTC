import random

def player_1_set_number():
    return str(random.randint(1000, 9999))  # Player 1 sets a random 4-digit number

def player_2_guess_number():
    return str(input("Player 2, enter your guess: "))

def get_correct_digits(secret_number, guessed_number):
    correct_digits = 0
    for i in range(4):
        if secret_number[i] == guessed_number[i]:
            correct_digits += 1
    return correct_digits

def main_game():
    print("Welcome to the Mastermind game!")
    player_1_number = player_1_set_number()
    print("Player 1 has set the number. It's your turn, Player 2!")

    attempts = 0
    while True:
        player_2_attempt = player_2_guess_number()
        attempts += 1
        correct_digits = get_correct_digits(player_1_number, player_2_attempt)

        if correct_digits == 4:
            print("Congratulations! Player 2 is the Mastermind!")
            break
        else:
            print(f"Player 2, you got {correct_digits} digits correct. Try again!")

    print(f"Player 2 took {attempts} attempts to guess the number. Now, it's Player 1's turn.")

    player_2_number = input("Player 2, set your 4-digit number: ")

    attempts_player_1 = 0
    while True:
        player_1_attempt = str(random.randint(1000, 9999))  # Player 1 makes a random guess
        attempts_player_1 += 1

        if player_1_attempt == player_2_number:
            print(f"Congratulations! Player 1 is the Mastermind! Player 1 took {attempts_player_1} attempts.")
            break

    if attempts_player_1 > attempts:
        print("Player 2 wins the game!")
    else:
        print("Player 1 wins the game!")

main_game()