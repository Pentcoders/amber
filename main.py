import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, admin, adminka, kytakber, kytakike, kytakoc, mindyrt, kytakdyrt, kytakbish, kytakalta, kytakete, kytakcig, kytaktyg, kytakfnew, kytak23, kytak006, mimi
import keyboard as kb
import functions as func
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled
import aiogram.utils.markdown as fmt
import sys
import io
    
  


storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
connection = sqlite3.connect('data.db')
q = connection.cursor()

class st(StatesGroup):
	item = State()
	item2 = State()
	kytak = State()
	buy = State()
	botom = State()
	summa = State()
	walamber = State()
	item6 = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer(f"'Добро пожаловать {message.from_user.first_name} ", reply_markup=kb.menu)
		else:
			await message.answer(f'Здравствуйте, {message.from_user.first_name} ! Поздравляем вас с регистрацией в нашем проекте!', reply_markup=kb.butmenu)
			#await message.answer(admin, f'Чел {message.from_user.first_name} {message.from_user.mention}')

@dp.message_handler(commands=['admin'])
async def start(message: types.Message):
	if message.chat.id == admin:
		await message.answer('<b>Интерфейс админки</b>\n\nАдмины: @Adres31, @AsterFerre, @Dmitriy_LD, @alex_mid1', reply_markup=kb.admmenu, parse_mode='HTML')
	elif message.chat.id == mimi:
		await message.answer('<b>Интерфейс админки</b>\n\nАдмины: @Adres31, @AsterFerre, @Dmitriy_LD, @alex_mid1', reply_markup=kb.admmenu, parse_mode='HTML')
	elif message.chat.id == kytakber:
		await message.answer('<b>Интерфейс админки</b>\n\nАдмины: @Adres31, @AsterFerre, @Dmitriy_LD, @alex_mid1', reply_markup=kb.admmenu, parse_mode='HTML')



@dp.message_handler(commands=['kytak'])
async def start(message: types.Message):
	await message.answer('You is better')

#####################################################################################################################################################################################################################
@dp.message_handler(content_types=['text'], text='🛠 Настройки')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('🛠 Настройки аккаунта', reply_markup=kb.settings)

@dp.message_handler(content_types=['text'], text='00')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('🛠 Настройки аккаунта', reply_markup=kb.settings)
	await bot.send_video(message.chat.id, open('vidos.mp4', 'rb'))


