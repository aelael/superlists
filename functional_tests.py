from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys

import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do List', header_text)
        
        # User is prompted to enter a To-Do List item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter To-Do List item'
        )

        # User enters list item "Test Item 1"
        inputbox.send_keys('Test Item 1')
        
        # After User presses ENTER key, page reloads with new To-Do List element
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows  = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Test Item 1' for row in rows),
            "New To-Do item did not appear in table"
        )

        # User is prompted to enter another To-Do List item
        # User enters list item "Test Item 2"
        self.fail('Ending test!')

        # After page updates, it shows both items in the User list
        # User sees notice that unique URL has been generated for his To-Do List

        # User follows the link and checks his To-Do List

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')