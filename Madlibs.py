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
        print "Goodbye and thanks for playing"
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print MegStory.playMadlibs()
        raw_input("Choose your path, traveller")
     elif response == "3":
        print JaredStory.playMadlibs()
        raw_input("Choose your path, traveller")
    else:
        print "OMG Got invalid menu option!!!"

