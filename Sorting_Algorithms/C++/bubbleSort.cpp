#include <stdio.h>
#include <conio.h>

int main()
{
    int i, j, n, temp, arr[10];
    printf("Bubble Sort:\n");

    printf("Enter the numbers element of the array: ");
    scanf("%d", &n);

    printf("\nEnter the elements of the array: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("\nSorted Array is: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    getch();
    return 0;
}
