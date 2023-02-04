# read names
with open("./Input/Names/invited_names.txt") as file:
    contents = file.read().splitlines()
    names = contents
    # # or
    # names = []
    # contents = file.readlines()
    # for content in contents:
    #     content.split()
    #     names.append(content)
print(names)

# read template
with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    letter_template = contents
print(letter_template)

# write and save custom letters
for name in names:
    # replace the placeholder with the name
    custom_letter = letter_template.replace("[name]", name)
    # remove white spaces before saving the file name
    name = name.replace(" ", "_")
    # create a new file for the custom letter
    with open(f"./Output/ReadyToSend/letter_to_{name.lower()}.txt", mode="w") as file:
        file.write(custom_letter)
        letter_template = contents
