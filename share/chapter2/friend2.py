from wxpy import *

bot = Bot(cache_path=True)

# 获取统计消息
print(bot.friends().stats_text())

# 获取特定属性的统计消息
print(bot.friends().stats(attribs=('province', 'sex')))


bot.logout()