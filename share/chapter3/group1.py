from wxpy import *

bot = Bot(cache_path=True)

# 获取所有群聊-活跃和保存的群
groups = bot.groups()

# 输出群人数
print(len(groups))

# 遍历输出所有群
for group in groups:
    print(group)


bot.logout()