text = input("Enter text : ")
dist = int(input("Enter Distance : "))
cipher = ""
rev = ""

for ch in text:
    i = ord(ch)
    ci = i + dist
    if(ci > ord('z')):
        ci = ci - (ord('z') - ord('a')) - 1
    cipher += chr(ci)

print(cipher)

for ch in cipher:
    i = ord(ch)
    ci = i - dist
    if(ci < ord('a')):
        ci = ci + (ord('z') - ord('a')) + 1
    rev += chr(ci)
print(rev)