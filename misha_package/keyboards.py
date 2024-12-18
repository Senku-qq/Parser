from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
import aiogram

setting_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Настройки ⚙️', callback_data='Настройки ⚙️'), InlineKeyboardButton(text='Сбросить настойки', callback_data='Сбросить настойки' )]    
],
                resize_keyboard=True,
                input_field_placeholder='Выберите пункт из меню')


languages = InlineKeyboardMarkup(inline_keyboard=[
    
    [InlineKeyboardButton(text='EN', callback_data='EN') ,  InlineKeyboardButton(text='UA',callback_data='UA'), InlineKeyboardButton(text='RU',callback_data='RU'), 
    InlineKeyboardButton(text='Выбрать свой язык', callback_data='Выбрать свой язык')],
],
                resize_keyboard=True,
                input_field_placeholder='Выберите пункт из меню')
percents = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='20%', callback_data='20%'), InlineKeyboardButton(text='40%', callback_data='40%'), 
    InlineKeyboardButton(text='60%', callback_data='60%') , InlineKeyboardButton(text='80%', callback_data='80%')],
],
                resize_keyboard=True,
                input_field_placeholder='Выберите пункт из меню')
setting = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Язык', callback_data='Язык'), InlineKeyboardButton(text='Объем', callback_data='Объем')]
])