from pynput.keyboard import Key, Controller as key_cl  #键盘控制器
from pynput.mouse import Button, Controller as mou_cl  #鼠标控制器
import time

# 键盘的控制函数
def keyboard_input(string):
    # 获取键盘权限
    keyboard = key_cl()
    # 设置数据类型
    keyboard.type(string)
    
# 鼠标的控制函数
def mouse_click():
    # 获取鼠标权限
    mouse = mou_cl()
    # 模拟左键按下
    mouse.press(Button.left)
    # 模拟左键弹起
    mouse.release(Button.left)

# 实现消息的发送函数
def send_message(number,string):
    print("程序在五秒钟之后开始执行")
    time.sleep(5)
    keyboard = key_cl()

    for i in range(number):
        keyboard_input(string)
        mouse_click()
        time.sleep(0.3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

if __name__ == '__main__':
    send_message(10,"祝您万圣节愉快！")
