import time
import numpy as np
from env_controllers.game_process_controller import GameProcessController
from env_controllers.key_board_controller import KeyBoardController
from env_controllers.screen_shots_controller import ScreenShotsController


class EnvController:
    
    def __init__(self, fps, frame_rate=4, save_file=False):
        self.game_controller = GameProcessController(fps=fps)
        self.ss_controller = ScreenShotsController(save_file=save_file)
        self.kb_controller = KeyBoardController()
        self.target_duration = frame_rate/fps
        
        self.last_ss = None
        self.current_ss = None
        self.max_position = None
        self.first_frame = True
        
        
        
    def start(self):
        self.kb_controller.stop_all_actions()
        time.sleep(0.1)
        self.game_controller.run_process()
        self.ss_controller.activate()
        self.last_ss = self.ss_controller.capture_frame()
        self.current_ss = self.last_ss 
        self.max_position = self.game_controller.current_output_json["position"]
        
        return np.stack((self.last_ss, self.current_ss), axis=0)
        
    
    def step(self, action):
        if self.first_frame:
            time.sleep(1)
            self.first_frame = False 
        self.game_controller.resume_process()
        
        self.kb_controller.perform_action(action)
        time.sleep(self.target_duration - 0.02)
        
        self.game_controller.pause_process()
        
        self.last_ss = self.current_ss
        self.current_ss = self.ss_controller.capture_frame()
        
        position = self.game_controller.current_output_json["position"]
        reward = position - self.max_position
        if position > self.max_position:
            self.max_position = position
        done = self.game_controller.current_output_json["terminate"]
        if done or reward < 0:
            reward = 0
        return np.stack((self.last_ss, self.current_ss), axis=0), reward, done
    
    def stop(self):
        self.game_controller.stop_process()
        self.kb_controller.stop_all_actions()
        