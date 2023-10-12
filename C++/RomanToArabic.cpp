#include <iostream>
#include <unordered_map>
using namespace std;

int romanToArabic(string s) {
    unordered_map<char, int> romanVals = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    int prevValue = 0;

    for (char c : s) {
        int currValue = romanVals[c];
        result += currValue;

        if (currValue > prevValue) {
            result -= 2 * prevValue;
        }

        prevValue = currValue;
    }

    return result;
}

int main() {
    string romanNumeral;
    
    cout << "Enter a Roman numeral: ";
    cin >> romanNumeral;
    
    int arabicNumeral = romanToArabic(romanNumeral);
    
    cout << "Arabic numeral equivalent: " << arabicNumeral << endl;

    return 0;
}
