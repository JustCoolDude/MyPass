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
                        data_base.write('\t'.join(string)+'\n')
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


if __name__ == '__main__':

    operation = StorageOperator()
    storage = Storage()


    # data_item = DataItem()
    # data_item.collect_data()
    # operation.write_data(data_item)
    #
    #
    #operation.print_all()
    #
    #
    operation.find_data(input("Введите имя сайта").strip().lower())
    #
    # operation.find_data(input("Введите имя сайта"), "erase")