import unittest
from password import Password

class TestPassword(unittest.TestCase):
   
   
    def setUp(self):
        '''
        set up method to run before each test case
        '''

        self.new_password = Password("instagram","zubeir","Abubakar","Black-heart","5250")
        
    def test_init(self):
        '''
        def test_init test case to see if the object is initialized correctly
        '''
        self.assertEqual(self.new_password.smedia,"instagram")
        self.assertEqual(self.new_password.first_name,"zubeir")
        self.assertEqual(self.new_password.last_name,"Abubakar")
        self.assertEqual(self.new_password.user_name,"Black-heart")
        self.assertEqual(self.new_password.password,"5250")

    def tearDown(self):
        Password.password_list = []

    def test_save_password(self):
            self.new_password.save_password()
            self.assertEqual(len(Password.password_list),1)

    def test_save_mulitple_password(self):
            self.new_password.save_password()
            test_password = Password("Snapchat","zubeir","Abubakar","Black-heart","5250") 
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)

    def test_delete_passwords(self):
            self.new_pass word.save_password()
            test_password = Password("facebook","Zubeir","Abubakar","Black-heart","5250") 
            test_password.save_password()

            self.new_password.delete_passwords()
            self.assertEqual(len(Password.password_list),1)

    def test_display_all_passwords(self):
            self.assertEqual(Password.display_passwords(),Password.password_list)


if __name__ == '__main__':
    unittest.main()