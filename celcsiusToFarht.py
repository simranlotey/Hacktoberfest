#To convert Celsius to Fahrenheit using Python
#below is the formula to convert Celsius to Fahrenheit  :
#F=95×C+32F=59​×C+32

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
