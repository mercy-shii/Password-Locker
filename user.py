class User:
    """
    Class that generates new instances of users
    """

    user_list = []


    def __init__(self,login_username,password):

      

        self.login_username = login_username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)    