import turtle
import csv
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Get x and y coordinates on mouse click
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()




# solution with csv
# answer_state = turtle.textinput("Guess the state", "What's another state name ?")
# with open('50_states.csv', 'r') as csvfile:
#     data = csv.DictReader(csvfile)
#     data_as_dict = list(data)
#
# for state_dict in data_as_dict:
#     if state_dict['state'].lower() == answer_state.lower():
#         print(state_dict)
#         turtle.penup()
#         turtle.teleport(int(state_dict['x']), int(state_dict['y']))
#         turtle.write(f"{state_dict['state']}", align="center", font=('Arial', 12, 'normal'))

# Solution with pandas
data = pd.read_csv('50_states.csv')
all_states = data.state.tolist()
all_matched_states = []
count_of_state = 0
t = turtle.Turtle()
t.hideturtle()
t.penup()


while count_of_state < len(all_states):
    answer_state = turtle.textinput(f"{count_of_state}/{len(all_states)} States Correct", "What's another state name ?").lower()
    if answer_state == "exit":
        break
    matches = data[data.state.str.lower() == answer_state]
    if len(matches) == 1:
        matched_state = matches.iloc[0].to_dict()
        if matched_state not in all_matched_states:
            all_matched_states.append(matched_state)
            t.teleport(int(matched_state['x']), int(matched_state['y']))
            t.write(matched_state['state'])
            count_of_state += 1

# turtle.mainloop()

# screen.exitonclick()