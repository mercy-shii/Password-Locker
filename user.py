class User:
    """
    class that generates new instances of users
    """
    User_list = []

    def __init__(self, name, account, passwords):
        self.name = name
        self.account = account
        self.passwords = passwords

      