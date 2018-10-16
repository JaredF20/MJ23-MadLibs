from getInput import * 

def playMadlibs(sm = False):
    print "Create this character wit and care and maybe you will find that the story fair."
    friend1 = getWord("Enter a Name: ", sm)
    action = getWord("Enter a past-tense verb: ", sm)
    sound = getWord("Enter a random sound: ", sm)
    place1 = getWord("Enter a foreign country: ", sm)
    animals1 = getWord("Enter a plural animal name: ", sm)
    food1 = getWord("Enter a common food: ", sm)
    weather = getWeather("Enter a common weather condition: ")
    numItems = getNumber("Enter a number: ", 2, 10)
    Items1 = getWord("Enter a plural household item: ", sm)
    insect1 = getWord("Enter a scary insect: ", sm)
    sport1 = getSport("Enter a common sport: ")

    output = ""
    output += " My teacher Mr. " + friend1 + " probably thinks I'm an idiot." 
    output += " Things started off pretty bad when I accidentally " + action + " his new computer with my fist."
    output += " Surprisingly, he didn't yell but just made a high pitched " + sound + " noise."
    output += " The next week things got even worse. I was doing a report on " + place1 + " except I accidentally talked about " + animals1 + " the entire time."
    output += friend1 + " was so upset. He told me I was a complete and utter " + food1 + "."
    output += " I was livid. I was going to make it " + weather + " in his classroom."
    output += " I quickly grabbed " + numItems + Items1 + " and swung them at " + friend1 + "."
    output += " Long story short, I was expelled. I got the last laugh though, because before I left I put a " + insect1 + " in the " + sport1 + " team's locker room. And guess what teacher was the head coach?" 
    
    
    return output 
 
