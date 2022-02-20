import unittest
from credentials import Credentials


class TestUser(unittest.TestCase):
    """
    Test case that defines test cases for the user class behaviour
    """


    def setUp(self):
        """
        set up the method that will run before each test case
        
        """
        self.new_credentials = Credentials("Instagram", "PUBG","987654")



    def test_init(self):
        '''
        test that the credential object is initialised as expected
        '''

        self.assertEqual(self.new_credentials.platform_name, "Instagram")
        self.assertEqual(self.new_credentials.platform_user_name, "PUBG")
        self.assertEqual(self.new_credentials.platform_user_password, "997654")    