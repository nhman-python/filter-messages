from utilities import check_message, is_admin_message
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

API_ID = 1234
API_HASH = "SDFGH"
PHONE_NUMBER = "+97255----"
SESSION_NAME = "filter-word"
GROUP_ID_FILTER = -123456
app = Client(SESSION_NAME, api_hash=API_HASH, api_id=API_ID, phone_number=PHONE_NUMBER)


@app.on_message(filters.text & filters.caption & filters.group & ~filters.me, group=GROUP_ID_FILTER)
async def filter_words(client: Client, message: Message):
    message_text = message.text or message.caption
    matched_action = check_message(message_text)
    if matched_action:
        user_id = message.from_user.id if message.from_user else message.sender_chat.id
        if await is_admin_message(client, message):
            await message.delete()
        elif matched_action == "ban":
            await client.ban_chat_member(message.chat.id, user_id)
        elif matched_action == "restrict":
            await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=False))
        elif matched_action == "delete":
            await message.delete()


if __name__ == '__main__':
    app.run()
