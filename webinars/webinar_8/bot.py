import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackContext
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from datetime import datetime
from database_new import handle_user, get_results, save_answer

BOT_TOKEN = '6589359799:AAG97ZJN2loKg_rpUwGF_NkKCUTKfsaujgw'

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

button_1 = KeyboardButton("About Me")
button_2 = KeyboardButton("Start a poll")
main_menu = [[button_1],
             [button_2]]

button_3 = KeyboardButton("Question 1")
button_4 = KeyboardButton("Question 2")
button_5 = KeyboardButton("Question 3")
button_6 = KeyboardButton("Back")
button_7 = KeyboardButton("Poll results")
poll_menu = [[button_3, button_4],
             [button_5],
             [button_6, button_7]]


def log_action(action, update: Update):
    tgid = update.effective_user.id
    username = update.effective_user.username
    fullname = update.effective_user.full_name
    log_time = datetime.now()
    print(f'{action} ----- id - {tgid}, username - {username}, fullname - {fullname}, time - {log_time}')


def start_command(update: Update, context):
    handle_user(update)
    log_action('start_command', update)
    update.message.reply_text("Привет, я бот",
                              reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True))


def help_command(update, context):
    log_action('help_command', update)
    text = f"/start - Запуск бота\n" \
           f"/help - Список команд"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True))


def about_me(update, context):
    log_action('about_me', update)
    text = f"Я бот для обучения"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True))


def start_poll(update, context):
    log_action('start_poll', update)
    text = 'Выбери вопрос'
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(poll_menu, resize_keyboard=True, one_time_keyboard=True))


def question_1(update, context: CallbackContext):
    log_action('question_1', update)
    context.user_data.update({"is_asked": True, "question_number": 1})
    text = "Как тебя зовут?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(poll_menu, resize_keyboard=True, one_time_keyboard=True))


def question_2(update, context: CallbackContext):
    log_action('question_2', update)
    context.user_data.update({"is_asked": True, "question_number": 2})
    text = "Сколько тебе лет?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(poll_menu, resize_keyboard=True, one_time_keyboard=True))


def question_3(update, context: CallbackContext):
    log_action('question_3', update)
    context.user_data.update({"is_asked": True, "question_number": 3})
    text = "Ты где?"
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(poll_menu, resize_keyboard=True, one_time_keyboard=True))


def poll_result(update, context: CallbackContext):
    results = get_results(update)
    log_action('poll_result', update)
    text = f'Имя - {results[1]}\n' \
           f'Возраст - {results[2]}\n' \
           f'Местоположение - {results[3]}'
    update.message.reply_text(text,
                              reply_markup=ReplyKeyboardMarkup(poll_menu, resize_keyboard=True, one_time_keyboard=True))


def text_handler(update: Update, context: CallbackContext):
    user_status = context.user_data.get("is_asked")
    if user_status:
        question_number = context.user_data["question_number"]
        answer = update.message.text
        save_answer(update, question_number, answer)
        context.user_data["is_asked"] = False
        context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за ответ")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я тебя не понимаю")


dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(MessageHandler(Filters.regex("Back") & ~Filters.command, start_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.regex("About Me") & ~Filters.command, about_me))
dispatcher.add_handler(MessageHandler(Filters.regex("Start a poll") & ~Filters.command, start_poll))

dispatcher.add_handler(MessageHandler(Filters.regex("Question 1") & ~Filters.command, question_1))
dispatcher.add_handler(MessageHandler(Filters.regex("Question 2") & ~Filters.command, question_2))
dispatcher.add_handler(MessageHandler(Filters.regex("Question 3") & ~Filters.command, question_3))
dispatcher.add_handler(MessageHandler(Filters.regex("Poll results") & ~Filters.command, poll_result))

dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_handler))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
