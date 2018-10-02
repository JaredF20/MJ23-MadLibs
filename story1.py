from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    singItem = getWord("Enter a singular household item: ")
    sport1 = getSport("Enter a common sport: ")
    friend2 = getWord("Enter a Female Name: ")
    sparkley = getWord("Enter a place or thing: ")
    townName = getTown("Enter a town in the Kearsarge District")
    output = ""
    output += "One day I was sprinting with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1 + ","
    output += " I quickly jumped into action. I grabbed a nearby " + singItem + " and I charged into battle."
    output += " Soon, everything turned into an agressive match of " + sport1 
    output += " ,I was winning and the " + animals1 + " did not stand a chance. "
    output += " When the battle was done, I claimed my prize: The lovely princess. " + friend2
    output += " It was love at first sight. She had blue eyes that sparkled like the " + sparkley
    output += " One thing lead to another and soon we had our own little guys running around. "
    output += "Eventually we settled down in the big city of " + townName
    
    
    
    return output
