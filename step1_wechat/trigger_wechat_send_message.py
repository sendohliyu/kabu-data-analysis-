print("Hello World")
print("Hello Richard")
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('李煜', sex=MALE)[0]
print(my_friend)
