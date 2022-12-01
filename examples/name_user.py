import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def name_user(message):
  msg = bot.send_message(message.chat.id, 'Hello {}! Thanks for using pyTelegramBotAPI'.format(message.from_user.full_name), 
  reply_markup= ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add('Thank you'))
  bot.register_next_step_handler(msg, next_)
  
def next_(message):
  if message.text == 'Thank you':
    bot.send_message(message.chat.id, '^^', reply_markup= ReplyKeyboardRemove())
    
if __name__ == '__main__':
  print('bot is active')
  bot.infinity_polling()
