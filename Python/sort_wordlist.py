# Function to sort a list of words in alphabetical order
def sort_words(word_list):
    return sorted(word_list)


def read_words_from_file(filename):
    with open(filename, 'r') as file:
        return [word.strip() for word in file]


def save_words_to_file(filename, word_list):
    with open(filename, 'w') as file:
        for word in word_list:
            file.write(word + '\n')


if __name__ == "__main__":
    option = input("Choose an option:\n1. Read words from a file\n2. Enter words manually\nEnter 1 or 2: ")

    if option == "1":
        filename = input("Enter the name of the file with words: ")
        word_list = read_words_from_file(filename)
    elif option == "2":
        word_list = input("Enter words separated by spaces: ").split()
    else:
        print("Invalid option")
        exit()

    sorted_words = sort_words(word_list)

    output_file = input("Enter the name of the output file: ")
    save_words_to_file(output_file, sorted_words)

    print("Words sorted and saved to", output_file)
