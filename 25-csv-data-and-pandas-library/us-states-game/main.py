# https://www.sporcle.com

# when using images in turtle they have to be converted to gif

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# we can make the shape of a turtle be an image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# example of how the teacher got the coordinates for the csv file
# def get_mouse_click_coordinates(x, y):
#     print(x, y)


# # event listener like key pressed
# turtle.onscreenclick(get_mouse_click_coordinates)


def make_guess(current, total):
    # make guess
    answer_state = screen.textinput(title=f"Guess the State {current}/{total}", prompt="Type a state name:").title()
    # print(answer_state)
    return answer_state


def read_states():
    # read csv with states
    state_data = pandas.read_csv("50_states.csv")
    # want to reformat the dict cause it feels bad to work with it in this structure
    states_raw_dict = state_data.to_dict()
    states_reformatted_dict = {}

    for state_index in range(0, len(states_raw_dict["state"])):
        state_name = states_raw_dict['state'][state_index]
        state_x_coord = states_raw_dict['x'][state_index]
        state_y_coord = states_raw_dict['y'][state_index]
        # print(f"{state_name} - X: {state_x_coord}, Y: {state_y_coord}")
        states_reformatted_dict[state_name] = {
            'x': state_x_coord,
            'y': state_y_coord
        }

    # print(states_reformatted_dict)
    return states_reformatted_dict


def lecturer_solution_main_takeaways():
    # read csv with states
    state_data = pandas.read_csv("50_states.csv")
    # tip: pandas can use csv column header names as attributes
    # way more elegant than what I did in def read_states():
    state_names = state_data.state.to_list()
    print(state_names)
    # ...
    # ...
    state_name = state_data[state_data.state == "Ohio"]
    print(state_name.state.item())


# lecturer_solution_main_takeaways()

states_guessed = 0
states_dict = read_states()
total_states = len(states_dict)
correct_guesses = []
while states_guessed < total_states:
    guess = make_guess(states_guessed, total_states)

    if guess.lower() == "exit":
        turtle.bye()
        break

    # check if guess is valid
    if guess in states_dict and guess not in correct_guesses:
        print(f"Guessed {guess} correctly!")
        states_guessed += 1
        correct_guesses.append(guess)
        # write state on screen
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(states_dict[guess]['x'], states_dict[guess]['y'])
        state_text.write(f"{guess}", align="center", font=("Courier", 15, "normal"))
    elif guess in correct_guesses:
        print(f"Already guessed {guess}!")
    else:
        print(f"Nope, there is no {guess}!")

# collect and save the states which we didn't manage to guess
missing_states = []
state_names_list = list(states_dict.keys())
# without list comprehension
# for state_index in range(0, total_states):
#     if state_names_list[state_index] not in correct_guesses:
#         missing_states.append(state_names_list[state_index])

# with list comprehension DAMN
[missing_states.append(state_names_list[state_index]) for state_index in range(0, total_states) if
 state_names_list[state_index] not in correct_guesses]

pandas.read_csv("50_states.csv")
# covert it into dict before making it into a dataframe for easier readability
missing_states_dt = pandas.DataFrame({'State': missing_states})
print(missing_states_dt)
missing_states_dt.to_csv("missed_states.csv")

# keeps screen open
turtle.mainloop()
