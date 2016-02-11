from wikipedia_parser.infobox import wikitext_parser as parse
from wikipedia_parser.infobox import image_helpers as image
from wikipedia_parser.infobox import names
from wikipedia_parser.infobox import wikitext_helpers as wtext_help

__author__ = 'oswaldjones'


class Infobox:

    def __init__(self, wtext):

        self.page_name = names.page_name(wtext)
        self.template_name = names.extract_infobox_name(wtext)
        self.image_filename = image.get_image_filename(wtext)
        self.image_url = image.get_image_url(self.image_filename)
        self.data = data(wtext)


def data(wtext):

    infobox_data = {}

    for key in wtext_help.data_keys(wtext):
        infobox_data[key] = {}

    for key in infobox_data:
        infobox_data[key]['plain_text'] = parse.get_simple_text(wtext, key)
        infobox_data[key]['wiki_links'] = parse.extract_page_links(wtext, key)
        infobox_data[key]['raw_text'] = parse.get_simple_text(wtext, key, clean=False)

    return infobox_data



