#include <iostream>

bool areArraysEqual(const int arr1[], const int arr2[], int size1, int size2) {
    // If the sizes of the arrays are different, they cannot be equal
    if (size1 != size2) {
        return false;
    }

    // Compare each element of the two arrays
    for (int i = 0; i < size1; i++) {
        if (arr1[i] != arr2[i]) {
            return false; // Arrays are not equal
        }
    }

    return true; // Arrays are equal
}

int main() {
    int array1[] = {1, 2, 3, 4, 5};
    int array2[] = {1, 2, 3, 4, 5};
    int size1 = sizeof(array1) / sizeof(array1[0]);
    int size2 = sizeof(array2) / sizeof(array2[0]);

    if (areArraysEqual(array1, array2, size1, size2)) {
        std::cout << "The two arrays are equal." << std::endl;
    } else {
        std::cout << "The two arrays are not equal." << std::endl;
    }

    return 0;
}
