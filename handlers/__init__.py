from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart

from .commands import start_handler, user_info_handler, help_handler
from .panel import user_statistic_handler, admin_panel_handler, ads_main_handler

router = Router(name="core")

# Commands handler functions
router.message.register(start_handler, CommandStart())
router.message.register(help_handler, Command("help"))
router.message.register(user_info_handler, Command("info"))

# Admin handler functions
router.message.register(admin_panel_handler, Command("panel"))
router.message.register(user_statistic_handler, F.text == "📊 Hisobot")
router.message.register(ads_main_handler, F.text == "💸 Reklama")
