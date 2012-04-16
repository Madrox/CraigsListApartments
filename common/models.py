from django.db import models
import parser
from filters import post_filter
import urllib
from BeautifulSoup import BeautifulSoup
from datetime import datetime


class Crawler(models.Model):
	link = models.URLField(max_length=100,null=False,primary_key=True)
	hits_email = models.EmailField(null=True)
	store_matches_only = models.BooleanField(default=True, null=False)
	enabled = models.BooleanField(default=True)
	last_run = models.DateTimeField()

	def listings(self):
		return parser.listings(
								urllib.urlopen(self.link).read()
								)

	class Meta:
		db_table = "craigslist_crawlers"


class Post(models.Model):
	crawler = models.ForeignKey(Crawler)
	link = models.URLField(max_length=100,null=False,primary_key=True)
	headline = models.CharField(max_length=300)
	email = models.EmailField(null=True)

	raw_html = models.TextField()
	raw_text = models.TextField()

	cost = models.DecimalField(max_digits=6,decimal_places=2,null=True)
	bedrooms = models.IntegerField(null=True)

	is_match = models.BooleanField(null=False)

	like = models.BooleanField(null=False,default=False)
	dislike = models.BooleanField(null=False,default=False)

	add_date = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = "craigslist_posts"

	def load(self, url):
		self.link = url
		html = urllib.urlopen(url).read()
		self.soup = BeautifulSoup(html)

		self.headline = unicode(self.soup.find('h2').getText())

		userbody = self.soup.find(id="userbody")
		if userbody is not None:
			self.raw_html = unicode(userbody)
			self.raw_text = unicode(userbody.getText())

		self.cost = parser.cost(self.headline+" "+self.raw_text)

		self.email = parser.cl_email(html)
		self.bedrooms = parser.bedrooms(html)

		self.is_match = post_filter(
								self.link,
								self.headline,
								self.raw_text,
								self.raw_html,
								self.cost,
								self.email,
								)


class Extraction(models.Model):
	link = models.ForeignKey(Post)
	namespace = models.CharField(max_length=100)
	value = models.TextField()


	class Meta:
		db_table = "craigslist_extracted_data"





