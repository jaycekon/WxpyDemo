from wxpy import *

# 普通登陆
bot = Bot(cache_path=True)


# 消息接收监听器
@bot.register()
def print_msg(msg):
    # 输出监听到的消息
    print(msg)


embed()
