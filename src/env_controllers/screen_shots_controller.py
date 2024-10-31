import numpy as np
import mss.tools
from PIL import Image
import pygetwindow as gw

class ScreenShotsController:    

    def __init__(self, save_file=False):
        self.game_window = None
        self.game_window_location = None
        self.sc_controller = None
        self.frame_index = 0
        self.save_file = save_file
        
    
    def activate(self):
        self.game_window = gw.getWindowsWithTitle('Mario AI Framework')[0]
        self.game_window.activate()
        self.game_window_location = self._get_window_location(self.game_window)
        self.sc_controller = mss.mss()
        
        
    def capture_frame(self):
        np_screenshot = self._transform(
            np.array(
                self.sc_controller.grab(self.game_window_location)
            )
        )
        if self.save_file:
            screenshot_image = Image.fromarray(np_screenshot)
            screenshot_image = screenshot_image.convert('L')
            screenshot_image.save("./img/" + str(self.frame_index) +".png")
        self.frame_index += 1
        return np_screenshot
    
    
    def _transform(self, np_img):
        reduced_img = np_img[::8, ::8, :]
        mono_img = np.mean(reduced_img, axis=2).astype(np.uint8)
        
        left, right, top, bottom = 2, 2, 1, 1
        
        cropped_img = mono_img[top:-bottom, left:-right]
        normalized_img = cropped_img / 255.0
        return normalized_img


    def _get_window_location(self, game_window):
        return {
            "top": game_window.top,
            "left": game_window.left,
            "width": game_window.width,
            "height": game_window.height,
        }