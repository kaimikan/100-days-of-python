alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
special_characters = "!@#$%^&*()-+?_=,<>/:;"

loop_cypher = True


def caesar(text, shift, cypher_direction):
    cypher_text = ""
    for letter in range(len(text)):
        # if text[letter].isdigit() or text[letter] in special_characters or text[letter] == " ":
        if not text[letter] in alphabet:
            cypher_text += text[letter]
        else:
            if cypher_direction == "encode":
                index = alphabet.index(text[letter]) + shift
                if index > len(alphabet) - 1:
                    index -= len(alphabet)
            elif cypher_direction == "decode":
                index = alphabet.index(text[letter]) - shift

            cypher_text += alphabet[index]

    print(f"The {cypher_direction}d text is {cypher_text}")


while loop_cypher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction != "encode" and direction != "decode":
        direction = input("Try again, type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if shift is 100 we handle it with this
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    print(f"SHIFT {shift}")
    caesar(text, shift, direction)

    choice = input("Go again y/n? ").lower()
    while choice != 'y' and choice != 'n':
        choice = input("Unidentified choice - go again y/n? ").lower()

    if choice == 'y':
        loop_cypher = True
    else:
        loop_cypher = False
