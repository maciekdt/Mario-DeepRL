from env_controllers.screen_shots_controller import ScreenShotsController
from env_controllers.key_board_controller import KeyBoardController
import threading
import random

ss_ct = ScreenShotsController()
kb_ct = KeyBoardController()
ss_ct.start_game()
while ss_ct.is_process_running:
    ss_ct.capture_frame(False)
    actions = [0,1,2,3]
    weights = [1, 0., 0., 0.]
    thread = threading.Thread(
        target=kb_ct.perform_action, args=(random.choices(actions, weights=weights, k=1)[0],)
    )
    thread.start()