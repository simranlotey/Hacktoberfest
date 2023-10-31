#include <stdio.h>

int main()
{
    int  i, low, high, mid, n, found = 0, size;
    printf("Enter the size of the array:");
    scanf("%d", &size);
    int a[size];
    printf("Binary Search:\n");
    printf("\nEnter the elements of the array: ");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("\nEnter the element to be searched: ");
    scanf("%d", &n);

    low = 0;
    high = size - 1;
    while (high >= low)
    {
        mid = (low + high) / 2;
        if (n == a[mid])
        {
            found = 1;
            break;
        }
        else if (n < a[mid])
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    if (found == 1)
    {
        printf("%d is present in index %d.\n", n, mid);
    }
    else
    {
        printf("%d is not present in the array.\n", n);
    }
    return 0;
}
