a = False
b = True

#If else
if a:
    print("1")
elif b:
    print("2")
else: 
    print("3")
 
#While loop
counter = 0
max = 4
while counter < max:
    print(f"the count is: {counter}")
    counter = counter + 1

#For loop

#using break
names = ["tosh", "max", "sparrow", "jimmy"]

for x in names:
    print(f"hello, {x}")
    #break out of the loop if a condition is met
    if x == "sparrow":
        break

#using continue
#continue is kind of like skip or restart. if the name is not sparrow, check the next one
for name in names:
    if name != "sparrow":
        continue
    print(f"hello, {name}")

#nested for loop breaking
count = 0
while True:
    count += 1
    if count == 5:
        print("count was reached")
        break
def find_target_name():
    for name in names:
        print(name)
        if name == "max":
            return "Found the special case"
print(find_target_name())