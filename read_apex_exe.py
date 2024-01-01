import os
import time
import win32gui
import win32api
import win32con
import win32process
import sys
import  msvcrt

def get_mesh_windows(hWndList, name):
	winhwnd= []
	for hWnd in hWndList:
		title = win32gui.GetWindowText(hWnd)
		clsname = win32gui.GetClassName(hWnd)
 
		#print 'title:%s' % (title)
		#print 'name:%s' % (clsname)

		if title.startswith(name):
			winhwnd.append(hWnd)
	return winhwnd

# 因为是特定apex服务，就直接懒散一点代码和数据一体化了
def forewindow():
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    apex = "Apex Legends"
    apex_exit = False
    wh = hWndList[0]
    for hWnd in hWndList:
        title = win32gui.GetWindowText(hWnd)
        if title == apex:
            apex_exit = True if not apex_exit else False
            print(title)
            wh = hWnd
    if not apex_exit:
        raise Exception("Apex Legends not found OR too much Apex Legends!")
        # sys.exit()
    print("apex's handle : ", wh) # print handle

    # win32gui.ShowWindow(wh,win32con.SW_SHOWMAXIMIZED)
    win32gui.SetForegroundWindow(wh)
    # 上述两行代码的效果是相同的,但是建议使用第二个，第一个使用好像存在bug


if __name__ == "__main__":
    print(sys.argv[0])
    print(str(sys.argv))
    # base_dir = sys.argv[1]
    # file = sys.argv[2]
    # print(base_dir)
    # print(file)
    # sys.exit()
    #启动两个程序，titles: mesh-view1, mesh-view2, start:不阻塞当前进程
    # os.system('start python dynamic_viewer.py ' + base_dir + ' ' + file)
    # os.system('start python dynamic_viewer1.py ' + base_dir + ' ' + file + '_Refine')

    #sleep 1s, 当前进程才能找到这两个窗口
    # time.sleep(1)

    # print 'search window with title mesh-view...'

    #搜索所有窗口
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # print(hWndList)
    apex = "Apex Legends"
    wh = hWndList[0]
    for hWnd in hWndList:
        title = win32gui.GetWindowText(hWnd)
        if title == apex:
            print(title)
            wh = hWnd
        # print(title)
        # print(type(title))
        # Apex Legends
    # sys.exit()
    # name = 'mesh-view'
    # winhwnds = get_mesh_windows(hWndList,name)
    # print 'there are %d windows named mesh-view '%len(winhwnds)
    print(wh) # print handle
    # win32gui.ShowWindow(wh,win32con.SW_SHOWMAXIMIZED)
    win32gui.SetForegroundWindow(wh)
    # 上述两行代码的效果是相同的,但是建议使用第二个，第一个使用好像存在bug
    time.sleep(1)
    win32api.keybd_event(32,0,0,0) # 32 -> spacebar
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)

    '''
    # win32gui.SetFocus(wh) # pywintypes.error: (5, 'SetFocus', '拒绝访问。')
 
    remote_thread, _ = win32process.GetWindowThreadProcessId(wh)
    current_thread = win32api.GetCurrentThreadId()
    # print(remote_thread)
    # print(current_thread)
    win32process.AttachThreadInput(current_thread, remote_thread, True)
    prev_handle = win32gui.SetFocus(wh)
    # win32gui.SetFocus(wh)
    '''

    '''
    ch = 'a'
    asc = ord(ch)
    win32api.PostMessage(wh, win32con.WM_CHAR, asc, 0)
    
    while True:
        # msvcrt 只是读取控制台输入
        ch = msvcrt.getch().decode(encoding="utf-8")
        if ch == 'q' :
            break
        asc = ord(ch)

        # for wh in winhwnds:
        win32api.PostMessage(wh, win32con.WM_CHAR, asc, 0) 
    '''
    # print "work done!"
    # pass