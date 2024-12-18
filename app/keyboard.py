from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 20%", callback_data="20"),
            InlineKeyboardButton(text="📝 30%", callback_data="30"),
            InlineKeyboardButton(text="📝 40%", callback_data="40")
        ],
        [
            InlineKeyboardButton(text="📝 50%", callback_data="50"),
            InlineKeyboardButton(text="📝 60%", callback_data="60"),
            InlineKeyboardButton(text="📝 70%", callback_data="70")
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
            InlineKeyboardButton(text="🇺🇦 Ukrainian", callback_data="uk"),
            InlineKeyboardButton(text="🇷🇺 Russian", callback_data="ru"),
        ],
        [
            InlineKeyboardButton(text="📎 Custom", callback_data="custom")
        ]
    ],
    resize_keyboard=True
)