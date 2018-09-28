from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    singItem = getWord("Enter a singular household item: ")
    sport1 = getSport("Enter a common sport: ")
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1
    output += " I quickly jumped into action. I grabbed a nearby " + singItem + " and I charged into battle."
    output += " Everything turned into an agressive match of " + getSport + "I was winning and the " +animals1 + " didn't stand a chance."
    
    
    
    return output
