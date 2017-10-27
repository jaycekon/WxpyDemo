from wxpy import *

# 普通登陆
bot = Bot(cache_path=True)

friend = ensure_one(bot.friends().search("网银监控报警"))

group = ensure_one(bot.friends().search("wxpy分享"))


# 消息接收监听器
@bot.register()
def print_msg(msg):
    # 输出监听到的消息的发送者：
    # 用户聊天
    print(msg.sender)
    # 群聊
    print(msg.member)
    msg.forward(bot.file_helper)


# 消息接收监听器
@bot.register(friend)
def reply_msg(msg):
    # 输出监听到的消息
    msg.reply("haode")


# 回复群聊中被@ 的
@bot.register(group)
def reply_msg(msg):
    # 输出监听到的消息
    if msg.is_at:
        msg.reply('haode')


embed()
