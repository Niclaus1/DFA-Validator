import re
# DFA - Validator

# states ask the number of q
# alphabet ask the allowed inputs
# transistions set transitions

"""PsuedoCode
1. Ask for the allowed input pattern 
    - Allowed only are 1,0 
    - if 1* means any number of 1
    - if 0* means any number of 0
    - if e1 means even number of 1
    - if o1 means odd number of 1
    - if e0 means even number of 0
    - if o0 means off number of 0
2. Generate a states as dictionary
3. create dictionary for each state
    q# : (input1: q#, input0: q#)
    - Print the dictionaries
4. In a While Loop, ask user to input some 1s & 0s
5. Ask user if he wants to stop
6. If yes
    - print all the inputs with each corresponding reponse (valid | invalid)
    - end program
7. Else
    - continue
"""
def Main():
    userInput = input("""
            1  = single 1
            0  = single 0
            1* = infinite number of 1
            0* = infinite number of 0
            e1 = even number of 1
            e0 = even number of 0
            o1 = odd number of 1
            o0 = odd number of 0
            *Use "," for each Unique Input*
    Create your Pattern: """)


    #Create State Dictionaries

    splitInput = userInput.split(",")
    countInput = len(splitInput)

    #Create a Dictionary - keys based on len(list)
    #Create a unique code per pattern
    stateDict = {}
    codePattern = ""
    for i in range (countInput):
        match splitInput[i]:
            case "1":
                stateDict["q" + str(i)] = "Single 1"
                codePattern = codePattern + "0" #Ucode
            case "0":
                stateDict["q" + str(i)] = "Single 0"
                codePattern = codePattern + "1" #Ucode
            case "1*":
                stateDict["q" + str(i)] = "Infinite 1s"
                codePattern = codePattern + "2" #Ucode
            case "0*":
                stateDict["q" + str(i)] = "Infinite 0s"
                codePattern = codePattern + "3" #Ucode
            case "e1":
                stateDict["q" + str(i)] = "Even 1"
                codePattern = codePattern + "4" #Ucode
            case "e0":
                stateDict["q" + str(i)] = "Even 0"
                codePattern = codePattern + "5" #Ucode
            case "o1":
                stateDict["q" + str(i)] = "Odd 1"
                codePattern = codePattern + "6" #Ucode
            case "o0":
                stateDict["q" + str(i)] = "Odd 0"
                codePattern = codePattern + "7" #Ucode
    print("")
    print(f"Each status of the Pattern is: {stateDict}")
    print("")
    print(f"Unique Code of the Pattern is: {codePattern}")
    print("")
    return codePattern
    
def UserInput():
    #4. In a While Loop, ask user to input some 1s & 0s
    #thoughts: creating a unique code per each pattern, where when we input the data, 
    #          it translates into a code for easy checking
    userInputs = []
    status = True
    while status:
        inputPattern = input(
    """ 
    Input your Patterns!
    Type stop to exit-- 
    """)
        userInputs.append(inputPattern)
        
        if inputPattern == "stop":
            userInputs.pop(-1)
            status = False
        
    return userInputs

def DataChecking():
    uniqueCode = Main()
    listOfInputs = UserInput()
    
    regex_map = {
        "0": "1",       # Single 1
        "1": "0",       # Single 0
        "2": "1*",      # Infinite 1s (zero or more)
        "3": "0*",      # Infinite 0s (zero or more)
        "4": "(11)*",   # Even 1s (consecutive blocks of 1s)
        "5": "(00)*",   # Even 0s
        "6": "1(11)*",  # Odd 1s
        "7": "0(00)*"   # Odd 0s
    }
    
    pattern = "^"
    for char in uniqueCode:
        pattern += regex_map.get(char, "")
    pattern += "$"
        
    for i in listOfInputs:
        if re.fullmatch(pattern, i):
            print(f"Input'{i}': VALID")
        else:
            print(f"Input'{i}': INVALID")
            
DataChecking()