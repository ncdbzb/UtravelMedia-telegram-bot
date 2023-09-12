import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


words = ['Демидовский завод',
         'Тургояк',
         'Уральский марс',
         'Полярный круг( 66 параллель )',
         'Аркаим']

answers = ['Демидовский завод - Вы сильны духом! Вашей решительности и трудолюбию нет равных. Если бы можно было снова изобрести пароход, вы бы это обязательно сделали. Для вас не существует преград и ваши амбиции безграничны!',
           'Тургояк - Вы глубокий и уравновешенный человек. Выходить сухими из воды - это ваше кредо. Горизонты ваших талантов и амбиции по-настоящему безкрайние',
           'Уральский Марс - Со стороны может показаться, что вы не с этой планеты. Ваша креативность и находчивость поражают! Порой ваша фантазия уносит вас в другие края и гравитация вас не может удержать',
           'Полярный круг - Вы можете показаться холодным и закрытым человеком, но на самом деле в вашем сердце живёт тепло и любовь, которая подобно северному сиянию освещает все вокруг',
           'Аркаим - Окружающим кажется, что в вас заключена мудрость столетий, и они не ошибаются. Вы - настоящий колодец знаний и умений. Доверьтесь своей интуиции, она вас не подведёт!']

count = [0, 0, 0, 0, 0]

startMarkup = types.InlineKeyboardMarkup(row_width=1)
startButton = types.InlineKeyboardButton(text='Начать', callback_data='startBtn')

startMarkup.add(startButton)


q1Markup = types.InlineKeyboardMarkup(row_width=1)
q1v1Btn = types.InlineKeyboardButton(text='Уверенный и внимательный', callback_data='1Демидовский завод')
q1v2Btn = types.InlineKeyboardButton(text='Спокойный и уравновешенный', callback_data='1Тургояк')
q1v3Btn = types.InlineKeyboardButton(text='Озорной и оригинальный', callback_data='1Уральский марс')
q1v4Btn = types.InlineKeyboardButton(text='Холодный и отстранённым', callback_data='1Полярный круг( 66 параллель )')
q1v5Btn = types.InlineKeyboardButton(text='Мудрый и загадочный', callback_data='1Аркаим')

q1Markup.add(q1v1Btn, q1v2Btn, q1v3Btn, q1v4Btn, q1v5Btn)


q2Markup = types.InlineKeyboardMarkup(row_width=1)
q2v1Btn = types.InlineKeyboardButton(text='Я плыву по течению', callback_data='2Тургояк')
q2v2Btn = types.InlineKeyboardButton(text='Я все беру под свой контроль', callback_data='2Демидовский завод')
q2v3Btn = types.InlineKeyboardButton(text='Жду пока ответ придет из космоса', callback_data='2Уральский марс')
q2v4Btn = types.InlineKeyboardButton(text='Мне все равно', callback_data='2Полярный круг( 66 параллель )')
q2v5Btn = types.InlineKeyboardButton(text='Мне помогает мудрость предков', callback_data='2Аркаим')

q2Markup.add(q2v1Btn, q2v2Btn, q2v3Btn, q2v4Btn, q2v5Btn)

q31m = types.InlineKeyboardMarkup(row_width=1)
q3v1 = types.InlineKeyboardButton(text='СпанчБоб', callback_data='3Тургояк')
q3v2 = types.InlineKeyboardButton(text='Звёздные воины', callback_data='3Уральский марс')
q3v3 = types.InlineKeyboardButton(text='Холодное сердце', callback_data='3Полярный круг( 66 параллель )')
q3v4 = types.InlineKeyboardButton(text='Властелин колец', callback_data='3Аркаим')
q3v5 = types.InlineKeyboardButton(text='Девчата', callback_data='3Демидовский завод')
q31m.add(q3v1, q3v2, q3v3, q3v4, q3v5)

q4Markup = types.InlineKeyboardMarkup(row_width=1)
q4v1Btn = types.InlineKeyboardButton(text='Выбрался на шашлыки с друзьями', callback_data='4Тургояк')
q4v2Btn = types.InlineKeyboardButton(text='Пошел на экскурсию', callback_data='4Демидовский завод')
q4v3Btn = types.InlineKeyboardButton(text='Полетел в космос', callback_data='4Уральский марс')
q4v4Btn = types.InlineKeyboardButton(text='Не выходил из дома', callback_data='4Полярный круг( 66 параллель )')
q4v5Btn = types.InlineKeyboardButton(text='Пошел в экскурсию на раскопки', callback_data='4Аркаим')

