import numpy as np
import mss.tools
from PIL import Image
import pygetwindow as gw
import subprocess
import time
import threading
import json
from transformers.img_primar_transformer import ImgPrimarTransformer

class ScreenShotsController:    
    _RUN_CMD = [
        'C:/Program Files/AdoptOpenJDK/jdk-14.0.2.12-hotspot/bin/java.exe',
        '-XX:+ShowCodeDetailsInExceptionMessages',
        '-cp',
        'C:/Users/maciek/AppData/Roaming/Code/User/workspaceStorage/bd4015aa9a4debd6f8184343cc90c1fa/redhat.java/jdt_ws/Mario-AI-Framework_5b511999/bin',
        'PlayLevel'
    ]
    
    def __init__(self):
        self.game_window = None
        self.game_window_location = None
        self.game_process = None
        self.sc_controller = None
        self.game_output = None
        self.is_process_running = False
        self.frame_index = 0
        self.img_trans = ImgPrimarTransformer()
        self.last_ss = None
        self.current_ss = None
        
    
    def start_game(self):
        self.game_process = subprocess.Popen(
            self._RUN_CMD,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        threading.Thread(target=self._read_output, daemon=True).start()
        self.is_process_running = True
        
        time.sleep(1)
        
        self.game_window = gw.getWindowsWithTitle('Mario AI Framework')[0]
        self.game_window.activate()
        self.game_window_location = self._get_window_location(self.game_window)
        self.sc_controller = mss.mss()
        print("Game started")
        
        
    def capture_frame(self, save_file=False):
        np_screenshot = self.img_trans.transform(
            np.array(
                self.sc_controller.grab(self.game_window_location)
            )
        )
        print("captured frame " + str(self.frame_index))
        if save_file:
            screenshot_image = Image.fromarray(np_screenshot)
            screenshot_image = screenshot_image.convert('L')
            screenshot_image.save("./img/" + str(self.frame_index) +".png")
        self.frame_index += 1
        
        game_output = self.game_output
        if(game_output):
            json_end_result = self._end_game(game_output)
            return json_end_result
        else:
            return np_screenshot
    
    def _end_game(self, game_output):
        self.game_process.terminate()
        self.is_process_running = False
        self.game_process.wait()
        print("Game ended")
        print("Frames number " + str(self.frame_index))
        return json.loads(game_output)
        
    def _read_output(self):
        while self.game_process.poll() is None:
            line = self.game_process.stdout.readline().strip()
            if line and self.game_output == None:
                self.game_output = line

    def _get_window_location(self, game_window):
        return {
            "top": game_window.top + 40,
            "left": game_window.left + 15,
            "width": game_window.width + 100,
            "height": game_window.height + 60
        }