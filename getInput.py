def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "2"
            or response == "Two"):
            response = "2"
            goodInput = True
        elif (response == "3"
            or response == "three"):
            response = "3"
            goodInput = True
        elif (response == "4"
            or response == "four"):
            response = "4"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True    
        elif (response == "Sloth"
              or response == "sloth"):
              goodInput = True
        else:
            print "Please make a valid choice"
    return response
    
def getWord(prompt, sm = False):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not sm:
            if not isSwear(word):
                goodInput = True
            else:
                print "Watch your language!"
        else:
            if isSwear(word):
                goodInput = True
            else:
                print "Swears only bitchacho"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") " + prompt)
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
    return word

def getSport(prompt, sm = False):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        sports = ["soccer",
                  "football",
                  "basketball",
                  "tennis",
                  "volleyball",
                  "baseball",
                  "archery",
                  "track",
                  "cross-country",
                  "hockey",
                  "fieldhockey", 
                  "boxing", 
                  "curling",
                  "cheerleading",
                  "rugby",
                  "jousting",
                  "fencing" ]
        if not sm:
            if not isSwear(word):
                if word in sports:
                    goodInput = True
                else:
                    print "Not a real sport!"
        else:
            if isSwear(word):
                goodInput = True
            else:
                print "Swears only bitchacho"
    return word
            
def getTown(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        towns = ["Newbury",
                 "Bradford",
                 "Sutton",
                 "Warner",
                 "Newlondon",
                 "Wilmot",
                 "Springfield" ]
        goodInput= True
        if word not in towns:
            goodInput = False
            print "That place is not real."
    return word

def getWeather(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        weather = ["rain",
                   "snow",
                   "fog",
                   "blizzard",
                   "storm",
                   "lightning",
                   "cloudy",
                   "clear",
                   "thunder",
                   "hail",
                   "sleet",
                   "sunshower",
                   "windy",
                   "overcast",
                   "haze",
                   "tornado",
                   "hurricane",
                   "sunny",
                   "tropical storm"]
        goodInput= True
        if word not in weather:
            goodInput = False
            print "Not in the weather forecast"
    return word

def isSwear(word):
    swearList = ["poop",
                "piss",
                "ass",
                "motherfucker",
                "fuck",
                "son of a bitch",
                "bitch",
                "cunt",
                "tit",
                "assfucker",
                "whore",
                "titty",
                "sperm",
                "vagina",
                "penis",
                "asshole",
                "retard",
                "schlong",
                "assfucker",
                "anus",
                "dong",
                "dick",
                "dongle",
                "whorehouse",
                "whore house",
                "dongles",
                "nipple",
                "nipples",
                "twat",
                "dickweed",
                "bitchtits",
                "wanker",
                "dickhead",
                "nutsack",
                "balls",
                "testicles",
                "pussy",
                "slut",
                "sluts",
                "Poop",
                "Piss",
                "Ass",
                "Motherfucker",
                "Fuck",
                "Son of a bitch",
                "Bitch",
                "Cunt",
                "Tit",
                "Assfucker",
                "Whore",
                "Titty",
                "Sperm",
                "Vagina",
                "Penis",
                "Asshole",
                "Retard",
                "Schlong",
                "Assfucker",
                "Anus",
                "Dong",
                "Dick",
                "Dongle",
                "Whorehouse",
                "Whore house",
                "Dongles",
                "Nipple",
                "Nipples",
                "Twat",
                "Dickweed",
                "Bitchtits",
                "Wanker",
                "Dickhead",
                "Nutsack",
                "Balls",
                "Testicles",
                "Pussy",
                "Slut",
                "Sluts",
                "fucked",
                "fucking"
                "Fucked",
                "Fucking",
                "assfucking" ,
                "assfucked",
                "gangbanging",
                "gangbanged",
                "foreplay",
                "fuckface",
                "douchecanoe",
                "clusterfuck",
                "fuckstick",
                "prick",        
                ]
    if word in swearList:
        return True
    else:
        return False

def SwearMode(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if isSwear(word):
            goodInput = True
        else:
            print "Swears only, bitch"
            
        
    return word 
