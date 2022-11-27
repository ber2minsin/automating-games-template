import pydirectinput
import time
import os
import pyautogui as pag
import win32gui
import keyboard
import pyperclip

def key_down(key):
    """Convenience function to press a list of keys \n
       `key` is a list of keys"""
    if isinstance(key, list):
        for k in key:
            pydirectinput.keyDown(k)
            time.sleep(5)
            pydirectinput.keyUp(k)
    else:
        pydirectinput.keyDown(k)
        time.sleep(0.03)
        pydirectinput.keyUp(k)

def screenshot(save_path=os.getcwd(), win_title=None):
    """Convenience function to take a screenshot of the window with the given title\n"""
    if win_title:
        x, y, w, h = find_window_movetop(win_title)
        pag.screenshot(save_path, region=(x, y, w, h))
    else:
        pag.screenshot(save_path)

def find_window_movetop(cls):
    """This function finds the window with the given class name and moves it to the top\n
       `return` the window's position and size `(x, y, w, h)`"""
    hwnd = win32gui.FindWindow(None, cls)
    win32gui.ShowWindow(hwnd,5)
    win32gui.SetForegroundWindow(hwnd)
    window_rect = win32gui.GetWindowRect(hwnd)
    client_rect = win32gui.GetClientRect(hwnd)
    region = x, y, w, h = window_rect[0], window_rect[1], client_rect[2], client_rect[3]

    print(region)
    return region


def get_active_window_title():
    """ This is an infinite loop that helps you get the title \n
        of the active window when `F12` key is pressed"""
    while True:
        if keyboard.is_pressed('f12'):
            title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            print(title)
            pyperclip.copy(title)
            return title


