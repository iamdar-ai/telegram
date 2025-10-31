import random
import telebot

BOT_TOKEN = "8397625470:AAHi0NdtWs3wjKLeR-QENccGX7Tp_b0EtZk"  # ← ТВОЙ ТОКЕН

# Создаем бота
bot = telebot.TeleBot(BOT_TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - кладезь народной мудрости, собранной по крупицам из заметок, сердец и умов людей. Я создан благодаря неприязни моей матери-фрилансерки (счастье в семье) Бреус Дарьи Юрьевны к hh.ru и восьмичасовому рабочему дню. А ещё благодаря друзьям и семье БДЮ, которые внесли свой бесценные вклад в этот ящик Пандоры.  Можешь тыкать рандомно или задать какой-нибудь вопрос. Помни, что ты всегда  можешь оправдать своё магическое мышление психоанализом и работой подсознания. А лучше вообще не оправдывайся. Пошли они все в жопу. В общем, если ты готов_а получить живительную каплю рандомной мудрости/хохмы дня, то используй /phrase и узнай, куда эта кривая дорожка заведёт тебя сегодня")


# Обработчик команды /phrase
@bot.message_handler(commands=['phrase'])
def send_phrase(message):
    try:
        # Читаем все фразы из файла
        with open('phrases.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        # Разделяем по пустым строкам (два переноса подряд)
        phrases = content.split('\n\n')

        # Убираем пустые элементы и лишние пробелы
        phrases = [p.strip() for p in phrases if p.strip()]

        if phrases:
            random_phrase = random.choice(phrases)
            bot.reply_to(message, random_phrase)
        else:
            bot.reply_to(message, "Фразы пока не добавлены")

    except FileNotFoundError:
        bot.reply_to(message, "Файл с фразами не найден")


# Обработчик команды /about
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Я бот с цитатами!")


# Запускаем бота
print("Bot started! Press Ctrl+C to stop")
bot.polling()