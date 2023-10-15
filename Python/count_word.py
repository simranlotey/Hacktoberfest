def count_words(text):
    # Split the text into words based on spaces
    words = text.split()
    return len(words)

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    word_count = count_words(input_text)
    print(f"Number of words in the text: {word_count}")
