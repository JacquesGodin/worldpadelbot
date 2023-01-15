from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


import padeldraft
from datetime import time

updater = Updater("5920011320:AAEyf6TWMbP3F8SCcMIJZq53vuhuDHZ6Lus",
                  use_context=True)


job = updater.job_queue


def weekly_draft(context):  # task that returns the list of drafted players
    # context.bot.send_message(chat_id=context.job.context,
    #                         text='Players drafted for upcoming week are:\n')
    context.bot.send_message(chat_id="-1001748512374",
                             text='Players drafted for upcoming week are:\n')
    match = padeldraft.draft()
    for x in range(0, 4):
        context.bot.send_message(chat_id=context.job.context, text=match[x])
        context.bot.send_message(chat_id="-1001748512374", text=match[x])
    # after picking the players, deletes the list_players' entries
    padeldraft.draftlist_reseter()
    # after picking the players, deletes the list_subscribers entries
    padeldraft.subscriberslist_reseter()


t = time(22, 2, 00, 000000)  # sets the time when the draft is going to occur
status = False


def jobDay(update, context):  # sets the date and time when the draft is going to occur
    job.run_daily(weekly_draft, t, days=(0, 1, 2, 3, 4, 5, 6),
                  context=update.message.chat_id)


# subscribes a new player to the draft list
def player_enroll(update: Update, context: CallbackContext):
    global status
    # in case the user has already prompted /enroll, status will be True. This is used to avoid adding to the list other words besides the player's name (e.g. "hey")
    if status == True:
        user = update.message.from_user
        subscription = padeldraft.subscriberid_verifier(user['id'])
        if subscription == False:
            answer = f'You already subscribed to the draft this week'
            update.message.reply_text(answer)
        else:
            player_name = update.message.text
            player_name = str.lower(player_name)
            confirmation = padeldraft.draftlist_verifier(player_name)

            if confirmation == True:
                answer = f'{player_name} has been added to the draft list'
                update.message.reply_text(answer)
            elif confirmation == False:
                answer = f'{player_name} is already in the draft list'
                update.message.reply_text(text=answer)
    status = False
    return status


# checks if the subscriptions window is still open
def enroll(update: Update, context: CallbackContext):
    padeldraft.timeframe_verifier_2()
    if padeldraft.timeframe_verifier_2() == True:
        update.message.reply_text(
            text='Subscription window still open! Who do you want to add to the draft list?')
        global status  # we set a global variable, that will be used by player_enroll function to control the conversation flow
        status = True
        return status

    else:
        print(padeldraft.timeframe_verifier_2())
        update.message.reply_text(
            text="Subscription window already closed")


# returns the list of players in the draft list
def draft_list(update: Update, context: CallbackContext):
    draftlist = padeldraft.players_list()
    print(draftlist)
    if draftlist == []:
        # context.bot.send_message(
        #    chat_id="-1001748512374", text="Draft list is still empty")
        update.message.reply_text(text="Draft list is still empty")
    else:
        # context.bot.send_message(
        #    chat_id="-1001748512374", text="the enrolled players for the coming week are:")
        update.message.reply_text(
            text="the enrolled players for the coming week are:")
        for item in draftlist:
            # context.bot.send_message(chat_id="-1001748512374", text=item)
            update.message.reply_text(text=item)


def help(update: Update, context: CallbackContext):
    help_text = "Use the following commands:" + "\n\n" + "/enroll - to add your name to the draft list" + \
        "\n" + "/draftlist - to check what names are on the list for the coming week's game"
    update.message.reply_text(text=help_text)


# chat handlers
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler('enroll', enroll))
updater.dispatcher.add_handler(CommandHandler("draftlist", draft_list))
updater.dispatcher.add_handler(CommandHandler(
    "start", jobDay, pass_job_queue=True))
updater.dispatcher.add_handler(MessageHandler(Filters.text, player_enroll))

updater.start_polling()
