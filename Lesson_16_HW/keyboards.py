from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup

from database import get_all_categories, get_products_by_category


def generate_phone_button():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Отправить свой контакт", request_contact=True)]
        ], resize_keyboard=True
    )


def generate_main_menu():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text='✅ Сделать заказ')],
            [KeyboardButton(text='📒 История'), KeyboardButton(text='🛒 Корзинка'), KeyboardButton(text='⚙ Настройки')]
        ], resize_keyboard=True
    )


def back_to_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Главное меню')]
    ], resize_keyboard=True)


def generate_category_menu():
    # TODO Получить общею сумму с корзинки
    categories = get_all_categories()

    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(
        InlineKeyboardButton(text=f'Ваша корзинка  (TODO сум)', callback_data='Ваша корзинка')
    )
    buttons = []
    for category in categories:
        bnt = InlineKeyboardButton(text=category[1], callback_data=f"category_{category[0]}")
        buttons.append(bnt)
    markup.add(*buttons)
    return markup


def generate_products_by_category(category_id):
    markup = InlineKeyboardMarkup(row_width=2)
    products = get_products_by_category(category_id)
    buttons = []
    for product in products:
        btn = InlineKeyboardButton(text=product[1], callback_data=f"product_{product[0]}")
        buttons.append(btn)
    markup.add(*buttons)
    return markup





