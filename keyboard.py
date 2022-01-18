from aiogram import types

butmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
butmenu.add(
    types.KeyboardButton('🔐 Кошелек'),
    types.KeyboardButton('💳 Купить Amber'),
    types.KeyboardButton('🧑🏻‍💻 О проекте'),
    types.KeyboardButton('🚨 Airdrop'),
    types.KeyboardButton('📋 Смарт контракт'),
    types.KeyboardButton('❓ Инструкция'),
)
#####################################################################################################################################################################################################################

pay = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
pay.add(
    types.InlineKeyboardButton(text='Оплатил', callback_data='lllllllllll'),
    types.InlineKeyboardButton(text='Отмена', callback_data='otmena'),
)

wallets = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
wallets.add(
    types.InlineKeyboardButton(text='Bep20', callback_data='Bep20'),
)

summa = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
summa.add(
    types.InlineKeyboardButton(text='20 USDT', callback_data='qqqqqqqqq'),
    types.InlineKeyboardButton(text='50 USDT', callback_data='wwwwwwww'),
    types.InlineKeyboardButton(text='100 USDT', callback_data='eeeeee'),
    types.InlineKeyboardButton(text='250 USDT', callback_data='rrrrrrrr'),
    types.InlineKeyboardButton(text='500 USDT', callback_data='tttttttt'),
    types.InlineKeyboardButton(text='1000 USDT', callback_data='yyyyyy'),
    types.InlineKeyboardButton(text='Другая сумма(от 20 USDT до 1000 USDT)', callback_data='uuuuuuue'),
)

ref = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
ref.add(
    types.InlineKeyboardButton(text='👥 Реферальная ссылка', callback_data='refka'),
    )

getmoney = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
getmoney.add(
    types.InlineKeyboardButton(text='➡️ Вывести', callback_data='netsred'))

kytak = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
kytak.add(
    types.InlineKeyboardButton(text='💳 Оплатить', url='https://bscscan.com/token/0xd8072c0a4fc844296ce440bdc81585744b635f27'),
    types.InlineKeyboardButton(text='Отмена', callback_data='otmena')
    )

#####################################################################################################################################################################################################################
wallet = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
wallet.add(
    types.InlineKeyboardButton(text='⬇️ Вывести на свой кошелёк', callback_data='get'),
    #types.InlineKeyboardButton(text='❓ Инструкция по выводу', callback_data='incruktion'),
)

butback = types.ReplyKeyboardMarkup(resize_keyboard=True)
butback.add(
    types.KeyboardButton('Отмена'))

butinc = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
butinc.add(
    types.KeyboardButton('Отмена'))

seti = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
seti.add(
    types.InlineKeyboardButton(text='Instagram', url='https://instagram.com/pandoragameonline?utm_medium=copy_link'),
    types.InlineKeyboardButton(text='Tik tok', url='https://vm.tiktok.com/ZSeSUE4eS/'),
    types.InlineKeyboardButton(text='Telegram', url='https://t.me/PandoraGameChannel'),
)

inline_btn_3 = types.InlineKeyboardButton('📲 Скачать игру', callback_data='popal')

seti.add(inline_btn_3)
#####################################################################################################################################################################################################################
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('💬 Рассылка'))


back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('⏪ Отмена')
)

csk = types.ReplyKeyboardMarkup(resize_keyboard=True)
csk.add(
    types.KeyboardButton('↪️ Отмена')
)

polzi = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
polzi.add(
    types.InlineKeyboardButton(text='@alex_mid1', callback_data='alex_mid1'),
    types.InlineKeyboardButton(text='@Techno_Web', callback_data='Techno_Web'),
    types.InlineKeyboardButton(text='@webcoderpt', callback_data='webcoderpt'),
    types.InlineKeyboardButton(text='@Adres31', callback_data='Adres31'),
    types.InlineKeyboardButton(text='@AsterFerre', callback_data='AsterFerre'),
    types.InlineKeyboardButton(text='@Dmitriy_LD', callback_data='Dmitriy_LD'),
    types.InlineKeyboardButton(text='@PROCoinPrivateSALE', callback_data='PROCoinPrivateSALE'),
    types.InlineKeyboardButton(text='@ZBOOM1', callback_data='ZBOOM1'),
    types.InlineKeyboardButton(text='@az77www', callback_data='az77www'),
    types.InlineKeyboardButton(text='@A_s_ko', callback_data='A_s_ko'),
    types.InlineKeyboardButton(text='@AlikTHOR', callback_data='@AlikTHOR'),

    )

def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='💬 Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='❎ Удалить', callback_data='ignor')
    )
    return quest

def fan(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='💬 Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='🟢 Summa', callback_data=f'{user_id}-bns'),

    )
    return quest
#####################################################################################################################################################################################################################
admmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
admmenu.add(
    types.KeyboardButton('📡 Рассылка'),
    types.KeyboardButton('🛠 Настройки'),
    types.KeyboardButton('⏪ Меню'),

    )


settings = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
settings.add(
    types.InlineKeyboardButton(text='💸 Цена монеты', callback_data='pricemonet'),
    types.InlineKeyboardButton(text='📊 Статистика', callback_data='statiks'))