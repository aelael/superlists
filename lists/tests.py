from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    '''homepage test'''

    def test_root_url_resolves_to_homepage_view(self):
        '''test: root url resolves to homepage view'''
        found    = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''test: home page returns correct HTML'''
        request  = HttpRequest()
        response = home_page(request)
        html     = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do List</title>', html)
        self.assertTrue(html.endswith('</html>'))