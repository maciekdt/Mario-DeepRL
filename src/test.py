from env_controllers.screen_shots_controller import ScreenShotsController
from env_controllers.key_board_controller import KeyBoardController
import threading
import random
import time

fps = 80
ss_ct = ScreenShotsController(fps=fps)
kb_ct = KeyBoardController()
ss_ct.start_game()
target_duration = 4/fps

while ss_ct.is_process_running:
    start_time = time.perf_counter()
    
    ss_ct.capture_frame(False)
    
    actions = [0,1,2,3,4,5]
    weights = [.3, 4, .05, .1, .1, .05]
    thread = threading.Thread(
        target=kb_ct.perform_action, args=(random.choices(actions, weights=weights, k=1)[0],)
    )
    thread.start()
    
    # Ensure each loop iteration takes the same time
    elapsed_time = time.perf_counter() - start_time
    remaining_time = target_duration - elapsed_time
    print("remaining_time: ", str(remaining_time))
    if remaining_time > 0:
        time.sleep(remaining_time)
    
target=kb_ct.stop_all_actions()