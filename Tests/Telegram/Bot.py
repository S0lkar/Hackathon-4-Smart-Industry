
###################################
## ------ Módulos necesarios ------
###################################

# pip install pyTelegramBotAPI
import telebot
import Nucleo


###################################
## ------ Acciones del bot ------
###################################

# Introducimos el token correspondiente.
bot = telebot.TeleBot('6934807191:AAG3JYwFm9yASTBBzKKIwJ4V9f3QvB1FizY')

# Es posible crear diferentes comandos y personalizarlos
@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "¡Buenos días!")


# La funcionalidad principal es una réplica de la que existe en la web de Repsol;
# responde al mensaje del usuario con el control de calidad pertinente.
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, Nucleo.Chatbot(message.text))
    
# El bot se mantiene activo mientras este script esté en ejecución
bot.infinity_polling()