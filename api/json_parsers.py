def wiki_text(r):

    wtext = None

    try:
        wtext = unicode(r.json().get('query').get('pages').values()[0].get('revisions')[0].get('*')).encode("utf-8")
    except:
        # in case json error
        pass

    return wtext


def wiki_html(r):

    html = None

    try:
        html = unicode(r.json().get('query').get('pages').values()[0].get('revisions')[0].get('*')).encode("utf-8")
    except:
        # in case json error
        pass

    return html


def wiki_page_id(r):

    pageid = None

    try:
        pageid = str(r.json()['query']['pages'].values()[0]['pageid']).encode("utf-8")
    except:
        # in case json error
        pass

    return unicode(pageid)


def wiki_title(r):

    title = None

    try:
        title = r.json()['query']['pages'].values()[0]['title'].replace(' ', '_').encode("utf-8")
    except:
        # in case json error
        pass

    return title


def wiki_expanded_templates(r):

    expanded = None

    try:
        expanded = unicode(r.json().get('query').get('pages').values()[0].get('revisions')[0].get('*')).encode("utf-8")
    except:
        # in case of json error
        pass

    return expanded


def wiki_categories(r_json):

    subcats = []

    if 'query' in r_json:
        for subcat in r_json.get('query').get('categorymembers'):
            if subcat['ns'] == 14:
                subcats.append((unicode(subcat['pageid']), subcat['title']))

    return subcats