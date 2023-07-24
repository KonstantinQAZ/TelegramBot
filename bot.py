#библиотеки, которые загружаем из вне
import telebot
TOKEN = ''

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("EPL 🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮")
	item2 = types.KeyboardButton("BundesLiga 🇩🇪")
	item3 = types.KeyboardButton("La Liga 🇪🇸")
	item4 = types.KeyboardButton("Seria A 🇮🇹")
	item5 = types.KeyboardButton("Ligue 1 🇫🇷")
	item6 = types.KeyboardButton("RPL 🇷🇺")

	markup.add(item1, item2, item3, item4, item5, item6)

	bot.send_message(message.chat.id, "Доброе утро, добрый день, добрый вечер, дорогой, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def connector(message):
	if message.chat.type == 'private':
		if message.text == 'EPL 🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮':
			bot.send_message(message.chat.id, 'https://www.skysports.com/premier-league-fixtures')
		elif message.text == 'BundesLiga 🇩🇪':
			bot.send_message(message.chat.id, 'https://www.bundesliga.com/en/bundesliga')
		elif message.text == 'La Liga 🇪🇸':
			bot.send_message(message.chat.id, 'https://www.laliga.com/en-GB')
		elif message.text == 'Seria A 🇮🇹':
			bot.send_message(message.chat.id, 'https://www.legaseriea.it/en')
		elif message.text == 'Ligue 1 🇫🇷':
			bot.send_message(message.chat.id, 'https://www.ligue1.com/')
		elif message.text == 'RPL 🇷🇺':
			bot.send_message(message.chat.id, 'https://premierliga.ru/')
		else:
			bot.send_message(message.chat.id, 'Мы тут ради футбола, разве нет?🤔')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
