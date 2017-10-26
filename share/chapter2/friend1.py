from wxpy import *

bot = Bot(cache_path=True)

# 获取所有好友
friends = bot.friends()

# 遍历输出好友名称
for friend in friends:
    print(friend)


