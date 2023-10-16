#include <iostream>
#include <string>

bool areAnagrams(std::string word1, std::string word2) {
    std::string cleanWord1 = word1;
    std::string cleanWord2 = word2;

    cleanWord1.erase(std::remove(cleanWord1.begin(), cleanWord1.end(), ' '), cleanWord1.end());

    cleanWord2.erase(std::remove(cleanWord2.begin(), cleanWord2.end(), ' '), cleanWord2.end());

    std::transform(cleanWord1.begin(), cleanWord1.end(), cleanWord1.begin(), ::tolower);

    std::transform(cleanWord2.begin(), cleanWord2.end(), cleanWord2.begin(), ::tolower);

    if (cleanWord1.length() != cleanWord2.length()) {
        return false;
    }

    std::sort(cleanWord1.begin(), cleanWord1.end());
    std::sort(cleanWord2.begin(), cleanWord2.end());

    return cleanWord1 == cleanWord2;

}

int main() {
    std::string word1 = "listen";
    std::string word2 = "silent";

    if (areAnagrams(word1, word2)) {
        std::cout << word1 << " and " << word2 << " are anagrams." << std::endl;
    } else {
        std::cout << word1 << " and " << word2 << " are not anagrams." << std::endl;
    }

    return 0;
}

