#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isVowel(char c) {
    c = tolower(c); // Convert the character to lowercase for case insensitivity
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int countVowels(const string& input) {
    int count = 0;
    for (char c : input) {
        if (isalpha(c) && isVowel(c)) {
            count++;
        }
    }
    return count;
}

int countConsonants(const string& input) {
    int count = 0;
    for (char c : input) {
        if (isalpha(c) && !isVowel(c)) {
            count++;
        }
    }
    return count;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    int vowelCount = countVowels(input);
    int consonantCount = countConsonants(input);

    cout << "Vowels: " << vowelCount << endl;
    cout << "Consonants: " << consonantCount << endl;

    return 0;
}
