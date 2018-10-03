from getInput import * 

def playMadlibs():
    Town = getTown("Enter a town in the Kearsarge District: ")
    friend1 = getWord("Enter a name: ")
    bodypart = getWord("Enter an appropriate body part: ") 
    numAnimals = getWord("Enter a plural animal name: ")
    building = getWord("Enter a common building in a town: ")
    halloweenC = getWord("Enter a common halloween creature: ")
    bodypart2 = getWord("Enter an appropriate body part: ")
    yourname = getName("Enter your name: ")
    
    output = ""
    output += "It was a dark and stormy night in " + Town
    output += ". My friend, " + friend1 + ", and I were walking down the street. "
    output += "Suddenly, a cool breeze made the hair stand up on my " + bodypart
    output += ". Out of nowhere a pack of " + numAnimals + " attacked " + friend1
    output += ". I panicked, so I left them there and took off towards the " + building 
    output += ". As I entered the building I saw a " + halloweenC 
    output += ". I turned around and ran out but it was too late, they grabbed me by my " + bodypart2
    output += ". 'Here Lies " + yourname + " gone but definitely forgotten' "
    
    
    
    
    
    
    return output 
