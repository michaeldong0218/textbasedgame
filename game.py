import termcolor
import random
import playsound
import art

print(termcolor.colored(art.text2art("Planet Omar"), "cyan"))
print ("Welcome to Planet Omar adventure game!")
print ("Would you like to start the game or read the rules and info?")
choice = input("Type start or rules: ")
if choice == "rules":
    print("In this game, you are playing as Omar, you and Daniel get lost in the London Underground.") 
    print("Try to make your way to the science museum on your own, while trying to evade zombies. Good luck!")
    input("press enter to continue: ")

name = input('\nPlease enter your name: ')
age = int(input('please enter your age: '))

def checkage(age):
    if age <= 8:
        result = False
    else:
        result = True 
    return result
if checkage(age):
    print("\nName: " + name)
    print("Age: " + str(age))
    print("Welcome to the game. enjoy!")
    input()
else:
    print("You are too young to play this game, sorry!")
    exit()

print("You and daniel are lost in the London Underground. You have a decision to make.") 
print("Do you want to go above ground, or stay underground?")
ground = False
while not ground:
    ground = input("Above ground[1] or underground [2]: ")
    if '1' in ground:
        ground = True
    elif '2' in ground:
        ground = True
    else:
        print("Sorry, incorrect answer, print either 1 or 2")

if ground == '1':
    print("\nYou and Daniel make your way up the stairs and are in the open in London.") 
    print("Where do you want to go now?")
elif ground == '2':
    print("\nYou and Daniel stay undeground and wait for the next subway to come.")

    
