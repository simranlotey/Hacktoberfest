#include <stdio.h>
int main()
{
    int n, i, j, temp;
    int arr[64];
    printf("Insertion Sort:\n");
    printf("Enter number of elements\n");
    scanf("%d", &n);
    printf("Enter the numbers:");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (i = 1; i < n; i++)
    {
        j = i;
        while (j > 0 && arr[j - 1] > arr[j])
        {
            temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
            j--;
        }
    }
    printf("Sorted list in ascending order:");
    for (i = 0; i < n; i++)
        printf("\t%d", arr[i]);
    printf("\n");
    return 0;
}
