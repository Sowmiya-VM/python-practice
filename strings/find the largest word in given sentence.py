txt = input("enter a word:")
words = txt.split()
largest = words[0]
for word in words:
    if len(word)>len(largest):
        largest = word
print("largest word is:",largest)
#explanation
#first we are getting outputfrom the user and we are splitting the given sentence for example
# i will become the great programmer splitted as ['i', 'will', 'become', 'the', 'great', 'programmer'] so we can easily count and go through the words and words[0] is 'i' we are assigning 
#so for a word in the given sentence by user if the word is larger then the intialized word then let that word be largest.

