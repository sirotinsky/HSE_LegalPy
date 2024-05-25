# users(tgid, username, fullname, reg_timestamp)
# users_log(tgid, action, timestamp)
# users_answers(tgid, question, answer)

import sqlite3
from telegram import Update
from datetime import datetime


class DB:
    db_path = "legalpy_2023.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()

    def insert_user(self, tgid, username, fullname):
        self.cur.execute(f"INSERT INTO users VALUES({tgid}, '{username}', '{fullname}', '{datetime.now()}')")

    def select_user(self, tgid):
        r = self.cur.execute(f"SELECT * FROM users WHERE tgid = {tgid}")
        return r.fetchone()

    def insert_poll(self, tgid):
        self.cur.execute(f"INSERT INTO polls VALUES({tgid}, 'Нет ответа', 'Нет ответа', 'Нет ответа')")

    def select_poll(self, tgid):
        r = self.cur.execute(f"SELECT * FROM polls WHERE tgid = {tgid}")
        return r.fetchone()

    def update_poll(self, tgid, question_number, answer):
        self.cur.execute(f"UPDATE polls SET question_{question_number} = '{answer}' WHERE tgid = {tgid}")


def handle_user(update: Update):
    with DB() as db:
        user = db.select_user(update.effective_user.id)
        if not user:
            db.insert_user(update.effective_user.id,
                           update.effective_user.username,
                           update.effective_user.full_name)
            db.insert_poll(update.effective_user.id)
        print('stop')


def get_results(update: Update):
    with DB() as db:
        results = db.select_poll(update.effective_user.id)
        return results


def save_answer(update: Update, question_number, answer):
    with DB() as db:
        db.update_poll(update.effective_user.id, question_number, answer)


if __name__ == "__main__":
    pass
