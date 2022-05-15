import unittest
import account_management
import connection_flask
import connection_flask as fl
import password
import main

class Test_funcs(unittest.TestCase):

    def test_get_criteria(self):
        print("\nget criteria")
        obj_criteria = password.Password.getPolicies()
        self.assertIsInstance(obj_criteria, dict)

    def test_hash_pw(self):
        print("\nhash")
        obj_hash_pw = password.Password.pw_encrypt("Test")
        test_hashed = "c6ee9e33cf5c6715a1d148fd73f7318884b41adcb916021e2bc0e800a5c5dd97f5142178f6ae88c8fdd98e1afb0ce4c8d2c54b5f37b30b7da1997bb33b0b8a31"
        self.assertEqual(obj_hash_pw, test_hashed)
        self.assertNotEqual(obj_hash_pw, test_hashed + '4')

    def test_hibp_api(self):
        print("\nHIBP")
        pw_object = password.Password
        self.assertIsInstance(pw_object.hibp("abcd1234"), int)


    def test_login(self):
        print("\nlogin\n")
        obj_login = account_management.Account
        self.assertTrue(obj_login.login("Nana", "a6sd54*aA+F"))     # 1   ||  1
        self.assertFalse(obj_login.login("Nana", "420:eNasdgA+"))   # 1   ||  0
        self.assertFalse(obj_login.login("Ana", "a6sd54*aA+F"))     # 0   ||  1
        self.assertFalse(obj_login.login("Anna", "420:eNasdgA+"))   # 0   ||  0


    def test_check_pw_policies(self):
        print("\nCheck password polices")
        obj_pw_policies = password.Password
        self.assertTrue(obj_pw_policies.check_password_criteria_L_and_CA("420:69Amada:3"))
        self.assertFalse(obj_pw_policies.check_password_criteria_L_and_CA("420:69A"))
        self.assertFalse(obj_pw_policies.check_password_criteria_L_and_CA("420:69mada:3"))
        self.assertFalse(obj_pw_policies.check_password_criteria_L_and_CA("420:69A:3"))
        # symbols are disabled
        self.assertTrue(obj_pw_policies.check_password_criteria_L_and_CA("42069Amada"))


    def test_pw_comparation(self):
        print("\npw + hash comparation")
        user_pw = "*This+is-a-T3est*"
        user_pw_hashed = "6e2d9147e5b56e818518113bc7832605ef1a57b51a9a160f1695ab0f7c2fd50958c250a34bb3fed2dade15d68294eaf8e95d25a3e1eb4085197a865120e7ddd2"
        obj_pw_comparation = password.Password
        self.assertTrue(obj_pw_comparation.pw_comparation(user_pw, user_pw_hashed))
        self.assertFalse(obj_pw_comparation.pw_comparation(user_pw, user_pw_hashed + '3'))

    def test_create_account(self):
        print("\n create account")
        obj_create_account = account_management.Account
        #after the test it will NOT be possible to test another use with the name CARLOS and receives the return TRUE
        #self.assertTrue(obj_create_account.create_account("Carlos", "as65d40GZJ6+DQ5ad-"))
        #user already exists
        self.assertFalse(obj_create_account.create_account("Thomas", "asd564+a4dGda+"))
        #password goes agains the policies
        self.assertFalse(obj_create_account.create_account("User_Neuer", "1346795007:69"))

    def test_check_double_users(self):
        print("\nCheck for double users")
        obj_double_users = account_management.Account
        self.assertTrue(obj_double_users.check_for_double_users("Tutu.json"))
        self.assertFalse(obj_double_users.check_for_double_users("Shork.json"))

    def test_gpw(self):
        print("\ngpw")
        obj_generate_pw = main
        self.assertFalse(obj_generate_pw.gpw("password_list", 20))

    def test_hash_hibp(self):
        print("Hash HIBP")
        obj_hibp = password.Password
        self.assertEqual(obj_hibp.pw_hash_for_hibp("Test"), "640ab2bae07bedc4c163f679a746f7ab7fb5d1fa")
        self.assertNotEqual(obj_hibp.pw_hash_for_hibp("Test"), "640ab2bae07bedc4c163f679a746f7ab7fb5d1fa" + '1')


if __name__ == '__main__':
    unittest.main()