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
stateDict = {}
for i in range (countInput):
    match splitInput[i]:
        case "1":
            stateDict["q" + str(i)] = "Single 1"
        case "0":
            stateDict["q" + str(i)] = "Single 0"        
        case "1*":
            stateDict["q" + str(i)] = "Infinite 1s"
        case "0*":
            stateDict["q" + str(i)] = "Infinite 0s"
        case "e1":
            stateDict["q" + str(i)] = "Even 1"
        case "e0":
            stateDict["q" + str(i)] = "Even 0"
        case "o1*":
            stateDict["q" + str(i)] = "Odd 1"
        case "o0":
            stateDict["q" + str(i)] = "Odd 0"

print(stateDict)
print(splitInput)

#4. In a While Loop, ask user to input some 1s & 0s
print("Input your patterns!")
print("Type 'stop' to exit")
status = True
while status:
    inputPattern = input()
    
    
    if inputPattern == "stop":
        status = False