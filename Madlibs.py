from screens import *
from getInput import *
import story1
import MegStory
import JaredStory

print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print quitGame()
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print MegStory.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
        print JaredStory.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "4":
        print secretHint()
        raw_input("Press Enter to Continue")
    elif response == "Sloth":
        print "Welcome to Swear World, Comrade"
        from swear import SwearMode
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "OMG Got invalid menu option!!!"

