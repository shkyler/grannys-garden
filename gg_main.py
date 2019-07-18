# This is the main file for the grannys garden game
from level01 import gg_trees
from level01 import gg_mounts
from level01 import gg_woodcutters
# Start by printing a splash screen
print("                         WELCOME TO GRANNYS GARDEN                      ")
def play_game():
  gg_trees.tree_game()
  # the second game is the kingdom of the mountains - details are in gg_mounts.py    
  gg_mounts.mounts_game()
  # the third game is the woodcutters house - details are in gg_woodcutters.py    
  gg_woodcutters.outside()
#gg_trees.tree_game()
play_game()