import eTrace.websites.websites, types

CALLERS = []
NAMES = {}

for item in list(globals().items()):
	if(isinstance(item, tuple)):
		if(isinstance(item[1], types.ModuleType)):
			if("websites." in item[1].__name__ and item[1].__name__ != "eTrace.websites.websites"):
				CALLERS.append(item[1].ask)
				NAMES[item[1].EMAIL] = item[1].NAME