import requests
import sys

def getToken (emailAddr, acc_pwd):

	url = "https://xxx.com/sessions"

	payload = "{\t\"email\":\"" + emailAddr + "\",\n\t\"password\":\"" + acc_pwd + "\" }"
	#print(payload)
	headers = {
		'Content-Type': "application/json",
		}

	response = requests.request("POST", url, data=payload, headers=headers)
	resp_json = response.json()
	#print(resp_json['token'])
	#print(response.text)
	#print(response['token'])
	return (resp_json['token'])

	
def getUUID (Xjwtauth):

	url = "https://xxx.com/account_details"

	payload = ""
	headers = {
		'X-Jwt-Authorization': Xjwtauth
		#'cache-control': "no-cache",
		}
	#print(headers)
	response1 = requests.request("GET", url, data=payload, headers=headers)
	data = response1.json()
	#print len(data)
	#print (data)
	uuid = data['subscriptions']['current_subscription']['uuid']
	print(uuid)
	return uuid

def cancelAccount (Xjwtauth, uuid, acc_pwd):

	url = "https://XXX.com/cancel"

	#payload = "{\t\"email\":\"" + emailAddr + "\",\n\t\"password\":\"" + acc_pwd + "\" }"
	payload = "{\n\"password\":\"" + acc_pwd + "\",\n\"uuid\":\"" + uuid + "\",\n\"cancel_reasons\": [\n\" Prod test Account \"\n]\n}"
	print(payload)
	headers = {
		'Content-Type': "application/json",
		'X-Jwt-Authorization': Xjwtauth
		}

	response = requests.request("POST", url, data=payload, headers=headers)
	resp_json = response.json()
	print(response.text)
	#print(resp_json['success'])
	return (resp_json['success'])
	
def main(argv=None):
	if argv is None:
		argv = sys.argv
	emailAddr = argv[1]
	acc_pwd = "XXXX"
	ret = getToken(emailAddr, acc_pwd)
	retp = getUUID(ret)
	status = cancelAccount(ret,retp,acc_pwd)
	#print (status)
	if status is True:
		print("Account Canceled Successfully")

if __name__ == '__main__':
    exit(main())
