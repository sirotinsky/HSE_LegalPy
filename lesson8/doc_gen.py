from io import StringIO, BytesIO
from docx import Document
from docx.shared import Inches


def make_a_doc(user_data, poll_data):
    document = Document()

    document.add_heading(f'Результаты пользователя id {user_data[0]}', 0)
    text = f"Результаты опроса:\n" \
           f"Ваш ИНН - {poll_data[1]}\n" \
           f"Ваc зовут - {poll_data[2]}\n" \
           f"Ваш возраст - {poll_data[3]} лет\n"
    document.add_paragraph(text)
    document.save(f"{user_data[0]}.docx")

