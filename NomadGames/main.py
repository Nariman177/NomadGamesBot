import telebot
from telebot import types
from parser import parse_timer
from ruparser import ruparse_timer
from engparser import engparse_timer
bot = telebot.TeleBot('6671788475:AAEqkDmRuPtvOcsUelBWIjl-b3Z6TcWovX8')
group_chat_id = '-1002203257219'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Kaz")
    item2 = types.KeyboardButton("Rus")
    item4 = types.KeyboardButton('Eng')
    markup.add(item1, item2, item4)
    bot.send_message(message.chat.id, f"Қош келдіңіз! Бастамас бұрын өзіңізге ыңғайлы тілді таңдауыңызды сұраймын.\n"
                                      f"\nДобро пожаловать для дальнейшего продолжения выберите какой язык предпочитаете\n"
                                      f"\nWelcome dear before we get started you need to chose language which you are prefer"
                                      ,reply_markup=markup)

@bot.message_handler(content_types=['text', 'photo', 'video'])
def main(message):
        if message.text == 'Rus':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Информация")
            item2 = types.KeyboardButton("Обьекты игр")
            item5 = types.KeyboardButton('Обратная связь')
            item6 = types.KeyboardButton('Выбрать другой язык')
            item7 = types.KeyboardButton('сколько времени осталось до старта игр')
            markup.add(item1, item2, item5, item6, item7)
            photo = open('ru-logo_human1.png', 'rb')
            bot.send_photo(message.chat.id, photo, f"Добро пожаловать, <b>{message.from_user.first_name}</b>\n ",
                           parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "Какими услугами мы можем вам помочь?", reply_markup=markup)

        if message.text == 'Обратная связь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да")
            item2 = types.KeyboardButton("нет в меню")
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Instagram - volunteer_nomadgameskz',
                                              url="https://www.instagram.com/volunteer_nomadgameskz?igsh=MXdxb3c1c29qdndudg==")
            btn2 = types.InlineKeyboardButton('2)Instagram - worldnomadgames2024',
                                              url="https://www.instagram.com/worldnomadgames2024?igsh=MWZsbjgzN2F5aDN1cg==")
            btn3 = types.InlineKeyboardButton('Facebook', url="https://www.facebook.com/worldnomadgames2024")
            btn.add(btn1, btn2, btn3)
            markup.add(item1, item2)

            msg = bot.send_message(message.chat.id,"Если вы хотите оставить сообщение или написать отзыв про бота, "
                                                   "то можете прямо тут нам написать", reply_markup=btn)
            bot.register_next_step_handler(msg,  handle_review)


        elif message.text == 'Да':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да")
            item2 = types.KeyboardButton("нет в меню")
            markup.add(item1, item2)
            msg = bot.send_message(message.chat.id, "Хорошо вы можете продолжить")
            bot.register_next_step_handler(msg, handle_review)
            # bot.send_message(message.chat.id, "хотите еще написать?", reply_markup=markup)

        if message.text == 'нет в меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Информация")
            item2 = types.KeyboardButton("Обьекты игр")
            item5 = types.KeyboardButton('Обратная связь')
            item6 = types.KeyboardButton('Выбрать другой язык')
            item7 = types.KeyboardButton('сколько времени осталось до старта игр')
            markup.add(item1, item2, item5, item6, item7)
            bot.send_message(message.chat.id, "Чем еще мы можем вам помочь?", reply_markup=markup)

        if message.text == 'Обьекты игр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardMarkup()
            item1 = types.KeyboardButton("Информация")
            item2 = types.KeyboardButton("Обьекты игр")
            item5 = types.KeyboardButton('Обратная связь')
            item6 = types.KeyboardButton('Выбрать другой язык')
            item7 = types.KeyboardButton('сколько времени осталось до старта игр')
            btn1.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70000001037972503"))
            btn2.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70000001018102444"))
            btn3.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70000001018088349"))
            btn4.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70000001018608940"))
            btn5.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70000001044480178"))
            btn6.add(types.InlineKeyboardButton("адрес", url="https://2gis.kz/astana/geo/70030076129741434"))

            markup.add(item1, item2, item5, item6, item7)

            bot.send_message(message.chat.id, "тут будут предоставлены все наши обьекты с ссылками на их адреса ",
                             reply_markup=markup)

            bot.send_message(message.chat.id, "ДВОРЕЦ ЕДИНОБОРСТВ ИМЕНИ ЖАКСЫЛЫКА УШКЕМПИРОВА\n"
                                              "Количество зрительских мест - 5 000\n"
                                              "Проводимые мероприятия: "
                                              "1)Қазақ күресі\n2)Алыш", reply_markup=btn1)

            bot.send_message(message.chat.id, "ЛЕДОВЫЙ ДВОРЕЦ «АЛАУ»\n"
                                              "Зрительских мест – 7 462\n"
                                              "Проводимые мероприятия: ГЛАВНАЯ АРЕНА, ЮЖНАЯ ЧАСТЬ БЕГОВОЙ ДОРОЖКИ:"
                                              "1)Ссирым\n2)Кураш\n3)Ашыртмалы аба гюреши - Арқан тартыс\n"
                                              "Проводимые мероприятия: ГЛАВНАЯ АРЕНА, СЕВЕРО- ЗАПАДНАЯ ЧАСТЬ БЕГОВОЙ ДОРОЖКИ:"
                                              "1)Асық ату\n2)Ордо\n"
                                              "Проводимые мероприятия: ГЛАВНАЯ АРЕНА, СЕВЕРО-ВОСТОЧНАЯ ЧАСТЬ БЕГОВОЙ ДОРОЖКИ"
                                              "1)Мас-рестлинг\n"
                                              "Проводимые мероприятия: ИГРОВОЙ ЗАЛ, ЗАПАДНАЯ БАШНЯ\n"
                                              "Тренировки по видам борьбы", reply_markup=btn2)

            bot.send_message(message.chat.id, "ГОСТИНИЦА «ДУМАН»\n"
                                              "Проводимые мероприятия: ГОСТИНИЦА «ДУМАН», КОНФЕРЕНЦ-ЗАЛ «ПАРЛАМЕНТ»"
                                              "\n1)Тоғызқұмалақ - Мангала\n2) Овари", reply_markup=btn3)

            bot.send_message(message.chat.id, "ИППОДРОМ «КАЗАНАТ» (КСОК «АРҒЫМАҚ», ЭТНОАУЛ)\n"
                                              "\nКоличество зрительских мест - 10 000 "
                                              "Длина скаковой дорожки – 1800 м"
                                              "\nПроводимые мероприятия: ИППОДРОМ «КАЗАНАТ»\n"
                                              "\n1)Гладкие скачки 1600м\n"
                                              "2)Гладкие скачки 2400м\n"
                                              "3)Гладкие скачки 3200м\n"
                                              "4)Жорға 9000м\n"
                                              "5)Құнан бәйге 11000м\n"
                                              "6)Топ бәйге 18000м\n"
                                              "7)Аламан бәйге 25000м\n"
                                              "8)Көкпар\n"
                                              "9)Торжественная церемония закрытия ВИК Астана 2024\n"
                                              "\nПроводимые мероприятия: ЭТНОАУЛ\n"
                                              "1)Состязания по национальным видам охота с птицами\n"
                                              "2)Аударыспақ\n"
                                              "3)Теңге ілу\n"
                                              "4)Жамбы ату\n"
                                              "\nПроводимые мероприятия: КСОК «АРҒЫМАҚ»\n"
                                              "\nДәстүрлі садақ ату", reply_markup=btn6)

            bot.send_message(message.chat.id, "НАЦИОНАЛЬНЫЙ МУЗЕЙ РК\n", reply_markup=btn4)

            bot.send_message(message.chat.id, "ЛЕГКОАТЛЕТИЧЕСКИЙ СПОРТИВНЫЙ КОМПЛЕКС «КАЗАХСТАН»\n", reply_markup=btn5)

            bot.send_message(message.chat.id, "чем еще можем помочь?", reply_markup=markup)

        if message.text == 'сколько времени осталось до старта игр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Информация")
            item2 = types.KeyboardButton("Обьекты игр")
            item5 = types.KeyboardButton('Обратная связь')
            item6 = types.KeyboardButton('Выбрать другой язык')
            item7 = types.KeyboardButton('сколько времени осталось до старта игр')
            markup.add(item1, item2, item5, item6, item7)

            wait_message = bot.send_message(message.chat.id, "Подождите это может занять 10-20 секунд...")

            timer_info = ruparse_timer()

            bot.delete_message(chat_id=message.chat.id, message_id=wait_message.message_id)

            bot.send_message(message.chat.id, f"{timer_info}",
                             parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "чем еще можем помочь?", reply_markup=markup)

        if message.text == 'Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Информация")
            item2 = types.KeyboardButton("Обьекты игр")
            item5 = types.KeyboardButton('Обратная связь')
            item6 = types.KeyboardButton('Выбрать другой язык')
            item7 = types.KeyboardButton('сколько времени осталось до старта игр')
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Об играх', callback_data='ob igrax')
            btn2 = types.InlineKeyboardButton('История игр', callback_data='istorya')
            btn3 = types.InlineKeyboardButton('Дата начало', callback_data='data')
            btn4 = types.InlineKeyboardButton('спорт программа', callback_data='sport')
            btn5 = types.InlineKeyboardButton('цели и задачи', callback_data='celly')
            btn6 = types.InlineKeyboardButton('билеты', callback_data='cilet')
            btn7 = types.InlineKeyboardButton('скидки', callback_data='skidky')
            markup.add(item1, item2, item5, item6, item7)
            btn.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(message.chat.id, "Какую информацию вам предоставить?", reply_markup=btn)
            bot.send_message(message.chat.id, "или можем выбрать другие функций", reply_markup=markup)

        if message.text == 'Выбрать другой язык':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Kaz")
            item2 = types.KeyboardButton("Rus")
            item4 = types.KeyboardButton('Eng')
            markup.add(item1, item2, item4)
            bot.send_message(message.chat.id,
                             f"для дальнейшего продолжения выберите какой язык предпочитаете\n", reply_markup=markup)


        if message.text == 'Kaz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Ақпарат")
            item2 = types.KeyboardButton("Ойын обьектілері")
            # item4 = types.KeyboardButton('Отделы')
            item5 = types.KeyboardButton('Кері байланыс')
            item7 = types.KeyboardButton('басталуына Қанша уақыт қалды')
            item6 = types.KeyboardButton('Тілді таңдауға қайту')
            markup.add(item1, item2, item5, item6, item7)
            photo = open('kaz-logo_abylay.png', 'rb')
            bot.send_photo(message.chat.id, photo,
                           f" Астана қаласында өтетін NomadGames ботына қош келдініз!! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\n",
                           parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "қандай қызметпен көмектесе аламыз?", reply_markup=markup)

        if message.text == 'Ойын обьектілері':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardMarkup()
            item1 = types.KeyboardButton("Ақпарат")
            item2 = types.KeyboardButton("Ойын обьектілері")
            # item4 = types.KeyboardButton('Отделы')
            item5 = types.KeyboardButton('Кері байланыс')
            item7 = types.KeyboardButton('басталуына Қанша уақыт қалды')
            item6 = types.KeyboardButton('Тілді таңдауға қайту')
            btn1.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70000001037972503"))
            btn2.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70000001018102444"))
            btn3.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70000001018088349"))
            btn4.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70000001018608940"))
            btn5.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70000001044480178"))
            btn6.add(types.InlineKeyboardButton("мекен-жайы", url="https://2gis.kz/astana/geo/70030076129741434"))

            markup.add(item1, item2, item5, item6, item7)

            bot.send_message(message.chat.id, "мұнда біздің барлық ойын обьектілері мен олардың орналасқан жердегі сілтемелер көрсетіледі",
                             reply_markup=markup)

            bot.send_message(message.chat.id, "Жақсылық Үшкемпіров атындағы жекпе-жек сарайы\n"
                                              "\nКөрермендер орнының саны - 5 000\n"
                                              "Өткізілетін іс-шаралар\n"
                                              "1)Қазақ күресі\n2)Алыш", reply_markup=btn1)

            bot.send_message(message.chat.id, "«АЛАУ» мұз айдыны\n"
                                              "\nКөрермендер орнының саны – 7 462\n"
                                              "Өткізілетін іс-шаралар: «Алау» МС, басты арена, жарыс жолының оңтүстік жақ бөлігі\n"
                                              "1)Ссирым,\n2)Кураш,\n3)Ашыртмалы аба гюреши - Арқан тартыс\n"
                                              "\nӨткізілетін іс-шаралар: «Алау» МС, басты арена, жарыс жолының батыс жақ бөлігі\n"
                                              "1)Асық ату,\n2)Ордо\n"
                                              "\nӨткізілетін іс-шаралар: «Алау» МС, басты арена, жарыс жолының шығыс жақ бөлігі\n"
                                              "1)Мас-рестлинг\n"
                                              "\nӨткізілетін іс-шаралар: «Алау» МС ойын залы, батыс жақ мұнара\n"
                                              "Күрес түрлері бойынша жаттығу", reply_markup=btn2)

            bot.send_message(message.chat.id, "«Думан» қонақ үйі\n"
                                              "Өткізілетін іс-шаралар: «Думан» қонақ үйі, КОНФЕРЕНЦ-ЗАЛ «ПАРЛАМЕНТ»"
                                              "\n1)Тоғызқұмалақ - Мангала,\n2) Овари", reply_markup=btn3)

            bot.send_message(message.chat.id, "«ҚАЗАНАТ» ипподромы («АРҒЫМАҚ» АССК, Этноауылы)\n"
                                              "\nКөрермендер орнының саны - 10 000 "
                                              "Жарыс жолының ұзындығы 1800 метр"
                                              "\nӨткізілетін іс-шаралар:«қазанат» ипподромы\n"
                                              "1)Ұшқыр бәйге 1600 м\n"
                                              "2)Ұшқыр бәйге 2400 м\n"
                                              "3)Ұшқыр бәйге 3200 м\n"
                                              "4)Жорға 9000м\n"
                                              "5)Құнан бәйге 11000м\n"
                                              "6)Топ бәйге 18000м\n"
                                              "7)Аламан бәйге 25000м\n"
                                              "8)Көкпар\n"
                                              "9)Астана 2024 ДКО салтанатты жабылу рәсімі\n"
                                              "\nӨткізілетін іс-шаралар: ЭТНОАУЛ\n"
                                              "1)Құс салу ұлттық түрлері бойынша сайыстар\n"
                                              "2)Аударыспақ\n"
                                              "3)Теңге ілу\n"
                                              "4)Жамбы ату\n"
                                              "\n«АРҒЫМАҚ» АССК: Өткізілетін іс-шаралар: Дәстүрлі садақ ату\n", reply_markup=btn6)

            bot.send_message(message.chat.id, "ҚР ұлттық музейі\n", reply_markup=btn4)

            bot.send_message(message.chat.id, "«QAZAQSTAN» жеңіл атлетика спорт кешені\n", reply_markup=btn5)

            bot.send_message(message.chat.id, "тағыда немен көмектесе аламыз??", reply_markup=markup)

        if message.text == 'басталуына Қанша уақыт қалды':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Ақпарат")
            item2 = types.KeyboardButton("Ойын обьектілері")
            # item4 = types.KeyboardButton('Отделы')
            item5 = types.KeyboardButton('Кері байланыс')
            item7 = types.KeyboardButton('басталуына Қанша уақыт қалды')
            item6 = types.KeyboardButton('Тілді таңдауға қайту')
            markup.add(item1, item2, item5, item6, item7)

            wait_message = bot.send_message(message.chat.id, "Күте тұрыңызшы, 10-20 секундтан кейін пайда болады...")

            timer_info = parse_timer()

            bot.delete_message(chat_id=message.chat.id, message_id=wait_message.message_id)

            bot.send_message(message.chat.id, f"{timer_info} қалды", parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "енді немен көмектесе аламыз?", reply_markup=markup)

        if message.text == 'Тілді таңдауға қайту':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Kaz")
            item2 = types.KeyboardButton("Rus")
            item4 = types.KeyboardButton('Eng')
            markup.add(item1, item2, item4)
            bot.send_message(message.chat.id,
                             f"өзіңізге ыңғайлы тілді таңдауыңызды сұраймын.\n" ,reply_markup=markup)

        if message.text == 'Ақпарат':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Ақпарат")
            item2 = types.KeyboardButton("Ойын обьектілері")
            # item4 = types.KeyboardButton('Отделы')
            item5 = types.KeyboardButton('Кері байланыс')
            item7 = types.KeyboardButton('басталуына Қанша уақыт қалды')
            item6 = types.KeyboardButton('Тілді таңдауға қайту')
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Ойын туралы', callback_data='turaly')
            btn2 = types.InlineKeyboardButton('Ойын тарихы', callback_data='tarix')
            btn3 = types.InlineKeyboardButton('Өткізілу күндері', callback_data='kunder')
            btn4 = types.InlineKeyboardButton('Мақсаттары', callback_data='maksat')
            btn5 = types.InlineKeyboardButton('Жеңілдіктер', callback_data='zhenildik' )
            btn6 = types.InlineKeyboardButton('Билеттер', callback_data='bylet')
            btn7 = types.InlineKeyboardButton('Спорт бағдарламасы', callback_data='bagdar')
            markup.add(item1, item2, item5, item6, item7)
            btn.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(message.chat.id, "Қандай ақапаратпен сізге бөлісейін?", reply_markup=btn)
            bot.send_message(message.chat.id, "немесе , басқа мәзірлерді тандай берсеніз болады", reply_markup=markup)

        if message.text == 'Кері байланыс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("иә")
            item2 = types.KeyboardButton("жоқ мәзірге оралайық")
            # item4 = types.KeyboardButton('Отделы')

            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Instagram - volunteer_nomadgameskz',
                                              url="https://www.instagram.com/volunteer_nomadgameskz?igsh=MXdxb3c1c29qdndudg==")
            btn2 = types.InlineKeyboardButton('Instagram - worldnomadgames2024',
                                              url="https://www.instagram.com/worldnomadgames2024?igsh=MWZsbjgzN2F5aDN1cg==")
            btn3 = types.InlineKeyboardButton('Facebook', url="https://www.facebook.com/worldnomadgames2024")
            btn.add(btn1, btn2, btn3)
            markup.add(item1, item2)

            msg = bot.send_message(message.chat.id, "төменде барлық кері байланыс сілтемелері берілген,"
                                              "сіз сол парақшаларға жаза аласыз немесе тікелей осы телеграмм ботыма", reply_markup=btn)
            bot.register_next_step_handler(msg, kzhandle_review)

        elif message.text == 'иә':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("иә")
            item2 = types.KeyboardButton("жоқ мәзірге оралайық")
            markup.add(item1, item2)
            msg = bot.send_message(message.chat.id, "Жарайды жалғастыра беріңіз")
            bot.register_next_step_handler(msg, kzhandle_review)

        if message.text == 'жоқ мәзірге оралайық':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Ақпарат")
            item2 = types.KeyboardButton("Ойын обьектілері")
            # item4 = types.KeyboardButton('Отделы')
            item5 = types.KeyboardButton('Кері байланыс')
            item7 = types.KeyboardButton('басталуына Қанша уақыт қалды')
            item6 = types.KeyboardButton('Тілді таңдауға қайту')
            markup.add(item1, item2, item5, item6, item7)
            bot.send_message(message.chat.id, "Қандай ақапаратпен тағыда сізге бөлісейін?", reply_markup=markup)

        if message.text == 'Eng':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            markup.add(item1, item2, item5, item6, item7)
            photo = open('logo-eng2.png', 'rb')
            bot.send_photo(message.chat.id, photo,
                           f" Welcome to 5th World Nomad Games <b>{message.from_user.first_name}</b>\n",
                           parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "How can we assist you?", reply_markup=markup)


        if message.text == 'choose another language':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Kaz")
            item2 = types.KeyboardButton("Rus")
            item4 = types.KeyboardButton('Eng')
            markup.add(item1, item2, item4)
            bot.send_message(message.chat.id,
                             f"chose language which you are prefer", reply_markup=markup)

        if message.text == 'call center and feedback':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Instagram - volunteer_nomadgameskz',
                                              url="https://www.instagram.com/volunteer_nomadgameskz?igsh=MXdxb3c1c29qdndudg==")
            btn2 = types.InlineKeyboardButton('2)Instagram - worldnomadgames2024',
                                              url="https://www.instagram.com/worldnomadgames2024?igsh=MWZsbjgzN2F5aDN1cg==")
            btn3 = types.InlineKeyboardButton('Facebook', url="https://www.facebook.com/worldnomadgames2024")
            btn.add(btn1, btn2, btn3)
            markup.add(item1, item2, item5, item6, item7)

            msg = bot.send_message(message.chat.id, "all feedback links will be provided below, "
                                              "or you can write your things at here", reply_markup=btn)
            bot.register_next_step_handler(msg, enghandle_review)

        if message.text == 'yes':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("yes")
            item2 = types.KeyboardButton("no go back to menu")
            markup.add(item1, item2)
            msg = bot.send_message(message.chat.id, "you can continue")
            bot.register_next_step_handler(msg, handle_review)

        if message.text == 'no go back to menu':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            markup.add(item1, item2, item5, item6, item7)

            markup.add(item1, item2, item5, item6, item7)
            bot.send_message(message.chat.id, "How can we assist you?", reply_markup=markup)

        if message.text == 'Game Objects':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardMarkup()
            btn4 = types.InlineKeyboardMarkup()
            btn5 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardMarkup()
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            btn1.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70000001037972503"))
            btn2.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70000001018102444"))
            btn3.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70000001018088349"))
            btn4.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70000001018608940"))
            btn5.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70000001044480178"))
            btn6.add(types.InlineKeyboardButton("location", url="https://2gis.kz/astana/geo/70030076129741434"))

            markup.add(item1, item2, item5, item6, item7)


            bot.send_message(message.chat.id, "you can see our objects with their location links(before you touch it, you need to add app which is called 2gis)", reply_markup=markup)

            bot.send_message(message.chat.id,
                             "KAZANAT HIPPODROME (ARGYMAK EQUESTRIAN SPORTS AND RECREATION COMPLEX, ETHNOAUL)\n"
                             "Description of the facility Quantity of spectator seats - 10,000\n"
                             "The length of the racing track is 1,800 m\n"
                             "Organized events: in Kazanat Hippodrome"
                             "1)Flat racing 1,600m\n"
                             "2)Flat racing 2,400m\n"
                             "3)Flat racing 3,200m\n"
                             "4)Zhorga 9,000m\n"
                             "5)Kunan bayge 11,000m\n"
                             "6)Top Bayge 18,000m\n"
                             "7)Alaman Bayge 25,000m\n"
                             "8)Kokpar\n"
                             "9)WNG Astana 2024 Closing ceremony\n"
                             "\nOrganized events: in ETHNOAUL\n"
                             "1)Competitions on national types of hunting with birds\n"
                             "2)Audaryspak\n"
                             "3)Tenge Ilu\n"
                             "4)Zhamby Atu\n"
                             "\nOrganized events: in ARGYMAK EQUESTRIAN SPORTS AND RECREATION COMPLEX\n"
                             "1)Dasturli Sadak Atu", reply_markup=btn6)

            bot.send_message(message.chat.id, "ZHAKSYLYK USHKEMPIROV WRESTLING PALACE\n"
                                              "Quantity of spectator seats - 5,000\n"
                                              "Organized events \n"
                                              "1)Kazakh Kuresi \n2)Alysh", reply_markup=btn1)

            bot.send_message(message.chat.id, "ALAU ICE PALACE\n"
                                              "Quantity of spectator seats - 7,462\n"
                                              "Organized events: in ALAU ICE PALACE, THE MAIN ARENA, SOUTHERN PART OF THE RUNNING TRACK\n"
                                              "\n1)Sssireum\n"
                                              "2)Kurash\n"
                                              "3)Ashyrtmaly Aba Gureshi\n"
                                              "4)Arkan Tartys\n"
                                              "Organized events: in ALAU ICE PALACE, THE MAIN ARENA, NORTHWESTERN PART OF THE RUNNING TRACK\n"
                                              "1)Asyk Atu\n"
                                              "2)Ordo\n"
                                              "Organized events: in ALAU ICE PALACE, THE MAIN ARENA, NORTH-EASTERN PART OF THE RUNNING TRACK\n"
                                              "1)Mas-wrestling"
                                              "Organized events: ALAU ICE PALACE, GAMING HALL, WESTERN TOWER\n"
                                              "1)Training by types of wrestling", reply_markup=btn2)

            bot.send_message(message.chat.id, "DUMAN HOTEL\n"
                                              "\nOrganized events: 1)Togyzkumalak - Mangala"
                                              "\n2)Oware", reply_markup=btn3)

            bot.send_message(message.chat.id, "NATIONAL MUSEUM OF RK", reply_markup=btn4)

            bot.send_message(message.chat.id, "ATHLETICS SPORTS COMPLEX «KAZAKHSTAN»", reply_markup=btn5)
            bot.send_message(message.chat.id, "anything else?", reply_markup=markup)

        if message.text == 'Information':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            btn = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('About the Games', callback_data='about')
            btn2 = types.InlineKeyboardButton('History of the Games', callback_data='history')
            btn3 = types.InlineKeyboardButton('All Dates', callback_data='date')
            btn4 = types.InlineKeyboardButton('Sports programs', callback_data='programs')
            btn5 = types.InlineKeyboardButton('Goals and Objectives', callback_data='goals')
            btn6 = types.InlineKeyboardButton('tickets', callback_data='tickets')
            btn7 = types.InlineKeyboardButton('Discounts', callback_data='Discounts')
            markup.add(item1, item2, item5, item6, item7)
            btn.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(message.chat.id, "What information should I share with you?", reply_markup=btn)
            bot.send_message(message.chat.id, "anything else?", reply_markup=markup)

        if message.text == 'how much time is left before the games start':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Information")
            item2 = types.KeyboardButton("Game Objects")
            # item4 = types.KeyboardButton('Otdel')
            item5 = types.KeyboardButton('call center and feedback')
            item6 = types.KeyboardButton('choose another language')
            item7 = types.KeyboardButton('how much time is left before the games start')
            markup.add(item1, item2, item5, item6, item7)

            wait_message = bot.send_message(message.chat.id, "Plaese wait,it takes 10-20 seconds...")

            timer_info = engparse_timer()

            bot.delete_message(chat_id=message.chat.id, message_id=wait_message.message_id)
            bot.send_message(message.chat.id, f"{timer_info}", parse_mode='html', reply_markup=markup)
            bot.send_message(message.chat.id, "anything else?", reply_markup=markup)


