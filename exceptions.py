#this will throw an error
try:
    int("a")
except ValueError:
    print("Dayum you failed")

print("this is the end of my error")
