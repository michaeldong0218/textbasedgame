import termcolor
import random
import art
#------------------------------------------
# functions 
def getgroundinput(correct):
    while not correct:
        answer = input("Stay on the subway [1] or go to the surface [2]: ")
        if answer == '1':
            correct = True
        elif answer == '2':
            correct = True
        else:
            print("\nPlease print either 1 to stay on the subway or 2 to go to the surface")
    return answer 

def checkage(age):
    if age >= 8:
        result = False
    else:
        result = True 
    return result

def directionChoice(correct):
    answer = False
    while not correct:
        print("Choose what direction you want to go: \n  N for North \n  E for East \n  S for South \n  W for West")
        answer = input("Enter either N, E, S, or W: ")
        if answer.lower() == 'n' or answer.lower() == 'e' or answer.lower() == 's' or answer.lower() == 'w':
            correct = True
        else: 
            print("\nWrong answer, please enter N, E, S, or W.")
    return answer.lower()
# ------------------------------------------

#start of game
print(termcolor.colored(art.text2art("Planet Omar"), "cyan"))
print ("Welcome to Planet Omar adventure game!")
print ("Would you like to start the game or read the rules and info?")
choice = input("Type start or rules: ")
if choice == "rules":
    print("\nIn this game, you are playing as Omar, you and Daniel get lost in the London Underground.") 
    print("Try to make your way to the science museum to reunite with your class. Good luck!")
    input("press enter to continue: ")

name = input('\nPlease enter your name: ')
age = int(input('please enter your age: '))

if checkage(age):
    print("You are too young to play this game, sorry!")
    
