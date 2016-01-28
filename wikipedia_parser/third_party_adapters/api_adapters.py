import mwclient
import wikipedia


# wobj
def fetch_wobj(id):
    # TODO: isdigit is not robust enough, a title could be number instead of an id
    wobj = None

    try:
        if str(id).isdigit():
            wobj = wikipedia.page(pageid=id, auto_suggest=False)
        else:
            wobj = wikipedia.page(title=id, auto_suggest=False)
    except:
        # error in 3rd party python-wikipedia package
        pass

    return wobj


# wobj
def fetch_wobj_pagelinks(wobj):

    if not wobj:
        return None

    return [x.encode('utf-8') for x in wobj.links]


# wobj
def fetch_wobj_html(wobj):

    if not wobj:
        return None

    return unicode(wobj.html()).encode("utf-8")


# wobj
def fetch_wobj_summary(wobj):

    if not wobj:
        return None

    return wobj.summary


# wmclient
def fetch_mwclient(id):

    MWCLIENT_SITE = mwclient.Site('en.wikipedia.org')

    return MWCLIENT_SITE.Pages[id]


# wobj with mwclient backup
def fetch_api_categories(id, wobj):

    categories = []

    try:
        if id.isdigit() and wobj:
            categories = wobj.categories
        else:
            page = fetch_mwclient(id)
            for category in list(page.categories()):
                categories.append(category.name)
            return categories
    except:
        pass

    return categories