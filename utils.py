import pydirectinput
import time
import os
import pyautogui as pag
import win32gui
import keyboard
import pyperclip
from PIL import ImageGrab

def key_down(key, delay=0.03):
    """Convenience function to press a list of keys \n
       `key` is a list of keys with `delay` between each key press"""
    if isinstance(key, list):
        for k in key:
            pydirectinput.keyDown(k)
            time.sleep(delay)

    else:
        pydirectinput.keyDown(k)
        time.sleep(delay)


def screenshot(save_path=None, win_title=None):
    """Convenience function to take a screenshot of the window with the given title\n"""
    if win_title:
        x, y, w, h = find_window_movetop(win_title)
        img = ImageGrab.grab(bbox=(x, y, x+w, y+h))
        if save_path:
            img.save(save_path)
    else:
        pag.screenshot(save_path)

def find_window_movetop(win_title):
    """This function finds the window with the given class name and moves it to the top\n
       `return` the window's position and size `(x, y, w, h)`"""
    hwnd = win32gui.FindWindow(None, win_title)
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


