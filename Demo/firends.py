from wxpy import *

bot = Bot()

# # 获取所有好友
# friends = bot.friends()
#
# # 遍历输出好友名称
# for friend in friends:
#     print(friend)
#
# 找到好友
friend = bot.friends.search('被单')[0]
print(friend)
#
# # 打印目标好友名称
# print(friend)

# groups = bot.groups()
#
# for group in groups:
#     print(group)
