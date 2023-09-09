from sys import argv

script, filename = argv

prompt = "> "
txt = open(filename)

print(f"Here is your {filename}")
print(txt.read())

print("Type the filename again:")
file_again=input(prompt)

txt_again = open(file_again)

print(txt_again.read())

