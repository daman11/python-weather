from services.weather_service import get_weather
from services.excel_services import save_to_excel
from gui.interface import generate_interface
import time
import threading

def fetch_data():
    while True:
        weather = get_weather()
        save_to_excel(weather)
        time.sleep(30)

def start():
    threading.Thread(target=fetch_data).start()
    generate_interface()
start()