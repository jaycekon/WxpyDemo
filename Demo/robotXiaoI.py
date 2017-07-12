from wxpy import *

bot = Bot()

# 获取好友
dear = bot.friends().search('被单')[0]

xiaoi = XiaoI('ZtGG41eUtg51', 'qSG7MItVqSXYvA8dEFvW')


@bot.register(dear)
def reply_my_friend(msg):
    print(msg)
    xiaoi.do_reply(msg)


embed()
