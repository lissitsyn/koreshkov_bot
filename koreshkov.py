import os
import random

from dotenv import load_dotenv
from telegram.ext import Updater, Filters, MessageHandler, MessageFilter

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')
updater = Updater(token=TELEGRAM_TOKEN)

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
    print(chat)
    if 'Костя' in update.message.text or 'Корешков' in update.message.text:
        context.bot.send_message(chat_id=chat.id, text='Хватит флудить, я в Америке! (Северной)')        
    elif 'Америк' in update.message.text:
        context.bot.send_message(chat_id=chat.id, text=f'Кто сказал про Америку?? Я как раз собираюсь в {AMERICAN_CITIES[random.randint(0, (len(AMERICAN_CITIES) - 1))]}')
    elif 'сужда' in update.message.text:
        context.bot.send_message(chat_id=chat.id, text='Я тоже осуждаю!')

def main():
    updater.dispatcher.add_handler(MessageHandler(Filters.text, who_said_america))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
