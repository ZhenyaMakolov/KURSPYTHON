import requests
from pprint import pprint
import datetime
import json

count = input(str('Введите количество фото?:')).lower()
id_vk = input(str('Введете свой id_vk:')).lower()


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def photo_info(self, count):
        url = 'https://api.vk.com/method/photos.get'
        photo_params = {
            'owner_id': self.id,
            'extended': '1',
            'album_id': 'profile',
            'count': count}
        responses = requests.get(url, params={**self.params, **photo_params}).json()
        return responses['response']['items']
    
    def photo_sort(self):
        photos = self.photo_info(count)
        vk_sizes = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
        dict1 = {}
        for photo in photos:
            size = max(photo['sizes'], key=lambda s: vk_sizes[s['type']])
            url1 = size['url']
            likes = photo['likes']['count']
            timestamp = photo["date"]
            value = datetime.datetime.fromtimestamp(timestamp)
            if likes not in dict1:
                dict1[likes] = url1
            else:
                dict1[f'{likes}_{value.date()}'] = url1
        return dict1

    def json_files(self):
        photos = self.photo_info(count)
        vk_sizes = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
        list_json = []
        for photo in photos:
            size = max(photo['sizes'], key=lambda s: vk_sizes[s['type']])
            sizes = size['type']
            likes = photo['likes']['count']
            dict_json_file = {
                'file_name': likes,
                'size': sizes
            }
            list_json.append(dict_json_file)
        pprint(list_json)
        with open('photo.json', 'w') as file:
            json.dump(list_json, file, indent=1)


class Yandex:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return {
            'Countent-Type': 'applecation/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.headers()
        respons = requests.put(f'{folder_url}/?path={path}', headers=headers)
        return respons

    def download(self, destination, sourses):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.headers()
        for key, value in sourses.items():
            pprint(key)
            params = {'path': f"{destination} {key}", 'overwrite': 'true', 'url': value}
            response = requests.post(url=url, headers=headers, params=params)


if __name__ == '__main__':
    TOKEN = ''
    access_token = ''
    vk = VK(access_token, id_vk)
    vk.photo_info(count)
    pprint(vk.json_files())
    photo_sort = vk.photo_sort()
    ya = Yandex(TOKEN)
    folder = (ya.create_folder('photo'))
    pprint(ya.download(destination='photo/vk', sourses=photo_sort))
    owner_id = vk_client.users_get(user_ids)
    for id in owner_id:
        photo_info = vk_client.get_photos(album_id, rev, id['id'], count)