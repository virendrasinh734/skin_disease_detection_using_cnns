import requests
def send_simple_message():
    
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "c3ad3573ab7ce397b2ba033c3ab5a746-db137ccd-f2138ffc"),
		data={"from": "Excited User <mailgun@sandbox61a9bae4643d4f44bd7724c038dfe166.mailgun.org>",
			"to": ["virendrasinhkhuman@gmail.com", "YOU@sandbox61a9bae4643d4f44bd7724c038dfe166.mailgun.org"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomeness!"})

p=send_simple_message()
print(p)