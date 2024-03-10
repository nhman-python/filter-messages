import logging
from utilities import check_message, is_admin_message
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

API_ID = 1234
API_HASH = "SDFGH"
PHONE_NUMBER = "+97255----"
SESSION_NAME = "filter-message"
GROUP_ID_FILTER = -100
app = Client(SESSION_NAME, api_hash=API_HASH, api_id=API_ID, phone_number=PHONE_NUMBER)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Loggers
logger = logging.getLogger(__name__)


@app.on_message((filters.text | filters.caption) & filters.group & ~filters.me)
async def filter_words(client: Client, message: Message):
    if message.chat.id != GROUP_ID_FILTER:
        return
    message_text = message.text or message.caption
    matched_action = check_message(message_text.lower())
    if matched_action:
        user_id = message.from_user.id if message.from_user else message.sender_chat.id
        if await is_admin_message(client, message):
            await message.delete()
            logger.info(f"Admin message deleted: {message_text}")
        elif matched_action == "ban":
            await client.ban_chat_member(message.chat.id, user_id)
            logger.info(f"User banned for message: {message_text}")
        elif matched_action == "restrict":
            await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=False))
            logger.info(f"User restricted for message: {message_text}")
        elif matched_action == "delete":
            await message.delete()
            logger.info(f"Message deleted: {message_text}")


if __name__ == '__main__':
    app.run()
