"""
The bot will be run from this file. Here the handler functions will be assigned.
"""

import logging
import handlers
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters, PreCheckoutQueryHandler

from bot_tokens import BOT_TOKEN

# Console logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def stop_bot(updater):
    logger.info("Shutting down...")
    updater.stop()
    logger.info("Done (shutdown)")


def main():
    if BOT_TOKEN == "":
        logger.error("TOKEN not defined. Put your bot token on bot_tokens.py")
        return

    updater = Updater(BOT_TOKEN)
    h = updater.dispatcher.add_handler

    # Assigning handlers
    h(MessageHandler(Filters.all, handlers.incoming_message))
    updater.dispatcher.add_error_handler(handlers.error)

    updater.start_polling()

    # CONSOLE
    while True:
        inp = input("")
        if inp:
            input_c = inp.split()[0]
            args = inp.split()[1:]
            strig = ""
            for e in args:
                strig = strig + " " + e

            if input_c == "stop":
                stop_bot(updater)
                break

            else:
                print("Unknown command")


if __name__ == '__main__':
    main()
