from wxpy import *
from wechat_sender import *

bot = Bot()

friend = bot.friends().search('被单')[0]

listen(bot, token='test', receivers=[friend])
