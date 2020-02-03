# Window switcher class definition
# PyGetWindow => import pygetwindow as gw
# https://pypi.org/project/PyGetWindow/

'''
REQUIREMENTS
============
=> settings.json should have the title of the background and foreground windows in the .json format.
'''

import pygetwindow as gw
import json
import os
from messenger import show_message
import subprocess
import pyautogui
import time
import datetime

class Switcher:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")
    SETTINGS_CONTENT = '''        
    {
        "background_path": "",
        "foreground_path": "",

        "background_window_title": "",
        "foreground_window_title": "",

        "reports_folder_path": ""
    }
    '''

    background_window_url = None
    foreground_window_url = None
    
    bg_window_title       = None
    fg_window_title       = None
    
    reports_folder_path   = None

    has_retrieved_settings = False
    has_reports_settings   = False
    
    def __init__(self):
        pass

    def create_settings_file(self):

        if os.path.exists(self.SETTINGS_FILE) and os.path.isfile(self.SETTINGS_FILE):
            if os.stat().st_size(self.SETTINGS_FILE) == 0:
                show_message("No settings in the settings.json file. Please Update", "WARNING")
                return
            else:
                show_message("Check for the proper settings in the settings.json file, otherwise ignore this message", "INFO")
        else:
            with open(self.SETTINGS_FILE, 'w+') as writer:
                writer.write(self.SETTINGS_CONTENT)
            
            show_message("settings file created, please populate the file with settings", "INFO")
        

    def retrieve_settings(self):
        
        if os.path.exists(self.SETTINGS_FILE) and os.path.isfile(self.SETTINGS_FILE):
            if os.stat(self.SETTINGS_FILE).st_size != 0:
                with open(self.SETTINGS_FILE, 'r') as reader:
                    settings = json.load(reader)
    
        else:
            self.create_settings_file()
        
        self.bg_window_title = settings['background_window_title']
        self.fg_window_title = settings['foreground_window_title']

        if not self.bg_window_title or not self.fg_window_title:
            show_message("Update the settings.json file with window title information", "INFO")
            return

        self.background_window_url = settings['background_path']
        self.foreground_window_url = settings['foreground_path']

        if not self.background_window_url or not self.foreground_window_url:
            show_message("Update the settings.json file with path to application executables", "INFO")
            return

        self.reports_folder_path   = settings['reports_folder_path']

        if not self.reports_folder_path or '' in str(self.reports_folder_path):
            self.has_reports_settings = False
            with open('logs.txt', 'a+') as writer:
                writer.writelines(str(datetime.date.today()) + "=> Recommended: Update the settings.json with correct reports folder path \n")

        self.has_retrieved_settings = True
        
    def check_settings(self):
        if self.has_retrieved_settings:
            show_message("Settings Checked - Good Status", "INFO")

    def check_reports(self):
        if self.has_reports_settings:
            show_message("Reports Folder settings found in settings.json file")
        else:
            show_message("No reports folder settings found in settings.json file")

    def starter(self):

        subprocess.Popen(f"{ str(self.background_window_url) }")
        
        time.sleep(1)
        
        tcp_ip_radio_btn_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'tcp_ip.png'))
        buttonx, buttony = pyautogui.center(tcp_ip_radio_btn_location)
        pyautogui.click(buttonx, buttony)
        
        ip_field_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'ip_input_field.png'))
        buttonx, buttony = pyautogui.center(ip_field_location)
        pyautogui.click(buttonx, buttony)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('192.168.1.191')

        port_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'port_field.png'))
        buttonx, buttony = pyautogui.center(port_location)
        pyautogui.click(buttonx, buttony)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('6001')

        connect_btn_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'connect_btn.png'))
        buttonx, buttony     = pyautogui.center(connect_btn_location)
        pyautogui.click(buttonx, buttony)
        
        time.sleep(1)

        pyautogui.press('enter')

        read_btn_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'read_btn.png'))
        buttonx, buttony  = pyautogui.center(read_btn_location)
        pyautogui.click(buttonx, buttony)
        
        BG_Window = gw.getWindowsWithTitle(str(self.bg_window_title))[0]
        BG_Window.minimize()

        subprocess.Popen(str(self.foreground_window_url))
        
        time.sleep(1)

        inventory_btn_location = pyautogui.locateOnScreen(os.path.join(self.BASE_DIR, 'inventory.png'))
        buttonx, buttony       = pyautogui.center(inventory_btn_location)
        pyautogui.click(buttonx, buttony)