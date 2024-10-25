from env.screen_shots_controller import ScreenShotsController

env_ct = ScreenShotsController()
env_ct.start_game()
while env_ct.is_process_running:
    env_ct.capture_frame(True)
    