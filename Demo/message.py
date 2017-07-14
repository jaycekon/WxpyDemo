from wxpy import *

bot = Bot()
# 获取好友
dear = bot.friends().search('被单')[0]

messages = bot.messages.search(keywords='测试', sender=bot.self)

for message in messages:
    print(message)


@bot.register()
def print_others(msg):
    print(msg)


embed()
