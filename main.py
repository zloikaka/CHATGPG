import telebot
import os
import dotenv

from openai_parser import get_response


dotenv.load_dotenv()
BOT_TOKEN = os.getenv("TELEGA_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    """Обработчик команды /start"""
    bot.send_message(message.chat.id, 'Hi')


@bot.message_handler(func=lambda message: True)
def text_message(message):
    """Обработчик личных текстовых сообщений."""
    user_id = message.chat.id
    user_message = message.text

    try:
        response = get_response(user_message)
        bot.send_message(user_id, response)
    except Exception as e:
        bot.send_message(message.chat.id, f'Не Получилось {e}')


if __name__ == '__main__':
    bot.polling()
