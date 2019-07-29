# eTrace

## Description

eTrace is a python tool that trace your email on internet. It founds every websites on which you have an account.

## Prerequisites

Pip installation :
```
python3 get-pip.py
```

## Install

From [PyPi](https://pypi.org/project/eTrace/) :
```
pip install eTrace
```

**Update**
```
pip install eTrace -U
```

## Uninstall

```
pip uninstall eTrace
```

## Utilisation

```
eTrace <EMAIL> <PASSWORD>
```

## Contribution

1. Fork

2. Create a new branch and checkout

#### Add a pop address

3. Add a key:value in pop.py

4. Pull request

#### Add a new website

3. Create a new file from template

```python
import requests

NAME = "mytemplate.com"
EMAIL = "my@template.com"

def ask(email):

	URL = 'https://mytemplate.com/password_reset'
	payload = {
	    
	}
	return requests.post(URL, data=payload).status_code

if __name__ == "__main__":
	print(ask("test@test.com"))
```

4. Find the POST request to mimic using the network tool of your browser

5. Implement the solution

6. Check if it works

7. Import your file in websites.py

8. Pull request

## Contact

Please contact [@LucBerge](https://github.com/LucBerge) for more informations.
