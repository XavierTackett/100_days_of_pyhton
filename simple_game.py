#Treasures island game 

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Different paths to choose
choice = input("You're at a lake house in the forest, do you go right or left?\n")
if choice == "left":
  choice2 = input("You've made it to the docks, do you want to 'wait' or 'swim' across?\n").lower()
  if choice2 == "wait":
    choice3 = input("You've made it to the island, theres three doors a red one, blue one, and a yellow one? which one do you choose?\n").lower()
    if choice3 == "red":
      print ("You walked into the dragons den, Game Over")
    elif choice3 == "blue":
      print("You fell into a well and drowned, Game Over")
    elif choice3 == "yellow":
      print ("you've made it to ther safe house, !!!!YOU WON!!!!")
    else:
      print("That door doesn't exist, Game Over")
  else:
    print("The monster of the lake pulled you down, Game Over")
else:
  print("The forest creatures captured you and ate you, Game Over")
 
