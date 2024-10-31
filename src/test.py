from model.custom_DQN import dqn_model
from stable_baselines3.common.callbacks import BaseCallback

dqn_model.learn(total_timesteps=50_000, log_interval=5, progress_bar=True)
dqn_model.save("dqn_mario")