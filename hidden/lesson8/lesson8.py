import os
from doc_gen import make_a_doc
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from dotenv import load_dotenv
from database import save_user, get_user, create_poll, get_poll, save_answer
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

button_1 = KeyboardButton("About Me")
button_2 = KeyboardButton("Start a poll")
button_3 = KeyboardButton("Question 1")
button_4 = KeyboardButton("Question 2")
button_5 = KeyboardButton("Question 3")
button_6 = KeyboardButton("Back")
button_7 = KeyboardButton("Poll results")

main_menu = [[button_1, button_2]]
poll_menu = [[button_3, button_4],
             [button_5],
             [button_6, button_7]]


def start_command(update, context):
    tgid = update.effective_user.id
    nickname = update.effective_user.username
    if get_user(tgid):
        pass
    else:
        save_user(tgid, nickname)
    update.message.reply_text("Привет, я бот", reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=False))


def help_command(update, context):
    update.message.reply_text("/start - Запуск бота\n"
                              "/help - Список комманд бота")


def about_me(update: Update, context: CallbackContext):
    tgid = update.effective_user.id
    info = get_user(tgid)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(info))


def start_poll(update: Update, context: CallbackContext):
    tgid = update.effective_user.id
    if result := get_poll(tgid):
        pass
    else:
        create_poll(tgid)
        result = get_poll(tgid)
    text = f"Ваша анкета - {result}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(poll_menu, one_time_keyboard=False))


def question_1(update: Update, context: CallbackContext):
    text = f"Сообщите ваш ИНН"
    context.user_data.update({"is_asked": True, "question_number": 1})
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(poll_menu, one_time_keyboard=False))


def question_2(update: Update, context: CallbackContext):
    text = f"Как вас зовут?"
    context.user_data.update({"is_asked": True, "question_number": 2})
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(poll_menu, one_time_keyboard=False))


def question_3(update: Update, context: CallbackContext):
    text = f"Сколько вам лет?"
    context.user_data.update({"is_asked": True, "question_number": 3})
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(poll_menu, one_time_keyboard=False))


def poll_result(update: Update, context: CallbackContext):
    tgid = update.effective_user.id
    user_data = get_user(tgid)
    poll_data = get_poll(tgid)
    text = f"Результаты опроса:\n" \
           f"Ваш ИНН - {poll_data[1]}\n" \
           f"Ваc зовут - {poll_data[2]}\n" \
           f"Ваш возраст - {poll_data[3]} лет\n"
    doc = make_a_doc(user_data, poll_data)
    update.message.reply_document(doc, filename='Poll.docx')
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(poll_menu, one_time_keyboard=False))


def text_handler(update: Update, context: CallbackContext):
    tgid = update.effective_user.id
    user_status = context.user_data.get("is_asked")
    if user_status:
        question_number = context.user_data["question_number"]
        answer = update.message.text
        save_answer(tgid, question_number, answer)
        context.user_data["is_asked"] = False
        context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за ответ")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я тебя не понимаю")


dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("help", help_command))

dispatcher.add_handler(MessageHandler(Filters.regex("About Me") & ~Filters.command, about_me))
dispatcher.add_handler(MessageHandler(Filters.regex("Start a poll") & ~Filters.command, start_poll))
dispatcher.add_handler(MessageHandler(Filters.regex("Question 1") & ~Filters.command, question_1))
dispatcher.add_handler(MessageHandler(Filters.regex("Question 2") & ~Filters.command, question_2))
dispatcher.add_handler(MessageHandler(Filters.regex("Question 3") & ~Filters.command, question_3))
dispatcher.add_handler(MessageHandler(Filters.regex("Back") & ~Filters.command, start_command))
dispatcher.add_handler(MessageHandler(Filters.regex("Poll results") & ~Filters.command, poll_result))

dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_handler))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
