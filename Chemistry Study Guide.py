# Define the periodic table
periodic_table = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
    'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25,
    'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu':29 , 'Zn' :30 , 
    'Ga' :31 , 'Ge' :32 , 'As' :33 , 'Se' :34 , 
    'Br' :35 , 'Kr' :36 , 
    # Add more elements here...
    # The first 45 elements are included for simplicity.
    # You can add more elements to the `periodic_table` dictionary as needed.
}

def study_periodic_table():
    print("Enter an element symbol or atomic number (or 'quit' to stop):")
    while True:
        query = input()
        if query.lower() == 'quit':
            break
        elif query.isdigit():
            # User entered an atomic number
            for element, atomic_number in periodic_table.items():
                if atomic_number == int(query):
                    print(f"The element with atomic number {query} is {element}.")
                    break
            else:
                print(f"No element found with atomic number {query}.")
        else:
            # User entered an element symbol
            if query in periodic_table:
                print(f"The atomic number of {query} is {periodic_table[query]}.")
            else:
                print(f"No element found with symbol {query}.")

study_periodic_table()
