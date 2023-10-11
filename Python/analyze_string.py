def analyze_string(_str):
    # Initialize counters
    vc = 0
    cc = 0
    nc = 0
    sc = 0

    # Define the set of vowels
    vowels = "AEIOUaeiou"

    # Iterate through each character in the input string
    for char in _str:
        if char.isalpha():
            if char in vowels:
                vc += 1
            else:
                cc += 1
        else:
            if char.isnumeric():
                nc += 1
            else:
                sc += 1

    return vc, cc, nc, sc


if __name__ == "__main__":
    input_string = input("Enter a string: ")

    vowel_count, consonant_count, number_count, special_char_count = analyze_string(input_string)

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Numbers: {number_count}")
    print(f"Special Characters: {special_char_count}")
