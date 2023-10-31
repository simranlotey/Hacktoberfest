#include <stdio.h>

void swap(int *a, int *b)
{

    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int arr[], int N, int i)
{
    int largest = i;

    // left = 2*i + 1
    int left = 2 * i + 1;

    // right = 2*i + 2
    int right = 2 * i + 2;

    // If left child is larger than root
    if (left < N && arr[left] > arr[largest])

        largest = left;

    // If right child is larger than largest
    // so far
    if (right < N && arr[right] > arr[largest])

        largest = right;

    // Swap and continue heapifying
    // if root is not largest
    // If largest is not root
    if (largest != i)
    {

        swap(&arr[i], &arr[largest]);

        // Recursively heapify the affected
        // sub-tree
        heapify(arr, N, largest);
    }
}

// Main function to do heap sort
void heapSort(int arr[], int N)
{

    // Build max heap
    for (int i = N / 2 - 1; i >= 0; i--)

        heapify(arr, N, i);

    // Heap sort
    for (int i = N - 1; i >= 0; i--)
    {

        swap(&arr[0], &arr[i]);

        // Heapify root element
        // to get highest element at
        // root again
        heapify(arr, i, 0);
    }
}

// A utility function to print array of size n
void printArray(int arr[], int N)
{
    for (int i = 0; i < N; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Driver's code
int main()
{
    int N, i;
    printf("Heap Sort:\n ");
    printf("Enter the number of elements: ");
    scanf("%d", &N);
    int arr[N];
    printf("Enter the elements: ");
    for (i = 0; i < N; i++)
        scanf("%d", &arr[i]);

    // Function call
    heapSort(arr, N);
    printf("Sorted array is\n");
    printArray(arr, N);
}
