def convert_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    bits = []
    while decimal:
        bits.append(str(decimal & 1))
        decimal >>= 1
    
    return ''.join(reversed(bits))

# Collect user input
num = int(input("Provide a decimal number: "))

# Convert and display the result
print(f"Binary of {num} is: {convert_to_binary(num)}")
