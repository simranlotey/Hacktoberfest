#include <stdio.h>

int linearSearch(int array[], int n, int x)
{

    // Going through array sequencially
    for (int i = 0; i < n; i++)
        if (array[i] == x)
            return i;
    return -1;
}

int main()
{
    int array[10], size;
    int key, i;
    printf("Enter the size of the array:");
    scanf("%d",&size);
    printf("Linear Search:\n");
    printf("Enter Array Elements:");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &array[i]);
    }
    printf("Enter the element to be searched:");
    scanf("%d", &key);
    int result = linearSearch(array, size, key);

    (result == -1) ? printf("Element not found\n") : printf("Element found at index: %d\n", result);
}