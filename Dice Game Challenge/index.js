var image1 = document.querySelectorAll("img")[0];
var image2 = document.querySelectorAll("img")[1];

var startTime = Date.now();
var rollInterval = setInterval(changeDiceImages, 300);

function changeDiceImages() {
    var currentTime = Date.now();
    var elapsedTime = currentTime - startTime;

    if (elapsedTime >= 1000) {
        clearInterval(rollInterval);
        rollDice();
        return;
    }

    var randomIndex1 = Math.floor(Math.random() * 6) + 1;
    var randomIndex2 = Math.floor(Math.random() * 6) + 1;

    image1.setAttribute("src", "images/dice" + randomIndex1 + ".png");
    image2.setAttribute("src", "images/dice" + randomIndex2 + ".png");
}

function rollDice() {
    // for player 1
    var randomNumber1 = Math.floor(Math.random() * 6) + 1; // 1-6
    var randomDiceImage = "images/dice" + randomNumber1 + ".png"; // dice1.png-dice6.png
    image1.setAttribute("src", randomDiceImage);

    // for player 2
    var randomNumber2 = Math.floor(Math.random() * 6) + 1; //1-6
    var randomDiceImage2 = "images/dice" + randomNumber2 + ".png"; // dice1.png-dice6.png
    image2.setAttribute("src", randomDiceImage2);

    if (randomNumber1 > randomNumber2) {
        document.querySelector("h1").innerHTML = "Player 1 Wins!!"
    }
    else if (randomNumber1 < randomNumber2) {
        document.querySelector("h1").innerHTML = "Player 2 Wins!!"
    }
    else {
        document.querySelector("h1").innerHTML = "Draw!!"
    }
}

// refresh function
function refresh() {
    window.location.reload();
}
