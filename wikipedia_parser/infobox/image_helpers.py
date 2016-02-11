import hashlib
import requests
from wikipedia_parser.infobox import wikitext_parser as parse

__author__ = 'oswaldjones'


def get_image_url(image_file):

    return validate_image_url(build_image_url_from_filename(image_file))


def is_valid_url(image_url):

    if not image_url:
        return False

    # TODO: this should be in wikipedia_api
    r = requests.head(image_url)
    # cmn.autolog(image_url + ' : ' + str(r.status_code))
    return r.status_code == requests.codes.ok


def validate_image_url(image_url):

    if not image_url:
        return None

    if is_valid_url(image_url):
        return image_url
    elif is_valid_url(image_url.replace('/wikipedia/en/', '/wikipedia/commons/')):
        return image_url.replace('/wikipedia/en/', '/wikipedia/commons/')
    else:
        # cmn.autolog(image_url + ': valid image_url could not be resolved')
        return None


def get_hex_path(image_file):

    if not image_file:
        return None

    hex_path = None

    m = hashlib.md5()
    m.update(image_file)
    hexed = m.hexdigest()
    if hexed:
        hex_path = '/' + str(hexed[0]) + '/' + str(hexed[:2]) + '/'

    return hex_path


def build_image_url_from_filename(image_file):

    if not image_file:
        return None

    return 'https://upload.wikimedia.org/wikipedia/en' + get_hex_path(image_file) + image_file


def get_image_filename(wtext):

    image_key_list = ['image', 'img', 'cover']

    filename = parse.get_simple_text(wtext, image_key_list)

    if filename:
        filename = filename.replace(' ', '_').encode('utf-8')
        if '[[' in filename:
            filename = filename.replace('[[', '').replace(']]', '')
        if filename.startswith('File:'):
            filename = filename.replace('File:', '')

    return filename


def get_alt(wtext):

    return parse.get_simple_text(wtext, 'alt')


def get_caption(wtext):

    return parse.get_simple_text(wtext, 'caption')



