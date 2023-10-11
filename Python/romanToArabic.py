# Define a function to convert a Roman numeral to an Arabic numeral.
def roman_to_arabic(roman):
    # Create a dictionary that maps Roman numerals to their Arabic equivalents.
    roman_to_arabic_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize variables for the result and the previous numeral's value.
    result = 0
    prev_value = 0
    
    # Iterate through the Roman numeral characters in reverse order.
    for numeral in reversed(roman):
        value = roman_to_arabic_map[numeral]
        
        # Compare the current numeral's value with the previous one.
        if value < prev_value:
            result -= value  # Subtract the current value if it's smaller.
        else:
            result += value  # Add the current value if it's greater or equal.
        
        prev_value = value  # Update the previous value for the next iteration.

    return result

# Import necessary modules for command-line argument parsing.
import argparse
import sys
import os

# Check if the script is executed as the main program.
if __name__ == '__main__':
    # Set up command-line argument parsing using argparse.
    parser = argparse.ArgumentParser()

    # Define a command-line argument for the input Roman numeral.
    parser.add_argument('-i', '--input', type=str, help='the Roman number to convert')

    # Parse the command-line arguments.
    args = parser.parse_args()

    # Call the roman_to_arabic function with the provided Roman numeral and display the result.
    arabic_number = roman_to_arabic(args.input)
    print('Arabic number: {}'.format(arabic_number))