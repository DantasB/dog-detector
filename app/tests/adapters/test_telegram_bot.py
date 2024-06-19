from unittest.mock import MagicMock
from app.src.adapters.telegram_bot import TelegramBot


def test_send_image():
    mock_bot = MagicMock(spec=TelegramBot)

    mock_bot.send_image("test_image")

    mock_bot.send_image.assert_called_once_with("test_image")
