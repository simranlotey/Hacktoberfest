#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> knapsackProblem(vector<vector<int>> items, int capacity) {
    vector<vector<int>> knapsackValues(items.size() + 1, vector<int>(capacity + 1, 0));
    for (int i = 1; i < items.size() + 1; i++) {
        int currentValue = items[i - 1][0];
        int currentWeight = items[i - 1][1];
        for (int c = 0; c < capacity + 1; c++) {
            if (currentWeight > c) {
                knapsackValues[i][c] = knapsackValues[i - 1][c];
            } else {
                knapsackValues[i][c] = max(
                    knapsackValues[i - 1][c],
                    knapsackValues[i - 1][c - currentWeight] + currentValue
                );
            }
        }
    }
    vector<int> sequence;
    int i = items.size();
    int c = capacity;
    while (i > 0) {
        if (knapsackValues[i][c] == knapsackValues[i - 1][c]) {
            i -= 1;
        } else {
            sequence.push_back(i - 1);
            c -= items[i - 1][1];
            i -= 1;
        }
        if (c == 0) break;
    }
    reverse(sequence.begin(), sequence.end());
    return {knapsackValues[items.size()][capacity], sequence};
}

int main() {
    vector<vector<int>> items = {{1, 2}, {4, 3}, {5, 6}, {6, 7}};
    int capacity = 10;
    vector<int> result = knapsackProblem(items, capacity);
    cout << "Maximum value: " << result[0] << endl;
    cout << "Items included: ";
    for (int i = 0; i < result[1].size(); i++) {
        cout << result[1][i] << " ";
    }
    cout << endl;
    return 0;
}