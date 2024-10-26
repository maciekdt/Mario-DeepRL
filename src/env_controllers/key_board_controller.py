from enum import Enum
import pyautogui
import time

class GameAction(Enum):
    JUMP = "up"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    SPECIAL = "shift"

class KeyBoardController:
    
    def __init__(self):
        self.last_actions = []

        
    def perform_action(self, action_index):
        print("Performed click")
        if action_index == 0:
            self._stop_last_actions()
            pyautogui.keyDown('right')
            self.last_actions.append('right')

        elif action_index == 1:
            self._stop_last_actions()
            pyautogui.keyDown('up')
            self.last_actions.append('up')
        
        elif action_index == 2:
            self._stop_last_actions()
            pyautogui.keyDown('up')
            pyautogui.keyDown('right')
            self.last_actions.append('up')
            self.last_actions.append('right')
            
        elif action_index == 3:
            self._stop_last_actions()
            pyautogui.keyDown('left')
            self.last_actions.append('left')
    
    def _stop_last_actions(self):
        for action in self.last_actions:  
            pyautogui.keyUp(action)
        self.last_actions = []
            
        