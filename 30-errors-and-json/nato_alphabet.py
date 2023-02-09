import pandas

# using code from day 26

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dict)

user_word = input("Enter a word to get it transcribed to phonetic code: ").upper()
characters = [letter for letter in user_word]

has_invalid_symbols = True
while has_invalid_symbols:
    for character in characters:
        try:
            nato_alphabet_dict[character]
        except KeyError:
            has_invalid_symbols = True
            user_word = input("Sorry, only letters in the phrase please: ").upper()
            characters = [letter for letter in user_word]
            break
        else:
            has_invalid_symbols = False

word_transcription = []
for letter in user_word:
    word_transcription.append(nato_alphabet_dict[letter])

print(f"The transcription for {user_word} is: {word_transcription}")


# lecturer solution - much cleaner
def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet. ")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
