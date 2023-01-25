from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class WebhookPayload(BaseModel):
    url: str


class Chat(BaseModel):
    last_name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    first_name: Optional[str]
    username: Optional[str]


class From(BaseModel):
    last_name: Optional[str]
    id: Optional[str]
    first_name: Optional[str]
    user_name: Optional[str]
    is_bot: Optional[str]


class ReplyMessage(BaseModel):
    date: Optional[int]
    chat: Optional[Chat]
    message_id: Optional[int]
    text: str


class Message(BaseModel):
    date: int
    chat: Optional[Chat]
    message_id: Optional[str]
    from_field: Optional[From]
    text: str

    class Config:
        fields = {
            "from_field": "from",
        }


class TelegramRequestBody(BaseModel):
    message: Optional[Message]

    def is_email(self):
        try:
            return EmailStr.validate(self.message.text)
        except ValueError:
            return False


class ChatGroup(BaseModel):
    id: Optional[int]
    title: Optional[str]
    type: Optional[str]


class MockVal(BaseModel):
    rand_int: Optional[int]


class OtherChatMember(BaseModel):
    user: Optional[From]
    status: Optional[str]


class MyChatMember(BaseModel):
    rand_int: Optional[int]
    chat: Optional[ChatGroup]
    from_field: Optional[From] = Field(alias="from")
    date: Optional[int]
    old_chat_member: Optional[OtherChatMember]
    new_chat_member: Optional[OtherChatMember]


class MessageBodyModel(BaseModel):
    update_id: Optional[int]
    message: Optional[Message]
    my_chat_member: Optional[MyChatMember]
    reply_to_message: Optional[ReplyMessage]


class ResponseToMessage(BaseModel):
    chat_id: Optional[str]
    text: str
    parse_mode: Optional[str] = "Markdown"

    class Config:
        orm_mode = True


class ReplyMarkup(BaseModel):
    keyboard: Optional[list]
    resize_keyboard: Optional[bool] = True


class KeyboardResponse(BaseModel):
    chat_id: Optional[str]
    text: str
    parse_mode: Optional[str] = "Markdown"
    reply_markup: Optional[ReplyMarkup]

    class Config:
        orm_mode = True


class GetUserInfo(BaseModel):
    chat_id: Optional[str]
    user_id: Optional[str]


class User(BaseModel):
    id: Optional[str]
    language_code: Optional[str]
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None


class TelegramMember(BaseModel):
    user: Optional[User]


class TelegramGetWebhookInfo(BaseModel):
    url: Optional[str]
    has_custom_certificate: Optional[bool]
    pending_update_count: Optional[int]
    max_connections: Optional[int]
    ip_address: Optional[str]