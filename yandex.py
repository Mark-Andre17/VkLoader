import requests


class Yandex:
    def __init__(self, folder_name, token_list):
        self.token = token_list[0]
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        self.headers = {'Authorization': self.token}
        self.folder = self.create_folder(folder_name)

    def create_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        if requests.get(url, headers=self.headers, params=params).status_code != 200:
            requests.put(url, headers=self.headers, params=params)
            print(f'\nПапка {folder_name} успешно создана в корневом каталоге Яндекс диска\n')
        else:
            print(f'\nПапка {folder_name} уже существует. Файлы с одинаковыми именами не будут скопированы\n')
        return folder_name

    def in_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        resource = requests.get(url, headers=self.headers, params=params).json()['_embedded']['items']
        in_folder_list = []
        for elem in resource:
            in_folder_list.append(elem['name'])
        return in_folder_list

    def create_copy(self, dict_files):
        files_in_folder = self.in_folder(self.folder)
        added_files_num = 0
        for key in dict_files.keys():
            if key not in files_in_folder:
                params = {'path': f'{self.folder}/{key}',
                          'url': dict_files[key],
                          'overwrite': 'false'}
                requests.post(self.url, headers=self.headers, params=params)
                print(f'Файл {key} успешно добавлен')
                added_files_num += 1
            else:
                print(f'Копирование отменено:Файл {key} уже существует')
        print(f'\nЗапрос завершен, новых файлов добавлено: {added_files_num}')
