#include <stdio.h>
#include <string.h>

int isPalindrome(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1])
            return 0;
    }
    return 1;
}

int main() {
    char word[] = "radar";
    if (isPalindrome(word))
        printf("%s is a palindrome.\n", word);
    else
        printf("%s is not a palindrome.\n", word);
    return 0;
}