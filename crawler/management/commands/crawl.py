from django.core.management.base import BaseCommand, CommandError
import urllib
import re
from common.models import Post,Extraction,Crawler
from datetime import datetime


class Command(BaseCommand):
    help = "Begins collecting from specified Craig's List URL"

    def handle(self, *args, **options):
        for crawler in Crawler.objects.filter(enabled=True):
            self.stdout.write("Starting {0}\n".format(crawler.link))
            for link in crawler.listings():
                try:
                    Post.objects.get(link=link)
                except Post.DoesNotExist:
                    self.stdout.write(link)
                    post = Post()
                    post.load(link)
                    post.crawler = crawler
                    if post.is_match: 
                        self.stdout.write(" Yes!\n")
                    else: 
                        self.stdout.write(" No\n")

                    if post.is_match or not crawler.store_matches_only:
                        post.save()
            crawler.last_run = datetime.now()
            crawler.save()
                

        self.stdout.write("Done!\n")

