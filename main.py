from userInput import takeUserInput, takeExpectedResult
from writerfunc import writeUserInput

captureTestCaseName = takeUserInput('Please provide the name of the test case & Hit \'q\' to quit: ')
if captureTestCaseName == 'q':
    quit()
captureUrl = takeUserInput('Please provide the url to  : ')
captureVariableName = takeUserInput('Please provide variable name to store the api body : ')
captureApiBody = takeUserInput('Please provide the full api body : ')
captureExpectedResult = takeExpectedResult('Please provide the expected results & Hit \'r\' to return back to main program : ')
writeUserInput(captureTestCaseName, captureUrl, captureVariableName, captureApiBody, captureExpectedResult)