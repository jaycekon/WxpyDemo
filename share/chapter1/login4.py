from wxpy import *

# 使用缓存进行登录
bot = Bot(cache_path=True)

bot.file_helper.send('hello world! login 4')

print("ending!")
