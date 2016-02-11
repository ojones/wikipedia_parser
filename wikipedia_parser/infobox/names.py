from wikipedia_parser.infobox import wikitext_parser as parse
from wikipedia_parser.infobox import clean_text as clean_help
from wikipedia_parser.infobox import wikitext_helpers as wtext_help

__author__ = 'oswaldjones'


def page_name(wtext):

    name = parse.get_simple_text(wtext, ['name', 'show_name', 'season_name', 'film name'])

    if not name:
        name = extract_page_name(wtext)

    return clean_help.clean_text(name)


def extract_page_name(wtext):

    name = None

    wtext_lines = wtext_help.get_wtext_lines(wtext)

    for line in wtext_lines:
        if not name:
            if line.startswith("\'\'") and not name:
                pieces = line.split("\'\'")
                try:
                    name = next(piece for piece in pieces if len(piece) >= 1)
                except:
                    pass
        else:
            break

    return name


def extract_infobox_name(wtext):

    name = None

    wtext_lines = wtext_help.get_wtext_lines(wtext)

    if wtext_lines:
        matched_line = None
        try:
            matched_line = next(line.strip() for line in wtext_lines
                                if line.strip().startswith("{{infobox")
                                or line.strip().startswith("{{Infobox"))
        except:
            pass

        if matched_line:
            line = matched_line.strip(' \t\n\r{').lower()
            name = clean_help.remove_html(line.replace("|", ""))

    return name



