#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

bool isPalindrome(const std::string& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        while (left < right && !std::isalnum(s[left])) {
            left++;
        }
        while (left < right && !std::isalnum(s[right])) {
            right--;
        }
        if (std::tolower(s[left]) != std::tolower(s[right])) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    std::string s;
    std::cout << "Enter a string: ";
    std::getline(std::cin, s);

    if (isPalindrome(s)) {
        std::cout << "The string is a palindrome." << std::endl;
    } else {
        std::cout << "The string is not a palindrome." << std::endl;
    }

    return 0;
}
