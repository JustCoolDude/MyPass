from dataclasses import dataclass
import os

from NewEdition.storage import Storage





class Formater:

    def input_formatind(self):
        pass

    def output_formating(self):
        pass


if __name__ == '__main__':
    storrage = Storage()
    storrage.write_data('gthdfz cnhjrf\n вторя строка')
    print(storrage.read_data())

