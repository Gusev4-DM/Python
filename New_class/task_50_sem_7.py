'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os

my_file_path = 'D:\Python\Test'

forms_video = ['.mp4', '.avi', '.MP4', '.AVI']
forms_audio = ['.mp3', '.AAC', '.MP3', '.aac']
forms_pictures = ['.jpeg', '.JPG', '.jpg', '.JPEG', '.png', '.PNG']


def sort_files(file_path):
    os.chdir(file_path)

    if not os.path.isdir('My video'):
        os.mkdir('My video')
    if not os.path.isdir('My audio'):
        os.mkdir('My audio')
    if not os.path.isdir('My pictures'):
        os.mkdir('My pictures')

    list_files = []
    for name_0 in os.walk(my_file_path):
        for name_1 in name_0:
            for name_2 in name_1:
                list_files.append(name_2)

    for file in list_files:
        if any(part in file for part in forms_video):
            os.replace(file, f'My video/{file}')
        if any(part in file for part in forms_audio):
            os.replace(file, f'My audio/{file}')
        if any(part in file for part in forms_pictures):
            os.replace(file, f'My pictures/{file}')
    
    # for file in list_files:
    #     print(file)
    #     if file.split('.')[-1] in forms_video:
    #         os.replace(file, f'my_video/{file}')
    #     if file.split('.')[-1] in forms_audio:
    #         os.replace(file, f'my_audio/{file}')
    #     if file.split('.')[-1] in forms_pictures:
    #         os.replace(file, f'my_pictures/{file}')


sort_files(my_file_path)

