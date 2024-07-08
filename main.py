import os
import psutil
import winreg as reg
import time
import json
import requests
from threading import Thread
from pathlib import Path
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def create_fake_process(name):
    while True:
        time.sleep(10)

def create_fake_registry_entries():
    for key_path, values in config['fake_registry_entries'].items():
        try:
            reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)
            registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
            for name, value in values.items():
                reg.SetValueEx(registry_key, name, 0, reg.REG_SZ, value)
            reg.CloseKey(registry_key)
            print(f"Fake registry entries created at {key_path}.")
        except Exception as e:
            print(f"Failed to create registry entries at {key_path}: {e}")

def create_fake_files():
    for file_path in config['fake_files']:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as file:
            file.write("This is a fake log file for Scary Chicken.")
        print(f"Fake file created at {file_path}.")


def simulate_network_traffic():
    while True:
        for url in config['network_endpoints']:
            try:
                response = requests.get(url)
                print(f"Fake network request to {url} returned status {response.status_code}.")
            except requests.RequestException as e:
                print(f"Failed to simulate network request to {url}: {e}")
        time.sleep(30)

def monitor_fake_processes(process_names):
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in process_names:
                break
        else:
            for name in process_names:
                Thread(target=create_fake_process, args=(name,)).start()
        time.sleep(5)

def create_image():
    width = 16
    height = 16
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=(255, 0, 0)
    )
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=(0, 255, 0)
    )
    return image

def on_quit(icon, item):
    icon.stop()

icon = pystray.Icon("Scary Chicken")
icon.menu = pystray.Menu(item('Quit', on_quit))
icon.icon = create_image()

def main():
    fake_process_names = config['fake_processes']

    for name in fake_process_names:
        Thread(target=create_fake_process, args=(name,)).start()

    create_fake_registry_entries()

    create_fake_files()

    Thread(target=simulate_network_traffic).start()

    Thread(target=monitor_fake_processes, args=(fake_process_names,)).start()

    icon.run()

if __name__ == "__main__":
    main()
