from django.contrib.auth.hashers import BasePasswordHasher

class MyPasswordHasher(BasePasswordHasher):
    algorithm = "mypw"

    def encode(self, password, salt):
        assert password is not None
        return password

    def verify(self, password, encoded):
        encoded_2 = self.encode(password, '')
        return encoded.upper() == encoded_2.upper()

    def safe_summary(self, encoded):
        return ''
