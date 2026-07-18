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
    
