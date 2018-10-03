from getInput import * 

def playMadlibs():
    Town = getTown("Enter a town in the Kearsarge District: ")
    friend1 = getWord("Enter a name: ")
    bodypart = getWord("Enter an appropriate body part: ") 
    
    
    
    
    
    output = ""
    output += "It was a dark and stormy night in " + Town
    output += ". My friend, " + friend1 + " , and I were walking down the street. "
    output += "Suddenly, a cool breeze made the hair stand up on my " + bodypart
  
    
    
    
    
    
    return output 
