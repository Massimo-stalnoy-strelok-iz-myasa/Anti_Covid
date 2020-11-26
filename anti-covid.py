import telebot
from telebot import types
import urls
import COVID19Py


flag = True

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1423490246:AAH86ALx0alw1yQmjVcAxmTqqlR95V0kUC8')
urls.get_content(urls.html.text)
urls.get_content_1(urls.html_1.text)
urls.get_content_2(urls.html_2.text)
# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    btn5 = types.KeyboardButton('Италия')
    btn6 = types.KeyboardButton('Германия')
    btn7 = types.KeyboardButton('Япония')
    btn8 = types.KeyboardButton('Франция')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    flag = True
    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \
        f"название страны, например: США, Украина, Россия и так далее, если хотите просмотреть локальные данные введите " \
        f"команду /local, если хотите вернуться к общей статистике введите /all"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)




# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
    global flag
    final_message = ""
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "/local":
        send_message = f"Введите ваш город, чтобы узнать индекс самоизоляции или индекс активности граждан. " \
                       f"Введите ваш адресс, чтобы узнать есть ли заболевшие в вашем доме"
        bot.send_message(message.chat.id, send_message)
        flag = False

    elif get_message_bot == "/all":
        send_message = f"Выберите страну из списка предложенных "
        bot.send_message(message.chat.id, send_message)
        final_message = "1"
        flag = True
    elif get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "во всём мире":
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if final_message == "" and flag:
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                f"{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    else:
        res = [i for i in urls.all_streets if get_message_bot in i]
        res = str(res)
        if get_message_bot in urls.all_activity_cities:
            ind = urls.all_activity_cities.index(message.text.lower())
            final_message = 'Город найден: Индекс активности в вашем городе ' + str(urls.all_activity[ind])
            bot.send_message(message.chat.id, final_message)
        if get_message_bot in urls.all_cities:
            ind = urls.all_cities.index(message.text.lower())
            final_message = 'Город найден: Индекс самоизоляции в вашем городе ' + str(urls.all_index[ind])
            bot.send_message(message.chat.id, final_message)

        elif get_message_bot in res:
            final_message = 'Ваш дом найден в базе данных, рекомендуем надевать перчатки и маску при выходе из дома'
            bot.send_message(message.chat.id, final_message)


# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)
