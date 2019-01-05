from django.test                    import LiveServerTestCase

from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions     import WebDriverException

import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    '''new User test'''

    def setUp(self):
        '''setting'''
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        '''tearing down'''
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        '''waiting for a row in the list table'''
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows  = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: User can start a list and retrieve it later'''
        # User loads To-Do List homepage
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Test Item 1')

        # User is prompted to enter another To-Do List item
        # User enters list item "Test Item 2"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Test Item 2')
        inputbox.send_keys(Keys.ENTER)

        # After page updates, it shows both items in the User list
        self.wait_for_row_in_list_table('1: Test Item 1')
        self.wait_for_row_in_list_table('2: Test Item 2')

        # User sees notice that unique URL has been generated for his To-Do List
        self.fail('Test end!')
        # User follows the link and checks his To-Do List
