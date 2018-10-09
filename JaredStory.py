from getInput import * 

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    action = getWord("Enter a past-tense verb: ")
    sound = getWord("Enter a random sound: ")
 
    
    
    
    
    output = ""
    output += " My teacher Mr. " + friend1 + " probably thinks I'm an idiot." 
    output += " Things started off pretty bad when I accidentally " + action + " his new computer with my fist."
    output += " Surprisingly, he didn't yell but just made a high pitched " + sound + " noise."
    output += " Ever since that day I have always "
    
    
    return output 
 
