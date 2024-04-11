'''Задание
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный подход для скачивания изображений.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
'''
'''------------------------------------Многопоточный подход----------------------------------------------------------'''
import requests
import threading
import time, os, sys

def download(url, start_time):
    response = requests.get(url) # Отправляем запрос на сервер
    if response.status_code != 200: # Проверяем, был ли запрос успешным
        print(f"Не удалось загрузить {url}. HTTP статус-код: {response.status_code}")
        return

    filename = url.split("/")[-1] # Получаем имя файла
    DIRECTORY = "img2"

    if not os.path.exists(DIRECTORY): # Проверяем наличие директории, если ее нет, создаем
        os.makedirs(DIRECTORY)

    with open(os.path.join(DIRECTORY, filename), 'wb') as file:
        file.write(response.content) # Записываем содержимое файла
    print(f"HTTP статус-код: {response.status_code} - Загружено >>> {url} за {time.time() - start_time:.2f} секунд")

if __name__ == '__main__':
    print('Start >>> Многопоточный подход')
    urls = sys.argv[1:] # Получаем URL-адреса
    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=(url, start_time))
        threads.append(thread)
        thread.start()

    for threads in threads:
        threads.join()
    print(f'Завершено за {time.time() - start_time:.2f} секунд')

# Пример запуска программы:

'''
py hw2.py https://cdn.pixabay.com/photo/2019/06/23/15/29/great-gallery-4293985_1280.jpg https://cdn.pixabay.com/photo/2022/07/24/04/58/milan-7340984_1280.jpg https://cdn.pixabay.com/photo/2021/08/20/18/33/british-museum-6561029_640.jpg https://cdn.pixabay.com/photo/2016/09/06/18/22/visitors-1649815_640.jpg https://cdn.pixabay.com/photo/2021/03/22/13/48/copyright-6114655_640.jpg
'''
'''
Start >>> Многопоточный подход
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2021/08/20/18/33/british-museum-6561029_640.jpg за 0.83 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2021/03/22/13/48/copyright-6114655_640.jpg за 0.83 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2016/09/06/18/22/visitors-1649815_640.jpg за 0.85 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2022/07/24/04/58/milan-7340984_1280.jpg за 0.93 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2019/06/23/15/29/great-gallery-4293985_1280.jpg за 0.94 секунд
Завершено за 0.95 секунд
'''
