import sys
import time
import logging
import json

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from bs4 import BeautifulSoup

from django.conf import settings


fresh = False


class RefreshEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        global fresh
        ACCEPTED_EXTENSIONS = getattr(settings, 'FRESH_ACCEPTED_EXTENSIONS', [
            '.py',
            '.html',
            '.js',
            '.css',
        ])
    
        for extension in ACCEPTED_EXTENSIONS:
            if event.src_path.lower().endswith(extension):
                fresh = True


class FreshMiddleware(object):

    def process_response(self, request, response):
        if not settings.DEBUG:
            return response

        global fresh
        mimetype = response._headers['content-type'][1]
        IGNORED_PAGES = getattr(settings, 'FRESH_IGNORED_PAGES', [
            '/admin/',
            '/admin_keywords_submit/',
        ])
        ignored = False

        for ignored_page in IGNORED_PAGES:
            if request.path.lower().startswith(ignored_page):
                ignored = True

        if not ignored:
            if mimetype == 'application/json':
                items = json.loads(response.content)
                if fresh and items.get('fresh') != None:
                    fresh = False
                    items['fresh'] = True
                    response.content = json.dumps(items)
            elif mimetype == 'text/html; charset=utf-8':
                soup = BeautifulSoup(response.content)
                url = settings.STATIC_URL + 'fresh/js/refresher.js'
                script_fresh = soup.new_tag('script', src=url)
                soup.head.append(script_fresh)
                response.content = soup.prettify()

        return response


    def watcher(self):
        observer = Observer()

        path = settings.SITE_ROOT
        event_handler = RefreshEventHandler()
        observer.schedule(event_handler, path, recursive=True)

        observer.start()

    def __init__(self):
        if settings.DEBUG:
            self.watcher()