def handle_review(message):
    review = message.text
    user_name = message.from_user.first_name
    if message.content_type == 'text':
        bot.send_message(group_chat_id, f'Новый отзыв от пользователя: {user_name}:\n\n{review}')
    elif message.content_type == 'photo':
        photo = message.photo[-1].file_id
        caption = message.caption if message.caption else 'Без подписи'
        # Отправляем фото в группу
        bot.send_photo(group_chat_id, photo, caption=f'Новое фото от пользователя: {user_name}\n\n{caption}')
    elif message.content_type == 'video':
        video = message.video.file_id
        caption = message.caption if message.caption else 'Без подписи'
        # Отправляем видео в группу
        bot.send_video(group_chat_id, video, caption=f'Новое видео от пользователя: {user_name}\n\n{caption}')
    bot.send_message(
        message.chat.id,
        f'спасибо <b>{user_name}</b> ваш отзыв был направлен на наш телеграмм канал', parse_mode='html')

    # Спрашиваем пользователя, хочет ли он оставить еще отзыв
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("нет в меню")
    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, "хотите еще написать?", reply_markup=markup)
    # main(message)

def kzhandle_review(message):
    review = message.text
    user_name = message.from_user.first_name

    if message.content_type == 'text':
        # Отправляем текстовый отзыв в группу
        bot.send_message(group_chat_id, f'Новый отзыв от пользователя: {user_name}:\n\n{review}')
    elif message.content_type == 'photo':
        photo = message.photo[-1].file_id  # Get the highest resolution photo
        caption = message.caption if message.caption else 'Без подписи'
        # Отправляем фото в группу
        bot.send_photo(group_chat_id, photo, caption=f'Новое фото от пользователя: {user_name}\n\n{caption}')
    elif message.content_type == 'video':
        video = message.video.file_id
        caption = message.caption if message.caption else 'Без подписи'
        bot.send_video(group_chat_id, video, caption=f'Новое видео от пользователя: {user_name}\n\n{caption}')

    bot.send_message(
        message.chat.id,
        f'рахмет <b>{user_name}</b> пікіріңіз біздің телеграмға жіберілді', parse_mode='html')

    # Спрашиваем пользователя, хочет ли он оставить еще отзыв
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("иә")
    item2 = types.KeyboardButton("жоқ мәзірге оралайық")
    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, "отзывты тағыда жазғыңыз келеді ма?", reply_markup=markup)

