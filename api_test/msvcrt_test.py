import msvcrt
import os

print("Please input your password:")
chars = []
while True:
    newChar = msvcrt.getch().decode(encoding="utf-8")
    # print("gap")
    # msvcrt.getch() 只是读取一个字符
    # print(type(newChar)) str
    if newChar in os.linesep:  # 如果是换行，则输入结束
        break
    elif newChar == '\b':
        # print("del")
        # '\b' 就是del <- 捏
        if chars: # 如果chars不为空呗
            del chars[-1]
            msvcrt.putch('\b'.encode(encoding='utf-8'))
            # msvcrt.putch('\b'.encode(encoding='utf-8'))
            # 下面的两行代码目的是为了将残留在屏幕上的 * 删除
            # 不然你的console就会仍然有原样的*，但是光标却在已经删除字符的下面
            msvcrt.putch(' '.encode(encoding='utf-8'))
            msvcrt.putch('\b'.encode(encoding='utf-8'))
            # 所以msvcrt.putch('\b') 只是将光标给putch

    else:
        chars.append(newChar)
        msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号


pwd = (''.join(chars))
print("\nyour password is:{0}".format(pwd))