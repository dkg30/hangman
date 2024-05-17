import random
import time
from data import logo, stages, word_list, alphabet

print(logo)

won = 0
rounds_num = 0


def hangman():
    global won, rounds_num
    chosen_word = random.choice(word_list)
    display = ["_"] * len(chosen_word)
    end_of_round = False
    lives = 6
    guessed_letters = []

    while not end_of_round:
        guess = input('\nGuess a letter: ').lower()
        if guess in guessed_letters:
            print(f"You' ve already guessed {guess}\n")
            continue
        guessed_letters.append(guess)
        if guess not in alphabet:
            print("Please provided a letter.")
            continue
        if guess not in chosen_word:
            print(f"You chose {guess}. It' s not in the word. You lose a life!")
            lives -= 1
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"{' '.join(display)}")
        print(stages[lives])
        if '_' not in display and lives > 0:
            end_of_round = True
            print('You win!')
            won += 1
        elif lives == 0:
            end_of_round = True
            print(f'You lose!\nThe word is "{chosen_word}"')
    rounds_num += 1


def play_again():
    while True:
        answer = input("\nWould you like to play again? (Y/n) ")
        if answer.upper() == "Y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please provide suitable answer!")


def summary():
    win_per_game = int(won / rounds_num * 100)
    print(f"\nYou won {win_per_game}% ({won}/{rounds_num}) of the times!")


def main():
    while True:
        hangman()
        if not play_again():
            break
    summary()
    time.sleep(5)


if __name__ == "__main__":
    main()
