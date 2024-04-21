import random
from data import logo, stages, word_list

chosen_word = random.choice(word_list)

display = []

for i in range(len(chosen_word)):
    display.append('_')

end_of_game = False

lives = 6

guessed_letters = []

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    if guess in guessed_letters:
        print(f"You' ve already guessed {guess}\n")
        continue
    guessed_letters.append(guess)
    if guess not in chosen_word:
        print(f"You chose {guess}. It' s not in the word. You lose a life!")
        lives -= 1
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(f"{' '.join(display)}")
    print(stages[lives])
    if '_' not in display and lives > 0:
        end_of_game = True
        print('You win!')
    elif lives == 0:
        end_of_game = True
        print(f'You lose!\nThe word is "{chosen_word}"')
