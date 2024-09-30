import turtle
import pandas
from states import Display

screen = turtle.Screen()
screen.title("U.S. States Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(725, 491)

data = pandas.read_csv('50_states.csv')
states = Display()

all_states = data.state.to_list()
correct_guesses = 0

# This was used to get the x, y cords inside the csv
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)

while correct_guesses != 50:
    answer_state = screen.textinput(
        title=f"{correct_guesses}/50 States Correct.", prompt="What's another states' name?").title()
    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        # Removes the correct guess out of the list so it won't be checked again
        all_states.remove(answer_state)
        state = data[data.state == answer_state]
        cords = (state.x.item(), state.y.item())
        states.show_state(answer_state, cords)
        correct_guesses += 1
