function findSecondSmallest(arr: number[]): number | null {
    if (arr.length < 2) {
        console.error("The array should contain at least two numbers.");
        return null;
    }

    let smallest = Infinity;
    let secondSmallest = Infinity;

    for (let num of arr) {
        if (num < smallest) {
            secondSmallest = smallest;
            smallest = num;
        } else if (num < secondSmallest && num !== smallest) {
            secondSmallest = num;
        }
    }

    if (secondSmallest === Infinity) {
        console.error("There is no second smallest number in the array.");
        return null;
    }

    return secondSmallest;
}

// Example usage
const array = [5, 3, 8, 1, 9, 2, 4];
const secondSmallest = findSecondSmallest(array);

if (secondSmallest !== null) {
    console.log("The second smallest number is:", secondSmallest);
}
