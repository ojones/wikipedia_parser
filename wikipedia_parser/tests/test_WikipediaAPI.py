import unittest

__author__ = 'oswaldjones'


class TestWikipediaAPI(unittest.TestCase):

    # this test requires http access to Wikipedia
    def test_WikipediaAPI(self):

        from wikipedia_parser.wikipedia_api import WikipediaAPI as api

        test_id = 'Ada_Lovelace'

        wiki_api = api.WikipediaAPI(test_id)

        self.assertEqual(wiki_api.title,   'Ada_Lovelace')
        self.assertEqual(wiki_api.page_id, '974')
        self.assertIsNotNone(wiki_api.html)
        self.assertIsNotNone(wiki_api.expanded_html)
        self.assertIsNotNone(wiki_api.wiki_text)
        self.assertIsNotNone(wiki_api.categories)
        self.assertIsNotNone(wiki_api.page_links)
        self.assertIsNotNone(wiki_api.summary)
