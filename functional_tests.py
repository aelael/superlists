from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''new User test'''

    def setUp(self):
        '''setting'''
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        '''tearing down'''
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: User can start a list and retrieve it later'''
        # User loads To-Do List homepage
        self.browser.get('http://localhost:8000')

        # User sees 'To-Do List' in webpage title
        self.assertIn('To-Do List', self.browser.title)
        self.fail('Ending test!')

        # User is prompted to enter a To-Do List item
        # User enters list item "Test Item 1"

        # User is prompted to enter another To-Do List item
        # User enters list item "Test Item 2"

        # After page updates, it shows both items in the User list
        # User sees notice that unique URL has been generated for his To-Do List

        # User follows the link and checks his To-Do List

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')