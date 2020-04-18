class User(Object):
    """
    class that generates new instances of users
    """
    User_list = []

    def _init_(self, name, account, passwords):
        self.name = name
        self.account = account
        self.passwords = passwords

pass        