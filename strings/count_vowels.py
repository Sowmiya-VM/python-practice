vowels = "AEIOUaeiou"
txt = input ("enter a word:")
count = 0
for letters in txt:
    if letters in vowels:
        count += 1
print("vowels:",count)
#explanation
# first we are giving what are all the vowels to python then its taking input from user and we are intializing count = 0
# now if the letter in the word typed by user has vowels in it then save it in count and move to next character and then print the count which contains how many vowels.
