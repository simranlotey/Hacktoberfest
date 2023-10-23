/*
Problem Link: https://leetcode.com/problems/is-subsequence/
Intuition:
- We want to determine if string 's' is a subsequence of string 't'.
- We can count the occurrences of each character in string 't' using an unordered_map.
- Then, we iterate through string 's' and check if each character is present in 't' and hasn't been exhausted.
- If we successfully find all characters in 's' in 't', we return true; otherwise, we return false.
*/

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        // Create an unordered_map to count characters in string 't'.
        unordered_map<char, int> charCount;

        // Count characters in string 't'.
        for (int i = 0; i < t.size(); i++)
        {
            charCount[t[i]]++;
        }

        // Check if string 's' can be formed from characters in 't'.
        for (int i = 0; i < s.size(); i++)
        {
            // If the character in 's' is found in 't' and hasn't been exhausted, decrement its count.
            if (charCount.find(s[i]) != charCount.end() && charCount[s[i]] > 0)
            {
                charCount[s[i]]--;
            }
            else
            {
                return false; // If the character in 's' cannot be found or has been exhausted in 't'.
            }
        }

        return true; // If we successfully found all characters in 's' in 't'.
    }
};
