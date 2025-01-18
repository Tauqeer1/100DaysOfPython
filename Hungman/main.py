import random
from hungman_stages import stages
from hungman_words import word_list

# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(f"Chosen Word: {chosen_word}")

display = []
for _ in range(word_length):
    display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # print(f"Guessed Letter: {guess}")
    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        for i in range(word_length):
            letter = chosen_word[i]
            if guess == letter:
                display[i] = letter
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(stages[lives])

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win")
    elif lives == 0:
        end_of_game = True
        print("You lose")