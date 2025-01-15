import random

word_list = ["ardvark", "baboon", "camel"]

# 1st way
# chosen_word = random.choice(word_list)
# 2nd way
chosen_word = word_list[random.randrange(0, len(word_list))]
word_length = len(chosen_word)
print(f"Chosen Word: {chosen_word}")

display = []

for _ in range(word_length):
    display.append("_")

guess = input("Guess a letter: ").lower()

print(f"Letter: {guess}")

for i in range(word_length):
    letter = chosen_word[i]
    if guess == letter:
        display[i] = letter
print(display)
