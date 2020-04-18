


class User:
    """
    class that generates new instances of users
    """
    user_list = []

    def _init_(self,username,account,passwords):
        self.username = username
        self.passwords = passwords
        self.account = account