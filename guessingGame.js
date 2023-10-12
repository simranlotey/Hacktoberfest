//Write a program to create a number guessing game where the user guesses a random number.

function startGame() {
  const randomNumber = Math.floor(Math.random() * 100) + 1; // Generate a random number between 1 and 100
  let attempts = 0;

  function guessNumber() {
    const userGuess = parseInt(prompt("Enter your guess (between 1 and 100):"));

    if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
      alert("Please enter a valid number between 1 and 100.");
      return guessNumber();
    }

    attempts++;

    if (userGuess < randomNumber) {
      alert("Too low! Try again.");
      return guessNumber();
    } else if (userGuess > randomNumber) {
      alert("Too high! Try again.");
      return guessNumber();
    } else {
      alert(`Congratulations! You guessed the number in ${attempts} attempts.`);
    }
  }

  guessNumber();
}

// Start the game
startGame();
