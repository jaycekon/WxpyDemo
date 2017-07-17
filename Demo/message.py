from wxpy import *

bot = Bot()
# 获取好友
my_friend = bot.friends().search('被单')[0]

# 搜索信息
messages = bot.messages.search(keywords='测试', sender=bot.self)

for message in messages:
    print(message)

# 发送文本
my_friend.send('Hello, WeChat!')
# 发送图片
my_friend.send_image('my_picture.png')
# 发送视频
my_friend.send_video('my_video.mov')
# 发送文件
my_friend.send_file('my_file.zip')
# 以动态的方式发送图片
my_friend.send('@img@my_picture.png')

# 发送公众号
my_friend.send_raw_msg(
    # 名片的原始消息类型
    raw_type=42,
    # 注意 `username` 在这里应为微信 ID，且被发送的名片必须为自己的好友
    raw_content='<msg username="wxpy_bot" nickname="wxpy 机器人"/>'
)


# 消息接收监听器
@bot.register()
def print_others(msg):
    # 输出监听到的消息
    print(msg)
    # 回复消息
    msg.reply("hello world")


embed()
