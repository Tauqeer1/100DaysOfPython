import random

from art import logo, vs
from game_data import data

def get_random_option():
    return random.choice(data)

def format_data(option):
    return f"{option['name']}, a {option['description']}, from {option['country']}"

def get_follower_count(option):
    return option['follower_count']

def check_answer(selection_option, follower_count_a, follower_count_b):
    return (selection_option == 'A' and follower_count_a > follower_count_b) or (selection_option == 'B' and follower_count_b > follower_count_a)


def game():
    print(logo)
    score = 0
    is_game_end = False
    option_a = get_random_option()
    option_b = get_random_option()

    while is_game_end != True:
        
        while option_a == option_b:
            option_b = get_random_option()
        
        print(f"Compare A: {format_data(option_a)}")
        print(vs)
        print(f"Against B: {format_data(option_b)}")

        user_selected_option = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        follower_count_a = get_follower_count(option_a)
        follower_count_b = get_follower_count(option_b)
        

        if check_answer(user_selected_option, follower_count_a, follower_count_b):
            score += 1
            option_a = option_b
            option_b = get_random_option()
            print(f"You're right! Current score: {score}")
        else:
            is_game_end = True
            print(f"Sorry, that's wrong. Final score: {score}")
            
game()
