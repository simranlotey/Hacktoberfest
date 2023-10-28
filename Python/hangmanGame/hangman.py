import sys
def draw_hangman(chances):
    if chances == 6:
        print("________ ")
        print("| | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")
        print("\n\n Game Over! You Lose")
        sys.exit(0)

def mainLoop():
    text = "helloew"
    textLength = len(set(text))  # without repeated chars
    
    chances = 7
    gameEnd = False

    validGuess = []

    while chances!= 0 or gameEnd:
        if len(validGuess) == textLength:
            gameEnd = True
            print("You win")
            sys.exit(0)

        guess = input("Guess the word, character by character: ")[0]
        if guess in text:
            if guess not in validGuess:
                validGuess.append(guess)
            print("".join([c if c in validGuess else "_" for c in text]))

        else:
            chances-=1
            draw_hangman(chances)

mainLoop()