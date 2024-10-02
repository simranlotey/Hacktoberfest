// Problem: Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

#include <iostream>
#include <vector>

using namespace std;

int majorityElement(vector<int>& nums) {
    int count = 0;
    int candidate = 0;

    // Step 1: Find a candidate using Boyer-Moore Voting Algorithm
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }

    // Step 2: Verify that the candidate is the majority element
    count = 0;
    for (int num : nums) {
        if (num == candidate) {
            count++;
        }
    }

    if (count > nums.size() / 2) {
        return candidate;
    } else {
        return -1; // If there is no majority element
    }
}

int main() {
    vector<int> nums = {2, 2, 1, 1, 2, 2, 2};
    int result = majorityElement(nums);
    if (result != -1) {
        cout << "Majority Element: " << result << endl;
    } else {
        cout << "No Majority Element found" << endl;
    }
    return 0;
}
