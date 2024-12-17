from userInput import takeUserInput, takeExpectedResult
from writerfunc import writeUserInput

captureTestCaseName = takeUserInput('Please provide the name of the test case : ')
fileName = captureTestCaseName+".py"
f = open(fileName, 'a')
f.write(f'from apiCall import apiCallFrom\n\n\n')
f.close()

count=0

while True:
    incremental = str(count)
    captureUrl = takeUserInput('Please provide the url to api OR hit \'q\' to quit : ')
    if captureUrl == 'q':
        quit()
    captureVariableName = takeUserInput('Please provide variable name to store the api body : ')
    captureApiBody = takeUserInput('Please provide the full api body : ')
    captureDescription = takeUserInput('Please provide a description of case performed : ')
    captureExpectedResult = takeExpectedResult('Please provide the expected results & Hit \'r\' to return back to main program : ')
    writeUserInput(fileName, captureUrl, captureVariableName, captureApiBody, captureDescription, captureExpectedResult, incremental)
    count+=1