from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self, key, f, token):
        self.key = Fernet.generate_key()
        self.f = Fernet(key)
        self.token = ""
        
    def encrypt(self):
        self.token = self.f.encrypt(b"Example message")

    def decrypt(self):
        self.f.decrypt(self.token)