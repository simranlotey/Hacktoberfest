const tilesContainer = document.querySelector(".tiles");
const colors = ["green", "aquamarine", "crimson", "blue", "dodgerblue", "gold", "greenyellow", "teal"]
const colorsPickList = [...colors, ...colors];
const tileCount = colorsPickList.length;

//Game State
let revealedCount = 0;
let activeTile = null;
let awaitingEndOfMove = false;

function buildTile(color){
    const element = document.createElement("div");
    element.classList.add("tile");
    element.setAttribute("data-color",color)
    element.setAttribute("data-revealed", "false");


    element.addEventListener("click", () =>{
        const revealed = element.getAttribute("data-revealed");

        if (awaitingEndOfMove 
            || revealed === "true"
            || element === activeTile){
           return;
        }

        element.style.backgroundColor = color
        if (!activeTile){
            activeTile = element;
            return;
        }

        const colorToMatch = activeTile.getAttribute("data-color");
        if (colorToMatch === color) {
            activeTile.setAttribute("data-revealed","true");
            element.setAttribute("data-revealed","true");

            awaitingEndOfMove = false;
            activeTile = null;
            revealedCount += 2;
            

            if (revealedCount === tileCount){
                alert('You won<3 Refresh the Site to start again')
            }

            return;
            
        }

        awaitingEndOfMove = true;
        setTimeout( () => {
            element.style.backgroundColor = null;
            activeTile.style.backgroundColor = null;
            awaitingEndOfMove = false;
            activeTile = null;
        },1000);
    })
    return element;
}

//Build up Tiles
for (let i = 0; i < tileCount; i++){

    const randomIndex = Math.floor(Math.random() * colorsPickList.length);
    const color = colorsPickList[randomIndex];
    const tile = buildTile(color)

    colorsPickList.splice(randomIndex, 1);
    
    tilesContainer.appendChild(tile)
}
