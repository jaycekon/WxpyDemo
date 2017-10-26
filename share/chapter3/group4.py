from wxpy import *

bot = Bot(cache_path=True)

# 获取目标群
group = bot.groups().search("网银监控报警")

friend = bot.friends().search("网银监控报警")

jiankong = ensure_one(group)

jiqiren = ensure_one(friend)

# 将联系人加入群聊
jiankong.add_members(jiqiren)

# 如果机器人在群聊，移除
if jiqiren in jiankong:
    jiankong.remove_members(jiqiren)

# for member in jiankong:
#     print(member.name)
#     if member.name == jiqiren.name:
#         print('移除{}群聊', jiqiren.name)
#         jiankong.remove_members(member)
