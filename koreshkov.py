import os
import random
import time

from dotenv import load_dotenv
from telegram.ext import Updater, Filters, MessageHandler, MessageFilter

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')
updater = Updater(token=TELEGRAM_TOKEN)

AMERICAN_CITIES = ['Нью-Йорк',
                   'Лос-Анджелес',
                   'Чикаго',
                   'Хьюстон',
                   'Филадельфия',
                   'Финикс',
                   'Сан-Антонио',
                   'Сан-Диего',
                   'Даллас',
                   'Сан-Хосе',]


class FilterAmerica(MessageFilter):
    def filter(self, message):
        return '/Америк' in message.text


class FilterConst(MessageFilter):
    def filter(self, message):
        return '/Костя' in message.text or '/Корешков' in message.text


def who_said_america(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=f'Кто сказал про Америку?? Я как раз собираюсь в {AMERICAN_CITIES[random.randint(0, len(AMERICAN_CITIES))]}')

def kostya(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Хватит флудить, я в Америке!')

filter_america = FilterAmerica()
filter_kostya = FilterConst()

def main():
    updater.dispatcher.add_handler(MessageHandler(filter_america, who_said_america))
    updater.dispatcher.add_handler(MessageHandler(filter_kostya, kostya))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()