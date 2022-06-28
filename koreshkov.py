import os
import random

from dotenv import load_dotenv
from telegram import Bot, Sticker
from telegram.ext import Updater, Filters, MessageHandler, MessageFilter

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')
updater = Updater(token=TELEGRAM_TOKEN)
bot = Bot(token=TELEGRAM_TOKEN)

AMERICAN_CITIES = ['Нью-Йорк',
                   'Лос-Анджелес',
                   'Чикаго',
                   'Хьюстон',
                   'Филадельфию',
                   'Финикс',
                   'Сан-Антонио',
                   'Сан-Диего',
                   'Даллас',
                   'Сан-Хосе',]


def who_said_america(update, context):
    chat = update.effective_chat
    try:
        if 'костя' in update.message.text.lower() or 'корешков' in update.message.text.lower():
            context.bot.send_message(chat_id=chat.id, text='Хватит флудить, я в Америке! (Северной)')        
        elif 'америк' in update.message.text.lower():
            context.bot.send_message(chat_id=chat.id, text=f'Кто сказал про Америку?? Я как раз собираюсь в {AMERICAN_CITIES[random.randint(0, (len(AMERICAN_CITIES) - 1))]}')
        elif 'сужда' in update.message.text.lower():
            context.bot.send_message(chat_id=chat.id, text='Я тоже осуждаю!')
        elif 'грузия' in update.message.text.lower() or 'грузии' in update.message.text.lower() or 'грузию' in update.message.text.lower():
            context.bot.send_message(chat_id=chat.id, text='Грузия, кстати, почти Америка')
    except AttributeError:
        context.bot.send_message(chat_id=chat.id, text='Мне ваши картиночки из Америки не видно!')


def main():
    updater.dispatcher.add_handler(MessageHandler(Filters.text, who_said_america))
    updater.dispatcher.add_handler(MessageHandler(Filters.sticker, who_said_america))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
