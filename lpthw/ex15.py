from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
fileagain = input("> ")

txt_again = open(fileagain)

print(txt_again.read())