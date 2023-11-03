//find the maximum sub array sum

function maxSubArraySum(arr, num) {
    if (num > arr.length) {
        return null;
    }
    var max = -Infinity;
    for (var i = 0; i < arr.length - num + 1; i++) {
        var temp = 0;
        for (var j = 0; j < num; j++) {
            temp += arr[i + j];
        }
        if (temp > max) {
            max = temp;
        }
    }
    return max;
}
console.log(maxSubArraySum([1, 2, 5, 2, 8, 1, 5], 2));