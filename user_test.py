import unittest
from user import User



class TestUser(unittest.TestCase):
    """
    Test that defines test case for the user class

    Args:unittest.Testcase: Testcase That helps in creating test_cases
    """

    def setUp(self):
      """
      set up method to run before each test case
      """

      self.new_user = User("One","Two","12345678")
    def tearDown(self):
      """
      tearDown method that will clean up after each test case has run
      """

      User.user_list = []


    def test_init(self):
      """
      test_init case to test if the user objects is initialised properly
      
      """
      self.assertEqual(self.new_user.first_name, "One")
      self.assertEqual(self.new_user.last_name, "Two")
      self.assertEqual(self.new_user.password, "12345678")
    
    def test_save_user(self):
      """
      test if the user object is saved in the user_list array

      """
      self.new_user.save_user()
      self.assertEqual(len(User.user_list),1)
    
if __name__== "__main__":
    unittest.main()