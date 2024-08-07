import telebot

bot = telebot.TeleBot('7188342666:AAErbszhhZY3RXzQ5xgCjEHOFnXu4hrIOiY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     '*Добрый вечер, пожалуйста выберите ваше настроение на данный момент из списка команд*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['melancholic'])
def mood1(message):
    bot.send_message(message.chat.id, '*[что-то грустное](https://vk.com/music/playlist/-147845620_737)*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['*happiness*'])
def mood2(message):
    bot.send_message(message.chat.id, '*[тут написано что-то подходящее](https://vk.com/music/playlist/-180375381_83)*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['thoughtful'])
def mood3(message):
    bot.send_message(message.chat.id, '*[учись, студент](https://vk.com/music/playlist/-32169030_520)*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['sleepy'])
def mood4(message):
    bot.send_message(message.chat.id,
                     '*[плейлист для сна](https://vk.com/music/album/-2000677508_19677508_07c61cbecabaab271d)*',
                     parse_mode='Markdown')


bot.infinity_polling()