else:
    print("\nName: " + name)
    print("Age: " + str(age))
    print("Welcome to the game. enjoy!")
    input()

    print("You and Daniel have been separated from your class that are going to a museum, and are lost in the London Underground. You have a decision to make.") 
    print("Do you want to go above ground, or stay underground?")
    #functionfromtop
    correct = False
    answer = getgroundinput(correct)
    
    if answer == '1':
        print("\nYou and Daniel get onto the next subway.")
        input("....")
        input("....")
        input("....")
        print("\nYou and Daniel have arrived at"+termcolor.colored(" Edgware Road", attrs = ["bold"])+ " station. Do you want to stay on the subway or go to the surface?")
        answer = getgroundinput(correct)
        if answer == '1':
            print("\nYou and Daniel stay on the subway and proceed to Earl's Court station")
            input("....")
            input("....")
            input("....")
            print("You and Daniel have now arrived at"+termcolor.colored(" Earl's Court", attrs = ["bold"])+" station.\nDo you want to stay on the subway or go to the surface?\n")
            answer = getgroundinput(correct)
            #3rdsubway
            if answer == '1':
                print("\nYou and Daniel stay on the subway and proceed to South Kesington station.")
                input(".....")
                input(".....")
                input(".....")
                input(".....")
                print("\nYou and Daniel have arrived at"+termcolor.colored(" South Kensington", attrs = ["bold"])+" station.\n Do you want to stay on the subway or go to the surface?\n")
                answer = getgroundinput(correct)
                if answer == '1':
                    print("\nYou and Daniel stay on the subway and proceed to Victoria Station.")
                    input("\n.....")
                    input("\n.....")
                    print("\nYou and Daniel have now arrived at"+termcolor.colored(" Victoria", attrs = ["bold"])+" Station.\nThis is the terminal station of this line. Please proceed aboveground.")
                    print("\nYou and Daniel are now at"+termcolor.colored(" Victoria", attrs = ["bold"])+" Street.")
                    direction19answer = False
                    while not direction19answer:
                        direction19 = directionChoice(False)
                        if direction19 == 'n':
                            print("\nPolice cars seem to be coming from that direction!\nYou turn back.\n")
                        if direction19 == 's':
                            print("\nThat seems to be the end of the street!\nYou turn back.\n")
                        if direction19 == 'e':
                            print("\nThere seems to be a parade coming through!\n")
                        if direction19 == "w":
                            print("\nYou and Daniel proceed to South Kensington street.\n")
                            input("...")
                            input("...")
                            print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                            direction19answer = True
                    #notfinished, need to add code from below
                elif answer == '2':
                    input("\nYou and Daniel make your way up the stairs and: ")
                        #add emojis here after
                    input("...")
                    input("...")
                    print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                    #ending no.1
            elif answer == '2':
                print("\nYou and Daniel are now at"+termcolor.colored(" Earl's Court", attrs = ["bold"])+ " road.\n")
                direction18answer = False
                while not direction18answer:
                    direction18 = directionChoice(False)
                    if direction18 == "n":
                        print("\nYou just came from that direction! Why go back?")
                    if direction18 == 'w':
                        print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                    if direction18 == 's':
                        print("\nThat seems to be the end of the street!")
                    if direction18 == 'e':
                        print("\nYou and Daniel proceed to South Kensington street.")
                        input("...")
                        input("...")
                        print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                        direction18answer = True
                #notcompleted, need to add code from below
        elif answer == '2':
            print("\nYou and Daniel make your way above the surface, and now are at"+termcolor.colored(" Edgware road", attrs = ["bold"])+" street.\n")
            direction12answer = False
            while not direction12answer:
                direction12answer = False
                while not direction12answer:
                    direction12 = directionChoice(False)
                    if direction12 == 's':
                        print("\nThere is a mysterious building, and you cannot get through.\n")
                    elif direction12 == 'n':
                        print("\nThere is a car accident on the street above!\n")
                    elif direction12 == 'e':
                        print("\nThere seems to be police cars going down that street!\n")
                    elif direction12 == 'w':
                        direction12answer = True
                        print("\nYou and Daniel proceed west to"+termcolor.colored(" Paddington street.", attrs = ['bold'])+"\nWhere do you want to go from here?\n")
                        direction13answer = False
                        while not direction13answer:
                            direction13 = directionChoice(False)
                            if direction13 == 'w':
                                print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.\n")
                            elif direction13 == 'n':
                                print("\nThere is a car accident on the street above!\n")
                            elif direction13 == 'e':
                                print("\nYou just came from that direction! Why go back?\n")
                            elif direction13 == 's':
                                direction13answer = True
                                print("\nYou and Daniel make your way to "+termcolor.colored("Notting Hill Gate ", attrs = ['bold'])+ "street.\n Where do you want to go from here?\n")
                                direction14answer = False
                                while not direction14answer:
                                    direction14 = directionChoice(False)
                                    if direction14 == "n":
                                        print("\nYou just came from that direction! Why go back?\n")
                                    if direction14 == "w":
                                        print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.\n")
                                    if direction14 == 'e':
                                        direction14answer = True
                                        print("\nYou and Daniel proceed to make your way to "+termcolor.colored("Bond street", attrs = ['bold'])+".\nWhere do you go from here?\n")
                                        direction15answer = False
                                        while not direction15answer:
                                            direction15 = directionChoice(False)
                                            if direction15 == 'n':
                                                print("\nThe policemen seem to have made a blockage for a previous accident.\nYou turn back.\n")
                                            if direction15 == 'e':
                                                print("\nThere is still a massive parade going through!\nYou and Daniel turn back.\n")
                                            if direction15 == "w":
                                                print("\nYou just came from that direction! Why go back?\n")
                                            if direction15 == "s":
                                                direction15answer = True
                                                print("\nYou and Daniel proceed south to "+termcolor.colored("Victoria street", attrs = ['bold'])+".\nWhere do you guys want to go now?\n")
                                                direction16answer = False
                                                while not direction16answer:
                                                    direction16 = directionChoice(False)
                                                    if direction16 == 'n':
                                                        print("You just came from that direction! Why go back?")
                                                    if direction16 == 's':
                                                        print("\nThat seems to be the end of the street!\nYou turn back.")
                                                    if direction16 == 'e':
                                                        print("\nThere STILL seems to be a parade coming through!")
                                                    if direction16 == "w":
                                                        print("\nYou and Daniel proceed to South Kensington street.")
                                                        input("...")
                                                        input("...")
                                                        print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                                                        direction16answer = True
                                    if direction14 == 's':
                                        direction14answer = True
                                        print("\nYou and Daniel have now arrived at"+termcolor.colored(" Earl's court", attrs = ['bold'])+" street.\nWhere do you go from here?")
                                        var = False
                                        direction17answer = False
                                        while not direction17answer:
                                            direction17 = directionChoice(False)
                                            if direction17 == "n":
                                                print("\nYou just came from that direction! Why go back?")
                                            if direction17 == 'w':
                                                print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                                            if direction17 == 's':
                                                print("\nThat seems to be the end of the street!")
                                            if direction17 == 'e':
                                                print("\nYou and Daniel proceed to"+termcolor.colored(" South Kensington", attrs = ['bold'])+" street.")
                                                input("...")
                                                input("...")
                                                print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                                                direction17answer = True
                                                direction14answer = True   
            #not finshed, need to add code from below
   
    elif answer == '2':
        print("\nYou and Daniel make your way up the stairs and are in the open in London.\n") 
        var = True
        while var:
            direction = directionChoice(False)
            
            if direction == 'n':
                print("\nUh Oh! There was a car accident and all exits have been blocked. \nYou and Daniel turn back.\n")

            if direction == 'e':
                print("\nThere is a huge parade coming through and you can't seem to get through. \nYou and Daniel turn back.\n")

            if direction == 's':
                var = False
                print("\nYou and Daniel walk south towards the next street and arrive at the London Central Mosque.\nDo you want to go inside? ")
                goinside = input("Enter either yes or no: ")
                if "yes" in goinside.lower():
                    print("\nYou see a man standing inside the mosque. Do you talk to him or do you go back outside?")
                    correct2 = False
                    while not correct2: 
                        helpoutside = input("Enter either 1 to talk or 2 to go back outside: ")
                        if helpoutside == '1':
                            #talking with mohamed
                            input("\"Hello! I am Mohamed! How may I help you?\" - Mohamed ")
                            input("\"We need to get to the science museum, do you have any tips?\" - Daniel ")
                            input("\"Sure! just go south two times and west one time\" - Mohamed ")
                            input("Press enter to continue")
                            correct2 = True
                        elif helpoutside == '2':
                            print("You and Daniel exit the museum and go back outside.")
                            correct2 = True
                        else:
                            print("\nSorry, please enter either 1 or 2!")
                print("\nYou are now at "+termcolor.colored("Bond street", attrs = ['bold'])+". Where do you want to go from here?\n")
                direction = directionChoice(False)
                if direction == 'n':
                    print("\nYou just came from that direction! Why go back?")
                if direction == 'e':
                    print("\nThere is still a massive parade going through!\nYou and Daniel turn back.")
                if direction == 's':
                    print("\nYou and Daniel proceed south, and are now at "+termcolor.colored("Victoria street", attrs = ['bold'])+". Where do you want to go now?")
                    direction8answer = False
                    while not direction8answer:
                        direction8 = directionChoice(False)
                        if direction8 == 'n':
                            print("You just came from that direction! Why go back?")
                        if direction8 == 's':
                            print("\nThat seems to be the end of the street!\nYou turn back.")
                        if direction8 == 'e':
                            print("\nThere STILL seems to be a parade coming through!")
                        if direction8 == "w":
                            print("\nYou and Daniel proceed to"+termcolor.colored(" South Kensington", attrs = ['bold'])+" street.")
                            input("...")
                            input("...")
                            print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                            direction8answer = True
                if direction == 'w':
                    print("\nYou and Daniel proceed west, and are now at"+termcolor.colored(" Notting Hill Gate", attrs = ['bold'])+" street. Where do you want to go now?")
                    direction9answer = False
                    while not direction9answer:
                        direction9 = directionChoice(False)
                        if direction9 == "n":
                            print("\nYou just came from that direction! Why go back?")
                        if direction9 == "w":
                            print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                        if direction9 == 'e':
                            direction9answer = True
                            print("\nYou and Daniel proceed to make your way to"+termcolor.colored(" Bond street", attrs = ['bold'])+".\nWhere do you go from here?\n")
                            direction10answer = False
                            while not direction10answer:
                                direction10 = directionChoice(False)
                                if direction10 == 'n':
                                    print("The policemen seem to have made a blockage for a previous accident.\nYou turn back.")
                                if direction10 == 'e':
                                    print("\nThere is still a massive parade going through!\nYou and Daniel turn back.")
                                if direction10 == "w":
                                    print("\nYou just came from that direction! Why go back?")
                                if direction10 == "s":
                                    direction10answer = True
                                    print("\nYou and Daniel proceed south to "+termcolor.colored("Victoria street", attrs = ['bold'])+".\nWhere do you guys want to go now?\n")
                                    direction11answer = False
                                    while not direction11answer:
                                        direction11 = directionChoice(False)
                                        if direction11 == 'n':
                                            print("You just came from that direction! Why go back?")
                                        if direction11 == 's':
                                            print("\nThat seems to be the end of the street!\nYou turn back.")
                                        if direction11 == 'e':
                                            print("\nThere STILL seems to be a parade coming through!")
                                        if direction11 == "w":
                                            print("\nYou and Daniel proceed to South Kensington street.")
                                            input("...")
                                            input("...")
                                            print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                                            direction11answer = True
                #notfinished

            elif direction == 'w':
                var = False
                print("\nYou have now arrived at"+termcolor.colored(" Edgware Road", attrs = ['bold'])+".\nWhere do you want to go now?\n ")
                direction2answer = False
                while not direction2answer:
                    direction2 = directionChoice(False)
                    if direction2 == 's':
                        print("\nThere is a mysterious building, and you cannot get through.\n")
                    elif direction2 == 'n':
                        print("\nThere is still a car accident on the street above!")
                    elif direction2 == 'e':
                        print("You just came from that direction! Why go back?")
                    elif direction2 == 'w':
                        direction2answer = True
                        print("\nYou and Daniel proceed west to "+termcolor.colored("Paddington street", attrs = ['bold'])+".\nWhere do you want to go from here?\n")
                        direction3answer = False
                        while not direction3answer:
                            direction3 = directionChoice(False)
                            if direction3 == 'w':
                                print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                            elif direction3 == 'n':
                                print("\nThere is still a car accident on the street above!")
                            elif direction3 == 'e':
                                print("\nYou just came from that direction! Why go back?")
                            elif direction3 == 's':
                                direction3answer = True
                                print("\nYou and Daniel make your way to "+termcolor.colored("Notting Hill Gate")+" street.\n Where do you want to go from here?\n")
                                direction4answer = False
                                while not direction4answer:
                                    direction4 = directionChoice(False)
                                    if direction4 == "n":
                                        print("\nYou just came from that direction! Why go back?")
                                    if direction4 == "w":
                                        print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                                    if direction4 == 'e':
                                        direction4answer = True
                                        print("\nYou and Daniel proceed to make your way to "+termcolor.colored("Bond street", attrs = ['bold'])+".\nWhere do you go from here?\n")
                                        direction5answer = False
                                        while not direction5answer:
                                            direction5 = directionChoice(False)
                                            if direction5 == 'n':
                                                print("The policemen seem to have made a blockage for a previous accident.\nYou turn back.")
                                            if direction5 == 'e':
                                                print("\nThere is still a massive parade going through!\nYou and Daniel turn back.")
                                            if direction5 == "w":
                                                print("\nYou just came from that direction! Why go back?")
                                            if direction5 == "s":
                                                direction5answer = True
                                                print("\nYou and Daniel proceed south to "+termcolor.colored("Victoria street", attrs = ['bold'])+".\nWhere do you guys want to go now?\n")
                                                direction7answer = False
                                                while not direction7answer:
                                                    direction7 = directionChoice(False)
                                                    if direction7 == 'n':
                                                        print("You just came from that direction! Why go back?")
                                                    if direction7 == 's':
                                                        print("\nThat seems to be the end of the street!\nYou turn back.")
                                                    if direction7 == 'e':
                                                        print("\nThere STILL seems to be a parade coming through!")
                                                    if direction7 == "w":
                                                        print("\nYou and Daniel proceed to South Kensington street.")
                                                        input("...")
                                                        input("...")
                                                        print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                                                        direction7answer = True
                                    if direction4 == 's':
                                        direction4answer = True
                                        print("\nYou and Daniel have now arrived at "+termcolor.colored("Earl's Court", attrs = ['bold'])+" street.\nWhere do you go from here?")
                                        var = False
                                        direction6answer = False
                                        while not direction6answer:
                                            direction6 = directionChoice(False)
                                            if direction6 == "n":
                                                print("\nYou just came from that direction! Why go back?")
                                            if direction6 == 'w':
                                                print("\nPolice cars seem to be coming to tend to accident! You and Daniel turn back.")
                                            if direction6 == 's':
                                                print("\nThat seems to be the end of the street!")
                                            if direction6 == 'e':
                                                print("\nYou and Daniel proceed to South Kensington street.")
                                                input("...")
                                                input("...")
                                                print("\n🥳🥳🥳\nThere it is! the Science Museum!\nYou and Daniel have been reunited with your friends!\nYour teachers, who have been frantically searching for you, are extremely relieved.\nCongratulations on being such a smart player!\n")
                                                direction6answer = True
                                                #ending 2

    
# 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