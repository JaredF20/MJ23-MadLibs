def SwearMode(prompt): #is this file used? If not it should be removed
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if swearList(word):
            goodInput = True
        else:
            print "Swears only, bitchacho"
            
        
    return word 
