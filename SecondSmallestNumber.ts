function findSecondSmallestNumber(arr: number[]): number {
  if (arr.length < 2) {
    throw new Error("Array should contain at least two elements");
  }

  let smallest = Number.MAX_VALUE;
  let secondSmallest = Number.MAX_VALUE;

  for (const num of arr) {
    if (num < smallest) {
      secondSmallest = smallest;
      smallest = num;
    } else if (num < secondSmallest && num !== smallest) {
      secondSmallest = num;
    }
  }

  if (secondSmallest === Number.MAX_VALUE) {
    throw new Error("No second smallest number found in the array");
  }

  return secondSmallest;
}

// Testcase:
/*const numbers = [5, 2, 9, 1, 5, 6];
const secondSmallest = findSecondSmallestNumber(numbers);
console.log("The second smallest number is: " + secondSmallest);
*/
