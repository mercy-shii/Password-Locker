class User:
    """
    Class that generates new instances of users
    """

    user_list = []


    def __init__(self,login_username,password):

      

        self.login_username = login_username
        self.password = password