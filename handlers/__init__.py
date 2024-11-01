from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart

from .commands import start_handler, user_info_handler, help_handler
from .panel import user_statistic_handler, admin_panel_handler, ads_main_handler, ads_send_handler, setting_btn_handler, setting_channel_add_handler, channel_add_handler, channel_add_id_handler, channel_delete_handler, channel_delete_id_handler, exit_handler
from .users import translation_handler
from states.state import AdsState, ChannelAddState, ChannelDeleteState

router = Router(name="core")

# Commands handler functions
router.message.register(start_handler, CommandStart())
router.message.register(help_handler, Command("help"))
router.message.register(user_info_handler, Command("info"))

# Admin handler functions
router.message.register(admin_panel_handler, Command("panel"))
router.message.register(user_statistic_handler, F.text == "📊 Hisobot")
router.message.register(ads_main_handler, F.text == "💸 Reklama")
router.message.register(ads_send_handler, AdsState.ads)
router.message.register(setting_btn_handler, F.text == "🛠 Sozlamalar")

# Users handler functions
router.message.register(setting_channel_add_handler, F.text == "Kanal ulash ⛓️")
router.message.register(channel_add_handler, ChannelAddState.url)
router.message.register(channel_add_id_handler, ChannelAddState.channel_id)

router.message.register(channel_delete_handler, F.text == "Kanal uzish ⛓️‍💥")
router.message.register(channel_delete_id_handler, ChannelDeleteState.channel_id)

router.message.register(exit_handler, F.text == "❌")

router.message.register(translation_handler)
