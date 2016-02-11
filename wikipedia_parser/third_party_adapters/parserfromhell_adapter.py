import re
import mwparserfromhell

from wikipedia_parser.tools import dict_helpers as dict_help


def templates(wtext, recursive=False):

    wikicode 		= mwparserfromhell.parse( wtext )
    page_templates 	= wikicode.filter_templates(recursive)

    return page_templates


def infobox_template(wtext):

    infobox_template = None

    page_templates 	= templates(wtext)
    pattern 		= re.compile("Infobox .*")
    infobox_matches = []

    for template in page_templates:
        if pattern.match( str( unicode(template.name).encode("utf-8") ) ):
            infobox_matches.append(template)

    if infobox_matches:
        # the first infobox is the main info box
        infobox_template = infobox_matches[0]

    return infobox_template


def infobox_template_name(infobox_template):

    name = None

    if infobox_template and infobox_template.name:
        name = str(infobox_template.name).strip().lower()

    return name


def infobox_key_values(infobox_template):

    key_values = []

    #Null and params check
    if not infobox_template:
        # cmn.autolog('no infobox_template passed to infobox_key_values')
        return None

    else:

        for param in infobox_template.params:
            # print "----------"
            # print type(param)

            if "=" in param:
                keyval 		= ( param.split('=', 1) )
                keyval[0] 	= keyval[0].strip()
                keyval[1] 	= keyval[1].strip()

                key_values.append( keyval )

    return key_values


def date_template(dateType, wtext):

    date_template = None

    page_templates 	= templates(wtext, recursive=True)
    matches = []

    for template in page_templates:
        try:
            template_name = template.name.strip().lower()

            if dateType in template_name and "date" in template_name:
                matches.append(template)
        except:
            pass

    if matches:
        date_template = matches[0]

    return date_template


def get_template(wtext, name):

    found_template = None

    page_templates = templates(wtext, recursive=True)
    matches = []

    for template in page_templates:
        template_name = str( unicode(template.name).encode("utf-8") ).lower()
        if name.lower() == template_name:
            matches.append(template)

    if matches:
        found_template = matches[0]

    return found_template


def extract_duration(wtext):

    duration = ""

    # hours   = None
    minutes = None
    seconds = None

    template = get_template(wtext, "duration")

    if template:
        if len(template.params) == 2:
            for item in template.params:
                # if "h=" in item:
                # 	hours   = unicode( item.split("=")[1] )
                if "m=" in item:
                    minutes = unicode( item.split("=")[1] )
                if "s=" in item:
                    seconds = unicode( item.split("=")[1] )

        # duration += str(hours)   if hours   else "00"
        # duration += ":"
        duration += str(minutes) if minutes else "00"
        duration += ":"
        duration += str(seconds) if seconds else "00"

    return duration if duration else None


def extract_date(date_template):

    if not date_template:
        return None

    date = None

    if len(date_template.params) > 3:

        year 	= unicode( date_template.get(1) )
        month 	= unicode( date_template.get(2) )
        day 	= unicode( date_template.get(3) )

        if year and month and day:
            date_list = [unicode(x) for x in [month, day, year]]
            date = '/'.join(date_list)
        elif year and month:
            date_list = [unicode(x) for x in [month, year]]
            date = '/'.join(date_list)
        elif year:
            date = year

    elif len(date_template.params) == 3:

        # cmn.autolog('non-standard date_template found')

        year	= unicode( date_template.get(1) )
        month	= unicode( date_template.get(2) )

        if year and month:
            date_list = [unicode(x) for x in [month, year]]
            date = '/'.join(date_list)

    elif len(date_template.params) == 2:

        #cmn.autolog('non-standard date template found')
        date = unicode( date_template.get(1) )

    elif len(date_template.params) == 1:

        #cmn.autolog('non-standard date template found')
        date = unicode( date_template.params[0] )

    return date


def get_birth_date(wtext):

    return extract_date( date_template("birth", wtext) )


def get_death_date(wtext):

    return extract_date( date_template("death", wtext) )


def template_dict(wtext):

    return dict_help.convert_to_dict(infobox_key_values(infobox_template(wtext)))



