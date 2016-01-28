import re

__author__ = 'oswaldjones'


def clean_text(text):


    text = remove_html(text)
    if text:
        text = remove_templates(text)
    if text:
        text = remove_link_brackets(text)
    if text:
        text = text.strip('\'\"\|').replace('  ', ' ')

    return text


def remove_html(text):

        if not text:
            return None

        clean = re.sub('<[^>]*>', '', text).strip()

        return clean if clean else None


def remove_templates(text):

    if not text:
        return None

    return re.sub(r'(\{\{[^}]+}\})', '', text).strip()


def remove_link_brackets(simple_text):

    text = simple_text

    if text:
        text = re.sub(r'\|(.*?)\]\]', '', text)

    return strip_pagelink_brackets(text)


def strip_pagelink_brackets(pagelink):

    return pagelink.replace('[[', '').replace(']]', '').strip()
