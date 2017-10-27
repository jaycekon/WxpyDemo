from wxpy import *

bot = Bot()

friend = bot.friends().search('网银监控报警')[0]

tuling = Tuling(api_key='80144c654b9846ed8b76c6f11cadfb3f')


@bot.register(friend)
def reply_my_friend(msg):
    print(msg)
    tuling.do_reply(msg)


embed()
