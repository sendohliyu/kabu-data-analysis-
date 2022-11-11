from pynput.mouse import Button, Controller as mou_cl  # 鼠标控制器
from pynput.keyboard import Key, Controller as key_cl  # 键盘控制器
from pynput.keyboard import Key, Controller
import pandas as pd
import sys
import os
import time

# 键盘的控制函数


def keyboard_input(string):
    # 获取键盘权限
    keyboard = key_cl()
    # 设置数据类型
    keyboard.type(string)


def mouse_click():
    # 获取鼠标权限
    mouse = mou_cl()
    # 模拟左键按下
    mouse.press(Button.left)
    # 模拟左键弹起
    mouse.release(Button.left)


# 实现消息的发送函数
def send_message(number, string):
    keyboard = key_cl()

    for i in range(number):
        keyboard_input(string)
        # mouse_click()
        time.sleep(0.4)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.4)


def check_message(file_name: str):
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = file_path + '/' + file_name
    print(file_path)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        print("No 'message.csv' can be found, please create such csv (with header) that includes two column: person, message")
        sys.exit()


def find_person(keyboard):
    keyboard.press(Key.cmd.value)
    keyboard.press('f')
    keyboard.release('f')
    keyboard.release(Key.cmd.value)


def send_message_one_row(row, keyboard):
    find_person(keyboard)

    send_message(1, row['person'])
    time.sleep(1)
    send_message(1, row['message'])
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


def send_messages(df):
    keyboard = Controller()
    for index, row in df.iterrows():
        send_message_one_row(row, keyboard)


if __name__ == '__main__':

    message_file_name = "message.csv"
    print("Checking if message.csv exists")

    df = check_message(message_file_name)
    print("message.csv exists")

    assert len(df.columns) == 2
    assert df.columns[0] == 'person'
    assert df.columns[1] == 'message'
    print("程序在3秒钟之后开始执行")
    time.sleep(3)
    send_messages(df)
