#include <iostream>
#include <vector>

void insertionSort(std::vector<int> &arr)
{
    size_t n = arr.size();
    for (size_t i = 1; i < n; ++i)
    {
        int key = arr[i];
        size_t j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j]; // Move elements greater than key to one position ahead
            --j;
        }
        arr[j + 1] = key; // Insert the key at the correct position
    }
}

int main()
{
    std::vector<int> arr = {12, 11, 13, 5, 6};

    insertionSort(arr);

    std::cout << "Sorted array: ";
    for (int num : arr)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