@dp.message_handler(content_types=['text'], text='🔐 Кошелек')
async def with_hidden_link(message: types.Message, state: FSMContext):
	if message.chat.id == mindyrt:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>100 213 ABR (1 470,78 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakoc:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakike:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakber:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>1800 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')	
	
	elif message.chat.id == kytakdyrt:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakbish:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>600 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakalta:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakete:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytakcig:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytaktyg:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytak23:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>400 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == kytak006:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Вывели: <b>400 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')
	
	elif message.chat.id == mimi:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\n<b>Amber</b>\n\n💵 Баланс: <b>2 000 000 ABR (1 520 332 000,00 RUB)</b>\n⬇️Вывели: <b>400 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')





	else:
		await message.answer(f"{fmt.hide_link('https://i.gifer.com/3OGMy.gif')}🔐 Кошелек\n\nAmber\n\n💵 Баланс: <b>0 ABR (0 RUB)</b>\n⬇️Выводили:<b>0 ABR</b>", reply_markup=kb.wallet, parse_mode='HTML')

@dp.message_handler(content_types=['text'], text='💳 Купить Amber')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('Введите адрес кошелька Bep20 Trust Wallet или Metamask с которого будет производится оплата.', reply_markup=kb.butback, parse_mode='markdown')
	await st.buy.set()

@dp.message_handler(content_types=['text'], text='🚨 Airdrop')
async def handledr(message: types.Message, state: FSMContext):
	if message.chat.id == kytakber:
		await message.answer(f'''
*Эйрдроп (airdrop)* — это процедура раздачи токенов для стимуляции игрового процесса. Получить токены бесплатно можно несколькими способами. 

  1. Найти и собрать монеты разбросанные по миру с использованием  геолокации. 
  2. Побеждать в битвах с монстрами.
  3. Выполнять внутриигровые квесты. 
  4. Распространять приложение благодаря реферальной системе.

*Собрав токены на сумму от 20$ вы сможете вывести их на свой криптовалютный кошелёк..*


👥 Партнерская программа:

Ваша ссылка для приглашения:
https://t.me/AmberPandoraBot?start={message.chat.id}

💡 Кол-во рефералов: *0* чел.
📈 Ваш личный реферальный процент: *5%*

⚙️ Заработанная сумма: *0* AMBR

 *Получить бесплатные монеты можно в игре.*
 https://pandoragame.page.link/sBNRzLhh79MNmBpL9
		''',  parse_mode='markdown')

	else:
		await message.answer(f'''
*Эйрдроп (airdrop)* — это процедура раздачи токенов для стимуляции игрового процесса. Получить токены бесплатно можно несколькими способами. 

  1. Найти и собрать монеты разбросанные по миру с использованием  геолокации. 
  2. Побеждать в битвах с монстрами.
  3. Выполнять внутриигровые квесты. 
  4. Распространять приложение благодаря реферальной системе.

*Собрав токены на сумму от 20$ вы сможете вывести их на свой криптовалютный кошелёк..*


👥 Партнерская программа:

Ваша ссылка для приглашения:
https://t.me/AmberPandoraBot?start={message.chat.id}

💡 Кол-во рефералов: *0* чел.
📈 Ваш личный реферальный процент: *5%*

⚙️ Заработанная сумма: *0* AMBR

 *Получить бесплатные монеты можно в игре.*
 https://pandoragame.page.link/sBNRzLhh79MNmBpL9
		''',  parse_mode='markdown')

@dp.message_handler(content_types=['text'], text='🧑🏻‍💻 О проекте')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('''
*Amber* - внутриигровая валюта и движущая сила игровой экономики Pandora, представляет собой токен BEP-20 в сети Binance Smart Chain (BSC). Все внутриигровые действия, покупки и вознаграждения на торговой площадке используются и выплачиваются в токенах Amber. 

*Pandora* - это  MMORPG игра в дополненной и виртуальной реальности , основанная на блокчейне, в которой используются децентрализованные финансы и NFT, с целью представить блокчейн миллионам геймеров с помощью возможностей игры для заработка. С внедрением блокчейна и NFT игроки смогут владеть своими игровыми активами, покупать и продавать их, а также монетизировать их в увлекательных сражениях PvP, майнинге PvP и обучении PvE.

Более подробно смотрите тут  Pandoragame.org
		''', reply_markup=kb.seti, parse_mode='markdown')

@dp.message_handler(content_types=['text'], text='⏪ Меню')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('Меню', reply_markup=kb.butmenu)

#####################################################################################################################################################################################################################
@dp.message_handler(content_types=['text'], text='⏪ Назад')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('⏪ Назад', reply_markup=kb.menu)

@dp.message_handler(content_types=['text'], text='📋 Смарт контракт')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('Смарт контракт Amber')
	await message.answer('0xbb2f331703db8b9b693f8da19cf77d9f1f4a1b88')

@dp.message_handler(content_types=['text'], text='❓ Инструкция')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('''
Для того чтобы вывести монеты следуйте инструкции. 
1. Создайте кошелёк Trust wallet. 
2. Добавьте монету Amber в свой кошелёк. 
3. Как купить usdt используя биржу Binanse и вывести usdt в кошелёк Trust wallet.
''')
	await message.answer('''
<b>1.как создать кошелек TrustWallet</b>

Скачайте кошелёк и надёжно сохраните парольную фразу из 12 слов ( seed ).
  Потеряв seed фразу вы никогда не сможете восстановить доступ к кошельку! 
https://trustwallet.com/ru
		''', parse_mode='HTML')
	await bot.send_video(message.from_user.id, open('vidos.mp4', 'rb'), caption='''
<b>2. Как добавить монету Amber в кошелек</b>
			''', reply_markup=kb.butmenu, parse_mode='HTML')

@dp.message_handler(content_types=['text'], text='Отмена')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('⏪ Назад', reply_markup=kb.butmenu)

@dp.message_handler(content_types=['text'], text='💬 Рассылка')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('Введите текст для рассылки.\n\nДля отмены нажми блять на кнопку ниже', reply_markup=kb.back)
			await st.item.set()
		else:
			await message.answer('Введите текст для рассылки.', reply_markup=kb.back)
			await st.item.set()

@dp.message_handler(content_types=['text'], text='📡 Рассылка')
async def hangdler(message: types.Message, state: FSMContext):
		await message.answer('Введите текст для рассылки.', reply_markup=kb.csk)
		await st.botom.set()

@dp.message_handler(content_types=['text'])
async def h(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			pass
		else:
			await message.answer('Не знаю о чем вы?')
			await bot.send_message(admin, f"<b>Получен новый вопрос!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')

#####################################################################################################################################################################################################################
@dp.callback_query_handler(lambda call: True) # Inline часть
async def cmd_image(call, state: FSMContext):
	if 'ans' in call.data:
		a = call.data.index('-ans')
		ids = call.data[:a]
		await call.message.answer('Введите ответ:', reply_markup=kb.back)
		await st.item2.set() # админ отвечает пользователю
		await state.update_data(uid=ids)
	if 'bns' in call.data:
		a = call.data.index('-bns')
		ids = call.data[:a]
		await call.message.answer('Введите summy:', reply_markup=kb.back)
		await st.item6.set() # админ отвечает пользователю
		await state.update_data(uid=ids)
	elif 'ignor' in call.data:
		await call.answer('Удалено')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()
#####################################################################################################################################################################################################################
	elif 'alex_mid1' in call.data:
		await call.message.answer('👤 @alex_mid1\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'Techno_Web' in call.data:
		await call.message.answer('👤 @Techno_Web\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'webcoderpt' in call.data:
		await call.message.answer('👤 @webcoderpt\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'Adres31' in call.data:
		await call.message.answer('👤 @Adres31\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'AsterFerre' in call.data:
		await call.message.answer('👤 @AsterFerre\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'Dmitriy_LD' in call.data:
		await call.message.answer('👤 @Dmitriy_LD\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif '000' in call.data:
		await call.message.answer('👤 @\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'PROCoinPrivateSALE' in call.data:
		await call.message.answer('👤 @PROCoinPrivateSALE\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ZBOOM1' in call.data:
		await call.message.answer('👤 @ZBOOM1\n\n💸Баланас: 0 ABR\n\nБольше информации в файле INFO')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
#####################################################################################################################################################################################################################
	elif 'incruktion' in call.data:
		await call.message.answer('''
Для того чтобы вывести монеты 
Следуйте видеоинструкции. 
1.как создать кошелек TrustWallet
2. Как добавить монету Amber в кошелек. 
3. Как отправить ваш адрес для зачисления монет.
			''')
		await bot.send_video(id, open('vidos.mp4', 'rb'))
	elif 'get' in call.data:
		await call.message.answer('Вставте ваш адрес кошелька  Bep20', reply_markup=kb.butinc)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await st.kytak.set()
	elif 'refka' in call.data:
		if message.chat.id == kytakber:
			await call.message.answer(f'''
👥 Партнерская программа:

Ваша ссылка для приглашения:
https://t.me/AmberPandoraBot?start=

💡 Кол-во рефералов: <b>1 чел.</b> 
📈 Ваш личный реферальный процент: <b>5%</b>
⚙️ Заработанная сумма: <b>0 AMBR</b>
			''', parse_mode='HTML')
		else:
			await call.message.answer(f'''
👥 Партнерская программа:

Ваша ссылка для приглашения:
https://t.me/AmberPandoraBot?start=

💡 Кол-во рефералов: <b>0 чел.</b> 
📈 Ваш личный реферальный процент: <b>5%</b>
⚙️ Заработанная сумма: <b>0 AMBR</b>
			''', parse_mode='HTML')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()
	elif 'otmena' in call.data:
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()		
	elif 'netsred' in call.data:
		await call.message.answer('На вашем балансе недостаточно средств')
	elif 'pricemonet' in call.data:
		await call.message.answer('В данные момент 1 цент за монету\nЧтобы изменить цену отправьте мне стоимоcть')
		await bot.delete_message(call.message.chat.id, call.message.message_id)

	elif 'statiks' in call.data:
		await call.message.answer('''
👥 Пользователей в боте: 11

Внизу список пользователей:

			''', reply_markup=kb.polzi)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'popal' in call.data:
		await call.message.answer('''
Добро пожаловать в мир Pandora. Устанавливайте приложение. Получайте награду.

https://pandoragame.page.link/sBNRzLhh79MNmBpL9
			''')
		await bot.delete_message(call.message.chat.id, call.message.message_id)

		
#####################################################################################################################################################################################################################
	elif 'qqqqqqqqq' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *20 USDT Bep20*

Вы получите: *200 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'20 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'wwwwwwww' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *50 USDT Bep20*

Вы получите: *500 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'50 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'eeeeee' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *100 USDT Bep20*

Вы получите: *1000 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'100 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'rrrrrrrr' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *250 USDT Bep20*

Вы получите: *2500 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'250 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'tttttttt' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *500 USDT Bep20*

Вы получите: *5000 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'500 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'yyyyyy' in call.data:
		await call.message.answer('''
Подтверждение операции

Вы заплатите: *1000 USDT Bep20*

Вы получите: *10 000 ABR* 

*Переведите USDT Bep20 на указанный адрес*

			''', parse_mode='markdown')
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')

		await bot.send_message(admin, f'1000 USD')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'uuuuuuue' in call.data:
		await call.message.answer('Oтправьте в сообщении произвольную сумму покупки от 20 USDT до 1000 USDT', reply_markup=kb.butback)
		await st.summa.set()
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		#####################
	elif 'Bep20' in call.data:
		await call.message.answer('*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')
		await bot.send_message(admin, f'Bep20')
		#####################
	elif 'lllllllllll' in call.data:
		await call.message.answer('⏳ Пополнения баланса займёт 25-30 сек')
		await bot.send_message(admin, f'Оплатил он!')
#####################################################################################################################################################################################################################
@dp.message_handler(state=st.summa)
async def h(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			pass
		elif message.text == 'Отмена':
			await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.butmenu)
			await state.finish()
		else:
			await message.answer('⏳Обработка ващего запроса...', reply_markup=kb.butmenu)
			await bot.send_message(admin, f"<b>Summa!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text} USDT", reply_markup=kb.fan(message.chat.id), parse_mode='HTML')
			await state.finish()


@dp.message_handler(state=st.buy)
async def h(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			pass
		elif message.text == 'Отмена':
			await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.butmenu)
			await state.finish()
		else:
			await message.answer('Выберите или укажите произвольную сумму покупки', reply_markup=kb.summa)
			await bot.send_message(admin, f"<b>Wallet!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')
			await state.finish()


@dp.message_handler(state=st.kytak)
async def proc(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.butmenu)
		await state.finish()
	elif message.text == '❓ Инструкция по выводу':
		await bot.send_video(message.from_user.id, open('vidos.mp4', 'rb'), caption='''
Для того чтобы вывести монеты 
Следуйте видеоинструкции. 
1.как создать кошелек TrustWallet
2. Как добавить монету Amber в кошелек. 
3. Как отправить ваш адрес для зачисления монет.
			''', reply_markup=kb.butmenu)
		await state.finish()

	else:
		await message.answer(f'Монеты AMB будут зачислены в течении 1 минуты!', reply_markup=kb.butmenu)
		await bot.send_message(admin, f"<b>Вставте ваш адрес кошелька</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')
		await state.finish()



@dp.message_handler(state=st.item2)
async def proc(message: types.Message, state: FSMContext):
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		await message.answer('Сообщение отправлено.', reply_markup=kb.menu)
		data = await state.get_data()
		id = data.get("uid")
		await state.finish()
		await bot.send_message(id, '{} ...'.format(message.text))

@dp.message_handler(state=st.item6)
async def proc(message: types.Message, state: FSMContext):
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		await message.answer('Сообщение отправлено.', reply_markup=kb.menu)
		data = await state.get_data()
		id = data.get("uid")
		await state.finish()
		await bot.send_message(id, '{} '.format(message.text))
		await bot.send_message(id,'*0x3Ee5658006f4A861FE4C7d36141fC4235739b923*', reply_markup=kb.pay, parse_mode='markdown')


@dp.message_handler(state=st.item)
async def process_name(message: types.Message, state: FSMContext):
	q.execute(f'SELECT user_id FROM users')
	row = q.fetchall()
	connection.commit()
	text = message.text
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		info = row
		await message.answer('Рассылка начата!', reply_markup=kb.menu)
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], str(text), reply_markup=kb.butmenu)
			except:
				pass
		await message.answer('Рассылка завершена!', reply_markup=kb.menu)
		await state.finish()

@dp.message_handler(state=st.botom)
async def process_name(message: types.Message, state: FSMContext):
	q.execute(f'SELECT user_id FROM users')
	row = q.fetchall()
	connection.commit()
	text = message.text
	if message.text == '↪️ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.admmenu)
		await state.finish()
	else:
		info = row
		await message.answer('Рассылка начата!', reply_markup=kb.admmenu)
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], str(text))
			except:
				pass
		await message.answer('Рассылка завершена!', reply_markup=kb.admmenu)
		await state.finish()


@dp.message_handler(state=st.walamber)
async def h(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			pass
		else:
			await message.answer('⏳Обработка ващего запроса...\nЖдите и не выходите из меню админки, иначе все сброситься!', reply_markup=kb.admmenu)
			await bot.send_message(admin, f"<b>Wallet sid!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')
			await state.finish()


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)