text = "Malayalam is my mother tongue"

words = text.split()
for word in words:
    temp = word[::-1]
    if(temp.lower() == word.lower()):
        print(word)