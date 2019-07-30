import poplib, time, re, requests, sys, types
from pop import POPS
from websites import CALLERS, NAMES

##############
# askServers #
##############

def askServers(email): #GitHub example

	numCallers = len(CALLERS)
	print("CALL 0/" + str(numCallers))

	for i in range(numCallers):
		CALLERS[i](email)
		print("\033[FCALL " + str(i+1) + "/" + str(numCallers))

###############
# getWebsites #
###############

def getWebsites(mailbox, email, password):

	all = {}
	numMessages = len(mailbox.list()[1])
	print("GET 0/" + str(numMessages))

	for i in range(numMessages):
		content = mailbox.retr(i+1)[1]
		sender = parseEmail(content)
		if(sender):
			website = getWebsiteFromEmail(sender)
			if(website):
				all[website] = i

		print("\033[FGET " + str(i+1) + "/" + str(numMessages))
	return all

def parseEmail(lines):
	for line in lines:
		str_line = str(line)
		if(not str_line.find("b'From:")):
			if('<' in str_line and '@' in str_line and '>' in str_line):
				return str_line[str_line.find("<")+1:str_line.find(">")]
	return None

def getWebsiteFromEmail(email):
	if(email in NAMES):
		return NAMES[email]
	else:
		return None

#############
# removeAll #
#############

def removeAll(mailbox, all):
	for one in all.values():
		mailbox.dele(one)

########
# MAIN #
########

def main(email, password):

	if(not isEmail(email)):
		raise Exception(email + " is not an email address.")

	mailbox = poplib.POP3_SSL(getPopFromUser(email))
	mailbox.user(email)
	mailbox.pass_(password)

	askServers(email)
	time.sleep(10) # wait 10 sec to receive the last email
	all = getWebsites(mailbox, email, password)

	print("===== " + str(len(all)) + " result(s) =====")
	for one in all.keys():
		print(one)

	#removeAll(mailbox, all)	#Not working. Why ?
	mailbox.quit()

def isEmail(email):
	return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email) 

def getPopFromUser(email):
	domain = getDomain(email)
	if(domain in POPS):
		return POPS[domain]
	else:
		raise Exception("Unknow pop address for domain " + domain)

def getDomain(email):
	return email[email.find("@")+1:email.rfind(".")]

##########
# GLOBAL #
##########

def help():
	print("Usage : '" + sys.argv[0] + " <EMAIL> <PASSWORD>'")

if __name__ == "__main__":
	try:
		if(len(sys.argv) == 3):
			main(sys.argv[1], sys.argv[2])
		else:
			help()
	except KeyboardInterrupt:
		None