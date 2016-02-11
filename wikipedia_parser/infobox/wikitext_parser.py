import re

from wikipedia_parser.infobox import clean_text as clean_help
from wikipedia_parser.infobox import wikitext_helpers as wtext_help
from wikipedia_parser.third_party_adapters import parserfromhell_adapter as adapter

__author__ = 'oswaldjones'


def get_simple_text(wtext, key, clean=True):

    text = None

    keys = key if type(key) is list else [key]

    template_dict = adapter.template_dict(wtext)
    wtext_lines = wtext_help.get_wtext_lines(wtext)

    if keys:
        for possible_key in keys:

            # try getting from parserfromhell
            if not text and template_dict:
                text = template_dict.get(possible_key)

            # final attempt if still no text
            if not text and wtext_lines:
                matched_line = wtext_help.find_key_val_line(wtext, possible_key)
                if matched_line:
                    key_val = matched_line.strip(' \t\n\r').split("=", 1)
                    if len(key_val) == 2:
                        text = key_val[1].strip()

    if text and clean:
        text = clean_help.clean_text(text)

    return text


def extract_page_links(wtext, key):

    links = []

    keys = key if type(key) is list else [key]

    template_dict = adapter.template_dict(wtext)
    wtext_lines = wtext_help.get_wtext_lines(wtext)

    if keys:
        for possible_key in keys:

            # try parserfromhell
            if not links and template_dict:
                if template_dict.get(possible_key):
                    matches = re.findall("\[\[(.*?)\]\]", template_dict.get(possible_key))
                    links = [link.split("|", 1)[0] for link in matches]

            # final attempt if still no links
            if not links and wtext_lines:
                matched_line = wtext_help.find_key_val_line(wtext_lines, possible_key)
                if matched_line:
                    key_val = matched_line.strip(' \t\n\r').split("=")
                    if len(key_val) == 2:
                        matches = re.findall("\[\[(.*?)\]\]", key_val[1].strip())
                        links = [link.split("|", 1)[0] for link in matches]

    return links



