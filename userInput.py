expectedResultArry = []

def takeUserInput(descOfUserInput):
    while True:
        userInput = input(descOfUserInput)
        if not userInput:
            continue
        else:
            return userInput
        
def takeExpectedResult(userExpectedResult):
    while True:
        userExpectedInput = input(userExpectedResult)
        if not userExpectedInput:
            continue
        elif userExpectedInput == 'r':
            return expectedResultArry
        else:
            expectedResultArry.append(userExpectedInput)