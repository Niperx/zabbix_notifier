import logging
import time
from aiogram.utils.exceptions import BotBlocked
from aiogram import Bot, Dispatcher, executor, types

import parser_module as pars
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
         'Новые Функции - Стата за день по звонкам,кабельтест (проблема с впн),допрос по времени тех кто взял прозвон',
         '']

# ПОЛЕТЕЛИ!
print("Бот запущен. Нажмите Ctrl+C для завершения")

# Функции
def get_keyboard(addr):
    buttons = []
    for i in range(1, 10):
        buttons.append(types.InlineKeyboardButton(text=str(addr[i]), callback_data=int(i)))
    keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

# Запуск
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def cmd_test1(message: types.Message):
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
        for i in todoo:
            await message.answer(i)
    elif message.text == "Прозвон":
        start_time = time.time()
        print('Start time')
        if message.from_user.id in id_access:
            global addr
            print('Начал Парс ' + "--- %s seconds ---" % (time.time() - start_time))
            await message.answer('Взлом пентагона, погодите')
            addr = pars.main()
            print('Запарсили ' + "--- %s seconds ---" % (time.time() - start_time))  # `10 СЕКУНД ???
            await message.reply('Каво?', reply_markup=get_keyboard(addr))

            # print("--- %s seconds ---" % (time.time() - start_time))
            print(message.chat.username + ' Нажал на прозвон')


@dp.callback_query_handler()
async def callbacks_num(call):
    global addresss
    if call.data == 'zabral':
        # print (call.from_user.username)
        await call.message.edit_text('❗️' + addresss + '❗️ Прозвоните по свету и ТВ Позязя ')
        await call.message.answer('@' + str(call.from_user.username) + ' Забрал(а) прозвон  - Спасибо больше ! ')
    else:
        await call.message.edit_text(text='☀' + str(addr[
                                                        int(call.data)]) + ' - Улетело на прозвон !☀')  # ))chat_id=call.message.chat.id, message_id=call.message.message_id  ,
        buttons = []
        buttons.append(types.InlineKeyboardButton(text='Я Заберу ', callback_data='zabral'))
        yakeyboard = types.InlineKeyboardMarkup(row_width=1)
        yakeyboard.add(*buttons)
        addresss = str(addr[int(call.data)])
        await bot.send_message(-747200418, '❗️' + addresss + '❗️ Прозвоните по свету и ТВ Позязя ',
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


# @dp.message_handler(commands="block")
# async def cmd_block(message: types.Message):
#     await time.sleep(10.0)  # Здоровый сон на 10 секунд
#     await message.reply("Вы заблокированы")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
'''

# https://docs.st65.ru/dosearchsite.action?cql=siteSearch+~+%22%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+%22&queryString=%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+
# Чат айди мэйн группы -787891312

# Разница между answer и reply простая: первый метод просто отправляет сообщение в тот же чат, второй делает "ответ" на сообщение из message:
# Для ответа в опреденный чат
#@dp.message_handler(commands="dice")

#async def cmd_dice(message: types.Message):
#    await message.bot.send_dice(-100123456789, emoji="🎲")

'''