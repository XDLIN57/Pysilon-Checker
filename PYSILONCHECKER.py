import os
import time
import requests
from bs4 import BeautifulSoup
from plyer import notification
import webbrowser
from playsound import playsound

URL = "https://tria.ge/s?q=family%3Apysilon"
latest_pysilon = None
SOUND_FOLDER = "sound"
SOUND_FILE = os.path.join(SOUND_FOLDER, "notification.mp3")

def setup_sound_folder():
    if not os.path.exists(SOUND_FOLDER):
        os.makedirs(SOUND_FOLDER)
    if not os.path.exists(SOUND_FILE):
        with open(SOUND_FILE, "wb") as f:
            f.write(b"\x00\x00")

def check_for_new_pysilon():
    global latest_pysilon
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        pysilon_entry = soup.find('a', class_='result-title')
        if not pysilon_entry:
            return
        pysilon_name = pysilon_entry.text.strip()
        pysilon_link = pysilon_entry['href']
        if pysilon_name != latest_pysilon:
            latest_pysilon = pysilon_name
            send_notification(pysilon_name, pysilon_link)
    except Exception as e:
        print(f"Error checking for new Pysilon: {e}")

def send_notification(pysilon_name, pysilon_link):
    try:
        notification.notify(
            title="A NEW PYSILON ARRIVED!",
            message=f"{pysilon_name}\nClick to download.",
            app_name="Pysilon Tracker",
            timeout=10
        )
        webbrowser.open(pysilon_link)
        playsound(SOUND_FILE)
    except Exception as e:
        print(f"Error sending notification or playing sound: {e}")

if __name__ == "__main__":
    setup_sound_folder()
    while True:
        check_for_new_pysilon()
        time.sleep(60)
