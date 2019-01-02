from django.test            import TestCase
from django.urls            import resolve
from django.http            import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):
    '''homepage test'''

    def test_uses_home_template(self):
        '''test: home page returns correct HTML'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        '''test: it is possible to save POST request'''
        response = self.client.post('/', data = {'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')