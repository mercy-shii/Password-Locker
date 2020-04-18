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
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_account == string:
                return user   
      