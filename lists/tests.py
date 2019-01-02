from django.test import TestCase

class SmokeTest(TestCase):
    '''toxicity test'''

    def test_bad_maths(self):
        '''test: wrong math calculations'''
        self.assertEqual(1 + 1, 3)