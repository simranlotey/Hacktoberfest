function bubbleSort(arr) {
  const length = arr.length;

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        // Swap elements
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }

  return arr;
}

// Example usage
const arr = [5, 3, 8, 1, 4];
console.log('Original array:', arr);
bubbleSort(arr);
console.log('Sorted array:', arr);
