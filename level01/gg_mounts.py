# this contains the functions for the kingdom of the mointains
import time

# this contains the dialoge while you are in the cave
def cave():
  # introduce the scenario
  time.sleep(2)
  print("You are inside the secret cave")
  time.sleep(2)
  print("The King and Queen of the mountains have been locked away in here by a Wicked Witch")
  time.sleep(2)
  print("Their 6 children have been taken away and hidden by the Witch")
  time.sleep(2)
  # ask does the user want to help - we only accept yes or y as an answer
  help_them = input("Would you like to help the King and Queen?").lower()
  while help_them not in ["y", "yes"]:
    print("That's not very nice!")
    time.sleep(1)
    help_them = input("Would you like to help the King and Queen?").lower()
  time.sleep(2)
  # explain what has to be done
  print("You must try to find the missing children.")
  time.sleep(2)
  print("The first one to look for is a girl called Esther.")
  time.sleep(2)
  print("The King and Queen's pet Raven will help you")
  time.sleep(2)
  # introduce the raven
  print("========================================================================")
  print("=                                                                      =")
  print("=                                             ***                      =")
  print("=                                          *********                   =")
  print("=                                     **********  ****                 =")
  print("=                 ***************************************              =")
  print("=           ****************************************************       =")
  print("=                  **************************************     **       =")
  print("=                      *****************************                   =")
  print("=                         ************************                     =")
  print("=                             *******************                      =")
  print("=                                *************                         =")
  print("=                                   *****                              =")
  print("=                                   *  *                               =")
  print("=                                   *  *                               =")
  print("=                                   * *****                            =")
  print("=                                   *                                  =")
  print("=                                *******                               =")
  print("========================================================================")
  time.sleep(2)
  print("I am the King and Queen's pet Raven.")
  time.sleep(2)
  print("I have MAGIC powers")
  # ask do they want the raven to help
  raven_help = input("Would you like me to help you?").lower()
  while raven_help not in ["y", "n", "yes", "no"]:
    time.sleep(1)
    raven_help = input("Would you like me to help you?").lower()
  if raven_help in ["n", "no"]:
    time.sleep(1)
    print("I am very sorry but the king and queen say I must help you.")
  time.sleep(2)  
  # go to the woodcutters house
  print("We must go to the Woodcutter's house.")
  time.sleep(2)
  print("The Witch has made the Woodcutter leave his home.")
  time.sleep(2)
  print("Now it is a prison for Esther.")
  time.sleep(2)
  
  # is the user ready to go
  ready = input("Are you ready to come with me?").lower()
  while ready not in ["y", "n", "yes", "no"]:
    time.sleep(1)
    ready= input("Are you ready to come with me?").lower()
  if ready in ["n", "no"]:
    time.sleep(1)
    print("Don't be silly. You are ready.")
    time.sleep(1)
    
def cave_enter():
  print("========================================================================")
  print("=          ^                           _____                           =")
  print("=         / \                         /     \                          =")
  print("=        /   \                   ____/       \                         =")
  print("=       /     ----------        |             \                        =")
  print("=      /                |      /               \-------------          =")
  print("=     /                  \    |      _/*\_                   \         =")
  print("=    /     ^    ^    ^    \ /       |*****|               ^   \        =")
  print("=   /     ^ ^  ^ ^  ^ ^            /*******\             ^ ^   \       =")
  print("=          |    |    |                                    |     |      =")
  print("=                                                                      =")
  print("=                                                                      =")
  print("=                                                            ^         =")
  print("=                                                           ^ ^        =")
  print("=                                                            |         =")
  print("=                                                                      =")
  print("=                                                                      =")
  print("=                                                                      =")
  print("========================================================================")
  time.sleep(1)  
  cave_check = input("Can you see a cave?").lower()
  while cave_check not in ["y","n","yes","no"]:
    cave_check = input("Can you see a cave?").lower()
  if cave_check in ['n','no']:
    time.sleep(1)
    print("Of course you can")

  cave_entry = input("Do you want to go into the cave?").lower()  
  while cave_entry not in ["y","n","yes","no"]:
    cave_entry = input("Do you want to go into the cave?").lower()
  if cave_entry in ['n','no']:
    print("Yes you do")
  cave()

def mounts_game():
    print("========================================================================")
    print("=          ^                           _____                           =")
    print("=         / \                         /     \                          =")
    print("=        /   \                   ____/       \                         =")
    print("=       /     ----------        |             \                        =")
    print("=      /                |      /               \-------------          =")
    print("=     /                  \    |      _/*\_                   \         =")
    print("=    /     ^    ^    ^    \ /       |*****|               ^   \        =")
    print("=   /     ^ ^  ^ ^  ^ ^            /*******\             ^ ^   \       =")
    print("=          |    |    |                                    |     |      =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("=                                                            ^         =")
    print("=                                                           ^ ^        =")
    print("=                                                            |         =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("=                                                                      =")
    print("========================================================================")
    print("Welcome to the KINGDOM OF THE MOUNTAINS")
    time.sleep(2)
    # check does the user have a password
    password_check = input("Do you have a password?").lower()
    # validate theinput with a while loop
    while password_check not in ["y","n","yes","no"]:
      password_check = input("That is not a valid answer").lower()
    # if there is no password go to the cave  
    if password_check in ["n", "no"]:
      cave_enter()
    # otherwise ask for the password  
    elif password_check in ["y", "yes"]:
      password = input("Please enter password: ").lower()
      # validate password with a loop
      while password not in ["sky", "river", "snow"]:
        password = input("Sorry, that is not a valid password")
      # user the password to skip to the correct level  
      if password == "snow":
        print("Level 2")
      elif password == "river":
        print("Level 3")
      elif password == "sky":
        print("Level 4")  
#mounts_game()        