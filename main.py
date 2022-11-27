from utils import key_down, screenshot, get_active_window_title
import pydirectinput as pdi
import time
import pyautogui as pag
import os

if __name__ == "__main__":
    title = get_active_window_title()
    screenshot(save_path=f"{os.getcwd()}/test.png", win_title=title)
    key_down(["t", "e", "s", "t"])
    pass
