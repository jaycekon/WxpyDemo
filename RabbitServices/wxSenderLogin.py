from wechat_sender import *
from wxpy import *

bot = Bot()

friend = bot.friends().search('被单')[0]
group = bot.groups().search('409')[0]

print(friend)
print(group)
#
listen(bot, token='test', receivers=[friend, group])
