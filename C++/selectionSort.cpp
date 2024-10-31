#include <bits/stdc++.h>
using namespace std;

void selection_sort(int arr[], int n) {
  for (int i = 0; i < n - 1; i++) {
    int mini = i;
    for (int j = i + 1; j < n; j++) {
      if (arr[j] < arr[mini]) {
        mini = j;
      }
    }
    int temp = arr[mini];
    arr[mini] = arr[i];
    arr[i] = temp;
  }

  cout << "After selection sort: " << "\n";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";
}

int main() {
  int n;
  cout << "Enter the number of elements: ";
  cin >> n;

  int arr[n];
  cout << "Enter the elements:\n";
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cout << "Before selection sort: " << "\n";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";

  selection_sort(arr, n);

  return 0;
}
