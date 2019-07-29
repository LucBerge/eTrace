import re, requests

NAME = "github.com"
EMAIL = "noreply@github.com"

def ask(email):

	s = requests.session()
	URL = 'https://github.com/password_reset'

	r1 = s.get(URL)
	authenticity_token = re.search("""<input type="hidden" name="authenticity_token" value="(.*?)"[^>]*?>""",r1.text,re.S|re.I)

	payload = {
	    'authenticity_token': authenticity_token.group(1),
	    'email': email
	}

	return requests.post(URL, data=payload, cookies=r1.cookies).status_code

if __name__ == "__main__":
	print(ask("test@test.com"))