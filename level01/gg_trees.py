# this contains the functions for the magic trees game
# import required libraries
import numpy as np
import time

# define a list of allowed letters and numbersfor the tree grid
letters = ['a','b','c','d']
numbers = [1,2,3]
# define a list of all possible combinations of these for the user to enter
allowed_options = []
for i in letters:
    for j in numbers:
        allowed_options.append(i+ str(j))
# set the magic tree to a1        
magic_tree = "a1"

# define a function to pick a tree at random and return the value
def pick_tree():
    global letters
    global numbers
    letter = np.random.choice(letters)
    number = str(np.random.choice(numbers))
    return(letter + number)

# define a function to generate a random tree and ask the user to pick one
def enter_choice(game_mode):
    global magic_tree
    global allowed_options
    # if the user enters 't' - the magic tree is set to a1 as a cheat
    if game_mode == "t":
        magic_tree = "a1"
    # otherwise - a random tree is picked   
    elif game_mode =="y":    
        magic_tree = pick_tree()
    # check the entered choice against the allowed values    
    choice = input("Which one do you think it is?")
    while choice not in allowed_options:
        choice = input("Sorry, thats not a valid tree. Please pick a valid option")
    # let the user keep guessing until they guess the correct tree
    if choice == magic_tree:
        print("Correct, the magic tree was, ", magic_tree)
    else:
        print("Sorry, there is not enough magic in that tree!")
        enter_choice(game_mode)

# define a function that plays the magic trees game on the console    
def tree_game(game_mode):
    print("========================================================================")
    print("=                                                                      =")
    print("=          ^              ^                ^                 ^         =")
    print("=   3     ^ ^            ^ ^              ^ ^               ^ ^        =")
    print("=          |              |                |                 |         =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("=          ^              ^                ^                 ^         =")
    print("=   2     ^ ^            ^ ^              ^ ^               ^ ^        =")
    print("=          |              |                |                 |         =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("=          ^              ^                ^                 ^         =")
    print("=   1     ^ ^            ^ ^              ^ ^               ^ ^        =")
    print("=          |              |                |                 |         =")
    print("=                                                                      =")
    print("=          a              b                c                 d         =")
    print("=                                                                      =")
    print("========================================================================")
    print("There is a magic tree here!")
    time.sleep(2)
    enter_choice(game_mode)
    






