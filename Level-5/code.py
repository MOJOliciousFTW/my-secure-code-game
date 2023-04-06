import os

from argon2 import PasswordHasher


class Argon2Hasher:
    def get_initial_hash(self, password: str):
        ph = PasswordHasher()
        return ph.hash(password)

    def check_password(self, password: str, known_hash):
        ph = PasswordHasher()
        return ph.verify(known_hash, password)


# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
SECRET_KEY = "TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8"
PASSWORD_HASHER = "MD5_hasher"
