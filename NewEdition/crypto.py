from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class Cripto:
    """
    class for encoding and decoding data

    """
    key_file_path: str = "keyfile.key"
    fernet = Fernet(open(key_file_path, 'rb').read())


    def generate_keyfile(self):
        """
        Initial key file generation

        Key file saw in keyfile.key
        :return: None
        """
        key = Fernet.generate_key()
        with open('keyfile.key', 'wb') as keyfile:
            keyfile.write(key)


    def encrypt(self, wrap_string: str) -> bytes:
        """
        Encrypts  string
        :param wrap_string: data in str formate for encrypt
        :return: encrypted string in bytes format
        """
        encrypted_string = self.fernet.encrypt(bytes(wrap_string.encode()))
        return encrypted_string


    def decrypt(self, encrypted_string: str) -> str:
        """
        Decrypts string
        :param encrypted_string: encrypted data in bytes formate
        :return: decrypted data in str formate
        """
        decrypted_string = self.fernet.decrypt(encrypted_string).decode()
        return decrypted_string
