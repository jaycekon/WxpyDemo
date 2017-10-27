from wxpy import *

# 将二维码输出到终端
bot = Bot(console_qr=2)

bot.file_helper.send('hello world! login 2')

print("ending!")
