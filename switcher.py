# Window switcher program, main class definition
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

class Switcher:

    SETTINGS_FILE = "settings.json"
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
        settings = ""

        if os.path.exists(self.SETTINGS_FILE) and os.path.isfile(self.SETTINGS_FILE):
            if not os.stat().st_size(self.SETTINGS_FILE) == 0:
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
        # work with subprocess
        import subprocess

        subprocess.call([str(self.background_window_url)])
        subprocess.call([str(self.foreground_window_url)])

    def is_window_available(self):
        '''
        check if the window title exists, if not, return False
        '''
        return False

    def move_window(self, x_cord, y_cord):
        pass

    def minimize_window(self, window):
        self.background_window_url.minimize()

    def click_at_coordinate(self):
        self.btn_coordinate = "coordinate"


if __name__ == '__main__':

    # Switcher.show_message("Something just like this", "INFO")
    # Switcher.show_message("Not found, I repeat, windows not found", "ERROR")
    pass