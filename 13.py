text = "Programming in Python"
f = open("code.txt", "w")
f.write(text)

f = open("code.txt", "r")
input_text = f.read()
print(input_text)