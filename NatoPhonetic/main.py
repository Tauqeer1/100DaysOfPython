import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
word = input("Enter a word: ").upper()
name_phonetic = [phonetic_dict[letter] for letter in word]

print(name_phonetic)