import random
import  hangman_stages
lives = 6
word_list = ["apple", "welcome", "beautiful"]
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]

print(" ".join(display))

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = guess

    print(" ".join(display))

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose!! :(")

    if '_' not in display:
        game_over = True
        print("You win!! :)")

    print(hangman_stages.stages[lives])