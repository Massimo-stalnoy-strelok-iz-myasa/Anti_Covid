import telebot
from PIL import Image
from telebot import types
import urls
bot = telebot.TeleBot('1423490246:AAH86ALx0alw1yQmjVcAxmTqqlR95V0kUC8')
urls.get_content(urls.html.text)
urls.get_content_1(urls.html_1.text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '''Приветствую''', reply_markup=keyboard())


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text.lower() == 'индекс самоизоляции':
        text = 'Введите ваш город'
        bot.send_message(chat_id, text, reply_markup=keyboard())
    if message.text.lower() in urls.all_cities:
        ind = urls.all_cities.index(message.text.lower())
        text = 'Город найден: Индекс самоизоляции в вашем городе ' + str(urls.all_index[ind])
        bot.send_message(chat_id, text, reply_markup=keyboard())




def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Индекс Самоизоляции')
    markup.add(btn1)
    return markup


if __name__ == "__main__":
    bot.polling(none_stop=True)
