import re

email_regex = re.compile(r'([\w\-\d]+@\w+\.craigslist\.org)',re.I)
cost_regex = re.compile(r'\$?(\d\d\d\d(\.\d\d)?)')
bedroom_regex = re.compile(r'(\d)br', re.I)
links_regex = re.compile(r'(http://\w+\.craigslist\.org/\w\w\w/apa/\d+\.html)', re.I)

def listings(text):
    return [
			link.group(1) 
			for link in links_regex.finditer(text)
			]

def cost(text):
	match = cost_regex.search(text)
	if match is not None:
		return match.group(1)
	else:
		return None

def cl_email(text):
	match = email_regex.search(text)
	if match is not None:
		return match.group(1)
	else:
		return None

def bedrooms(text):
	match = bedroom_regex.search(text)
	if match is not None:
		return match.group(1)
	else:
		if text.lower().find("studio"): return 0
		else: return -1

