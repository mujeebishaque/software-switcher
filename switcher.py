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
from messenger import Messenger
import win32gui
import subprocess
import pyautogui
import time


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
    
    def __init__(self):
        pass

    def create_settings_file(self):

        if os.path.exists(self.SETTINGS_FILE) and os.path.isfile(self.SETTINGS_FILE):
            if os.stat().st_size(self.SETTINGS_FILE) == 0:
                Messenger.show_message("No settings in the settings.json file. Please Update", "WARNING")
                return
            else:
                Messenger.show_message("Check for the proper settings in the settings.json file, otherwise ignore this message", "INFO")
        else:
            with open(self.SETTINGS_FILE, 'w+') as writer:
                writer.write(self.SETTINGS_CONTENT)
            
            Messenger.show_message("settings file created, please populate the file with settings", "INFO")
        

    def retrieve_settings(self):
        
        if os.path.exists(self.SETTINGS_FILE) and os.path.isfile(self.SETTINGS_FILE):
            # if not os.stat().st_size(self.SETTINGS_FILE) == 0:
            with open(self.SETTINGS_FILE, 'r') as reader:
                settings = json.load(reader)
    
        else:
            self.create_settings_file()
             
        self.bg_window_title = settings['background_window_title']
        self.fg_window_title = settings['foreground_window_title']

        if not self.bg_window_title or not self.fg_window_title:
            Messenger.show_message("Update the settings.json file with window title information", "INFO")
            return

        self.background_window_url = settings['background_path']
        self.foreground_window_url = settings['foreground_path']

        if not self.background_window_url or not self.foreground_window_url:
            Messenger.show_message("Update the settings.json file with path to application executables", "INFO")
            return

        self.reports_folder_path   = settings['reports_folder_path']

        if not self.reports_folder_path:
             Messenger.show_message("Recommended: Update the settings.json file with path to reports folder", "INFO")

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

        
        # Open background window i.e. SKI Demo App
        # Check radio field
        # Click on ip_field and sendkeys
        # Click on port_field and sendkeys
        # subprocess.Popen(f"{ str(self.foreground_window_url) }")


    def is_window_available(self):
        '''
        get list of all windows, match them against the titles in settings.json
        '''
        return False

    def move_window(self, x_cord, y_cord):
        '''
        1 - Move background window to a certain position
        2 - Call the click_at_coordinate button to click on start button
        3 - Check if the button texts changes, if yes, minimize window - OPTIONAL
        4 - shift control to the main window
        '''
        pass

    def make_window_active(self, window_title):
        # get_window = gw.getWindowsWithTitle(str(window_title))
        
        # hwnd = win32gui.FindWindow(None, str(window_title))
        # # print(hwnd)
        # win32gui.SetForegroundWindow(hwnd)  # put the window in foreground
        # win32gui.MoveWindow(hwnd, -7, 0, 500, 500, True)
        pass

    def minimize_window(self, window):
        self.background_window_url.minimize()

    def click_at_coordinate(self):
        self.btn_coordinate = "coordinate"
