import telebot

bot = None
token = '5186609321:AAHn9_y4kihzwJ8rLAuDa8T_9EuWhW2hFck'
admin = 395039609


def main():
    global bot
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        print(message)
        bot.send_message(message.chat.id, 'Привет')
        bot.message_handler(content_types='text')

    @bot.message_handler(content_types='text')
    def message_reply(message):
        print(message)


def senddata(data):
    bot.send_message(admin, f'user registered : {data["username"]}')
