import os
import time
import win32gui
import win32api
import win32con
import win32process
import sys
import  msvcrt
import pyautogui
import cv2
import numpy as np
from PIL import Image, ImageStat
from functions import screem_shot,interface
import keyboard

# 和functions 中的 dectstart函数本质相似，故改进
def retuen2interface():
    time.sleep(2)
    # 如果在设置页面则直接 esc
    if not interface():
        esc_simu()
    else:
        return True
    
    # 如果不是esc，则应该是在结算界面
    if not interface():
        time.sleep(2)
        pyautogui.moveTo(1800, 1050)
        pyautogui.click()
        pyautogui.moveTo(900, 730)
        pyautogui.click()
        time.sleep(7)
        pyautogui.moveTo(960, 1000)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
    else:
        return True
    
    if not interface():
        keyboard.send(57)
        time.sleep(0.5)
        keyboard.send(57)
        time.sleep(0.5)
        keyboard.send(57)
        time.sleep(0.5)
        keyboard.send(57)
        time.sleep(0.5)
    else:
        return True
    # 如果都不是则循环
    if not interface():
        return False
    time.sleep(1)


def spacebar_simu():
    time.sleep(2)
    win32api.keybd_event(32,0,0,0) # 32 -> spacebar
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)

def esc_simu():
    time.sleep(2)
    win32api.keybd_event(27,0,0,0) # 27 -> esc
    win32api.keybd_event(27,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(2)

def esc_back_simu():
    time.sleep(2)
    win32api.keybd_event(27,0,0,0)
    win32api.keybd_event(27,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)
    win32api.keybd_event(27,0,0,0)
    win32api.keybd_event(27,0,win32con.KEYEVENTF_KEYUP,0)
    # time.sleep(0.1)
    # win32api.keybd_event(27,0,0,0) # 32 -> spacebar
    # win32api.keybd_event(27,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)
    retuen2interface()

def giveup_jumpleader():
    time.sleep(1)
    win32api.keybd_event(20,0,0,0)
    time.sleep(4)
    win32api.keybd_event(20,0,win32con.KEYEVENTF_KEYUP,0)
        
    
def medkit():
    time.sleep(2)
    keyboard.send("7")
    # win32api.keybd_event(103,0,0,0) # 103 -> number 7
    # win32api.keybd_event(103,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(5) # 打小药时常

def medbot():
    time.sleep(2)
    keyboard.send("0")
    # win32api.keybd_event(96,0,0,0) # 96 -> number 0
    # win32api.keybd_event(96,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(40) # q的冷却

if __name__ == "__main__":
    retuen2interface()