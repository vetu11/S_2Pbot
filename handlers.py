"""
Here should be declared all functions that handle the supported Telegram API calls.
"""

import random
import const


def _generate_message_que_dise():

    que_list = ["Q", "q", "Que", "que", "Qué", "qué"]
    separator = [", ", " "]
    dise_list = ["dise"]

    return random.choice(que_list) + random.choice(separator) + random.choice(dise_list)


def incoming_message(bot, update):
    print("mssage")
    update.effective_message.reply_text(_generate_message_que_dise(), quote=False)


def error(bot, update, error):
    bot.send_message(const.ADMIN_TELEGRAM_ID, "The update:\n%s\nhas caused this error:\n%s" % (str(update), str(error)))
