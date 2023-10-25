const randomNumber = Math.floor(Math.random() * 100) + 1;

let attempts = 0;

function checkGuess() {
  const guessInput = document.getElementById('guess');
  const message = document.getElementById('message');
  const userGuess = parseInt(guessInput.value);
  attempts++;

  if (userGuess === randomNumber) {
    message.innerHTML = `Congratulations! You guessed the number ${randomNumber} in ${attempts} attempts.`;
    message.style.color = 'green';
    guessInput.disabled = true;
  } else if (userGuess < randomNumber) {
    message.innerHTML = `Try a higher number. Attempts: ${attempts}`;
    message.style.color = 'red';
  } else {
    message.innerHTML = `Try a lower number. Attempts: ${attempts}`;
    message.style.color = 'red';
  }

  guessInput.value = '';
}