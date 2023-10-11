def generate_pascals_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row with a single element 1
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)
        new_row.append(1)
        triangle.append(new_row)

    return triangle


def display_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        padding = max_width - len(row_str)
        left_padding = padding // 2
        right_padding = padding - left_padding
        print(" " * left_padding + row_str + " " * right_padding)


if __name__ == "__main__":
    N = int(input("Enter the number of rows (i.e. 10): "))
    pascals_triangle = generate_pascals_triangle(N)
    display_pascals_triangle(pascals_triangle)
