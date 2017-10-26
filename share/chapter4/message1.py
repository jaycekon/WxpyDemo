from wxpy import *

# 普通登陆
bot = Bot(cache_path=True)

friend = ensure_one(bot.friends().search("黄伟杰"))

# 发送文本文件
friend.send_msg("hello world")

# 发送图片
friend.send_image("D:/QR.png")

friend.send_raw_msg(
    # 名片的原始消息类型
    raw_type=42,
    # 注意 `username` 在这里应为微信 ID，且被发送的名片必须为自己的好友
    raw_content='<msg username="wxpy_bot" nickname="wxpy 机器人"/>'
)

print("ending!")
