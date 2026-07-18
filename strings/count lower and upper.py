txt = input("enter a word:")
lower = 0
upper = 0
for letter in txt:
    if letter.isupper() == True:
        upper += 1
    if letter.islower() == True:
        lower += 1
print("the lower letters are:",lower)
print("the upper letters are:",upper)
