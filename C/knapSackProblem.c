#include <stdio.h>
#include <stdlib.h>

int* knapsackProblem(int items[][2], int numItems, int capacity) {
    int** knapsackValues = (int**)malloc((numItems + 1) * sizeof(int*));
    for (int i = 0; i < numItems + 1; i++) {
        knapsackValues[i] = (int*)calloc(capacity + 1, sizeof(int));
    }

    for (int i = 1; i < numItems + 1; i++) {
        int currentValue = items[i - 1][0];
        int currentWeight = items[i - 1][1];
        for (int c = 0; c < capacity + 1; c++) {
            if (currentWeight > c) {
                knapsackValues[i][c] = knapsackValues[i - 1][c];
            } else {
                knapsackValues[i][c] = (knapsackValues[i - 1][c] > knapsackValues[i - 1][c - currentWeight] + currentValue) ? knapsackValues[i - 1][c] : knapsackValues[i - 1][c - currentWeight] + currentValue;
            }
        }
    }

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = knapsackValues[numItems][capacity];

    int* sequence = (int*)malloc(numItems * sizeof(int));
    int i = numItems;
    int c = capacity;
    int count = 0;
    while (i > 0) {
        if (knapsackValues[i][c] == knapsackValues[i - 1][c]) {
            i -= 1;
        } else {
            sequence[count] = i - 1;
            c -= items[i - 1][1];
            i -= 1;
            count += 1;
        }
        if (c == 0) break;
    }

    int* itemsIncluded = (int*)malloc(count * sizeof(int));
    for (int j = 0; j < count; j++) {
        itemsIncluded[j] = sequence[j];
    }
    result[1] = count;

    free(knapsackValues);
    free(sequence);

    return itemsIncluded;
}

int main() {
    int items[][2] = {{1, 2}, {4, 3}, {5, 6}, {6, 7}};
    int numItems = 4;
    int capacity = 10;
    int* itemsIncluded = knapsackProblem(items, numItems, capacity);
    int numIncluded = itemsIncluded[numItems];
    printf("Maximum value: %d\n", knapsackProblem(items, numItems, capacity)[0]);
    printf("Items included: ");
    for (int i = 0; i < numIncluded; i++) {
        printf("%d ", itemsIncluded[i]);
    }
    printf("\n");
    free(itemsIncluded);
    return 0;
}