from wxpy import *

bot = Bot(cache_path=True)

# 获取目标群
group = bot.groups().search("网银监控报警")

jiankong = ensure_one(group)

print(jiankong)
