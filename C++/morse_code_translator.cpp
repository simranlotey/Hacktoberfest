#include <iostream>
#include <iomanip>
#include <string>
#include <iterator>
#include <sstream>
#include <cctype>

using namespace std;

string englishToMorse(const string &englishText, const char alphaN[], const string morse[], size_t size)
{
    string morseText;

    for (size_t i = 0; i < englishText.length(); ++i)
        for (size_t n = 0; n < size; ++n)
            if (static_cast<char>(std::toupper(static_cast<unsigned char>(englishText[i]))) == alphaN[n])
                morseText += morse[n] + ' ';

    return morseText;
}

string morseToEnglish(const string &morseText, const char alphaN[], const string morse[], size_t size)
{
    string convText;
    std::istringstream iss(morseText);

    for (std::string m; iss >> m;)
        for (size_t n = 0; n < size; ++n)
            if (morse[n] == m)
                convText += alphaN[n];

    return convText;
}

int main()
{
    const string morse[]{
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----",
        "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."};

    const char alphaN[]{
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

    static_assert(std::size(morse) == std::size(alphaN));

    int choice{};

    while (choice != 3)
    {
        cout << "Please choose an option <1/2/3>\n";
        cout << "1. Convert English text message to Morse Code.\n";
        cout << "2. Convert Morse Code to English text message.\n";
        cout << "3. Exit.\n\n";

        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
        {
            string englishText;

            cout << "Please type in your message in English\n";
            getline(cin >> ws, englishText);
            // cout << "you typed " << englishText << '\n';

            cout << englishToMorse(englishText, alphaN, morse, std::size(alphaN)) << "\n\n";
        }
        break;

        case 2:
        {
            string morseText;

            cout << "Please type in your message in morse\n";
            getline(cin >> ws, morseText);
            // cout << "you typed " << morseText << '\n';

            cout << morseToEnglish(morseText, alphaN, morse, std::size(alphaN)) << "\n\n";
        }
        break;

        case 3:
            cout << "thanks for using the program.\n";
            break;

        default:
            cout << "Invalid option\n";
        }
    }
}