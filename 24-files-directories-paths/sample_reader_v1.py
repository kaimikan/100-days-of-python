# absolute file path -> C drive for windows
# file = open("/Users/User/Python/24-files-directories-paths-directories-paths/sample_text.txt")
# relative file path -> depends on where you are -> ./folder_name or ../parent_folder_neighbor
file = open("sample_text.txt")
contents = file.read()
print(contents)
# we need to close the file, so we don't take up resources
# (else python might close it automatically, same as many browser tabs)
file.close()
