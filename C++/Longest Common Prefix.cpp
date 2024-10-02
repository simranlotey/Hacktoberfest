// Problem: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";

    string prefix = strs[0]; // Start with the first string as the prefix

    for (int i = 1; i < strs.size(); ++i) {
        while (strs[i].find(prefix) != 0) { // Check if the current prefix is found at the start
            prefix = prefix.substr(0, prefix.length() - 1); // Reduce the prefix length
            if (prefix.empty()) return ""; // No common prefix
        }
    }

    return prefix;
}

int main() {
    vector<string> strs = {"flower", "flow", "flight"};
    string result = longestCommonPrefix(strs);
    cout << "Longest Common Prefix: " << result << endl;
    return 0;
}
