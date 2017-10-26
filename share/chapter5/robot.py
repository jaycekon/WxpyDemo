from wxpy import *

bot = Bot()

# 获取好友
friend = bot.friends().search('陈大美女')[0]

tuling = Tuling(api_key='80144c654b9846ed8b76c6f11cadfb3f')


# 使用图灵机器人自动与指定好友聊天
@bot.register(friend)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)


embed()
