from wikipedia_parser.wikipedia_api import WikipediaAPI as api
from wikipedia_parser.infobox import Infobox as info
import pprint
pp = pprint.PrettyPrinter(indent=4, width=100)


if __name__ == "__main__":

    # wikipedia id can be digit or name
    page = 'Ada_Lovelace'

    wiki_api = api.WikipediaAPI(page)
    pp.pprint(dir(wiki_api))
    pp.pprint(wiki_api.title)
    pp.pprint(wiki_api.page_id)

    infobox = info.Infobox(wiki_api.wiki_text)
    pp.pprint(dir(infobox))
    pp.pprint(infobox.data)

