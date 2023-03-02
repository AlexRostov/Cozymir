import telebot
from telebot.types import Message

bot_client = telebot.TeleBot(token = "5999596906:AAF3nY8dhPXvgqIUUCNNImK0vffZW54MMg4") # создание сущности бота
@bot_client.message_handler(commands=["start"]) # декаратор

def echo(message: Message):  # функсция эхо бота
    bot_client.reply_to(message=message, text=" Привет") # ответ на сообщение
    bot_client.send_message(chat_id=message.chat.id, text="sample") # отправка сообщение пользователю.



bot_client.polling() # запуск бота