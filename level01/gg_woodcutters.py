# the woodcutters house
import time
inventory = []

def fig_puzzle():
  # introduce the puzzle
  time.sleep(1)
  print("Before you can go in you must solve a little puzzle.")
  time.sleep(1)
  # ask the user to guess the word
  answer = input("There is a secret word on the house. What is it?").lower()
  # if they get it wrong - give them the first clue and ask again
  if answer != "fig":
    time.sleep(1)
    print("No. The word is on the wall")  
    time.sleep(1)  
    answer = input("There is a secret word on the house. What is it?").lower()
    # if they get it wrong again - give them the second clue and ask again
    if answer != "fig":
      time.sleep(1)
      print("No. The word is typed with asterixes.") 
      time.sleep(1)
      answer = input("There is a secret word on the house. What is it?").lower()
      # if they get it wrong a thord time - use a loop to tell them the answer and keep asing until they get it right
      while answer != "fig":
        time.sleep(1)
        print("No. The word is FIG.") 
        time.sleep(1)
        answer = input("There is a secret word on the house. What is it?").lower()
      
def stick():
  global inventory
  time.sleep(1)
  print("We are in the hallway.")
  time.sleep(1)
  print("It is very dark but you can see a long stick by the wall.")
  time.sleep(1)
  take_stick = input("Are you going to take it?").lower()
  if take_stick in ["y", "yes"]:
    inventory.append("stick")
    time.sleep(1)
    print("You now have a stick and an apple")

def cupboard():
  print("cupboard")
  hallway()

def stairs():
  print("stairs")
  hallway()

def kitchen():
  print("kitchen")
  hallway()

def backroom():
  print("backroom")
  hallway()  

def hallway():
  # define a list of rooms adjacent to the hallway
  hallway_rooms = ["kitchen", "backroom", "cupboard", "stairs"]
  time.sleep(1)
  # introdce the hallway
  print("We are in the hallway.")
  print("It is very dark but you can see")
  time.sleep(1)
  print("a door leading to the kitchen")
  time.sleep(1)
  print("a door leading to the backroom")
  time.sleep(1)
  print("a cupboard")
  time.sleep(1)
  print("and some stairs")
  time.sleep(1)
  # ask the user where they want to go and validate input
  next_room = input("Where do you wish to go?").lower()
  while next_room not in hallway_rooms:
    next_room = input("Where do you wish to go?").lower()
  # go to the selected room  
  if next_room == "kitchen":
    kitchen()
  elif next_room == "backroom":
    backroom()
  elif next_room == "cupboard":
    cupboard()
  elif next_room == "stairs":
    stairs()     


def outside():
  # this function acts as a main function for this part of the game
  global inventory
  # print the graphic
  print("========================================================================")
  print("=        ___                                                           =")
  print("=       |   |________________________________________                  =")
  print("=      /                                             \                 =")
  print("=     /                                               \                =")
  print("=    /_________________________________________________\               =")
  print("=     |                   ***_______                   |               =")
  print("=     |                    *________|                  |               =")
  print("=     |                    *                           |               =")
  print("=     |     *******___    ***                          |     §         =")
  print("=     |     *_________|                                |    §§§        =")
  print("=     |     ******____|                 ******         |   §O§§§       =")
  print("=     |     *                           *              |  §O§§O§§      =")
  print("=     |     *         ()        ()      *  ***   ()    |   § % §       =")
  print("=     |         ()    ()    ()  ()      *    *   ()    |     %         =")
  print("=     |_________()____()____()__()______******___()____|     %         =")
  print("=                                                                      =")
  print("=                                                                      =")
  print("========================================================================") 
  # introduce the house ans ask th user if they want to enter
  print("This is the Woodcutter's house")
  time.sleep(1)
  house_entry = input("Would you like to go in?").lower()
  while house_entry not in ["y","n","yes","no"]:
    time.sleep(1)
    house_entry = input("Would you like to go in?").lower()
  if house_entry in ['n','no']:
    time.sleep(1)
    print("Come on. You will have to be brave.")
  # call the fig puzzle function
  fig_puzzle()
  time.sleep(1)
  # once the puzzle is solved procede
  print("Now we can go inside but we must be very careful.")
  time.sleep(1)
  print("The Witch has set some traps for you!")
  # ask the user if they want an apple - dont take 'NO' for an answer!
  apple = input("Would you like to take an apple from the tree?").lower()
  while apple not in ["yes", "y"]:
    apple = input("Would you like to take an apple from the tree?").lower()
  # add the apple to inventory
  time.sleep(1)
  print("Keep the apple safe.")
  print("I will let us in now.")
  time.sleep(1)
  inventory.append("apple") 
  # go inside - ask does the user want to take the stick
  stick()    
  # start exploring from the hallway
  hallway()
outside()    