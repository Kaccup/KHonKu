import telebot

bot = telebot.TeleBot('1911075972:AAGrQrbIcmhPrDnyq6GqcItCwNO5F-UHLNE')


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Начало')
    msg = bot.send_message(message.chat.id, text='Выберите раздел', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='Рассказы', callback_data='first'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Анекдоты', callback_data='second'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Шутки за 300', callback_data='three'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Черный юмор', callback_data='four'))

    if message.text == 'Начало':
        msg = bot.send_message(message.chat.id, text='Что желаем?)))', reply_markup=menu1)
        #bot.register_next_step_handler(msg, step2)
        bot.register_next_step_handler(msg, step3)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(telebot.types.InlineKeyboardButton(text='Космос детям', callback_data='three'))
    menu2.add(telebot.types.InlineKeyboardButton(text='Рыбалка', callback_data='four'))
    menu2.add(telebot.types.InlineKeyboardButton(text='Love Story', callback_data='five'))
    menu2.add(telebot.types.InlineKeyboardButton(text='Случай в походе', callback_data='six'))
    if call.data == 'first':
        msg = bot.send_message(call.message.chat.id, 'Вы выбрали рассказы:', reply_markup=menu2)
        bot.register_next_step_handler(msg, step2)


@bot.callback_query_handler(func=lambda call: True)
def step3(call):
    menu3 = telebot.types.InlineKeyboardMarkup()
    menu3.add(telebot.types.InlineKeyboardButton(text='Новый год', callback_data='seven'))
    menu3.add(telebot.types.InlineKeyboardButton(text='Винни-Пух', callback_data='eight'))
    menu3.add(telebot.types.InlineKeyboardButton(text='Про собак', callback_data='nine'))
    menu3.add(telebot.types.InlineKeyboardButton(text='Чукча', callback_data='ten'))
    if call.data == 'second':
        msg = bot.send_message(call.message.chat.id, 'Вы выбрали Анекдоты:', reply_markup=menu3)
        bot.register_next_step_handler(msg, step3)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я расскажу Анекдот. напиши - /start")

    elif message.text == "three":
        bot.send_message(message.from_user.id, "В детстве думал: - Ура, скоро Новый год! Сейчас думаю: "
                                                   "- Твою мать, скоро опять Новый год...😂 ")
        bot.send_message(message.from_user.id, "- Как ты встретил Новый год? - Как подарок. "
                                                   "- В смысле? - Всю ночь под ёлкой валялся! 😂")
        bot.send_message(message.from_user.id, "Хочу на Новый год: пачку нервов, упаковку терпения, "
                                               "хронического здоровья, неизлечимого счастья"
                                                   " и вечно беременного кошелька! 😂")
        bot.send_message(message.from_user.id, "На Новый год тёща подарила мне два билета в театр."
                                                   " Жена приболела, дети уехали на горных лыжах кататься..."
                                                   " Вот я и думаю, в чем подвох? 😂")
def step4(call):
    if call.data == 'three':
        msg = bot.send_message(call.message.chat.id, 'Конец')
    else:
        pass


bot.polling(none_stop=True)
