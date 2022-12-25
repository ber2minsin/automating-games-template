from utils import key_down, screenshot, get_active_window_title, get_window_size
import pydirectinput as pdi
import time
import pyautogui as pag
import os
import keyboard
import cv2
import numpy as np


if __name__ == "__main__":
    # test_title = get_active_window_title()
    test_title = "illet"
    key_down([x for x in "test"], delay=1)

    cv2.namedWindow("Capture", cv2.WINDOW_NORMAL)


    # Doing this in every loop probably would slow the capture, so we dont support resizes

    size = get_window_size(test_title)
    cv2.resizeWindow("Capture", size[2], size[3])
    while not keyboard.is_pressed("f8"):

        img = screenshot(save_path=f"{os.getcwd()}/test.png", win_title=test_title)
        npimg = np.array(img)
        npimg = cv2.cvtColor(npimg, cv2.COLOR_BGR2RGB)

        cv2.imshow("Capture", npimg)

        key = cv2.waitKey(1)


# cv2.destroyWindow("Capture")


