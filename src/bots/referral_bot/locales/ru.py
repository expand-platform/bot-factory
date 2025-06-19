from telebot.types import BotCommand
#? bot engine
from bot_engine.languages.Locale import Locale
from bot_engine.data.Users import USER_ACTIONS

#? constats
from bots.referral_bot.config.BotCommands import BOT_COMMANDS
from bots.referral_bot.config.BotButtons import BOT_BUTTONS

from bots.referral_bot.data.NotionPages import NOTION_PAGE
from bots.referral_bot.data.TelegramLinks import TELEGRAM_LINKS


RU_LOCALE = Locale(
    language_name="ru",
    
    command_descriptions = {
        BOT_COMMANDS.start: "Старт",
        BOT_COMMANDS.conditions: "Условия",
        BOT_COMMANDS.payment: "Сколько заработаю?",
        BOT_COMMANDS.about: "О платформе EXPAND",     
        BOT_COMMANDS.info: "Разделы и справка",
    },

    button_texts = {
        BOT_BUTTONS.languages: ["Русский", "Українська"],
    },

    messages= { 
        BOT_COMMANDS.start: [
            f"👋 Привет!\n\nЭто — реферальный бот Дамира: создателя [«Платформы EXPAND»]({NOTION_PAGE.home}) и [бота для изучения программирования]({TELEGRAM_LINKS.platform_bot_link})",
            f"Ты *правда* можешь подзаработать деньжат, если поможешь мне выполнить одно задание.\n\nНажми /{BOT_COMMANDS.conditions}, чтобы узнать детали задачи — и сколько я за это плачу",
        ], 

        
        BOT_COMMANDS.conditions: [
        f"🔗 *Что нужно сделать?*\n\nЯ — учитель по программированию. Я ищу способных студентов, которые будут у меня учиться — и ты можешь помочь мне с поиском:\n\n1. ✍ Ты пишешь своим друзьям и знакомым и предлагаешь им записаться на бесплатный *вводный урок* к классному учителю программирования (я правда классный учитель, иначе кто сделал все эти [материалы]({NOTION_PAGE.home}) и [бот]({TELEGRAM_LINKS.platform_bot_link}), а?)\n\n2. 🤝 Если твой друг или подруга согласятся учиться у меня, они *оплачивают первый месяц учёбы* (после знакомства со мной и первого вводного урока)\n\n3.  После оплаты я перевожу часть их денег тебе *прямо на карту* 💳.\n\n💰 Сумму можешь узнать в /{BOT_COMMANDS.payment} ",
        ],


        BOT_COMMANDS.payment: [
            f"🌱 Уровень 1: *500 грн* за первого студента",
            f"🌿 Уровень 2: *1000 грн* за второго студента",
            f"🌵 Уровень 3: *1500 грн* за третьего студента",
            f"🌳 Уровень 4: *2000 грн* за четвёртого студента",
            f"🌗 Уровень 5: Индивидуальные условия оплаты",
            f"Я работаю честно: получил оплату от твоих ребят — перевёл деньги тебе 💳. Win-win",
            f"Сколько стоит обучение: /{BOT_COMMANDS.prices}",
            f"Детальнее обо мне можешь узнать в /{BOT_COMMANDS.about}"
        ],
        
        BOT_COMMANDS.prices: [
            f" *Сколько стоит обучение у Дамира?*",
            f"⭐ Персональные уроки: от 3000 грн в месяц",
            f"⏳ Урок длится 120 минут",
            f"🍀 4 урока на месяц - по выходным",
            f"➕ В цену входят домашка, помощь с задачами посреди недели, подбор персональных задач и проектов по мере твоего развития",
            f"Детальнее обо мне можешь узнать в /{BOT_COMMANDS.about}"
        ],
        

         BOT_COMMANDS.about: [
            f"⭐ Меня зовут Дамир. «Платформа EXPAND» — это мой авторский курс и обучение программированию.\n",
            f"Ко мне приходят люди, которые хотят научиться писать код и найти работу в IT", 
            
            f"⭐ Я могу научиться тебя HTML / CSS, JavaScript (Vue и React), Python, PHP и помочь развить навыки фронтенд и бекенд-разработчика.",

            f"📚 Ты можешь начать обучение на платформе прямо сейчас, за это не нужно платить деньги:",
            f"{NOTION_PAGE.home}",
            
            f"🤖 Я разработал бот для интересного изучения программирования: {TELEGRAM_LINKS.platform_bot}",
            
            f"🤙 Написать лично: {TELEGRAM_LINKS.damir_teacher}",
            f"Условия реферальной программы: /{BOT_COMMANDS.conditions}",
        ], 
         
        
        BOT_COMMANDS.info: [
            f"*Основные разделы*",
            
            f"🀄 Главная страница Платформы: \n{NOTION_PAGE.home}\n\n⭐ /{BOT_COMMANDS.start} — Старт\n⭐ /{BOT_COMMANDS.conditions} — Условия\n⭐ /{BOT_COMMANDS.payment} — Сколько заработаю?\n⭐ /{BOT_COMMANDS.about} — О платформе EXPAND\n⭐ /{BOT_COMMANDS.info} — Разделы и справка\n",

            f"❓ Задать вопрос: {TELEGRAM_LINKS.damir_teacher}"
        ],
    }
)
