from .conftest import Config
from telegram_sender import TelegramSender


def test_telegram_sender(config: Config):
    ts = TelegramSender(bot_token=config.bot_token)
    res = ts.msg(chat_id=config.chat_id, msg="test message")
    assert res.ok

def test_telegram_sender_bad_token(config: Config):
    ts = TelegramSender(bot_token='xxx')
    res = ts.msg(chat_id=config.chat_id, msg="test message")
    assert res.ok == False

def test_telegram_sender_bad_chat(config: Config):
    ts = TelegramSender(bot_token=config.bot_token)
    res = ts.msg(chat_id=111, msg="test message")
    assert res.ok == False

