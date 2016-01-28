from itertools import izip

import requests
import grequests

import urls
import json_parsers as parse


def simple_request(id):

    return requests.get(urls.make_url(id))


def category_search(search_category):

    data = {}

    params = {
        'action'  : 'query',
        'list'    : 'categorymembers',
        'cmtype'  : 'subcat',
        'prop'    : 'info',
        'format'  : 'json',
        'cmlimit' : '500',
    }

    search_category = str(search_category)

    if search_category.isdigit():
        params['cmpageid'] = search_category
    else:
        params['cmtitle'] = search_category

    r = requests.get('https://en.wikipedia.org/w/wikipedia_api.php', params=params)

    try:
        data = r.json()
    except:
        # r.json() sometimes throws errors
        pass

    return data


def async_response(id):

    response = {}

    url_list = [
        urls.make_url(id, is_html=True),
        urls.make_url(id, is_expanded=True),
        urls.make_url(id),
    ]

    rs = (grequests.get(u) for u in url_list)
    response_list = grequests.map(rs)

    response['wiki_html'] = response_list[0]
    response['wiki_expanded_html'] = response_list[1]
    response['wiki_text'] = response_list[2]

    return response


def async_related(add_call_list):

    url_list = []
    for related_id in add_call_list:
        url_list.append(urls.make_url(related_id[1]))
        url_list.append(urls.make_url(related_id[1], is_html=True))

    rs = (grequests.get(u) for u in url_list)
    responses = grequests.map(rs)

    return responses


def related_data(add_call_list):

    related = {}

    add_texts     = {}
    add_htmls     = {}

    count = 0
    for r_text, r_html in pairwise(async_related(add_call_list)):
        try:
            add_texts[add_call_list[count][0]] = parse.wiki_text(r_text)
            add_htmls[add_call_list[count][0]] = parse.wiki_html(r_html)
        except:
            # r.json() is risky so putting in try
            pass
        count += 1

    related['add_texts'] = add_texts
    related['add_htmls'] = add_htmls

    return related


def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

