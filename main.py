from userInput import takeUserInput, takeExpectedResult
from writerfunc import writeUserInput

captureTestCaseName = takeUserInput('Please provide the name of the test case : ')
captureProductName = takeUserInput('Please provide the name of the Product : ')
fileName = captureTestCaseName+".py"
f = open(fileName, 'a')
f.write(f'from apiCall import apiCallFrom\n')
f.write(f'from postApiCall import apiCall\n\n\n')
f.write(f'TotalPass=0\n')
f.write(f'TotalFail=0\n\n')
f.write(f'productName="{captureProductName}"\n\n')
f.close()

while True:
    captureUrl = takeUserInput('Please provide the url to api OR hit \'q\' to quit : ')
    if captureUrl == 'q':
        print('You have quited from the program')
        break
    captureApiBody = takeUserInput('Please provide the full api body : ')
    captureDescription = takeUserInput('Please provide a description of case performed : ')
    captureExpectedResult = takeExpectedResult('Please provide the expected results & Hit \'r\' to return back to main program : ')
    writeUserInput(fileName, captureUrl, captureApiBody, captureDescription, captureExpectedResult)
    captureExpectedResult.clear()

f = open(fileName, 'a')
f.write(f"print('Total Pass : ', TotalPass)\n")
f.write(f"print('Total Fail : ', TotalFail)\n\n")
f.write(f"if (TotalFail > 0):\n")
f.write(f"\tprint('{captureTestCaseName} Test case : FAILED')\n")
f.write(f'\tresult="FAIL"\n')
f.write(f"else:\n")
f.write(f"\tprint('{captureTestCaseName} Test case : PASSED')\n")
f.write(f'\tresult="PASS"\n')
f.write(f"captureResponse = apiCall('{fileName}', productName, result)\n")
f.write(f"print(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
f.close()