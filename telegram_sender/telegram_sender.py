from typing import Any
import requests
from .models import TelegramResponse

PARSE_MODES = ['html', 'markdown']


class TelegramSender:
    def __init__(self, bot_token: str) -> None:
        self.api_url = f'https://api.telegram.org/bot{bot_token}/'

    def _http_request(self, url: str, data: dict[Any, Any]) -> dict[Any, Any]:
        return requests.post(url=url, json=data).json()

    def command(self, cmd: str, data: dict[Any, Any]) -> dict[Any, Any]:
        return self._http_request(self.api_url + cmd, data=data)

    def msg(self, chat_id: int, msg: str, parse_mode: str = 'html', notify: bool = False):
        if parse_mode not in PARSE_MODES:
            raise ValueError('parse_mode "%s" not in %s' % (parse_mode, PARSE_MODES))

        received_dict = self.command('sendMessage', data={
            'text': msg,
            'chat_id': chat_id,
            'parse_mode': 'html',
            'disable_notification': not notify}
        )

        return TelegramResponse(**received_dict)
