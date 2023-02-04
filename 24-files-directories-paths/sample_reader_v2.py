# this way we don't need to close the file, python automatically takes care of it

# mode is read-only (r) by default
# r - read
# w - write
# a - append

# READING
with open("sample_text.txt") as file:
    contents = file.read()
    print(contents)

# WRITING
with open("sample_text.txt", mode="w") as file:
    file.write("Writing.")

# APPEND
with open("sample_text.txt", mode="a") as file:
    file.write("New writing.")

# if python does not find the file it will create it for us
with open("new_sample_text.txt", mode="w") as file:
    file.write("new file")
