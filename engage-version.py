#!python3
import console
import requests

stacks = [2, 3, 4, 5, 7]
sbUser = ""
sbPass = ""

console.clear()

for stackNum in stacks:
	sbURL = "https://service" + str(stackNum) + ".soundbite.com/site/c/4/PlatformManagementService/showSystemInfo/"
	
	for attempt in range(3):
		try:
			r = requests.get(sbURL, auth=(sbUser, sbPass))
			rj = r.json()

			for item in rj['data']:
				if item['name'] == 'SoundBiteVersion':
					print('Stack ' + str(stackNum) + ': Engage ' + item['value'])
					break					
			break
					
		except:
			pass
			
	else:
		print('Stack ' + str(stackNum) + ': error')