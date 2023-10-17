'''
                                                    📝 Introduction:
• A magic square is a square grid of numbers where each row, column, and diagonal add up to the same total.
• Find the "magic constant" sum of each row, column, and diagonal with S = n[(n^2 + 1)/2] where n is the number of squares in each row.
• Use a solving technique based on the size of the magic square and how many boxes are in each row or column.

                                                    🧩 Steps:
1) In any magic square, 1 is located at position (n/2, n-1).
2) Let's say the position of 1 i.e. (n/2, n-1) is (p, q), then next number which is 2 is located at (p-1, q+l) position.
    Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it O.
3) If the calculated position already contains a number then decrement the column by 2 and increment the row by 1.
4) If anytime row position becomes -1 and column becomes n, switch it to (O, n-2).
'''


def magic_square(num):
    # Create an empty 2D square matrix:
    square_matrix = []

    # Initialize all elements to 0:
    for i in range(num):
        emp_list = []
        for j in range(num):
            emp_list.append(0)
        square_matrix.append(emp_list)

    # Initialize the starting position in the middle column and the last row:
    i = num // 2
    j = num - 1

    # Calculate the total number of cells in the square matrix and initialize count to 1:
    size = num * num
    count = 1

    while (count <= size):
        # Condition Number - 4:
        if (i == -1 and j == num):
            j = num - 2
            i = 0
        else:
            # When Column value exceeds:
            if (j == num):
                j = 0

            # When Row Becomes -1:
            if (i < 0):
                i = num - 1

        # Check if the cell in the square matrix is already filled.
        if (square_matrix[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        else:
            # Fill the cell with the current count value.
            square_matrix[i][j] = count
            count = count + 1

        # Condition Number - 1:
        i = i - 1
        j = j + 1

    # Print the Magic Square.
    print("\nThe Magic Square of", num, "X", num, "is:\n")
    for i in range(num):
        for j in range(num):
            print(square_matrix[i][j], end=" ")
        print()

    print()
    # Calculate and print the sum of each Row/Column/Diagonal of the magic square.
    print("The sum of each Row/Column/Diagonal of", num,
          "X", num, "matrix is:", (num * ((num**2) + 1) // 2))


# Prompt the user to enter the square matrix size and call the magic_square function.
magic_square(int(input("Enter the square matrix size: ")))
