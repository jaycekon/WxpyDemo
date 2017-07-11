from wxpy import *

bot = Bot()

# 添加自己为好友
bot.self.add()

# 接收好友邀请
bot.self.accept()

bot.self.send('你真帅！')

print('ending!')