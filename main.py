from vk import VkLoader
from yandex import Yandex
from config import get_token_id
from config import tokenYa, tokenVK

if __name__ == '__main__':

    my_VK = VkLoader(get_token_id(tokenVK))
    print(my_VK.json)

    my_yandex = Yandex('Вк фото скопированы', get_token_id(tokenYa))
    my_yandex.create_copy(my_VK.export_dict)
