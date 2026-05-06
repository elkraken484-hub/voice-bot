import telebot
from gtts import gTTS
import os

# التوكن الخاص بك
TOKEN = '8642862579:AAEdnn4W6AeQ5B_OrGZ9kLsmtPOkDFBno8Q'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "أهلاً بك! ابعتلي أي نص وهحولهولك لصوت عربي فوراً.")

@bot.message_handler(func=lambda message: True)
def text_to_speech(message):
    try:
        tts = gTTS(text=message.text, lang='ar')
        file_name = f"voice_{message.chat.id}.mp3"
        tts.save(file_name)
        with open(file_name, "rb") as audio:
            bot.send_voice(message.chat.id, audio)
        os.remove(file_name)
    except Exception as e:
        bot.reply_to(message, "حصل مشكلة، جرب تاني.")

bot.polling()
