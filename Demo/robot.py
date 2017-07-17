from wxpy import *

bot = Bot()

# 获取好友
dear = bot.friends().search('被单')[0]

tuling = Tuling(api_key='******')


# 使用图灵机器人自动与指定好友聊天
@bot.register(dear)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)


embed()