def enghandle_review(message):
    review = message.text
    user_name = message.from_user.first_name

    if message.content_type == 'text':
        bot.send_message(group_chat_id, f'Новый отзыв от пользователя: {user_name}:\n\n{review}')
    elif message.content_type == 'photo':
        photo = message.photo[-1].file_id
        caption = message.caption if message.caption else 'Без подписи'
        bot.send_photo(group_chat_id, photo, caption=f'Новое фото от пользователя: {user_name}\n\n{caption}')
    elif message.content_type == 'video':
        video = message.video.file_id
        caption = message.caption if message.caption else 'Без подписи'
        bot.send_video(group_chat_id, video, caption=f'Новое видео от пользователя: {user_name}\n\n{caption}')

    bot.send_message(
        message.chat.id,
        f'thank you <b>{user_name}</b> your feedback was sent to our telegram',parse_mode='html')

    # Спрашиваем пользователя, хочет ли он оставить еще отзыв
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("yes")
    item2 = types.KeyboardButton("no go back to menu")
    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, "do you want write another message?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        #rus
        if call.data == 'ob igrax':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("Подробнее", url="https://worldnomadgames.kz/ru/news/ob-igrah"))

            bot.send_message(call.message.chat.id,  f"<b>Всемирные игры кочевников - </b>"
                                                    f"международные спортивные состязания по этническим видам спорта."
                                                    f"В основе соревнований – народные игры исторически кочевых народов "
                                                    f"Центральной Азии. ВИК направлены на развитие этноспортивного и"
                                                    f"этнокультурного движения как наследия человеческой цивилизации.",
                           parse_mode='html',  reply_markup=btn1)

        if call.data == 'istorya':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("Подробнее",
                                                url="https://worldnomadgames.kz/ru/news/ob-igrah"))

            bot.send_message(call.message.chat.id, f"<b>История Игр - </b>"
                                                    f" Международное спортивное событие, задуманное и впервые "
                                                   f"реализованное в Кыргызской Республике, получило глобальный статус,"
                                                   f"охватывая все больше стран и привлекая внимание широкой аудитории "
                                                   f"не только в Евразии.С передачей права проведения ВИК Казахстану, "
                                                   f"расширился и список стран, принимавших Игры.\n"
                                                   f"<b>Впервые Всемирные игры кочевников прошли в Кыргызстане.<u>Город Чолпон-Ата принимал международные соревнования трижды:</u></b>"
                                                   f"\n1)в 2014 г. – 583 спортсмена из 19 стран, 10 видов спорта.\n"
                                                   f"2)в 2016 г. – 1 200 спортсменов из 62 стран, 26 видов спорта.\n"
                                                   f"3)в 2018 г. – 2 000 спортсменов из 82 стран, 37 видов спорта.\n"
                                                   f"<u>4-е Всемирные игры кочевников состоялись в 2022 году в Турции, "
                                                   f"город Изник. 3 000 спортсменов из 102 стран, 13 видов спорта.</u>",parse_mode='html',reply_markup=btn1)

        if call.data == 'data':
            btn1 = types.InlineKeyboardMarkup()

            btn1.add(types.InlineKeyboardButton("Подробнее", url="https://worldnomadgames.kz/ru/news/ob-igrah"))

            bot.send_message(call.message.chat.id, 'Дата и место проведения')
            bot.send_message(call.message.chat.id, 'Место проведения: <b>Республика Казахстан, город Астана</b>\n'
                                                   'Игры пройдут: <b>с 8 по 14 сентября 2024 года.</b>\n'
                                                   'Дни приезда спортивных делегаций: 7-8 сентября 2024 года\n'
                                                   'Аккредитация спортивных делегаций: 7-8 сентября 2024 года.\n'
                                                   'Торжественная церемония открытия: 8 сентября 2024 года\n'
                                                   'Торжественная церемония закрытия: 14 сентября 2024 года\n'
                                                   'День отъезда делегаций: 15 сентября 2024 года.\n'
                                                   '\nСентябрь – отсылка к празднику, отмечающему завершение '
                                                   'перекочевки с летней на зимнюю стоянку. Путь каравана людей и '
                                                   'животных с юртами и имуществом традиционно заканчивался на новой '
                                                   'стоянке тоем с ритуалами, играми и состязаниями.', parse_mode='html',reply_markup=btn1)

        if call.data == 'celly':
            bot.send_message(call.message.chat.id, 'ЦЕЛИ И ЗАДАЧИ', parse_mode='html')
            bot.send_message(call.message.chat.id, '\tВИК Астана 2024, опираясь на этнокультурное наследие народов мира, имеют следующие цели и задачи:\n'
                                                   '1. Развитие всемирного этно-спортивного движения.\n'
                                                   '2. Популяризация, развитие и продвижение на международной арене видов этноспорта, традиционных игр и состязаний народов мира.\n'
                                                   '\n'
                                                   '3. Сохранение исторического культурного наследия и многообразия народов мира в эпоху глобализации.\n'
                                                   '4. Содействие научному и организационно-методическому обоснованию этно-спортивного движения, видов этноспорта, традиционных игр и состязаний народов мира\n'
                                                   '5. Укрепление и дальнейшее развитие межрелигиозного и межкультурного диалога, взаимопонимания, дружбы, согласия и сотрудничества между народами мира, демонстрация их культурного многообразия.\n'
                                                   ,parse_mode='html')

        if call.data == 'cilet':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(
                types.InlineKeyboardButton("Купить Билеты можно тут", url="https://zakazbiletov.kz/ru/search/kazakhstan?query=&categories[0]=256&sorting=asc"))
            bot.send_message(call.message.chat.id, f"<b>Про Билеты</b>", parse_mode='html')

            bot.send_message(call.message.chat.id, f"<b>УВАЖАЕМЫЙ ЧИТАТЕЛЬ - </b>"
                                                   f"Продажа билетов на 5-е Всемирные игры кочевников будет "
                                                   f"проводиться поэтапно. На некоторых объектах идет реконструкция "
                                                   f"и зрительская рассадка меняется. В этой связи продажа билетов "
                                                   f"на Церемонию Открытия и Церемонию Закрытия начнется позже.", parse_mode='html')

            bot.send_message(call.message.chat.id, f"<b>Онлайн билеты можно будет приобрести на сайте официального билетного оператора www.zakazbiletov.kz </b>"
                                                   f" Офлайн-кассы будут открыты на трех объектах непосредственно перед "
                                                   f"началом соревнований в сентябре 2024 года в г. Астана.", parse_mode='html',reply_markup=btn1)

        if call.data == 'skidky':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("подробнее", url="https://worldnomadgames.kz/ru/page/bilety"))
            bot.send_message(call.message.chat.id,
                             f"<b>ЛЬГОТЫ И СКИДКИ ДЛЯ ЗРИТЕЛЕЙ 5-Х ВСЕМИРНЫХ ИГР КОЧЕВНИКОВ</b>",
                             parse_mode='html')

            bot.send_message(call.message.chat.id,
                             f"<b>1. Бесплатные билеты предусмотрены для следующих категорий граждан:\n</b>"
                             f"1) дети 0-5 лет включительно без предоставления места;і;\n"
                             f"2) инвалиды I, II группы.\nПримечание: Бесплатные билеты предоставляются только в офлайн-кассах при предъявлении соответствующего документа.\n"
                             f"<b>2.Скидки на билеты предусмотрены для следующих категорий граждан::</b>"
                             f"\n1)–  школьный тариф (от 6 до 18 лет) - 50% от основного тарифа;\n"
                             f"\n2)–  пенсионный тариф - 50% от основного тарифа.\nПримечание: льготные билеты приобретаются только в офлайн-кассах при предъявлении соответствующего документа.\n"
                             f"<b>Ескертпе: тегін билет тиісті құжат ұсынылған кезде офлайн кассаларда ғана беріледі.</b>\n"
                             f"Бесплатные билеты, скидки для школьников и пенсионеров не распространяются на Церемонию Открытия Игр."
                             f"Бесплатные билеты не распространяются на финал игры Көкпар.", parse_mode='html',
                             reply_markup=btn1)

        if call.data == 'sport':
            mark = types.InlineKeyboardMarkup()

            mark.add(types.InlineKeyboardButton("Подробнее про спортивную программу", url="https://worldnomadgames.kz/ru/page/sportivnaya-programma"))

            bot.send_message(call.message.chat.id, 'внизу будет приведена Спортивная программа  ВИК АСТАНА 2024 и ссылка для подробной информаций')
            bot.send_message(call.message.chat.id, '<b>НАРОДНЫЕ ИГРЫ: </b>'
                                                   '1)Вид Спорта: Асық\n'
                                                   'Описание: Кидать Асық\n'
                                                   'Место проведения: Ледовый дворец «Алау»'
                                                   '2)Вид Спорта: Ордо\n'
                                                   'Описание: Ордо\n'
                                                   'Место проведения: Ледовый дворец «Алау»\n'
                                                   '3)Вид Спорта: Арқан Тарту\n'
                                                   'Описание: Тянуть Канат\n'
                                                   'Место проведения: Ледовый дворец «Алау»', parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>КОННЫЕ СКАЧКИ: </b>'
                                                   '1)Вид Спорта: Гладкие скачки 1600 м\n'
                                                   'Описание: Классические гладкие скачки\n'
                                                   'Место проведения: Ипподром «Казанат»'
                                                   '2)Вид Спорта:  Гладкие 2400 м\n'
                                                   'Описание: Классические гладкие скачки\n'
                                                   'Место проведения: Ипподром «Казанат» \n'
                                                   '3)Вид Спорта:  Гладкие 3200 м\n'
                                                   'Описание: Классические гладкие скачки\n'
                                                   'Место проведения: Ипподром «Казанат»\n'
                                                   '4)Вид Спорта:  Жорға\n'
                                                   'Описание:  Забег иноходцев (9 000 м)\n'
                                                   'Место проведения: Ипподром «Казанат» \n'
                                                   '5)Вид Спорта: Құнан бәйге\n'
                                                   'Описание: Скачки на длинные дистанции (11 000 м)\n'
                                                   'Место проведения: Ипподром «Казанат»\n'
                                                   '6)Вид Спорта: Топ бәйге \n'
                                                   'Описание: Скачки на длинные дистанции (18 000 м)\n'
                                                   'Место проведения: Ипподром «Казанат»\n'
                                                   '7)Вид Спорта: Аламан бәйге\n'
                                                   'Описание: Скачки на длинные дистанции (25 000 м)\n'
                                                   'Место проведения: Ипподром «Казанат»\n', parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>СОСТЯЗАНИЯ НА ЛОШАДЯХ: </b>'
                                                   '1)Вид Спорта: Көкпар\n'
                                                   'Описание: Командное состязание на лошадях \n'
                                                   'Место проведения: Ипподром «Казанат»'
                                                   '2)Вид Спорта: Аударыспақ\n'
                                                   'Описание: Борьба верхом на лошадях\n'
                                                   'Место проведения: Этноаул \n'
                                                   '3)Вид Спорта:  Теңге ілу \n'
                                                   'Описание:  Индивидуальное состязание на лошадях\n'
                                                   'Место проведения: Этноаул', parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>СОСТЯЗАНИЯ ПО НАЦИОНАЛЬНЫМ ВИДАМ БОРЬБЫ: </b>'
                                                   '1)Вид Спорта: Қазақ күресі\n'
                                                   'Описание: Национальная борьба(РК)\n'
                                                   'Место проведения: Дворец единоборств им. Ж.Ушкемпирова '
                                                   '2)Вид Спорта: Ашыртмалы аба гюреши\n'
                                                   'Описание: Национальная борьба (Турецкая Республика) \n'
                                                   'Место проведения: Ледовый дворец «Алау»\n'
                                                   '3)Вид Спорта: Кураш\n'
                                                   'Описание: Национальная борьба (Республика Узбекистан)\n'
                                                   'Место проведения: Ледовый дворец «Алау» '
                                                   '4)Вид Спорта: Ссирым\n'
                                                   'Описание: Национальная борьба на поясах(Республика Корея)\n'
                                                   'Место проведения: Ледовый дворец «Алау»'
                                                   '4)Вид Спорта: Алыш\n'
                                                   'Описание: Национальная борьба на поясах(Республика Кыргызская)\n', parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>СОРЕВНОВАНИЯ ПО ВИДАМ ЕДИНОБОРСТВ: </b>'
                                                   '1)Вид Спорта: Мас-рестлинг\n'
                                                   'Описание: Национальное состязание(Российская Федерация) \n'
                                                   'Место проведения:Ледовый дворец «Алау» '
                                                   '2)Вид Спорта: (Алып көшпенді) «Powerful nomad»\n'
                                                   'Описание: Состязание силачей \n'
                                                   'Место проведения: Этноаул\n'
                                                    , parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>ТРАДИЦИОННЫЕ ИНТЕЛЛЕКТУАЛЬНЫЕ ИГРЫ: </b>'
                                                   '1)Вид Спорта: Тоғызқұмалак \n'
                                                   'Описание: Интеллектуальная игра (Республика Казахстан)\n'
                                                   'Место проведения: Гостиница «Думан»'
                                                   '2)Вид Спорта:  Мангала \n'
                                                   'Описание: Интеллектуальная игра (Турецкая Республика)\n'
                                                   'Место проведения: Гостиница «Думан» \n'
                                                   '3)Вид Спорта: Овари\n'
                                                   'Описание:  Интеллектуальная игра (страны Западной Африки)\n'
                                                   'Место проведения: Гостиница «Думан»', parse_mode='html')
            bot.send_message(call.message.chat.id, '<b>СОСТЯЗАНИЯ ПО СТРЕЛЬБЕ ИЗ ТРАДИЦИОННОГО ЛУКА И СТРЕЛЬБЕ ИЗ ТРАДИЦИОННОГО ЛУКА НА ЛОШАДЯХ: </b>'
                                                   '1)Вид Спорта:Дәстүрлі садақ ату\n'
                                                   'Описание:Стрельба из традиционного лука\n'
                                                   'Место проведения: КСОК «Аргымак»'
                                                   '2)Вид Спорта:  Жамбы ату\n'
                                                   'Описание: Стрельба из традиционного лука верхом на лошадии\n'
                                                   'Место проведения: Этноаул \n'
                                                   , parse_mode='html')
            bot.send_message(call.message.chat.id,'<b>СОСТЯЗАНИЯ ПО НАЦИОНАЛЬНЫМ ВИДАМ ОХОТА С ПТИЦАМИ: </b>'
                                                     '1)Вид Спорта: Бүркіт\n'
                                                     'Описание: Охота с беркутом\n'
                                                     'Место проведения: Этноаул'
                                                     '2)Вид Спорта:  Қаршыға\n'
                                                     'Описание: Охота с ястребом\n'
                                                     'Место проведения: Этноаул \n'
                                                     '3)Вид Спорта:  Ителгі\n'
                                                     'Описание: Охота с соколом\n'
                                                     'Место проведения: Этноаул', parse_mode='html', reply_markup= mark)

       #kazak
        if call.data == 'turaly':
                btn1 = types.InlineKeyboardMarkup()
                btn1.add(types.InlineKeyboardButton("нақтырақ", url="https://worldnomadgames.kz/ru/news/ob-igrah"))

                bot.send_message(call.message.chat.id, f"<b>Ойындар туралы</b>", parse_mode='html')

                bot.send_message(call.message.chat.id, f"<b>Дүниежүзілік көшпенділер ойындары - </b>"
                                                       f" – этникалық спорт түрлерінен өткізілетін халықаралық спорт жарыстары."
                                                       f" Жарыстар Орталық Азияның тарихи көшпелі халықтарының ұлттық ойындарына"
                                                       f" негізделген. ДКО адамзат өркениетінің мұрасы ретінде этноспорттық "
                                                       f"және этномәдени қозғалысты дамытуға бағытталған.", parse_mode='html', reply_markup=btn1)

        if call.data == 'bylet':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("Билеттерді осы сілтеме арқылы сатып аласыз", url="https://zakazbiletov.kz/ru/search/kazakhstan?query=&categories[0]=256&sorting=asc"))

            bot.send_message(call.message.chat.id, f"<b>Билеттер туралы</b>", parse_mode='html')

            bot.send_message(call.message.chat.id, f"<b>Құрметті оқырман - </b>"
                                                   f"5-ші Дүниежүзілік көшпенділер ойындарына билеттердің сатылуы "
                                                   f" кезең-кезеңмен өткізіледі. Кейбір нысандарда қайта құру жұмыстары "
                                                   f"жүргізіліп жатқандықтан көрермендерді отырғызатын орындар өзгеруі "
                                                   f"мүмкін. Осыған орай Ашылу және Жабылу Рәсімдеріне билет сату "
                                                   f"кейінірек басталады.", parse_mode='html')

            bot.send_message(call.message.chat.id, f"<b>Онлайн билетті ресми билет операторы zakazbiletov.kz </b>"
                                                   f"сайтынан онлайн режимінде сатып алуға болады (с    ілтеме арқылы кіре аласыз). Офлайн кассалар "
                                                   f"үш нысанда 2024 жылдың қыркүйегінде Астана қаласында жарыс "
                                                   f"басталар алдында ашық болады.", parse_mode='html', reply_markup=btn1)

        if call.data == 'tarix':
             btn1 = types.InlineKeyboardMarkup()
             btn1.add(types.InlineKeyboardButton("нақтырақ", url="https://worldnomadgames.kz/ru/news/ob-igrah"))
             bot.send_message(call.message.chat.id, f"<b>Ойындар тарихы - </b>"
                                                       f" Алғаш рет Қырғыз Республикасында ойластырылып, жүзеге асырылған "
                                                       f"халықаралық спорттық шара әлемдік мәртебеге ие болып, барған сайын, "
                                                       f"Еуразия кеңістігін ғана емес, басқа да көптеген елдерді қамтып, "
                                                       f"кең аудиторияның назарын аударды. Дүниежүзілік ойындарды өткізу "
                                                       f"құқығының Қазақстанға берілуімен ойындарды өткізетін елдердің тізімі де кеңейді.\n"
                                                       f"<b>Дүниежүзілік көшпенділер ойындары алғаш рет Қырғызстанда өтті.<u>Чолпон-Ата қаласы халықаралық жарыстарды үш рет қабылдады::</u></b>"
                                                       f"\n1)2014 жылы – 19 елден 10 спорт түрінен 583 спортшы.\n"
                                                       f"2)2016 жылы – 62 елден 26 спорт түрінен 1 200 спортшы..\n"
                                                       f"3)2018 жылы – 82 елден 37 спорт түрінен 2 000 спортшы.\n"
                                                       f"<u>44-ші Дүниежүзілік көшпенділер ойындары 2022 жылы Түркияның "
                                                       f" Изник қаласында өткізілді. 102 елден 13 спорт түрінен 3 000 спортшы.</u>",
                                 parse_mode='html', reply_markup=btn1)

        if call.data == 'zhenildik':
            btn1 = types.InlineKeyboardMarkup()
            btn1.add(types.InlineKeyboardButton("нақтырақ", url="https://worldnomadgames.kz/kz/page/bilety"))
            bot.send_message(call.message.chat.id, f"<b>5-ші Дүниежүзілік көшпенділер ойындарының көрермендеріне арналған жеңілдіктер</b>", parse_mode='html')

            bot.send_message(call.message.chat.id,
                             f"<b>1. Азаматтардың келесі санаттары үшін тегін билеттер қарастырылған:\n</b>"
                             f"1) 0-5 жас аралығындағы балаларға, бөлек орын берілмейді;\n"
                             f"2) I, II топтағы мүгедектерге.\n"
                             f"<b>2. Билеттерге шегерімдер азаматтардың келесі санаттары үшін қарастырылған:</b>"
                             f"\n1)–  оқушы тарифі (6 жастан 18 жасқа дейін) –  негізгі тарифтің 50% жеңілдік ;\n"
                             f"\n2)–  зейнеткер тарифі –  негізгі тарифтен 50% жеңілдік\n"
                             f"<b>Ескертпе: тегін билет тиісті құжат ұсынылған кезде офлайн кассаларда ғана беріледі.</b>\n"
                             f"Ойындардың Ашылу және Жабылу Рәсімдеріне тегін билеттер мен жеңілдіктер қарастырылмайды."
                             f"Көкпар ойынының финалына тегін билеттер қарастырылмайды.",parse_mode='html', reply_markup=btn1)

        if call.data == 'kunder':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton("нақтырақ", url="https://worldnomadgames.kz/kz/news/ob-igrah"))
            bot.send_message(call.message.chat.id, 'ОЙЫНДАРДЫҢ ӨТКІЗІЛУ МЕРЗІМІ ЖӘНЕ ОРНЫ')
            bot.send_message(call.message.chat.id, 'Өткізу орны: <b>Қазақстан Республикасы, Астана қаласы.</b>\n'
                                                       'Өткізу мезгілі:: <b>2024 жылғы 8 - 14 қыркүйек</b>\n'
                                                       'Спорт делегацияларының келетін күндері: 2024 жылы, 7-8 қыркүйек.\n'
                                                       'Спорт делегацияларын аккредиттеу: 2024 жылы 7-8 қыркүйек.\n'
                                                       'Салтанатты ашылу рәсімі: 2024 жылғы 8 қыркүйек\n'
                                                       'Салтанатты жабылу рәсімі: 14 қыркүйек 2024 жылы\n'
                                                       'Делегациялардың кейін қайтатын күні: 15 қыркүйек 2024 жылы.\n'
                                                       '\nСентябрь – отсылка к празднику, отмечающему завершение '
                                                       'перекочевки с летней на зимнюю стоянку. Путь каравана людей и '
                                                       'животных с юртами и имуществом традиционно заканчивался на новой '
                                                       'стоянке тоем с ритуалами, играми и состязаниями.',parse_mode='html', reply_markup=btn)

        if call.data == 'maksat':
                bot.send_message(call.message.chat.id, 'МАҚСАТТАР МЕН МІНДЕТТЕР', parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 '\tАстана 2024 ДКО бағдарламасы дәстүрлі түрде үш бағыттағы іс-шараларды қамтиды: спорт, мәдениет, ғылым:\n'
                                 '\tАстана 2024 ДКО әлем халықтарының этномәдени мұрасына сүйене отырып, келесі мақсаттар мен міндеттерді алға қояды: \n'
                                 '1. Дүниежүзілік этноспорттық қозғалыстың дамуы.\n'
                                 '2. Әлем халықтарының этникалық спорт түрлерін, дәстүрлі ойындары мен жарыстарын халықаралық аренада танымал ету, дамыту және ілгері жылжыту.\n'
                                 '\n'
                                 '3. Жаһандану дәуірінде әлем халықтарының тарихи мәдени және алуан түрлі мұрасын сақтау.\n'
                                 '4. Этноспорттық қозғалысты, этноспорт түрлерін, әлем халықтарының дәстүрлі ойындары мен жарыстарын ғылыми, ұйымдастырушылық және әдістемелік тұрғыдан негіздеуге ықпал жасау. \n'
                                 '5.  Әлем халықтары арасындағы дінаралық және мәдениетаралық диалогты, өзара түсіністікті, достықты, келісім мен ынтымақтастықты нығайту және одан әрі дамыту, олардың мәдени әртүрлілігін көрсету..\n'
                                 , parse_mode='html')

        if call.data == 'bagdar':
                mark = types.InlineKeyboardMarkup()

                mark.add(types.InlineKeyboardButton("нақтырақ",
                                                    url="https://worldnomadgames.kz/ru/page/sportivnaya-programma"))

                bot.send_message(call.message.chat.id, 'АСТАНА 2024 ДКО СПОРТ БАҒДАРЛАМАСЫ')
                bot.send_message(call.message.chat.id, '<b>Халық ойындары: </b>'
                                                       '1)Спорт түрі: Асық\n'
                                                       'Сипаттамасы: Асық ату\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы'
                                                       '2)Спорт түрі: Ордо\n'
                                                       'Сипаттамасы: Ордо\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы\n'
                                                       '3)Спорт түрі: Арқан тартыс\n'
                                                       'Сипаттамасы: Арқанды Тарту\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы', parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Ат жарысы: </b>'
                                                       '1)Спорт түрі: Ұшқыр бәйге 1600 м\n'
                                                       'Сипаттамасы: Классикалық ұшқыр бәйге\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n'
                                                       '2)Спорт түрі: Ұшқыр бәйге  2400 м\n'
                                                       'Сипаттамасы: Классикалық ұшқыр бәйге\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы \n'
                                                       '3)Спорт түрі:  Ұшқыр бәйге 3200 м\n'
                                                       'Сипаттамасы: Классикалық ұшқыр бәйге\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n'
                                                       '4)Спорт түрі: Жорға\n'
                                                       'Сипаттамасы: Жорға шабысы (9 000 м)\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n'
                                                       '5)Спорт түрі: Құнан бәйге\n'
                                                       'Сипаттамасы: Алыс қашықтықта өтілетін ат шабыстары (11 000 м)\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n'
                                                       '6)Спорт түрі: Топ бәйге\n'
                                                       'Сипаттамасы: Алыс қашықтықта өтетін ат шабыстары  (18 000 м)\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n'
                                                       '7)Спорт түрі: Аламан бәйге\n'
                                                       'Сипаттамасы: Алыс қашықтықта өтетін ат шабыстары (25 000 м) \n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы\n', parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Ат үстіндегі сайыстар: </b>'
                                                       '1)Спорт түрі: Көкпар\n'
                                                       'Сипаттамасы: Ат үстіндегі командалық сайыс\n'
                                                       'Өткізілетін орны: «Қазанат» ипподромы'
                                                       '2)Спорт түрі: Аударыспақ\n'
                                                       'Сипаттамасы: Ат үстіндегі күрес\n'
                                                       'Өткізілетін орны: Этноаул \n'
                                                       '3)Спорт түрі:  Теңге ілу \n'
                                                       'Сипаттамасы: Ат үстіндегі жеке сайыс\n'
                                                       'Өткізілетін орны: Этноаул', parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Ұлттық күрес түрлері бойынша сайыстар: </b>'
                                                       '1)Спорт түрі: Қазақ күресі\n'
                                                       'Сипаттамасы: Ұлттық күрес (Қазақстан Республикасы)\n'
                                                       'Өткізілетін орны: Ж.Үшкемпіров атындағы Жекпе-жек сарайы\n'
                                                       '2)Спорт түрі: Ашыртмалы аба гюреши\n'
                                                       'Сипаттамасы: Ұлттық белбеу күресі (Түркия Республикасы)\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы\n'
                                                       '3)Спорт түрі: Кураш\n'
                                                       'Сипаттамасы: Ұлттық күрес (Өзбекстан Республикасы)\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы'
                                                       '4)Спорт түрі: Ссирым\n'
                                                       'Сипаттамасы: Ұлттық белбеу күресі (Корея Республикасы)\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы'
                                                       '4)Спорт түрі: Алыш\n'
                                                       'Сипаттамасы:Ұлттық белбеу күресі (Қырғыз Республикасы)\n'
                                                       'Өткізілетін орны: Ж.Үшкемпіров атындағы Жекпе-жек сарайы',
                                 parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Жекпе-жек түрлері бойынша сайыстар: </b>'
                                                       '1)Спорт түрі: Мас-рестлинг\n'
                                                       'Сипаттамасы: Ұлттық сайыс (Ресей Федерациясы)\n'
                                                       'Өткізілетін орны: «Алау» мұзайдын сарайы'
                                                       '2)Спорт түрі: (Алып көшпенді) «Powerful nomad»\n'
                                                       'Сипаттамасы: Күштері мықты адамдардын арасындағы сайысы\n'
                                                       'Өткізілетін орны: Этноаул\n', parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Дәстүрлі зияткерлік ойындар: </b>'
                                                       '1)Спорт түрі: Тоғызқұмалак \n'
                                                       'Сипаттамасы:Зияткерлік ойын (Қазақстан Республикасы)\n'
                                                       'Өткізілетін орны:«Думан» қонақ үйі Конференц-залы'
                                                       '2)Спорт түрі:  Мангала \n'
                                                       'Сипаттамасы:Зияткерлік ойын(Түркия Республикасы)\n'
                                                       'Өткізілетін орны:«Думан» қонақ үйі Конференц-залы\n'
                                                       '3)Спорт түрі: Овари\n'
                                                       'Сипаттамасы:Зияткерлік ойын (Батыс Африка елдері) \n'
                                                       'Өткізілетін орны:«Думан» қонақ үйі Конференц-залы',
                                 parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 '<b>Дәстүрлі садақ ату және ат үстінде дәстүрлі садақ ату сайыстары: </b>'
                                 '1)Спорт түрі:Дәстүрлі садақ ату\n'
                                 'Сипаттамасы:Дәстүрлі садақ ату\n'
                                 'Өткізілетін орны: «Арғымақ» АССК'
                                 '2)Спорт түрі:  Жамбы ату\n'
                                 'Сипаттамасы:Ат үстіндегі дәстүрлі садақ ату\n'
                                 'Өткізілетін орны: Этноаул \n', parse_mode='html')
                bot.send_message(call.message.chat.id, '<b>Құс аулаудың ұлттық түрлері бойынша сайыстар: </b>'
                                                       '1)Спорт түрі: Бүркіт\n'
                                                       'Сипаттамасы: Бүркітпен бірге аулау\n'
                                                       'Өткізілетін орны: Этноаул'
                                                       '2)Спорт түрі:  Қаршыға\n'
                                                       'Сипаттамасы: қаршығамен бірге аулау   \n'
                                                       'Өткізілетін орны: Этноаул \n'
                                                       '3)Спорт түрі:  Ителгі\n'
                                                       'Сипаттамасы: Ителгі салу\n'
                                                       'Өткізілетін орны: Этноаул', parse_mode='html',
                                 reply_markup=mark)

    #english
    if call.data == 'about':
        btn1 = types.InlineKeyboardMarkup()
        btn1.add(types.InlineKeyboardButton("link", url="https://worldnomadgames.kz/en/news/ob-igrah"))

        bot.send_message(call.message.chat.id, f"<b>About the Games</b>", parse_mode='html')

        bot.send_message(call.message.chat.id, f"<b>The World Nomad Games  - </b>"
                                               f"are international sports competitions in ethnic sports. "
                                               f"The competition is based on folk games of historically nomadic "
                                               f"peoples of Central Asia. WNG are aimed at the development of ethno-sports "
                                               f"and ethno-cultural movement as a heritage of human civilization.",
                         parse_mode='html', reply_markup=btn1)


    if call.data == 'history':
        btn1 = types.InlineKeyboardMarkup()
        btn1.add(types.InlineKeyboardButton("more information",
                                            url="https://worldnomadgames.kz/en/news/ob-igrah"))

        bot.send_message(call.message.chat.id, f"<b>History of the Games - </b>"
                                               f"The international sporting event, conceived and first organized in the "
                                               f"Kyrgyz Republic, has gained a global status, covering more and "
                                               f"more countries and attracting the attention of a wide audience not "
                                               f"only in Eurasia. With the transfer of the right to host the WNG to "
                                               f"Kazakhstan, the list of countries hosting the Games has expanded.\n"
                                               f"<b>For the first time, the World Nomad Games were held in Kyrgyzstan.<u>The city of Cholpon-Ata has hosted international competitions three times:</u></b>"
                                               f"\n1)in 2014 – 583 athletes from 19 countries, 10 sports.\n"
                                               f"2)in 2016 – 1 200 athletes from 62 countries, 26 sports.\n"
                                               f"3)in 2018 – 2 000 athletes from 82 countries, 37 sports.\n"
                                               f"<u>The 4th World Nomad Games were held in 2022 in Iznik, "
                                               f"Turkey. 3 000 athletes from 102 countries, 13 sports.</u>", parse_mode='html',
                         reply_markup=btn1)


    if call.data == 'date':
        btn = types.InlineKeyboardMarkup()
        btn.add(types.InlineKeyboardButton("more details", url="https://worldnomadgames.kz/en/news/ob-igrah"))
        bot.send_message(call.message.chat.id, 'Dates')
        bot.send_message(call.message.chat.id, 'Venue: <b>Republic of Kazakhstan, Astana city.</b>\n'
                                               'The Games will be held from:<b>September 8 to September 14, 2024</b>\n'
                                               'Days of arrival of sports delegations:  September 7-8, 2024.\n'
                                               'Accreditation of sports delegations: September 7-8, 2024.\n'
                                               'Opening ceremony: September 8, 2024\n'
                                               'Closing ceremony: September 14, 2024.\n'
                                               'Days of departure of delegations: September 15, 2024\n'
                                               '\nSeptember is a reference to the traditional time of the holiday, '
                                               'marking the completion of the migration from summer to winter camping. '
                                               'The path of the caravan of people and animals with yurts and possessions '
                                               'traditionally ended at the new camping area with rituals, games and '
                                               'competitions.', parse_mode='html',
                         reply_markup=btn)

    if call.data == 'goals':
        bot.send_message(call.message.chat.id, 'GOALS AND OBJECTIVES', parse_mode='html')
        bot.send_message(call.message.chat.id,
                         '\tThe WNG Astana 2024 program traditionally provides for activities in three areas: sport, culture and science:\n'
                         '\tThe WNG Astana 2024, relying on the ethno-cultural heritage of the peoples of the world, has the following goals and objectives: \n'
                         '1. Development of the global ethno-sports movement\n'
                         '2. Popularization, development and promotion of ethnosports, traditional games and competitions of the peoples of the world on the international arena.\n'
                         '3. Preservation of the historical cultural heritage and the diversity of the worlds peoples in an era of globalization.\n'
                         '4. Assistance to scientific and organizational-methodological substantiation of ethno-sports movement, types of ethno-sports, traditional games and competitions of the peoples of the world. \n'
                         '5.Strengthening and further development of inter-religious and intercultural dialog, mutual understanding, friendship, harmony and cooperation among the peoples of the world, demonstration of their cultural diversity.\n'
                         , parse_mode='html')

    if call.data == 'programs':
        mark = types.InlineKeyboardMarkup()

        mark.add(types.InlineKeyboardButton("more information",
                                            url="https://worldnomadgames.kz/ru/page/sportivnaya-programma"))
        bot.send_message(call.message.chat.id, 'WNG ASTANA 2024 SPORTS PROGRAM')
        bot.send_message(call.message.chat.id, '<b>Folk games: </b>'
                                               '1)Kind of sport: Asyk Atu\n'
                                               'Description: throw Asyk\n'
                                               'Venue/location: Alau Ice Palace'
                                               '2)Kind of sport: Ordo\n'
                                               'Description: throw Ordo\n'
                                               'Venue/location: Alau Ice Palace\n'
                                               '3)Kind of sport: Arkan Tartys\n'
                                               'Description: pull the rope Arkan\n'
                                               'Venue/location: Alau Ice Palace', parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>Horse racing: </b>'
                                               '1)Kind of sport: Flat racing 1,600 m\n'
                                               'Description: Classic smooth racing\n'
                                               'Venue/location: Kazanat Hippodrome\n'
                                               '2)Kind of sport: Flat racing 2,400 m\n'
                                               'Description: Classic smooth racing\n'
                                               'Venue/location: Kazanat Hippodrome \n'
                                               '3)Kind of sport: Flat racing 3,200 m\n'
                                               'Description: Classic smooth racing\n'
                                               'Venue/location: Kazanat Hippodrome\n'
                                               '4)Kind of sport: Zhorga\n'
                                               'Description: Pacing horse racing (9,000 m)\n'
                                               'Venue/location: Kazanat Hippodrome\n'
                                               '5)Kind of sport: Kunan Baige\n'
                                               'Description: Long-distance horse racing (11,000 m)\n'
                                               'Venue/location: Kazanat Hippodrome\n'
                                               '6)Kind of sport: Top Baige\n'
                                               'Description: Long-distance horse racing (18,000 m)\n'
                                               'Venue/location: Kazanat Hippodrome\n'
                                               '7)Kind of sport: Alaman Baige\n'
                                               'Description: Long-distance horse racing (25,000 m)\n'
                                               'Venue/location: Kazanat Hippodrome\n', parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>Horseback competitions: </b>'
                                               '1)Kind of sport: Kokpar\n'
                                               'Description: Team competition on horseback\n'
                                               'Venue/location: Kazanat Hippodrome'
                                               '2)Kind of sport: Audaryspak\n'
                                               'Description: Horseback wrestling\n'
                                               'Venue/location: Ethnoaul\n'
                                               '3)Kind of sport: Tenge Ilu\n'
                                               'Description: Individual horseback competition\n'
                                               'Venue/location: Ethnoaul', parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>National wrestling competitions: </b>'
                                               '1)Kind of sport: Kazakh Kuresi\n'
                                               'Description: National wrestling (The Republic of Kazakhstan)\n'
                                               'Venue/location: Wresting Palace named after Zh.Ushkempirov\n'
                                               '2)Kind of sport: Ashyrtmaly Aba Gureshi\n'
                                               'Description: National belt wrestling (The Turkish Republic)\n'
                                               'Venue/location: Alau Ice Palace\n'
                                               '3)Kind of sport: Kurash\n'
                                               'Description: National wrestling (The Republic of Uzbekistan)\n'
                                               'Venue/location: Alau Ice Palace'
                                               '4)Kind of sport: Ssireum\n'
                                               'Description: National belt wrestling (The Republic of Korea)\n'
                                               'Venue/location: Alau Ice Palace'
                                               '5)Kind of sport: Alysh\n'
                                               'Description:Ұлттық белбеу күресі (Қырғыз Республикасы)\n'
                                               'Venue/location: Wresting Palace named after Zh.Ushkempirov',
                         parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>Competitions in martial arts: </b>'
                                               '1)Kind of sport: Mas-wrestling\n'
                                               'Description:National competition (the Russian Federation)\n'
                                               'Venue/location: Alau Ice Palace'
                                               '2)Kind of sport: «Powerfulnomad» (Alyp koshpendi) \n'
                                               'Description: Strongman competition\n'
                                               'Venue/location: Ethnoaul\n', parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>Traditional intellectual games: </b>'
                                               '1)Kind of sport: Togyzkumalak \n'
                                               'Description:Intellectual game (The Republic of Kazakhstan)\n'
                                               'Venue/location:Duman Hotel Conference hall'
                                               '2)Kind of sport: Mangala \n'
                                               'Description:Intellectual game (The Turkish Republic)\n'
                                               'Venue/location:Duman Hotel Conference hall\n'
                                               '3)Kind of sport: Oware\n'
                                               'Description:Intellectual game (West African countries)\n'
                                               'Venue/location:Duman Hotel Conference hall', parse_mode='html')
        bot.send_message(call.message.chat.id,
                         '<b>Traditional archery and horseback archery competitions: </b>'
                         '1)Kind of sport:Dasturli Sadak Atu\n'
                         'Description:Traditional archery\n'
                         'Venue/location: Argymak equestrian sports and recreation complex'
                         '2)Kind of sport: Zhamby Atu\n'
                         'Description:Traditional horseback archery\n'
                         'Venue/location: Ethnoaul\n', parse_mode='html')
        bot.send_message(call.message.chat.id, '<b>National hunting with birds: </b>'
                                               '1)Kind of sport: Burkit\n'
                                               'Description: Hunting with an eagle\n'
                                               'Venue/location: Ethnoaul'
                                               '2)Kind of sport:Karshyga\n'
                                               'Description: Hunting with a hawk\n'
                                               'Venue/location: Ethnoaul\n'
                                               '3)Kind of sport: Itelgi\n'
                                               'Description: Hunting with a falcon\n'
                                               'Venue/location: Ethnoaul', parse_mode='html', reply_markup=mark)

    if call.data == 'tickets':
        mark = types.InlineKeyboardMarkup()

        mark.add(types.InlineKeyboardButton("buy a ticket",
                                            url="https://zakazbiletov.kz/en/search/kazakhstan?query=&categories[0]=256&sorting=asc"))
        bot.send_message(call.message.chat.id,  f"DEAR FRIEND, <b>{call.message.from_user.first_name}</b>\n ", parse_mode='html')
        bot.send_message(call.message.chat.id,
                         '\tTicket sales for the 5th World Nomad Games will be carried out in several stages. Some venues '
                         'are undergoing reconstruction and the seating arrangements for spectators are changing. '
                         'In this regard, ticket sales for the Opening Ceremony and Closing Ceremony will start later.\n'
                         '\tOn March 21, the first stage of ticket sales for competitions of already prepared sports '
                         'facilities begins, such as the Alau Ice Palace, the Martial Arts Palace named after. '
                         'Zh.Ushkempirov, equestrian complex "Argymak". \n'
                         '1. Development of the global ethno-sports movement\n'
                         '2. Popularization, development and promotion of ethnosports, traditional games and competitions of the peoples of the world on the international arena.\n'
                         '3. Preservation of the historical cultural heritage and the diversity of the worlds peoples in an era of globalization.\n'
                         '4. Assistance to scientific and organizational-methodological substantiation of ethno-sports movement, types of ethno-sports, traditional games and competitions of the peoples of the world. \n'
                         '5.Strengthening and further development of inter-religious and intercultural dialog, mutual understanding, friendship, harmony and cooperation among the peoples of the world, demonstration of their cultural diversity.\n'
                         , parse_mode='html', reply_markup=mark)

    if call.data == 'Discounts':
        btn1 = types.InlineKeyboardMarkup()
        btn1.add(types.InlineKeyboardButton("more details", url="https://worldnomadgames.kz/en/page/bilety"))
        bot.send_message(call.message.chat.id,
                         f"<b>BENEFITS AND DISCOUNTS FOR SPECTATORS OF THE 5TH WORLD NOMAD GAMES:</b>",
                         parse_mode='html')

        bot.send_message(call.message.chat.id,
                         f"<b>1.Free tickets are provided for the following categories of citizens::\n</b>"
                         f"1) children 0-5 years old, without a seat;\n"
                         f"2) disabled people from groups I and II.;\n<b>Note: Free tickets are only available at offline ticket offices with the appropriate document.</b>\n"
                         f"<b>2. Discounts on tickets are provided for the following categories of citizens:</b>"
                         f"\n1) school tariff (from 6 to 18 years old) - 50% of the basic tariff;;\n"
                         f"\n2)pension tariff - 50% of the basic tariff.\n"
                         f"<b>Note: discount tickets can only be purchased at offline ticket offices upon presentation of the appropriate document.</b>\n"
                         f"Free tickets and discounts for school students and pensioners do not apply to the Opening Ceremony of the Games."
                         f"Free tickets do not apply to the final of the Kokpar game.", parse_mode='html',
                         reply_markup=btn1)


bot.polling(none_stop=True, interval=0)
