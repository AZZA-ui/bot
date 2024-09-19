import telebot

TOKEN = '7343123457:AAEsoj7fVxW-jvTJOpAVPfqJDgJfH2lCNxM'


subject_links = {
    'алгебра': 'https://www.mathway.com/ru/Algebra',
    'геометрия': 'https://www.geogebra.org/', 
    'физика': 'https://ru.khanacademy.org/science/physics',
    'химия': 'https://ru.khanacademy.org/science/chemistry',
    'биология': 'https://ru.khanacademy.org/science/biology',
    'история': 'https://history.wikireading.ru/', 
    'литература': 'https://www.litres.ru/',
    'русский язык': 'https://www.rustore.ru/catalog/app/com.gdzme',
    'английский язык': 'https://www.memrise.com/',
    'информатика': 'https://www.sololearn.com/'
}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для обучения! Что ты хочешь узнать?")

@bot.message_handler(func=lambda message: message.text.lower() in subject_links)
def send_gdz_link(message):
    subject = message.text.lower()
    link = subject_links.get(subject)
    if link:
        bot.reply_to(message, f"Вот ссылка на приложения: {link}")
    else:
        bot.reply_to(message, "Извини, я пока не знаю, где найти ГДЗ по этому предмету.")

@bot.message_handler(func=lambda message: message.text.lower() == 'помощь')
def help_message(message):
    bot.reply_to(message, "Я могу помочь найти ссылки на ГДЗ по различным предметам. Просто напиши название предмета.")

bot.polling()


