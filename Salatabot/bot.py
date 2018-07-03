# -*- coding: utf-8 -*-
import telebot
import os

token = "583265743:AAE5Qu4WZyJGOHwCGZjo_-acE8Vw1pmX5t0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def handle_start(message):
    user_markup.row('U+1F601')
    user_markup.row('U+1F60A', 'U+1F620')
    bot.send_message(message.chat.id, 'Выбери подходящий эмодзи', reply_markup = user_marcup)

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == 'U+1F601':
        directory = 'C:/Users/asalatik/Desktop/1'
        oll_files_in_directory = os.listdir(directory)
        print(oll_files_in_directory)
        for file in oll_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == 'U+1F601':
         directory = 'C:/Users/asalatik/Desktop/3'
         oll_files_in_directory = os.listdir(directory)
         print(oll_files_in_directory)
         for file in oll_files_in_directory:
             img = open(directory + '/' + file, 'rb')
             bot.send_chat_action(message.from_user.id, 'upload_photo')
             bot.send_photo(message.from_user.id, img)
             img.close()

@bot.message_handler(content_types = ['text'])
def handle_text(message):
        if message.text == 'U+1F601':
            directory = 'C:/Users/asalatik/Desktop/1'
            oll_files_in_directory = os.listdir(directory)
            print(oll_files_in_directory)
            for file in oll_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.from_user.id, img)
                img.close()

@bot.message_handler(content_types = ['text'])
def handle_test (message):
        if message.text == "Привет":
            bot.send_message(message.chat.id, "Привет")
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, "Отлично!")
        else:
            bot.send_message(message.chat.id, "Выберите эмодзи из таблицы!")

bot.polling(none_stop = True)


