from apiCall import apiCallFrom


urlOfApi=r'''http://10.0.1.127:8001/fcgi-bin/services/SubscriberProv'''

expectedResultArry=['<resultCode xmlns="http://soap.provisioning.sdr.s2200.product.tayana.com/xsd">0</resultCode>']

apiBodyVar=r'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://soap.provisioning.sdr.s2200.product.tayana.com/xsd"> <soapenv:Header> <xsd:authenticationToken> <xsd:username>CISPROV</xsd:username> <xsd:password>xi19ci2</xsd:password> </xsd:authenticationToken> </soapenv:Header> <soapenv:Body> <xsd:removeSubscriber> <xsd:msisdn>61464253304</xsd:msisdn> </xsd:removeSubscriber> </soapenv:Body> </soapenv:Envelope>'''

userDefinedDescription=r'Delete Subscriber'

def DeleteSubscriber(getUrl, apiBodyVar, description, expectedResult):
	passCount=0
	failCount=0

	response=apiCallFrom(urlOfApi, apiBodyVar)

	for expectedResultVal in expectedResultArry:
		if expectedResultVal in response:
			print(f"{expectedResult} is present in response : string match success")
			passCount+=1
		else:
			print(f"{expectedResult} is not present in response : string match failed")
			failCount+=1
	print(f"Total num of pass count : {passCount}")
	print(f"Total num of fail count : {failCount}")

	if failCount > 0:
		print(f"{userDefinedDescription} : FAIL")
	else:
		print(f"{userDefinedDescription} : PASS")


DeleteSubscriber(urlOfApi, apiBodyVar, userDefinedDescription, expectedResultArry)



urlOfApi=r'''http://10.0.1.127:8001/fcgi-bin/services/SubscriberProv'''

expectedResultArry=['<resultCode xmlns="http://soap.provisioning.sdr.s2200.product.tayana.com/xsd">0</resultCode>']

apiBodyVar=r'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://soap.provisioning.sdr.s2200.product.tayana.com/xsd"> <soapenv:Header> <xsd:authenticationToken> <xsd:username>CISPROV</xsd:username> <xsd:password>xi19ci2</xsd:password> </xsd:authenticationToken> </soapenv:Header> <soapenv:Body> <xsd:addSubscriber> <xsd:msisdn>61464253304</xsd:msisdn> <xsd:spid>1</xsd:spid> <xsd:svcgrade>0</xsd:svcgrade> <xsd:rateplan>20004</xsd:rateplan> <billcycledate>1</billcycledate> <provType>11</provType> <subAcctNo>100003</subAcctNo> <customerCos>1102000</customerCos> <param3>01</param3> <packBucket>1073741824</packBucket> <packBucketUnit>B</packBucketUnit> </xsd:addSubscriber> </soapenv:Body> </soapenv:Envelope>'''

userDefinedDescription=r'Create Subscriber'

def CreateSubscriber(getUrl, apiBodyVar, description, expectedResult):
	passCount=0
	failCount=0

	response=apiCallFrom(urlOfApi, apiBodyVar)

	for expectedResultVal in expectedResultArry:
		if expectedResultVal in response:
			print(f"{expectedResult} is present in response : string match success")
			passCount+=1
		else:
			print(f"{expectedResult} is not present in response : string match failed")
			failCount+=1
	print(f"Total num of pass count : {passCount}")
	print(f"Total num of fail count : {failCount}")

	if failCount > 0:
		print(f"{userDefinedDescription} : FAIL")
	else:
		print(f"{userDefinedDescription} : PASS")


CreateSubscriber(urlOfApi, apiBodyVar, userDefinedDescription, expectedResultArry)



