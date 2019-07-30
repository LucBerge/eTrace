import requests

NAME = "instagram.com"
EMAIL = "security@mail.instagram.com"

def ask(email):

	URL = 'https://www.instagram.com/accounts/password/reset/'

	headers={
		"Accept":"*/*",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"en-US,en;q=0.5",
		"Connection":"keep-alive",
		"Content-Length":"60",
		"Content-Type":"application/x-www-form-urlencoded",
		"Cookie":"ig_cb=1; csrftoken=Vnt9rdCz1GBPA9yiRtwb5ur8FHRY0pXi; rur=FRC; mid=XT7pdAAEAAHpIHBl43InDlyCz0Lk",
		"Host":"www.instagram.com",
		"Referer":"https://www.instagram.com/accounts/password/reset/",
		"TE":"Trailers",
		"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
		"X-CSRFToken":"Vnt9rdCz1GBPA9yiRtwb5ur8FHRY0pXi",
		"X-IG-App-ID":"936619743392459",
		"X-Instagram-AJAX":"79d0a43d9853",
		"X-Requested-With":"XMLHttpRequest"
	}

	payload = {
		"email_or_username" : email,
		"recaptcha_challenge":""
	}

	return requests.post(URL, data=payload, headers=headers).status_code

if __name__ == "__main__":
	print(ask("test@test.com"))