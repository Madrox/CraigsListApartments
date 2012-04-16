from django.http import HttpResponse
from django.template import Template, Context
import os

def ui(request):
	path = os.path.dirname(os.path.realpath(__file__))
	with open(os.path.join(path,"ui.html")) as f:
		# Doing this instead of using django's built-in
		# template manager to avoid walkthroughs of
		# settings.py
		html = "".join(f.readlines())

	tmpl = Template(html)
	context = Context()

	return HttpResponse(tmpl.render(context))