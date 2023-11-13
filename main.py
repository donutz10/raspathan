import requests
from lxml import html
from datetime import datetime
import time
import pygame

def get_prayer_times(url):
    # Fetch the webpage
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # XPath for each prayer time
    xpaths = {
        'Fajr': '//*[@id="top-city-table"]/table/tbody/tr[2]/td[2]',
        'Dhuhr': '//*[@id="top-city-table"]/table/tbody/tr[2]/td[4]',
        'Asr': '//*[@id="top-city-table"]/table/tbody/tr[2]/td[5]',
        'Maghrib': '//*[@id="top-city-table"]/table/tbody/tr[2]/td[6]',
        'Isha': '//*[@id="top-city-table"]/table/tbody/tr[2]/td[7]'
    }

    prayer_times = {}
    for name, xpath in xpaths.items():
        element = tree.xpath(xpath)
        if element:
            prayer_time = datetime.strptime(element[0].text.strip(), '%I:%M %p').strftime('%H:%M')
            prayer_times[name] = prayer_time

    return prayer_times

def play_sound(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():
    prayer_url = "https://www.islamicfinder.org/world/qatar/"
    prayer_times = get_prayer_times(prayer_url)
    print(prayer_times)
    while True:
        current_time = datetime.now().strftime('%H:%M')

        if current_time == '23:59':
            print('Refreshing prayer times. Wait 60 seconds')
            time.sleep(60)  # Wait for 5 minutes
            prayer_times = get_prayer_times(prayer_url)  # Refresh prayer times
            print(prayer_times)
            continue

        for name, prayer_time in prayer_times.items():
            if current_time == prayer_time:
                print(f"It's time for {name} prayer.")
                sound_file = "2.wav" if name == 'Fajr' else "1.wav"
                play_sound(sound_file)

        time.sleep(60)

if __name__ == "__main__":
    main()
