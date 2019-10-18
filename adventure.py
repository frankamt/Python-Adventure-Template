__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our game,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    print(text2art('Ant', font='alpha'))
    print(text2art('Arc', font='alpha'))
    print(text2art('Tic', font='alpha'))
    print(text2art('Dude', font='alpha'))

def north():
    print ("To go north press n then enter")

def east():
    print ("To go east press e then enter")

def south():
    print ("to go south press s then enter")

def west():
    print ("To go west press w then enter")

def diary():
    print ("If you want to read Diary of a Wimpy Kid type D")

def catch():
    print ("If you want to read Catcher in the Rye type R")

def vert():
    print ("If you want to read American Vertigo type A")

def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name, explorer?")
    #randint is a great way of adding some variety to your players statistics through randomness
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you an explorer?", "Are you from this base?", "There is a snow storm heading towards research base"]
    npcnamechoice = ["Bzork", "Jormes", "Jojo Siwa", "Joe"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the scientist")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "JOOOOOOEEEEE"
    print ("\nSuddenly you hear a roar, and from the shadows you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Strength" % str(enemyMP))


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to the land of Antarctica, %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your strength is" + " " + str(MP))
sleep(2)


print ("Would you like to venture out onto the tundra? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You are in your home, with a roaring fireplace in front of you, above the fire you can see your knife and forcefield")
    print ("Would you like to take your knife and forcefield? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("knife")
        weapons.append("forcefield")
        print ("You are now carrying your %s and your %s" % (weapons[0], weapons[1]))
        print ("Armed with your %s and %s you swing open the door to your home and see endless ice in all directions." % (weapons[0], weapons[1]))
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see endless ice in all direction.")
else:
    print ("You stay at home, sat in your favourite chair watching the fire get bigger. Antarctica no longer has a hero. But...")
    sleep(2)
    diary()
    catch()
    vert()
    move = input("What book would you like to read?")
    if move == 'R':
        print ("You made the right choice.")
        print ("You live happily ever after. Game Over.")
        sys.exit(0)
    elif move == 'D':
        print ("You suck.")
        print ("You're dead. Game Over.")
        sys.exit(0)
    elif move == 'A':
        print ("You suck")
        print ("You're dead. Game Over")
        sys.exit(0)
    else:
        print ("Reading is good, not reading is bad. YOU SUCK!")
        print ("Game Over.")
        sys.exit(0)

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A scientist is in your path and greets you")
    print ("It's nice and sunny, maybe it's not the day to be a hero")
    print ("You return home and make a fire. On that fire you prepare your scrambled eggs. You want to read a book, but which book?")
    sleep(2)
    diary()
    catch()
    vert()
    move = input("What book would you like to read?")
    if move == 'R':
        print ("You made the right choice.")
        print ("You live happily ever after. Game Over.")
        sys.exit(0)
    elif move == 'D':
        print ("You suck.")
        print ("You're dead. Game Over.")
        sys.exit(0)
    elif move == 'A':
        print ("You suck")
        print ("You're dead. Game Over")
        sys.exit(0)
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the research base which lies to the east of your home.")
    print ("A scientist is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the seals, stopping to take in the beauty")
    print ("A seal is in your path and greets you\n")

villager()
enemy()
sleep()

fight = input("Do you wish to fight?" )

if fight == "y":
    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You swing your knit and cause %s of damage" % str(hit))
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,3)
        print ("Your enemy swings a club at you and causes %s of damage" % str(enemyhit))
        HP = HP - enemyhit
        print (HP)
else:
    print ("You turn and run away from your enemy")

print ("This is where this template ends, this is now YOUR world, build your adventure and share it with the world")

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|)")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/)")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")