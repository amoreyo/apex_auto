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
from keyboard_simu import esc_simu,spacebar_simu,esc_back_simu

def choose_liveline():
    time.sleep(2)
    # 直接pyautogui.click 好像有时候无法触发,不懂
    pyautogui.moveTo(900, 50) # "主界面" "英雄选角页面"
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(850, 900) # "英雄选角页面" "奶妈"
    pyautogui.click()
    time.sleep(1)

# 如果未满50等级，则默认匹配
def choose_rank():
    time.sleep(2)
    pyautogui.moveTo(150, 850) # "主界面" "模式"
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(750, 650) # "模式" "rank"
    pyautogui.click()

def choose_dou():
    time.sleep(2)
    pyautogui.moveTo(150, 850) # "主界面" "模式"
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(350, 650) # "模式" "rank"
    pyautogui.click()

def choose_tri():
    time.sleep(2)
    pyautogui.moveTo(150, 850) # "主界面" "模式"
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(350, 450) # "模式" "rank"
    pyautogui.click()

def cancel_teammate():
    time.sleep(2)
    pyautogui.moveTo(150, 670) # "主界面" "模式"
    pyautogui.click()


def ready():
    time.sleep(2)
    pyautogui.moveTo(150, 950) # "准备就绪"
    pyautogui.click()

def quitgame():
    time.sleep(2)
    # esc_simu() # 为什么这个esc没有响应？
    # pyautogui.press('esc'): # 这个esc也没有响应？？？？
    # spacebar_simu() # 为什么空格也没有响应
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
    # 这里加入esc_simu的原因是，傻逼apex不知道什么时候会给你弹出来商店页面的广告
    # esc_simu()
    # esc_back_simu()



    




