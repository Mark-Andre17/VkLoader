import requests
from config import get_time, get_max_dpi


class VkLoader:

    def __init__(self, token_list, version='5.131'):
        self.token = token_list[0]
        self.id = token_list[1]
        self.version = version
        self.start_params = {'access_token': self.token, 'v': self.version}
        self.json, self.export_dict = self.sort_info()

    def get_photo_info(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id,
                  'album_id': 'profile',
                  'photo_sizes': 1,
                  'extended': 1}
        photo_info = requests.get(url, params={**self.start_params, **params}).json()['response']
        return photo_info['count'], photo_info['items']

    def get_logs_only(self):
        photo_count, photo_items = self.get_photo_info()
        result = {}
        for i in range(photo_count):
            likes_count = photo_items[i]['likes']['count']
            url_download, picture_size = get_max_dpi(photo_items[i]['sizes'])
            time_warp = get_time(photo_items[i]['date'])

            new_value = result.get(likes_count, [])
            new_value.append({'add_name': time_warp,
                              'url_picture': url_download,
                              'size': picture_size})
            result[likes_count] = new_value
        return result

    def sort_info(self):
        json_list = []
        sorted_dict = {}
        picture_dict = self.get_logs_only()
        for elem in picture_dict.keys():
            for value in picture_dict[elem]:
                if len(picture_dict[elem]) == 1:
                    file_name = f'{elem}.jpeg'
                else:
                    file_name = f'{elem} {value["add_name"]}.jpeg'
                json_list.append({'file name': file_name, 'size': value["size"]})
                sorted_dict[file_name] = picture_dict[elem][0]['url_picture']
        return json_list, sorted_dict
