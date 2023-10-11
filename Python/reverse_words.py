def reverse_words(sentence):
    # Split the sentence into words using whitespace as the separator
    words = sentence.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed words to form a new sentence
    rev = ' '.join(reversed_words)

    return rev


if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")

    reversed_sentence = reverse_words(input_sentence)

    print("Reversed sentence:", reversed_sentence)
