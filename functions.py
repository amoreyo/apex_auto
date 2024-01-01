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
import math

# backimg =Image.open("./screem_shot/backpic.png")
# backstat =ImageStat.Stat(backimg)
# # 统计最大 最小值（RGB3个通道的）
# # print(backstat.extrema)
# # 统计均值, 每个通道的像素值总和
# # print(backstat.mean)
# print(sum(backstat.mean)) 165

# foreimg =Image.open("./screem_shot/forepic.png")
# forestat =ImageStat.Stat(foreimg)
# # 统计最大 最小值（RGB3个通道的）
# # print(forestat.extrema)
# # 统计均值, 每个通道的像素值总和
# # print(forestat.mean)
# print(sum(forestat.mean)) 279
def screem_shot_save(name):
    time.sleep(2)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    name = "./swap/" + name + ".png"
    
    cv2.imwrite(name, image)

def forepic_shot_save():
    time.sleep(2)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    name = "./screem_shot/forepic.png"
    
    cv2.imwrite(name, image)

def screem_shot():
    time.sleep(2)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    return  image

def gausskern(l=3, sig=1):
    """
    creates gaussian kernel with side length `l` and a sigma of `sig`
    """
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

# 主要还是通过定时截图，然后判断是否已经出局
def deadteam():
    settlementimg =Image.open("./screem_shot/settlementpic.png")
    settlementnp = np.asarray(settlementimg)
    # 823,114
    # 1090,185
    settlementnp = settlementnp[114:190,823:1090]
    # print(settlementnp.shape) # (76, 267, 3)
    # 先做高斯模糊，然后同游戏截图对比，计算差值，在一定区间就符合
    # 看网上的代码不如自己手撸高斯核
    gkern = gausskern()
    # print(gkern.shape) # 3,3
    # print(gkern)
    # print(np.sum(gkern))
    # 我就不做那么精细了，就不引入padding这种东西了
    settlementnp_g = np.zeros((76-2,267-2,3))
    for i in range(76-2):
        for j in range(267-2):
            # print(settlementnp[i,j])
            settlementnp_clip = settlementnp[i:i+3,j:j+3]
            for k in range(3):
                for l in range(3):
                    # print(settlementnp_clip[k,l])
                    # print(gkern[k,l])
                    settlementnp_clip[k,l] = gkern[k,l] * settlementnp_clip[k,l]
                    # print(settlementnp_clip[k,l])
                    # sys.exit()
            # print(settlementnp_clip.shape)
            settlementnp_clip = np.sum(settlementnp_clip, axis=(0,1))
            # print(settlementnp_clip)
            # print(i,j)
            settlementnp_g[i,j] = settlementnp_clip*4

    # im = Image.fromarray(settlementnp_g.astype(np.uint8))
    # im.save("clip.jpeg")
    tmp_shotimage = screem_shot()
    tmp_shotimage = tmp_shotimage[114:190,823:1090]
    # print(tmp_shotimage.shape)
    
    tmp_shotimage_g = np.zeros((76-2,267-2,3))
    for i in range(76-2):
        for j in range(267-2):
            tmp_shotimage_clip = tmp_shotimage[i:i+3,j:j+3]
            for k in range(3):
                for l in range(3):
                    tmp_shotimage_clip[k,l] = gkern[k,l] * tmp_shotimage_clip[k,l]
            tmp_shotimage_clip = np.sum(tmp_shotimage_clip, axis=(0,1))
            tmp_shotimage_g[i,j] = tmp_shotimage_clip*4
    
    # print(tmp_shotimage_g.shape)
    # print(settlementnp_g.shape)
    cz = np.sum(np.absolute(tmp_shotimage_g - settlementnp_g))
    # print(cz)
    if cz < 60000:
        return True
    else:
        return False

def interface():
    '''
    # foreimg =Image.open("./screem_shot/forepic.png")
    # # forenp = np.asarray(foreimg)
    # backstat =ImageStat.Stat(foreimg)
    foreimg_avg = 279
    tmp_shotimage = screem_shot()
    tmp_shotimage_avg = np.average(tmp_shotimage)*3
    cz = abs(tmp_shotimage_avg - foreimg_avg)
    # print(cz)
    if cz < 10:
        return True
    else:
        return False
    '''
    foreimg =Image.open("./screem_shot/forepic.png")
    forenp = np.asarray(foreimg)
    forenp = forenp[:, :, ::-1]
    tmp_shotimage = screem_shot()
    # print(forenp.shape)
    # print(tmp_shotimage.shape)
    # print(forenp[500,500])
    # print(tmp_shotimage[500,500])
    cznp = np.sum(np.absolute(forenp - tmp_shotimage)) / 10000000
    # print(cznp)
    if cznp < 35:
        return True
    else:
        return False


if __name__ == "__main__":
    interface()



