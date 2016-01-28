import unittest
import os

__author__ = 'oswaldjones'


class TestInfobox(unittest.TestCase):

    def test_Infobox(self):

        from wikipedia_parser.infobox import Infobox as info

        wiki_text = ""

        # wiki text for Ada_Lovelace has been saved to local .txt file for testing
        tests_folder = os.path.dirname(os.path.realpath(__file__))
        with open(tests_folder + '/Ada_Lovelace_wiki_text.txt') as f:
            wiki_text = f.read()

        infobox = info.Infobox(wiki_text)

        self.assertEqual(infobox.page_name,      'Ada, Countess of Lovelace')
        self.assertEqual(infobox.template_name,  'infobox person')
        self.assertEqual(infobox.image_filename, 'Ada_Lovelace_portrait.jpg')
        self.assertEqual(infobox.image_url,      'https://upload.wikimedia.org/wikipedia/commons/a/a4/Ada_Lovelace_portrait.jpg')

        # plain_text is empty string because wiki templates are striped for plain text
        self.assertEqual(
            infobox.data['parents']['plain_text'], '')

        # raw_text shows that the value is just one wiki template signified by surrounding {{double braces}}
        self.assertEqual(
            infobox.data['parents']['raw_text'],
            '{{plainlist |'
            '\n* [[Lord Byron|George Gordon Byron, 6th Baron Byron]]'
            '\n* [[Anne Isabella Byron, Baroness Byron|Anne Isabella Milbanke, 11th Baroness Wentworth]]'
            '\n  }}')

        # wiki_links are page titles to other Wikipedia pages
        self.assertEqual(
            infobox.data['parents']['wiki_links'], [u'Lord Byron', u'Anne Isabella Byron, Baroness Byron'])
