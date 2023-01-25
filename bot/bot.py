from bot import schemas, http


class BaseBotInterface:

    def __init__(self, token):
        self.token = token

    TELEGRAM_BASE_URL = "https://api.telegram.org/bot"
    TELEGRAM_SET_WEBHOOK_URL = "/setWebhook"
    TELEGRAM_SEND_MESSAGE_URL = "/sendMessage"
    TELEGRAM_REMOVE_WEBHOOK = '/deleteWebhook'
    TELEGRAM_GET_CUSTOMER_INFO = '/getChatMember'
    TELEGRAM_GET_WEBHOOK_INFO = '/getWebhookInfo'

    async def set_webhook(self) -> bool:
        payload = schemas.WebhookPayload(url=f"{config.domain}/bots/telegram/webhook{self.token}")
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_SET_WEBHOOK_URL
        req = await http.post_request(url=url, payload=payload.dict())
        return req.status_code == 200

    async def delete_webhook(self) -> bool:
        payload = schemas.WebhookPayload(url=f"{config.domain}/bots/telegram/webhook{self.token}")
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_REMOVE_WEBHOOK
        req = await http.post_request(url=url, payload=payload.dict())
        return req.status_code == 200

    async def get_info(self, chat_id: str, user_id: str) -> schemas.TelegramMember:
        payload = schemas.GetUserInfo(chat_id=chat_id, user_id=user_id)
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_GET_CUSTOMER_INFO
        req = await http.post_request(url=url, payload=payload.dict())
        return schemas.TelegramMember(**req.json()['result'])

    async def send_message(self, chat_id: str, message: str) -> bool:
        message = schemas.ResponseToMessage(chat_id=chat_id, text=message)
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_SEND_MESSAGE_URL
        req = await http.post_request(url=url, payload=message.dict())
        return req.status_code == 200

    async def set_keyboard(self, chat_id: str, message: str, answer: list) -> bool:
        reply_markup = schemas.ReplyMarkup(keyboard=[answer])
        message = schemas.KeyboardResponse(chat_id=chat_id, text=message, reply_markup=reply_markup)
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_SEND_MESSAGE_URL
        req = await http.post_request(url=url, payload=message.dict())
        return req.status_code == 200

    async def get_webhook_info(self) -> schemas.TelegramGetWebhookInfo:
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_GET_WEBHOOK_INFO
        req = await http.get_request(url=url)
        return req.json()
