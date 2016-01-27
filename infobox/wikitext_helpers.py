from third_party_adapters import parserfromhell_adapter as adapter

__author__ = 'oswaldjones'


def get_wtext_lines(wtext):

    lines = []

    if wtext:
        lines = wtext.split('\n')

    return lines


def find_line_startswith(wtext, match_text):

    matched_line = None

    matchers = match_text if type(match_text) is list else [match_text]
    wtext_lines = get_wtext_lines(wtext)

    if matchers and wtext_lines:
        for possible_match in matchers:
            # TODO: should use loop break instead of this conditional
            if not matched_line:
                try:
                    matched_line = next(
                        line for line in wtext_lines if ' '.join(line.split()).startswith(possible_match))
                except:
                    pass

    return matched_line


def data_keys(wtext):

    keys = set()

    template_dict = adapter.template_dict(wtext)
    if template_dict:
        for key in template_dict:
            keys.add(key)

    for line in key_val_lines(wtext):
        key_val = line.split("=")
        if len(key_val) == 2:
            keys.add(key_val[0])

    return keys


def key_val_lines(wtext):

    lines = []

    for line in lines:
        if line.startswith("|") and "=" in line:
            lines.append(line)

    return lines


def lines_before_page_heading(wtext):

    lines = []

    for line in get_wtext_lines(wtext):
        lines.append(line)
        if line.startswith("=="):
            break

    return lines


def find_key_val_line(wtext_lines, key):

    matched_key_val = None

    key_variations = [unicode(key), unicode(key).capitalize(), unicode(key).upper()]

    key_val_lines = [line[1:].strip() for line in wtext_lines if line.startswith("|") and "=" in line]

    for possible_match in key_variations:
        if not matched_key_val:
            try:
                matched_key_val = next(line for line in key_val_lines if line.startswith(possible_match))
            except:
                pass

    return matched_key_val
