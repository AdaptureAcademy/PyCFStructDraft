
class Credentials:
    def __init__(self, file:str):
        self.file = file
        self.X_Auth_Email = ""
        self.X_Auth_Key = ""
        self.get_credentials()

    def get_credentials(self):
        # Read credentials from file an return a Credentials object with the stripped values (no whitespace)
        with open(self.file, "r") as f:
            text_cred = f.readline()
            email, key = text_cred.split(",")
        self.X_Auth_Email = email.strip()
        self.X_Auth_Key = key.strip()