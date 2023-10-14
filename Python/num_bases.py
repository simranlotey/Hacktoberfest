def convert_base(number, from_base, to_base):
    try:
        # Convert the number from the source base to decimal
        decimal_number = int(number, from_base)

        # Convert the decimal number to the target base
        result = format(decimal_number, 'x' if to_base == 16 else 'b' if to_base == 2 else 'd')

        return result
    except ValueError:
        return "Invalid input"

if __name__ == "__main__":
    number = input("Enter a number: ")
    from_base = int(input("Enter the source base (e.g., 2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))
    to_base = int(input("Enter the target base (e.g., 2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))

    converted_number = convert_base(number, from_base, to_base)
    if converted_number == "Invalid input":
        print("Invalid input. Please check the number and base.")
    else:
        print(f"Converted number: {converted_number}")
