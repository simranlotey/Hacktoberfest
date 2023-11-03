// Binary Search Function
function binarySearch(arr: number[], target: number): number | null {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid; // Found the target
    } else if (arr[mid] < target) {
      left = mid + 1; // Target is on the right half
    } else {
      right = mid - 1; // Target is on the left half
    }
  }

  return null; // Target not found
}

// Quicksort Function
function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left: number[] = [];
  const right: number[] = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

// Example usage
const sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const targetValue = 7;

const result = binarySearch(sortedArray, targetValue);

if (result !== null) {
  console.log(`Found ${targetValue} at index ${result}.`);
} else {
  console.log(`${targetValue} not found in the array.`);
}

const unsortedArray = [4, 2, 8, 6, 1, 3, 9, 7, 5];
const sortedResult = quickSort(unsortedArray);
console.log("Sorted Array:", sortedResult);