from enum import Enum
import pyautogui
pyautogui.PAUSE = 0
import time


class GameAction(Enum):
    JUMP = "up"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    SPECIAL = "shift"

class KeyBoardController:
    
    def __init__(self):
        self.last_actions = []
        
    
    _ACTIONS = [
        ['right'],
        ['right', 'up'],
        ['up'],
        ['left'],
        ['left', 'up'],
        []
    ]
        
        
    def perform_action(self, current_action_index):
        for last_action in self.last_actions:
            if last_action not in self._ACTIONS[current_action_index]:
                self.last_actions.remove(last_action)
                pyautogui.keyUp(last_action)
            elif last_action ==  'up':
                pyautogui.keyUp('up')
                time.sleep(.005)
                pyautogui.keyDown('up')
                
                
        for current_action in self._ACTIONS[current_action_index]:
            if current_action not in self.last_actions:
                self.last_actions.append(current_action)
                pyautogui.keyDown(current_action)
        
        print("Performed click ", str(self._ACTIONS[current_action_index]))
    
    def stop_all_actions(self):
        for last_action in self.last_actions:
            pyautogui.keyUp(last_action)
            self.last_actions.remove(last_action)
        