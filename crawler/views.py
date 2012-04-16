# Create your views here.
from django.http import HttpResponse
from common.models import Crawler
from django.core import management
from common.models import Post
from django.core import serializers
import json


def start(request):
	resp = { 
		'run': True
		}

	management.call_command('crawl', url)

	return HttpResponse(json.dumps(resp))

def create(request):
	resp = {
		'created': False, 
		'usage': { 
			'url': "Parameter to identify the Craig's List URL.",
			'email': "Optional. Email to notify when there are new hits.",
			'store_matches_only': "Optional. Set to 1 to not store posts that don't match a filter.",
		}
	}

	url = request.REQUEST.get('url')
	email = request.REQUEST.get('email')
	store_matches_only = request.REQUEST.get('store_matches_only',"0")
	if url is not None:
		try:
			crawler = Crawler.objects.get(link = url)
		except Crawler.DoesNotExist:
			crawler = Crawler(link = url)
			resp['created'] = True
		crawler.hits_email = email
		crawler.store_matches_only = (store_matches_only == "1")
		crawler.save()
		resp['email'] = email
		resp['store_matches_only'] = (store_matches_only == "1")
		resp['enabled'] = crawler.enabled

	return HttpResponse(json.dumps(resp))


def list(request):
	resp = {
		'usage': { 
			'crawler': "Optional. Crawler URL to filter on.",
			'likes_only': "Optional. Set to 1 to only show liked posts.",
			'non_matches': "Optional. Set to 1 to show posts that don't match a filter.",
		}
	}

	filters = { 'is_match': True }

	if request.REQUEST.get("likes_only","0") == "1":
		filters["likes"] = True

	if request.REQUEST.get("non_matches","0") == "1":
		del filters["is_match"]

	posts = json.loads(
					serializers.serialize(
										"json", 
										Post.objects.filter(**filters).order_by('add_date').reverse(), 
										ensure_ascii=False
										)
										)



	resp['posts'] = posts
	return HttpResponse(json.dumps(resp))
