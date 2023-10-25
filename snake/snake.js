const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');

// Define the snake's initial position and direction.
let snakeX = 100;
let snakeY = 100;
let snakeDirection = 'right';

// Define the food's initial position.
let foodX = Math.floor(Math.random() * canvas.width);
let foodY = Math.floor(Math.random() * canvas.height);

// Create a restart button element.
const restartButton = document.createElement('button');
restartButton.textContent = 'Restart';
restartButton.addEventListener('click', function () {
    // Restart the game.
    snakeX = 100;
    snakeY = 100;
    snakeDirection = 'right';

    foodX = Math.floor(Math.random() * canvas.width);
    foodY = Math.floor(Math.random() * canvas.height);
});

// Append the restart button element to the document body.
document.body.appendChild(restartButton);

// Draw the snake and the food.
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the snake.
    ctx.fillStyle = 'green';
    ctx.fillRect(snakeX, snakeY, 10, 10);

    // Draw the food.
    ctx.fillStyle = 'red';
    ctx.fillRect(foodX, foodY, 10, 10);
}

// Update the snake's position.
function updateSnake() {
    // Move the snake in the current direction.
    switch (snakeDirection) {
        case 'right':
            snakeX += 10;
            break;
        case 'left':
            snakeX -= 10;
            break;
        case 'up':
            snakeY -= 10;
            break;
        case 'down':
            snakeY += 10;
            break;
    }

    function updateSnake() {
        // Move the snake in the current direction.
        switch (snakeDirection) {
            case 'right':
                snakeX += 10;
                break;
            case 'left':
                snakeX -= 10;
                break;
            case 'up':
                snakeY -= 10;
                break;
            case 'down':
                snakeY += 10;
                break;
        }

        // Check if the snake's head is colliding with the food.
        if (snakeX === foodX && snakeY === foodY) {
            // The snake has eaten the food.
            // Grow the snake by one unit.
            snakeX += 10;

            // Spawn new food in a random location.
            foodX = Math.floor(Math.random() * canvas.width);
            foodY = Math.floor(Math.random() * canvas.height);
        }

        // Check if the snake has collided with the game grid.
        if (snakeX < 0 || snakeX >= canvas.width || snakeY < 0 || snakeY >= canvas.height) {
            // Game over.
            alert('Game over!');

            // Restart the game.
            restartButton.click();

            return;
        }
    }


   
}

// Handle keyboard input.
document.addEventListener('keydown', function (event) {
    switch (event.keyCode) {
        case 37: // Left arrow
            if (snakeDirection !== 'right') {
                snakeDirection = 'left';
            }
            break;
        case 38: // Up arrow
            if (snakeDirection !== 'down') {
                snakeDirection = 'up';
            }
            break;
        case 39: // Right arrow
            if (snakeDirection !== 'left') {
                snakeDirection = 'right';
            }
            break;
        case 40: // Down arrow
            if (snakeDirection !== 'up') {
                snakeDirection = 'down';
            }
            break;
    }
});

// Start the game loop.
setInterval(updateSnake, 100);
setInterval(draw, 100);
