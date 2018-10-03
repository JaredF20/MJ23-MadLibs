from getInput import * 

def playMadlibs():
    Town = getTown("Enter a town in the Kearsarge District: ")
    friend1 = getWord("Enter a name: ")
    bodypart = getWord("Enter an appropriate body part: ") 
    numAnimals = getWord("Enter a plural animal name: ")
    building = getWord("Enter a common building in a town: ")
    
    
    
    
    output = ""
    output += "It was a dark and stormy night in " + Town
    output += ". My friend, " + friend1 + " , and I were walking down the street. "
    output += "Suddenly, a cool breeze made the hair stand up on my " + bodypart
    output += ". Out of nowhere a pack of " + numAnimals + " attacked " + friend1
    output += ". I panicked, so I left them there and took off towards the " + building 
    
    
    
    
    
    return output 
