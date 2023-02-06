import pandas

# Step 1: Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet)

# nato_alphabet_dict = {}
# Loop through rows of a data frame
# for (index, row) in nato_alphabet.iterrows():
#     # Access index and row
#     # print(row.letter, row.code)
#     nato_alphabet_dict[row.letter] = row.code
#     # Access row.student or row.score
#     pass

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dict)

# Step 2: Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word to get it transcribed to phonetic code: ")
# word_transcription = []
# for letter in user_word:
#     word_transcription.append(nato_alphabet_dict[letter.upper()])
word_transcription = [nato_alphabet_dict[letter.upper()] for letter in user_word]

print(f"The transcription for {user_word} is: {word_transcription}")
