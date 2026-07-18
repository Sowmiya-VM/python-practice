txt = input("enter a word :")
index = len(txt) - 1
while index >= 0:
    print(txt[index])
    index = index - 1
//explanation
// using while loop we are reversing a string here 
// now first we are getting an input from the user then since the length of the text is lets say the word nature then its 6 but usually indexing starts from 0 
// so we reducing the length of original text and next while lets say index is 5 so 5>=0 then print txt[0] which is for the word nature n then txt[1] means a like that it will move in loop
// for the loop to continue to the next character we use this index = index - 1 so thats how we reverse a string using a loop.
