from wxpy import *

bot = Bot(cache_path=True)

# 跟文件传输助手聊天
bot.file_helper.send("hello world!")

# 搜索好友
friend = bot.friends().search("黄伟杰", sex=MALE, city='广州')

print(friend)

# 确定获取唯一的好友
friend = bot.friends().search("黄伟杰")

weijie = ensure_one(friend)

print(weijie)
