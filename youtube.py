from pytube import YouTube

def download_video(video_url):
    try:
        yt = YouTube(video_url)

        print(f"Название: {yt.title}")
        print(f"Длительность: {yt.length} секунд")

        stream = yt.streams.get_highest_resolution()

        print("Начинаем скачивание...")
        print("Скачивание завершено!")
        input()

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    while True:
        video_url = input("Введите URL видео YouTube (или '0' для выхода): ")
        
        if video_url == '0':
            print("Выход из программы.")
            break
        
        download_video(video_url)
