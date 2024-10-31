from stable_baselines3 import DQN
from env.mario_env import MarioEnv
from model.custom_CNN_feature_extractor import CustomCNNFeatureExtractor


custom_policy_kwargs = dict(
    features_extractor_class=CustomCNNFeatureExtractor,
    features_extractor_kwargs=dict(features_dim=256),
    net_arch = []
)

dqn_model = DQN(
    policy = "MlpPolicy",
    env = MarioEnv(),
    policy_kwargs = custom_policy_kwargs,
    verbose = 1,
    
    learning_rate=.001,
    gamma=.9,
    
    buffer_size = 1024,
    train_freq=(1, "episode"),
    batch_size=256,
    
    exploration_final_eps=.05,
    exploration_fraction=.5 
)

