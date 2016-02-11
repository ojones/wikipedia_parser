#!/usr/bin/python
#! -*- coding: utf-8 -*-


import logging

from wikipedia_parser.third_party_adapters import api_adapters as adapter
from wikipedia_parser.wikipedia_api import http_calls as fetch
from wikipedia_parser.wikipedia_api import json_parsers as parse

logging.getLogger("requests").setLevel(logging.WARNING)


class WikipediaAPI:

    def __init__(self, search_id, all_http_calls=True):

        wobj = adapter.fetch_wobj(search_id)

        self.search_id = handle_redirect(search_id, wobj)

        response           = fetch.async_response(self.search_id)
        self.html          = parse.wiki_html(response.get('wiki_html'))
        self.expanded_html = parse.wiki_expanded_templates(response.get('wiki_expanded_html'))
        self.wiki_text     = parse.wiki_text(response.get('wiki_text'))
        self.title         = parse.wiki_title(response.get('wiki_text'))
        self.page_id       = parse.wiki_page_id(response.get('wiki_text'))

        self.categories = None
        self.page_links = None
        self.summary    = None

        # these external calls take longer currently not asynchronous
        if all_http_calls:
            self.categories = adapter.fetch_api_categories(self.search_id, wobj)
            self.page_links = adapter.fetch_wobj_pagelinks(wobj)
            self.summary    = adapter.fetch_wobj_summary(wobj)


def handle_redirect(id, wobj):

    id = unicode(id)

    if not wobj:
        return id

    if id.isdigit():
        id = wobj.pageid
    else:
        id = wobj.title.replace(' ', '_').encode('utf-8')

    return id





