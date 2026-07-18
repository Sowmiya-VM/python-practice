original = input("enter a word:") 
reverse = ""                   
count = len(original)-1
while count>=0:
    reverse = reverse + original[count]
    count -= 1
if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
# explanation
# first we get the input from the user and why we save an empty string? its because imagine the word PYTHON now i take 
#an character p and write it down then y and then t..notice i write it down somewhere like an whiteboard so if i need to write it down i need an whiteboard
# so we need an empty string before we start so we can store the reversed string to check at last. now we need the index of the word the user typed so we use len(of what user typed) - 1 because for example the word python has 6 as length 
# but indexing starts from zero like 0 1 2 3 4 5 so 5 is the length for indexing
#now EMPTY string + original[0] = reverse which means lets take the example word python original[0] is p then original[1] is y  and so on its printing in reverse 
# so the reverse an empty string stores the reversed word of original word which user has typed 
#now count -= 1 has to be typed so the python goes to next character like p then y then t like that or else infinite loop will execute 
# now we are checking the condition if what user typed is equal to what reversed is example the word madam is same even when we reverse right..so if it is equal print palindrome else print not palindrome.
