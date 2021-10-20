print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

game_active = False

while not game_active:
  game_start = input("Enter 'START' to start your adventure!\nReady? ")
  game_start = game_start.upper()
  if game_start == "START":
    game_active = True


while game_active:
  print("You're in the forest, on your way to the next village... but something happens. A sheet of paper blows towards you in the wind. You catch it and find out, it's a treasure map! You decide to look for the treasure on this map! You head into the next town to prepare for the dangerous adventure. You head into the shop and you only have enough gold for 'ARMOR', a 'SHIELD, and a 'SWORD'. Which will you choose?")
  
  choice_1 = input("You choose to buy the ('ARMOR', 'SHIELD', 'SWORD'): ")

  if choice_1 == "ARMOR":
    print("You equip the ARMOR and continue your journey. It was a tight fit, but you'll be safe from attacks! According to the map, the treasure is on an island! The island is just up ahead, and you think about how to get there! Swimming isn't an option because you're wearing armor. You found a small boat, but it sank because the armor is too heavy! You try to take off the armor but it's stuck! You decide to go back to the village for the day, still trying to get the armor off during the entire walk. You see a doctor and they say, you are stuck in the suit of armor forever. You give up.\nGAME OVER...")
    game_active = False
  elif choice_1 == "SHIELD":
    print("You equip the SHIELD... or try to. It's too heavy for you! You pick it up to exit the store, only to immediately drop it outside. It's much too heavy to carry around! You decide to return it, but the clerk says you've already paid for it and dragged it ouside! NO REFUNDS! Without any equipment, you aren't ready to look for the treasure! With all your might, you try picking up the shield one more time... You hurt your back...\nGAME OVER...")
    game_active = False
  elif choice_1 == "SWORD":
    print("You equip the SWORD and continue your journey. According to the map, the treasure is on an island! The island is just up ahead, and you think about how to get there! You realize you have two options: 'SWIM' or find a 'BOAT'")

  choice_2 = input("You choose to ('SWIM', 'BOAT'): ")
  
  if choice_2 == "SWIM":
    print("You start swimming over to the island. Oh no! Halfway through, you got a cramp! There's no land nearby and you're too far from the shore to rest! You start sinking, losing your vision... You start drowning and everything is dark.\nGAME O-\n\nWAIT! You woke up! You find yourself on the shore of Treasure Island! You see something move quickly in the water, swimming away from you gracefully. You were saved. You rest for a bit and continue your journey, into the temple. There are two doors... 'LEFT' and 'RIGHT', which will you open?")
  elif choice_2 == "BOAT":
    print("You decide to boat across. You got lucky and found a boat! You take the boat and start sailing towards the island. Suddenly, you're attacked by arrows. You hear a yell, 'SOMEONE STOLE OUR BOAT!' Arrows continue to head in your direction. You paddle faster. You're struck in the shoulder with an arrow! You bleed heavily and can't paddle anymore! The attackers swim towards you... 'THIS IS THE END'\nGAME OVER...")
    game_active = False

  choice_3 = input("You chose the door on the ('LEFT', 'RIGHT'): ")

  if choice_3 == "LEFT":
    print("You enter the left door... and fall into a pit... So close to the treasure, but unfortunate turn of events.\nGAME OVER...")
  elif choice_3 == "RIGHT":
    print("You enter the right door... and see a chest. You slowly walk up to it, avoiding possible traps... but calm down after realizing this room has no traps. You rush over to open the chest. Inside, you find a note... it says, 'Why'd you follow a random map flying your way and think it was a good idea?' You questioned your life decisions...\nADVENTURE COMPLETE, TREASURE ACQUIRED!")

  game_active = False