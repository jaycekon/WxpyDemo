from wxpy import *

bot = Bot()
# 获取好友
dear = bot.friends().search('被单')[0]

print(dear)
# 发送消息
dear.send('发一条信息过来，文字的')


# 监听消息
@bot.register()
def print_others(msg):
    print(msg)
    # 转发消息
    msg.forward(bot.file_helper)


embed()
