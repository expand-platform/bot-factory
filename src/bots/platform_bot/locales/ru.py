from telebot.types import BotCommand
#? bot engine
from bot_engine.languages.Locale import Locale
from bot_engine.data.Users import USER_ACTIONS

#? constats
from bots.platform_bot.config.BotCommands import BOT_COMMANDS
from bots.platform_bot.config.Buttons import BOT_BUTTONS

from bots.platform_bot.data.NotionPages import NOTION_PAGE
from bots.platform_bot.data.TelegramLinks import TELEGRAM_LINKS


RU_LOCALE = Locale(
    language_name="ru",
    
    command_descriptions = {
        BOT_COMMANDS.start: "Старт",
        BOT_COMMANDS.about: "Куда я попал?",     
        BOT_COMMANDS.prices: "Цены",
        BOT_COMMANDS.ask: "Задать вопрос",
        BOT_COMMANDS.help: "Разделы и справка",
    },

    button_texts = {
        BOT_BUTTONS.languages: ["Русский", "Українська"],
    },

    messages= { 
        BOT_COMMANDS.start: [
            "👋 Welcome! Ты попал на «Платформу EXPAND» — дом для всех программистов",
            "Это — бот для бесплатного изучения JavaScript, Python, PHP и других языков программирования",

            "Меня зовут Дамир, я — создатель «Платформы EXPAND»",
            
            f"Переходи в интересующий тебя раздел и начинай осваиваться:",
            
            f"🤖 HTML / CSS: {NOTION_PAGE.html_css}\n⚡ JavaScript: {NOTION_PAGE.javascript}\n🍏 Vue: {NOTION_PAGE.vue}\n\n💎 Python: {NOTION_PAGE.python}\n🐘 PHP: {NOTION_PAGE.php}\n🔗 NodeJS: {NOTION_PAGE.node_js}\n🐞 Фулл-стек: {NOTION_PAGE.full_stack}\n\n🔲 Задачи: {NOTION_PAGE.tasks}\n🏆 Проекты: {NOTION_PAGE.projects}",
        ], 

        
        BOT_COMMANDS.prices: [""
        "🔗 Цены на групповые и индивидуальные занятия можно посмотреть тут:",
        f"{NOTION_PAGE.prices}",
        f"Вводный урок и первая консультация — бесплатно, в /{BOT_COMMANDS.ask}",
        ],


        BOT_COMMANDS.ask: [
            f"🌗 Ты можешь задать вопрос мне лично:",
            f"{TELEGRAM_LINKS.best_prepod}",
        ],
        

         BOT_COMMANDS.about: [
            f"⭐ Меня зовут Дамир. «Платформа EXPAND» — это мой авторский курс и обучение программированию.\n"
            f"Ко мне приходят люди, которые хотят научиться писать код и найти работу в IT", 
            
            f"⭐ Я могу научиться тебя HTML / CSS, JavaScript (Vue и React), Python, PHP и помочь развить навыки фронтенд и бекенд-разработчика.",

            f"⭐ Я лично готовлю все материалы, видео, задачи и проекты — и стараюсь делать всё это с изюминкой",

            f"⭐ Ты можешь начать обучение на платформе прямо сейчас, за это не нужно платить деньги:",
            f"{NOTION_PAGE.home}",
        ], 
         
        
        BOT_COMMANDS.help: [
            f"*Основные разделы*",
            
            f"🀄 Главная страница Платформы: \n{NOTION_PAGE.home}\n\n",

            f"*Языки*:\n\n🤖 HTML / CSS: {NOTION_PAGE.html_css}\n⚡ JavaScript: {NOTION_PAGE.javascript}\n🍏 Vue: {NOTION_PAGE.vue}\n\n💎 Python: {NOTION_PAGE.python}\n🐘 PHP: {NOTION_PAGE.php}\n🔗 NodeJS: {NOTION_PAGE.node_js}\n🐞 Фулл-стек: {NOTION_PAGE.full_stack}",
            
            f"*Задачи и проекты*\n\n🔲 Задачи: {NOTION_PAGE.tasks}\n🏆 Проекты: {NOTION_PAGE.projects}",
            
            f"*Цены и контакты*\n\n🌓 Если ты ищешь учителя / наставника, тебе в /{BOT_COMMANDS.prices}\n\n💁‍♂️ Если нужна личная помощь, я тут: /{BOT_COMMANDS.ask}",
        ],
        

        #? ADMIN
        #? User Actions
        USER_ACTIONS.SLASH_COMMAND: [
            "{first_name} @{username} перешёл в /{slash_command}",
        ]
    }
)
