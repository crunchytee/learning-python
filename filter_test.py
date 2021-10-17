def min_age(age):
    min_age = 18
    if age > min_age:
        return True
    else: 
        return False

def min_age_concise(age):
    min_age = 18
    return age > min_age

age_list = (5,33,56,2,3,66,2,17,21)

x = filter(min_age_concise, age_list)

print(x)
print(tuple(x))