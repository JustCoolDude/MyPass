from dataclasses import dataclass


@dataclass(init=False)
class DataItem:
    site: str
    login: str
    password: str

    def collect_data(self):
        self.site = input("Введите сайт: ").strip().lower()
        self.login = input("Введите лоин: ")
        self.password = input("Введите пароль: ")

    def __str__(self):
        return (str(self.__dict__))
        # return (f"{self.site}\t{self.login}\t{self.password}")


@dataclass
class Storage:
    file_path: str = "P.txt"

    def del_data(self, index):
        with open(self.file_path, 'r', encoding='utf-8') as data_base:
            data_list = [i.strip().split('\t') for i in data_base.readlines()]
            del_confirm = False
            site = data_list[index][0]
            print(f'Удалить данные сайта: {site}? Y/N')
            if input().lower() == 'y': del_confirm = True
            if del_confirm:
                data_list.pop(index)
                with open(self.file_path, 'w', encoding='utf-8') as data_base:
                    for string in data_list:
                        data_base.write('\t'.join(string) + '\n')
                print(f"данные сайта {site} успешно удалены")

    def get_data(self):
        """
        :return: list of data
        """
        with open(self.file_path, 'r', encoding='utf-8') as data_base:
            return (''.join(list(data_base)))

    def write(self, datastr: str):
        """
        write rata in storage
        """
        with open(self.file_path, 'a', encoding='utf-8') as data_base:
            data_base.write(datastr + "\n")
            data_base.close()


@dataclass
class StorageOperator:
    storage = Storage()

    def _data_decoding(self, wrap_str: str) -> list[list]:
        return [i.split('\t') for i in wrap_str.split('\n')]

    def _data_coding(self, data: DataItem) -> str:
        return '\t'.join([data.__dict__[i] for i in data.__dict__])

    def _get_data(self) -> list:
        data_list = self._data_decoding(self.storage.get_data())
        return data_list

    def print_all(self):
        data = self._get_data()
        [print(*i) for i in data]

    def find_data(self, reqest: str, do_with_found: str = 'print'):
        found_request = False
        for index, item in enumerate(self._get_data()):
            if item[0] == reqest:
                found_request = True
                if do_with_found == 'print':
                    print(f'Сайт: {item[0]}\nЛогин: {item[1]}\nПароль: {item[2]}')
                    break
                elif do_with_found == "erase":
                    self.storage.del_data(index)
                    break

        if not found_request: print(f'Сайт {reqest} не найден')

    def write_data(self, wrap_data: DataItem):
        formatted_data = self._data_coding(wrap_data)
        self.storage.write(formatted_data)


@dataclass
class Program:
    operation = StorageOperator()
    storag = Storage()

    def do_choice(self, choise: int):

        def add_alement():
            data_item = DataItem()
            data_item.collect_data()
            self.operation.write_data(data_item)

        def print_all():
            self.operation.print_all()

        def del_element():
            self.operation.find_data(input("Введите имя сайта для удаления: "), "erase")

        def find_site():
           self.operation.find_data(input("Введите имя сайта").strip().lower())

        function_list = {1: add_alement, 2: find_site, 3:del_element, 4:print_all}
        if choise <= len(function_list):
            return function_list[choise]()
        else:
            print('Такой команды нет')

if __name__ == '__main__':

    done= False
    while not done:
        program = Program()
        print("""
Выберите действие:
(1) Добавить элемент
(2) Найти данные
(3) Удалить данные
(4) Вывести весь список
(5) Exit
    """)
        try:
            choice = int(input())
        except ValueError:
            print("Неверный ввод")
        else:
            if choice   != 5:
                program.do_choice(choice)
                done = False if input('Продолжить? y/n ').lower() == 'y' else True
            else:
                done = True

