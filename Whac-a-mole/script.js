const gameContainer = document.querySelector(".container");
const allMoleItems = document.querySelectorAll(".item");
let startGame,
  startTime,
  countDown = 20,
  score = 0;

const timeCount = document.getElementById("time-count");
const scoreCount = document.getElementById("score-count");

gameContainer.addEventListener("click", function (e) {
  if (e.target.classList.contains("mole-clicked")) {
    score++;
    scoreCount.innerHTML = score;

    const bushElem = e.target.parentElement.previousElementSibling;

    let textEl = document.createElement("span");
    textEl.setAttribute("class", "whack-text");
    textEl.innerHTML = "whack!";
    bushElem.appendChild(textEl);

    setTimeout(() => {
      textEl.remove();
    }, 1000);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  // total game time is 20 seconds
  startTime = setInterval(() => {
    timeCount.innerHTML = countDown;
    countDown--;
  }, 1000);

  startGame = setInterval(() => {
    showMole();
  }, 500);
});

// shows mole
function showMole() {
  if (countDown <= 0) {
    clearInterval(startGame);
    clearInterval(startTime);
    timeCount.innerHTML = "0";
  }
  let moleToAppear = allMoleItems[getRandomValue()].querySelector(".mole");
  moleToAppear.classList.add("mole-appear");
  hideMole(moleToAppear);
}

function getRandomValue() {
  let rand = Math.random() * allMoleItems.length;
  return Math.floor(rand);
}

// hide Mole
function hideMole(moleItem) {
  setTimeout(() => {
    moleItem.classList.remove("mole-appear");
  }, 1000);
}
// Get a reference to the reload button
const reloadButton = document.getElementById("reload-button");

// Add a click event listener to the button
reloadButton.addEventListener("click", () => {
  // Reload the page when the button is clicked
  location.reload();
});
