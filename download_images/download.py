import os
import threading
import requests

urls = [
    "https://wallhaven.cc/w/v9ele8",
    "https://wallhaven.cc/w/kwwdv6",
    "https://wallhaven.cc/w/421g29",
    "https://wallhaven.cc/w/k9m63q"
    "https://wallhaven.cc/w/45kd89",
    "https://wallhaven.cc/w/j8yrpq",
    "https://wallhaven.cc/w/zy5y1o",
    "https://wallhaven.cc/w/x6pl9v",
    "https://wallhaven.cc/w/we628p",
    "https://wallhaven.cc/w/ex9gwo",
    "https://wallhaven.cc/w/1pd1o9",
    "https://wallhaven.cc/w/m3zjx1",
    "https://wallhaven.cc/w/1ppld1",
    "https://wallhaven.cc/w/yxqzpd",
    "https://wallhaven.cc/w/kx82d6",
    "https://wallhaven.cc/w/l83o92",
    "https://wallhaven.cc/w/7p39gy",
    "https://wallhaven.cc/w/7p39gy",
    "https://wallhaven.cc/w/qzdqvr"
    "https://wallhaven.cc/w/zyxvqy",
    "https://wallhaven.cc/w/kx98xd",
    "https://wallhaven.cc/w/zygeko",
    "https://wallhaven.cc/w/kx36mq",
    "https://wallhaven.cc/w/m9xyg8",
    "https://wallhaven.cc/w/o59gvl",
    "https://wallhaven.cc/w/28p95m",
    "https://wallhaven.cc/w/9mjoy1",
    "https://wallhaven.cc/w/e7jj6r",
    "https://wallhaven.cc/w/j3m8y5",
]


def donwload_image(url: str):
    response = requests.get(url)
    filename = url.split('/')[-1] + '.png'

    download_dir = create_dir()

    with open(f"{download_dir}/{filename}", 'wb') as file:
        file.write(response.content)


def create_threads(url_list: list):
    threads = []

    for url in url_list:
        thread = threading.Thread(target=donwload_image, args=(url,))
        thread.start()

        threads.append(thread)

    close_threads(threads)


def close_threads(threads_list: list):
    for thread in threads_list:
        thread.join()

    print('all images were donwloaded')


def create_dir():
    home_dir = os.path.expanduser('~/Tomi/')
    download_dir = os.path.join(home_dir, 'download_images', 'downloaded_by_parallel')

    try:
        os.makedirs(download_dir, exist_ok=True)
        print('Se creó el directorio exitosamente.')
        return download_dir

    except FileExistsError:
        print('El directorio ya existe, no se requiere creación adicional.')

    except Exception as e:
        print(f'Ocurrió un error al crear el directorio: {e}')


if __name__ == "__main__":
    create_threads(urls)
