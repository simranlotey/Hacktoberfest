// Problem: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money. Find the maximum amount you can rob without robbing two adjacent houses.

#include <iostream>
#include <vector>
using namespace std;

int rob(vector<int>& nums) {
    if (nums.empty()) return 0;    // If no houses, return 0
    if (nums.size() == 1) return nums[0];  // If only one house, rob it

    int prev2 = 0;   // This holds the value for two houses back
    int prev1 = 0;   // This holds the value for the previous house

    for (int num : nums) {
        int temp = max(prev1, prev2 + num);  // Max between robbing this house or skipping
        prev2 = prev1;   // Update two steps back
        prev1 = temp;    // Update one step back
    }

    return prev1;  // Return the max money that can be robbed
}

int main() {
    vector<int> houses = {2, 7, 9, 3, 1};
    cout << "Maximum money robbed: " << rob(houses) << endl;
    return 0;
}
