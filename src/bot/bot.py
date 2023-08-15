import telebot

from bot.config import TOKEN


class Bot:
    __bot = telebot.TeleBot(TOKEN)

    @classmethod
    def get_bot(cls):
        return cls.__bot
