class User:
    """
    class that generates new instances of users
    """
    user_list = []

    def __init__(self, name, account, passwords):
        self.name = name
        self.account = account
        self.passwords = passwords

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)  

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 

    @classmethod
    def find_by_account(cls,string):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: account to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.account == string:
                return user   
      
    @classmethod
    def user_exists(cls, string):
        """
        method that helps to confirm the existence of the account and the returns boolean
        """
        for user in cls.user_list:
            if user.account == string:
                return True
        return False  

    @classmethod
    def display_user(cls):
        """
        method that returns the User list
        """
        return cls.user_list

    @classmethod
    def copy_passwords(cls, string):
        password_found = User.find_by_account(string)
        copy(password_found.passwords)
    
class Account:
    account_list = []

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save_account(self):
        Account.account_list.append(self)

    def delete_account(self):
        Account.account_list.remove(self)    


