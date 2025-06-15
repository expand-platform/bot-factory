from dataclasses import dataclass, field

@dataclass
class Command:
    name: str
    description: str

@dataclass
class BotCommands:
    start: Command = field(default_factory=lambda: Command(name="start", description="Старт"))
    add_product: Command = field(default_factory=lambda: Command(name="add", description="Додати товар"))
    remove_product: Command = field(default_factory=lambda: Command(name="remove", description="Видалити товар"))
    parse: Command = field(default_factory=lambda: Command(name="parse", description="Перевiрити змiни в товарах"))
    set_time: Command = field(default_factory=lambda: Command(name="schedule", description="Задати час парсингу"))
    info: Command = field(default_factory=lambda: Command(name="info", description="Звiт"))
    menu: Command = field(default_factory=lambda: Command(name="menu", description="Всi команди бота"))

bot_commands = BotCommands()
