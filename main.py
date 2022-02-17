import logging
import json
from aiogram.utils.exceptions import BotBlocked
from aiogram import Bot, Dispatcher, executor, types, asyncio

# import parser_module as pars
from config import TOKEN


#ops
id_access = [388850647, 252457864, 102749042, 674126672, 190112213]
#               Я       Кирилл     Водопьянов   Толя
cmds = ['Прозвон', 'Кабельтест', 'todo']

addr = []
addresss = ' '

todoo = ['Оптимизация парсинга', 'Решаем с глобальными переменками',
         'Добавить всех старших', 'Оптимизация работы в автономном режиме',
         'Залить на бэкап', 'Оптимизация кнопок', 'Система обработки',
         'Новые Функции - Стата за день по звонкам,кабельтест (проблема с впн),допрос по времени тех кто взял прозвон']

# ПОЛЕТЕЛИ!
print("Бот запущен. Нажмите Ctrl+C для завершения")

# Функции
def get_keyboard(addr):
    buttons = []
    for i in range(10):
        buttons.append(types.InlineKeyboardButton(text=str(addr[i]), callback_data=int(i)))
    keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

# Запуск
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    for i in cmds:
        keyboard.add(types.KeyboardButton(text=i))
    print(message.chat.id)
    await message.answer('Привет!, Че мутим?) ', reply_markup=keyboard)


@dp.message_handler()
async def get_message(message: types.Message):
    print(str(message.from_user.id) + ' Написал ' + message.text)
    if message.text == "Пиу Пиу":
        await message.answer('Ты что, Кабельтест? ')
    elif message.text == "Кабельтест":
        await message.answer('Пиу Пиу')
    elif message.text == "todo":
        text = ''
        for n, i in enumerate(todoo, start=1):
            text += str(n) + '. ' + i + '\n\n'
        await message.answer(text)
    elif message.text == "Прозвон":
        if message.from_user.id in id_access:
            global addr
            await message.answer('Взлом жопы, погодите')
            with open("info.json", 'r', encoding='utf-8') as read_info:
                result = json.load(read_info)
            addr = result
            await message.answer('Каво?', reply_markup=get_keyboard(addr))

            # print("--- %s seconds ---" % (time.time() - start_time))
            print(message.chat.username + ' Нажал на прозвон')


@dp.callback_query_handler()
async def callbacks_num(call):
    global address
    if call.data == 'zabral':
        # print (call.from_user.username)
        await call.message.edit_text('❗️' + address + '❗️ Прозвоните по свету и ТВ Позязя ')
        await call.message.answer('@' + str(call.from_user.username) + ' Забрал(а) прозвон  - Спасибо большое ! ')
    else:
        await call.message.edit_text(text='☀' + str(addr[int(call.data)]) + ' - Улетело на прозвон !☀')  # ))chat_id=call.message.chat.id, message_id=call.message.message_id  ,
        buttons = []
        buttons.append(types.InlineKeyboardButton(text='Я Заберу ', callback_data='zabral'))
        yakeyboard = types.InlineKeyboardMarkup(row_width=1)
        yakeyboard.add(*buttons)
        address = str(addr[int(call.data)])
        await bot.send_message(-747200418, '❗️' + address + '❗️ Прозвоните по свету и ТВ Позязя ',
                               reply_markup=yakeyboard)

'''
  requests.get('https://api.telegram.org/bot{}/sendMessage'.format(tokenbot), params=dict(
  chat_id='-747200418',
  text='❗️' +  str(addr[int(call.data)]) + '❗️ Прозвоните по свету и ТВ Позязя '))
'''


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True

@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

'''

# https://docs.st65.ru/dosearchsite.action?cql=siteSearch+~+%22%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+%22&queryString=%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+
# Чат айди мэйн группы -787891312

'''