from api import ExternalAPI as api
from infobox import Infobox as info


if __name__ == "__main__":

    import pprint
    pp = pprint.PrettyPrinter(indent=4, width=100)

    # wikipedia id can be digit or name
    test_id = 'Ada_Lovelace'

    ext_api = api.ExternalAPI(test_id)
    infobox = info.Infobox(ext_api.wiki_text)

    pp.pprint(dir(ext_api))
    pp.pprint(ext_api.title)
    pp.pprint(ext_api.page_id)

    pp.pprint(dir(infobox))
    pp.pprint(infobox.data)

