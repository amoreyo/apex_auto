import os
import time
import win32gui
import win32api
import win32con
import win32process
import sys
import  msvcrt
import pyautogui
from read_apex_exe import forewindow
from keyboard_simu import esc_back_simu,esc_simu,retuen2interface,spacebar_simu,giveup_jumpleader,medkit,medbot
from mouse_simu import choose_liveline,choose_rank,ready,choose_tri,choose_dou,quitgame,cancel_teammate
from functions import screem_shot_save,screem_shot,deadteam,interface,forepic_shot_save
import keyboard

def load():
    time.sleep(2)
    spacebar_simu()
    # 怕apex商店广告不即使加载所以先睡10s
    time.sleep(10)
    esc_back_simu()
    choose_liveline()
    esc_back_simu()
    choose_rank()
    esc_back_simu()
    cancel_teammate() # 可能会因为活动而不在原来的位置
    

if __name__ == "__main__":
    forewindow()
    # load()
    # load完了之后更新forepic.png
    # medbot()
    # medkit()
    # sys.exit()
    forepic_shot_save()
    game_round = 0
    while True:
        count = 0
        while not retuen2interface():
            count = count + 1
            # 截图
            screem_shot_save(str(count)+"count")
            if count == 30:
                raise Exception("unknow error")
        ready()
        while True:
            if not interface():
                break
        print("entre game!")
        # 进入比赛
        while True:
            # time.sleep(60)
            medbot()
            medkit()
            if deadteam():
                screem_shot_save(str(game_round)+"game_round")
                game_round  = game_round + 1
                print("quit game!")
                keyboard.send(57)
                quitgame()
                break
            keyboard.send(57)
            quitgame() # 这里循环quit是因为担心第二名。就不存在deadteam的检测了
            if interface(): # 如果发现已经返回了主页面
                screem_shot_save(str(count)+"interface")
                print("alread return to the interface")
                break
        print("game over!")
        # 退出比赛
    # choose_liveline()
    # esc_back_simu()
    # choose_rank()
    # esc_back_simu()
    # cancel_teammate()
    # ready()

    # giveup_jumpleader()
    # medkit()
    # medbot()
    # while True:
    #     time.sleep(10)
    #     if deadteam():
    #         print("quit game!")
    #         quit()

    # quit()
    