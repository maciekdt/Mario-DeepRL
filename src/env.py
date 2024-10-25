import pygetwindow as gw
import pyautogui
import time
import mss.tools
import numpy as np
from PIL import Image
import subprocess

command = [
    'C:/Program Files/AdoptOpenJDK/jdk-14.0.2.12-hotspot/bin/java.exe',
    '-XX:+ShowCodeDetailsInExceptionMessages',
    '-cp',
    'C:/Users/maciek/AppData/Roaming/Code/User/workspaceStorage/bd4015aa9a4debd6f8184343cc90c1fa/redhat.java/jdt_ws/Mario-AI-Framework_5b511999/bin',
    'PlayLevel'
]
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
time.sleep(1)
game_window = gw.getWindowsWithTitle('Mario AI Framework')[0]
game_window.activate()
left, top, width, height = game_window.left, game_window.top, game_window.width, game_window.height
print(left, top, width, height)
region = {
    "top": game_window.top + 40,
    "left": game_window.left + 15,
    "width": game_window.width - 30,
    "height": game_window.height - 50
}

sct = mss.mss()
i = 0


'''pyautogui.keyDown('right')
time.sleep(3)
pyautogui.keyUp('right')'''
pyautogui.keyDown('right')
while process.poll() is None:
    """pyautogui.keyDown('right')
    time.sleep(3)
    pyautogui.keyUp('right')"""
    
    """output = process.stdout.readline()
    if output:
        print(f"OUTPUT: {output.strip()}")"""
        
    
    screenshot = sct.grab(region)
    screenshot_np = np.array(screenshot)
    screenshot_image = Image.fromarray(screenshot_np)
    screenshot_image.save("./img/" + str(i) +".png")
    i+=1