from wxpy import *

bot = Bot()

friend = bot.friends().search('被单')[0]

friend.send('发那个游戏的链接给我一下！ 测试ing')


@bot.register()
def print_others(msg):
    print(msg)
    print(msg.member)
    if msg.member == friend:
        msg.forward(bot.file_helper)
        # 转发消息


embed()
