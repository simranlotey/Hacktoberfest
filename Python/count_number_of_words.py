# Develop a program that counts the number of words in a given text input.

# Provide the text whose number of words you want to count.
text = input("Enter you text: ")

word = text.split()

print(f"The number of words in your given text is {len(word)}")