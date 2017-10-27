from wxpy import *

# 普通登陆
bot = Bot()

# 登陆完成后，向文件助手发送一条消息
bot.file_helper.send('hello world! login1')

print("ending!")

bot.logout()
