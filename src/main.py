import os
import django
from django.core.exceptions import ValidationError
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "message_sender.settings")
django.setup()


from bot.bot import Bot
from simple_message_sender.models import ExtendedUser


bot = Bot.get_bot()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! Отправь нам свой уникальный номер, чтобы мы могли распознать тебя.')


@bot.message_handler(content_types='text')
def message_reply(message):
    is_registered = True
    try:
        ExtendedUser.objects.get(chat_id=message.chat.id)
    except ExtendedUser.DoesNotExist:
        is_registered = False
    if is_registered:
        bot.send_message(message.chat.id, "Этот чат уже есть в системе!")
        return
    try:
        user = ExtendedUser.objects.get(uuid=message.text)
        if not user.chat_id:
            user.chat_id = message.chat.id
            user.save()
            bot.send_message(message.chat.id, "Токен успешно добавлен!")
        else:
            bot.send_message(message.chat.id, "Такой пользователь уже есть в системе!")

    except ExtendedUser.DoesNotExist:
        bot.send_message(message.chat.id, "Такой токен не существует!")
    except ValidationError:
        bot.send_message(message.chat.id, "Некорректный токен!")




bot.infinity_polling()