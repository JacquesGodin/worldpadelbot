from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import padeldraft

updater = Updater("5823803149:AAGCcGME54IdXp83gUkaoGVLVEcXvyAgsNY",
                  use_context=True)


def callback_alarm(update: Update, context: CallbackContext):
    update.message.reply_text(
        chat_id=-1001748512374, text='Hi, This is a daily reminder')

# chat_id=update.effective_chat.id,


def reminder(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Daily reminder has been set! You\'ll get notified at 8 AM daily')
    context.job_queue.run_daily(callback_alarm, context=update.message.chat_id, days=(
        0, 1, 2, 3, 4, 5, 6), time=time(hour=1, minute=48, second=10))


def player_enroll(update: Update, context: CallbackContext):

    # TEmos que ter aqui uma lógica para não apanhar os nomes caso a janela não esteja aberta
    player_name = update.message.text
    player_name = str.lower(player_name)

    confirmation = padeldraft.draftlist_verifier(player_name)
    if confirmation == True:
        answer = f'You enrolled {player_name}'
        update.message.reply_text(answer)
    elif confirmation == False:
        answer = f'{player_name} is already enrolled'
        update.message.reply_text(chat_id=-1001748512374, text=answer)


def enroll(update: Update, context: CallbackContext):
    padeldraft.timeframe_verifier_2()
    if padeldraft.timeframe_verifier_2() == True:
        update.message.reply_text(
            text='Window still open! Who do you want to enroll?')
    else:
        update.message.reply_text(
            text="draft window already ended")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/youtube - To get the youtube URL
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/geeks - To get the GeeksforGeeks URL""")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('enroll', enroll))
updater.dispatcher.add_handler(CommandHandler('reminder', reminder))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

updater.dispatcher.add_handler(MessageHandler(Filters.text, player_enroll))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
