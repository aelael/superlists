from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    '''homepage test'''

    def test_root_url_resolves_to_homepage_view(self):
        '''test: root url resolves to homepage view'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)