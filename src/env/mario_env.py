import gymnasium as gym 
from gymnasium import spaces
import numpy as np

from env_controllers.env_controller import EnvController


class MarioEnv(gym.Env):
    metadata = {'render.modes': ['console']}
    
    def __init__(self):
        super(MarioEnv, self).__init__()
        
        self.action_space = spaces.Discrete(6)
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(2, 79, 79), dtype=np.float64
        )
        self.fps = 80
        self.frame_rate = 4
        self.env_controller = None
        self.initial_observation = None
        
    def reset(self, seed=None, options=None):
        if self.env_controller != None:
            self.env_controller.stop()
        self.env_controller = EnvController(fps=self.fps, frame_rate=self.frame_rate)
        initial_observation = self.env_controller.start()
        return initial_observation, {}

    def step(self, action):
        observation, reward, terminated = self.env_controller.step(action)
        truncated = False
        info = {}
        return observation, reward, terminated, truncated, info

    def render(self, mode='console'):
        pass

    def close(self):
        self.env_controller.stop()