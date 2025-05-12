try:
    f = open("Test.txt", "w")
    f.write("Hello Good Morning!")
except IOError:
    print("Error while writing !")