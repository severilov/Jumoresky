# -*- coding: utf-8 -*- 

import vk_api
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

login = ''
password = ''
vk_id = '' #ID приложения
VERSION = '5.73'
GLOBAL_COUNT = 0

def get_wall_posts(group_id, i):
    session = vk_session.get_api()
    posts = []
    # максимум за один запрос можно получить 100 постов
    # у owner_id -- id группы всегда в начале должен быть "-"
    # offset -- начиная с какого поста по счету парсить
    posts = session.wall.get(owner_id = '-' + group_id, offset = 100*i, count = 100, version = VERSION)
    return posts

def get_text_from_posts(posts):
    texts = []
    for i in range(len(posts['items'])):
        texts.append(posts['items'][i]['text'])
    return texts

def write_to_txt(texts):
    with open('post.txt', 'a') as file:
        for text in texts:
            file.write(text+'\n\n')
            global GLOBAL_COUNT
            GLOBAL_COUNT += 1

def main():
    group_id_list = ['92876084','45491419']  # Groups IDs
    for id in group_id_list:
        for i in range (100):
            texts = get_text_from_posts(get_wall_posts(id, i))
            write_to_txt(texts)

if __name__ == '__main__':
    # авторизируемся
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    main()
    print('Количество распарсенных анеков: %d' %GLOBAL_COUNT) # 20000 постов