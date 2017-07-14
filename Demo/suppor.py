import logging
from wechat_sender import LoggingSenderHandler

logger = logging.getLogger(__name__)


# spider code here
def test_spider(body):
    logger.exception(body)


def init_logger():
    sender_logger = LoggingSenderHandler('spider', level=logging.EXCEPTION)
    logger.addHandler(sender_logger)


if __name__ == '__main__':
    init_logger()
    test_spider('hello world')
