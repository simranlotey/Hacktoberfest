// Problem: Given two integer arrays, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays.


#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> countMap;
    vector<int> result;

    // Step 1: Count frequencies of elements in the first array
    for (int num : nums1) {
        countMap[num]++;
    }

    // Step 2: Iterate through the second array and find common elements
    for (int num : nums2) {
        if (countMap[num] > 0) {
            result.push_back(num);
            countMap[num]--; // Decrease the count as we've used this element
        }
    }

    return result;
}

int main() {
    vector<int> nums1 = {4, 9, 5, 9};
    vector<int> nums2 = {9, 4, 9, 8, 4};
    vector<int> result = intersect(nums1, nums2);

    // Output the result
    cout << "Intersection: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
