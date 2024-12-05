#function to count the number of words
def counter(text):
    words = text.split()
    return len(words)
#request the text
text = input("Enter the text: ")
print("The text has", counter(text), "words")