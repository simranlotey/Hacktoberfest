import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("Indian States and Union Territories Game")
image = "indian_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states.csv")
states_list = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 35:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/35 States Correct", prompt="What's another state's "
                                                                                            "name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Learn.csv")
        break
    if answer_state in states_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


screen.exitonclick()
