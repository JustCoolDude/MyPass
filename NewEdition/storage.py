from dataclasses import dataclass
import os


@dataclass
class Storage:
    """Klass for writing and reading data in file"""
    file_path: str = 'Passwords.txt'
    # if file_path not in os.listdir(): raise MyException

    def write_data(self, data: str):
        """
        Writind data:str in file
        :param data: data for writing
        :return:
        """
        if data:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(data)

    def read_data(self):
        """
        Reading all data from file
        :return: all data in str formate
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data


