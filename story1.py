from getInput import *

def playMadlibs(sm = False):
    friend1 = getWord("Enter a Name: ", sm)
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a plural animal name: ", sm)
    singItem = getWord("Enter a singular household item: ", sm)
    sport1 = getSport("Enter a common sport: ")
    friend2 = getWord("Enter a Female Name: ", sm)
    sparkley = getWord("Enter a place or thing: ", sm)
    townName = getTown("Enter a town in the Kearsarge District: ")
    output = ""
    output += "One day I was wrestling with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1 + ","
    output += " I quickly jumped into action. I grabbed a nearby " + singItem + " and I charged into battle."
    output += " Soon, everything turned into an agressive match of " + sport1 
    output += " ,I was winning and the " + animals1 + " did not stand a chance. "
    output += " When the battle was done, I claimed my prize: The lovely princess " + friend2
    output += ". It was love at first sight. She had blue eyes that sparkled like " + sparkley
    output += ". One thing lead to another and soon we had our own little guys running around. "
    output += "Eventually we settled down in the big city of " + townName + " and lived happily ever after."
    
    
    
    return output
