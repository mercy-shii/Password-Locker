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

      