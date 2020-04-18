import unittest 
from user import User 

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Mercy","Facebook","shii254") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.name,"Mercy")
        self.assertEqual(self.new_user.account,"Facebook")
        self.assertEqual(self.new_user.passwords,"shii254")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Jules","Twitter","ogolla1") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Shii","Instagram","lola90") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)       
    
    def test_find_user_by_account(self):
        '''
        test to check if we can find a user by account and display information
        '''

        self.new_user.save_user()
        test_user = User("Candy","whatsapp","abebe89") 
        test_user.save_user()

        found_user = User.find_by_account("whatsapp")

        self.assertEqual(found_account.passwords,test_user.passwords)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("me", "linkedIn", "12@12")
        test_user.save_user()
        user_exists = User.user_exists("linkedIn")
        self.assertTrue(user_exists)

    def test_display_credentials(self):
        self.assertEqual(User.display_credentials(), User.User_list)  

    def test_copy_passwords(self):
        """
        this method tests coping the password to clip board
        """
        self.new_credentials.save_details()
        User.copy_passwords("facebook")
        self.assertEqual(self.new_credentials.passwords, pyperclip.paste())
    


if __name__ == '__main__':
    unittest.main()