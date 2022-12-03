import pandas
import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(f"Guessed states: {len(guessed_states)}/50", "Enter a new state: " ).title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in list_of_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)