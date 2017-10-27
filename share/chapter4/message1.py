from wxpy import *

# 普通登陆
bot = Bot(cache_path=True)

friend = ensure_one(bot.friends().search("黄伟杰"))

# 发送文本文件
friend.send_msg("hello world")

# 发送图片
friend.send_image("D:/QR.png")


print("ending!")

bot.logout()
