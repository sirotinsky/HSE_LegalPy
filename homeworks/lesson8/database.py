import sqlite3


class DB:
    db_path = "legalpy.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()

    def insert_user(self, tgid, nickname):
        self.cur.execute(f"INSERT INTO users VALUES({tgid}, '{nickname}')")

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


def get_user(tgid):
    with DB() as db:
        user = db.select_user(tgid)
    return user


def save_user(tgid, nickname):
    with DB() as db:
        db.insert_user(tgid, nickname)


def get_poll(tgid):
    with DB() as db:
        result = db.select_poll(tgid)
    return result


def create_poll(tgid):
    with DB() as db:
        db.insert_poll(tgid)


def save_answer(tgid, question_number, answer):
    with DB() as db:
        db.update_poll(tgid, question_number, answer)


if __name__ == "__main__":
    pass
