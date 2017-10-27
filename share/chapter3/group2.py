from wxpy import *

bot = Bot(cache_path=True)

# 获取目标群
group = bot.groups().search("wxpy分享")

jiankong = ensure_one(group)

print(jiankong)

bot.logout()
