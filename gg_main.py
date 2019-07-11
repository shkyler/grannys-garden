# This is the main file for the grannys garden game
from level01 import gg_trees
from level01 import gg_mounts
from level01 import gg_woodcutters
# Start by printing a splash screen and asking the user would they like to play
print("                         WELCOME TO GRANNYS GARDEN                      ")
start = input("                                  Ready to start?                       ")
# the first game is the magic tree game - details are in gg_trees.py
# as a cheat, if the user enters 't' - we set the magic tree to 'a1'
if start == "t":
    gg_trees.tree_game("t")
elif start == "y":
    gg_trees.tree_game("y")
elif start == "n":
    print("OK, bye!")
    quit()
# the second game is the kingdom of the mountains - details are in gg_mounts.py    
gg_mounts.mounts_game()
# the third game is the woodcutters house - details are in gg_woodcutters.py    
gg_woodcutters.outside()