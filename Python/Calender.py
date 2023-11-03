import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

def main():
    print("Basic Calendar Display\n")

    while True:
        year = int(input("Enter the year (e.g., 2023): "))
        month = int(input("Enter the month (1-12): "))

        if 1 <= month <= 12:
            cal = display_calendar(year, month)
            print("\n", cal)
        else:
            print("Invalid month. Please enter a valid month (1-12).\n")

        choice = input("Do you want to view another calendar (yes/no)? ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
