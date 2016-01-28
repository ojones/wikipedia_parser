## Synopsis

Uses Wikipedia API to store page id, title, html, wiki text, expanded templates, categories, page links, and summary in one class object for easy reference.  Also parses infobox data from wiki text, including page name, template name, image name, image url, and labeled key value data.

## Code Example

Instantiate Wikipedia API object with page name or id:
```
# wikipedia id can be digit or name (redirects are handled :)
page = 'Ada_Lovelace'
wiki_api = WikipediaAPI(page)
```
Here is the print list of available api resources 
```
> print(dir(wiki_api))
[   ...
    'categories',
    'expanded_html',
    'html',
    'page_id',
    'page_links',
    'search_id',
    'summary',
    'title',
    'wiki_text']
```
If an infobox is present on page, you can parse the infobox data:
```
# wiki text can be from anywhere, does not need to come from WikipediaAPI object
wiki_text = wiki_api.wiki_text
infobox = Infobox(wiki_text)
```
Here is the print list of available attributes 
```
> print(dir(infobox))
[   ...
    'data',
    'image_filename',
    'image_url',
    'page_name',
    'template_name']
```
Infobox "data" is a dict of plain_text (ie no wiki templates), raw_text, and wiki links to other pages:
```
{   u'birth_date': {   'plain_text': u'',
                       'raw_text': u'{{birth date|1815|12|10|df=yes}}',
                       'wiki_links': []},
    u'birth_name': {   'plain_text': u'The Hon. Augusta Ada Byron',
                       'raw_text': u'The Hon. Augusta Ada Byron',
                       'wiki_links': []},
    u'birth_place': {   'plain_text': u'London, England',
                        'raw_text': u'London, England',
                        'wiki_links': []},
    u'caption': {   'plain_text': u'Ada, Countess of Lovelace, 1840',
                    'raw_text': u'Ada, Countess of Lovelace, 1840',
                    'wiki_links': []},
    u'children': {   'plain_text': u'',
                     'raw_text': u'{{plainlist |\n* [[Byron King-Noel, Viscount Ockham|Byron King-Noel, Viscount Ockham and 12th Baron Wentworth]]\n* [[Anne Blunt, 15th Baroness Wentworth]]\n* [[Ralph King-Milbanke, 2nd Earl of Lovelace]]}}',
                     'wiki_links': [   u'Byron King-Noel, Viscount Ockham',
                                       u'Anne Blunt, 15th Baroness Wentworth',
                                       u'Ralph King-Milbanke, 2nd Earl of Lovelace']},
    u'death_date': {   'plain_text': u'',
                       'raw_text': u'{{death date and age|1852|11|27|1815|12|10|df=yes}}',
                       'wiki_links': []},
    u'death_place': {   'plain_text': u'Marylebone, London, England',
                        'raw_text': u'[[Marylebone]], London, England',
                        'wiki_links': [u'Marylebone']},
    u'field': {   'plain_text': u'Mathematics, computing',
                  'raw_text': u'Mathematics, computing',
                  'wiki_links': []},
    u'image': {   'plain_text': u'Ada Lovelace portrait.jpg',
                  'raw_text': u'Ada Lovelace portrait.jpg',
                  'wiki_links': []},
    u'name': {   'plain_text': u'Ada, Countess of Lovelace',
                 'raw_text': u'Ada, Countess of Lovelace',
                 'wiki_links': []},
    u'parents': {   'plain_text': u'',
                    'raw_text': u'{{plainlist |\n* [[Lord Byron|George Gordon Byron, 6th Baron Byron]]\n* [[Anne Isabella Byron, Baroness Byron|Anne Isabella Milbanke, 11th Baroness Wentworth]]\n  }}',
                    'wiki_links': [u'Lord Byron', u'Anne Isabella Byron, Baroness Byron']},
    u'resting_place': {   'plain_text': u'Church of St. Mary Magdalene, Hucknall, Nottingham, England',
                          'raw_text': u'[[Church of St. Mary Magdalene, Hucknall]], Nottingham, England',
                          'wiki_links': [u'Church of St. Mary Magdalene, Hucknall']},
    u'spouse': {   'plain_text': u'William King-Noel, 1st Earl of Lovelace',
                   'raw_text': u'[[William King-Noel, 1st Earl of Lovelace]]',
                   'wiki_links': [u'William King-Noel, 1st Earl of Lovelace']},
    u'title': {   'plain_text': u'Countess of Lovelace',
                  'raw_text': u'Countess of Lovelace',
                  'wiki_links': []}}
```
## Motivation

[wtf_wikipedia](https://github.com/spencermountain/wtf_wikipedia) and [mwparserfromhell](https://github.com/earwig/mwparserfromhell) were the best wikipedia parsers I could find.  This one is better. 

## Installation

Currently only works on Python 2.7 :(
```
> python setup.py install
```

## Tests

```
> py.text
```

## Contributors

Don't be shy.

## License

MIT
