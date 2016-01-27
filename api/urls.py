ENDPOINT = "https://en.wikipedia.org/w/api.php"


def make_url(id, is_expanded=False, is_html=False):

    # TODO: isdigit is not robust enough, title could be number instead of string
    return make_id_url(id, is_expanded, is_html) if str(id).isdigit() else make_title_url(id, is_expanded, is_html)


def make_title_url(id, is_expanded=False, is_html=False):

    url = ENDPOINT + "?action=query&titles=" + url_safe_spaces(str(id)) + "&prop=revisions|pageprops&rvprop=content&format=json"
    if is_expanded:
        url += "&rvexpandtemplates"
    if is_html:
        url = ENDPOINT + "?format=json&rvprop=content&prop=revisions&rvparse=&titles=" + url_safe_spaces(str(id)) + "&rvlimit=1&action=query"

    return url


def make_id_url(id, is_expanded=False, is_html=False):

    url = ENDPOINT + "?action=query&pageids=" + url_safe_spaces(str(id)) + "&prop=revisions|pageprops&rvprop=content&format=json"
    if is_expanded:
        url += "&rvexpandtemplates"
    if is_html:
        url = ENDPOINT + "?format=json&rvprop=content&prop=revisions&rvparse=&pageids=" + url_safe_spaces(str(id)) + "&rvlimit=1&action=query"

    return url


def url_safe_spaces(text):

    return text.replace(" ", "%20")