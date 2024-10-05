#include <iostream>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()

using namespace std;

int main() {
    // Seed random number generator
    srand(static_cast<unsigned int>(time(0)));
    
    // Generate a random number between 1 and 100
    int numberToGuess = rand() % 100 + 1;
    int playerGuess = 0;
    int attempts = 0;

    cout << "Welcome to the Guess the Number game!" << endl;
    cout << "I'm thinking of a number between 1 and 100." << endl;
    cout << "Can you guess what it is?" << endl;

    // Game loop
    while (playerGuess != numberToGuess) {
        cout << "Enter your guess: ";
        cin >> playerGuess;
        attempts++;

        if (playerGuess > numberToGuess) {
            cout << "Too high! Try again." << endl;
        } else if (playerGuess < numberToGuess) {
            cout << "Too low! Try again." << endl;
        } else {
            cout << "Congratulations! You've guessed the number in " << attempts << " attempts." << endl;
        }
    }

    return 0;
}
