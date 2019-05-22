
class UserModel:

    @staticmethod
    def validate_subscription(form):
        pass

    @staticmethod
    def get_by_id(userid):
        pass

    @staticmethod
    def get_by_email(email):
        pass

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, password):
        pass

    def is_authenticated(self):
        pass

    def save(self):
        pass