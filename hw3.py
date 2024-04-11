'''Задание
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать асинхронный подход для скачивания изображений.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
'''
'''--------------------------------------Асинхронный подход----------------------------------------------------------'''
import asyncio
import aiohttp
import time, os, sys


async def download(url, start_time):
    async with aiohttp.ClientSession() as session:  # Создаем сессию
        async with session.get(url) as response:  # Отправляем запрос на сервер
            if response.status != 200:  # Проверяем, был ли запрос успешным
                print(f"Не удалось загрузить {url}. HTTP статус-код: {response.status_code}")
                return

            filename = url.split("/")[-1]  # Получаем имя файла
            directory = "img3"

            if not os.path.exists(directory):  # Проверяем наличие директории, если ее нет, создаем
                os.makedirs(directory)

            with open(os.path.join(directory, filename), "wb") as file:
                file.write(await response.read())  # Записываем содержимое файла
            print(f"HTTP статус-код: {response.status} - Загружено >>> {url} за {time.time() - start_time:.2f} секунд")


async def main():
    print('Start >>> Асинхронный подход')
    start_time = time.time()
    tasks = []
    urls = sys.argv[1:]  # Получаем URL-адреса из аргументов командной строки
    for url in urls:
        task = asyncio.ensure_future(download(url, start_time))
        tasks.append(task)
    await asyncio.gather(*tasks)
    return start_time


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start_time = loop.run_until_complete(main()) # Запускаем цикл событий
    print(f'Завершено за {time.time() - start_time:.2f} секунд')

'''
py hw3.py https://cdn.pixabay.com/photo/2019/06/23/15/29/great-gallery-4293985_1280.jpg https://cdn.pixabay.com/photo/2022/07/24/04/58/milan-7340984_1280.jpg https://cdn.pixabay.com/photo/2021/08/20/18/33/british-museum-6561029_640.jpg https://cdn.pixabay.com/photo/2016/09/06/18/22/visitors-1649815_640.jpg https://cdn.pixabay.com/photo/2021/03/22/13/48/copyright-6114655_640.jpg
'''
'''
Start >>> Асинхронный подход
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2016/09/06/18/22/visitors-1649815_640.jpg за 0.22 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2021/08/20/18/33/british-museum-6561029_640.jpg за 0.23 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2021/03/22/13/48/copyright-6114655_640.jpg за 0.27 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2019/06/23/15/29/great-gallery-4293985_1280.jpg за 0.32 секунд
HTTP статус-код: 200 - Загружено >>> https://cdn.pixabay.com/photo/2022/07/24/04/58/milan-7340984_1280.jpg за 0.38 секунд
Завершено за 0.38 секунд
'''
