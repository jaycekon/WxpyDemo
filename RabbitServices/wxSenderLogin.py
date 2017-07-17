from wechat_sender import *
from wxpy import *

bot = Bot(qr_path="qr.png")

group = bot.groups().search('监控报警')[0]

print("微信登陆成功！进行监控报警功能！")
print(group)

#
listen(bot, token='test', receivers=[group])
