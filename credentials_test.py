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
        self.new_credentials = Credentials("Instagram", "PUGb","987654")



    def     