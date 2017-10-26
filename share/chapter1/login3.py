from wxpy import *

# 将二维码保存到目的地址
bot = Bot(qr_path="D:/QR.png")

bot.file_helper.send('hello world! login 3')

print("ending!")
