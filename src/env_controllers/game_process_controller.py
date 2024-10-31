import json
import subprocess
import threading
import time
import psutil


class GameProcessController:
    _run_cmd = [
        'C:/Program Files/AdoptOpenJDK/jdk-14.0.2.12-hotspot/bin/java.exe',
        '-XX:+ShowCodeDetailsInExceptionMessages',
        '-cp',
        'C:/Users/maciek/AppData/Roaming/Code/User/workspaceStorage/bd4015aa9a4debd6f8184343cc90c1fa/redhat.java/jdt_ws/Mario-AI-Framework_5b511999/bin',
        'PlayLevel'
    ]
    
    def __init__(self, fps):
        self.game_process = None
        self.fps = fps
        self.current_output_json = None
        self.output_read_thread = None
        self.psutil_process = None
        
        self._run_cmd.append(str(fps))
        
    def run_process(self):
        self.game_process = subprocess.Popen(
            self._run_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.psutil_process = psutil.Process(self.game_process.pid)
        self.output_read_thread = threading.Thread(
            target=self._read_output,
            daemon=True
        )
        self.output_read_thread.start()
        time.sleep(1)
    
    
    def stop_process(self):
        self.game_process.terminate()
        
    def pause_process(self):
        if self.psutil_process:
            self.psutil_process.suspend()
            
    def resume_process(self):
        if self.psutil_process:
            self.psutil_process.resume()
        
        
    def _read_output(self):
        while self.game_process.poll() is None:
            line = self.game_process.stdout.readline().strip()
            if line:
                try:
                    self.current_output_json = json.loads(line)
                    if self.current_output_json["terminate"] == True:
                        break
                except:
                    print(f"Failed to decode JSON from output: {line}")