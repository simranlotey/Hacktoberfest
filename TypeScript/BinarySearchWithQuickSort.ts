function binarySearch(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid; // Found the target value at index 'mid'
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1; // Target value not found in the array
}

function quicksort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quicksort(left), pivot, ...quicksort(right)];
}

/* Testcase
const unsortedArray = [13, 7, 3, 9, 5, 11, 1];
const sortedArray = quicksort(unsortedArray);
const targetValue = 7;
const result = binarySearch(sortedArray, targetValue);

if (result !== -1) {
  console.log(`The target value ${targetValue} was found at index ${result}.`);
} else {
  console.log(`The target value ${targetValue} was not found in the array.`);
}
*/
