def SwearMode(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if swearList(word):
            goodInput = True
        else:
            print "Swears only, bitchacho"
            
        
    return word 