q4Markup.add(q4v1Btn, q4v2Btn, q4v3Btn, q4v4Btn, q4v5Btn)

q5Markup = types.InlineKeyboardMarkup(row_width=1)
q5v1Btn = types.InlineKeyboardButton(text='В Атлантиду', callback_data='5Тургояк')
q5v2Btn = types.InlineKeyboardButton(text='Отправился в Царскую Россию', callback_data='5Демидовский завод')
q5v3Btn = types.InlineKeyboardButton(text='Отправился в 2600 год и полетел на выходные на Марс', callback_data='5Уральский марс')
q5v4Btn = types.InlineKeyboardButton(text='Ледниковый период', callback_data='5Полярный круг( 66 параллель )')
q5v5Btn = types.InlineKeyboardButton(text='Древний Египет', callback_data='5Аркаим')

q5Markup.add(q5v1Btn, q5v2Btn, q5v3Btn, q5v4Btn, q5v5Btn)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я тестовый бот для задания от команды Utravel media и 4 канала 😊\n"
                         "Тест: <b>Какая ты Уральская достопримечательность?</b>", parse_mode='html',
                         reply_markup=startMarkup)


@dp.message_handler()
async def send_error(message: types.Message):
    await message.reply('Такой команды нету, напишите /start для перезапуска')


@dp.callback_query_handler(text='startBtn')
async def start(message: types.Message):
    with open('media/que1.jpg', 'rb') as q1:
        await bot.send_photo(message.from_user.id, q1)
    await bot.send_message(message.from_user.id, "В обществе я позиционирую себя как:", reply_markup=q1Markup)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('1'))
async def analyze(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    count[words.index(code)] += 1

    with open('media/que2.jpg', 'rb') as q2:
        await bot.send_photo(callback_query.from_user.id, q2)
    await bot.send_message(callback_query.from_user.id, "При решений проблем я чаще всего занимаю такую позицию:",
                           reply_markup=q2Markup)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('2'))
async def analyze2(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    count[words.index(code)] += 1

    await bot.send_message(callback_query.from_user.id, "С какими фильмами ты себя асcоциируешь?")
    with open('media/spangebob.jpg', 'rb') as q31:
        await bot.send_photo(callback_query.from_user.id, q31, reply_markup=q31m)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('3'))
async def analyze2(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    count[words.index(code)] += 1

    with open('media/que4.jpg', 'rb') as q4:
        await bot.send_photo(callback_query.from_user.id, q4)
    await bot.send_message(callback_query.from_user.id, "В свой идеальный выходной я бы…", reply_markup=q4Markup)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('4'))
async def analyze2(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    count[words.index(code)] += 1

    with open('media/que5.jpg', 'rb') as q5:
        await bot.send_photo(callback_query.from_user.id, q5)
    await bot.send_message(callback_query.from_user.id, "Если бы у меня была машина времени, я бы отправился…",
                           reply_markup=q5Markup)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('5'))
async def analyze2(callback_query: types.CallbackQuery):
    code = callback_query.data[1:]
    count[words.index(code)] += 1

    index = count.index(max(count))

    if index == 0:
        with open('media/demidov.jpg', 'rb') as a1:
            await bot.send_photo(callback_query.from_user.id, a1)
    elif index == 1:
        with open('media/turgoyak.jpg', 'rb') as a2:
            await bot.send_photo(callback_query.from_user.id, a2)
    elif index == 2:
        with open('media/mars.jpg', 'rb') as a3:
            await bot.send_photo(callback_query.from_user.id, a3)
    elif index == 3:
        with open('media/pol.jpg', 'rb') as a4:
            await bot.send_photo(callback_query.from_user.id, a4)
    elif index == 4:
        with open('media/arkaim.jpg', 'rb') as a5:
            await bot.send_photo(callback_query.from_user.id, a5)
    await bot.send_message(callback_query.from_user.id, answers[index])
    for i in range(len(count)):
        count[i] = 0


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)