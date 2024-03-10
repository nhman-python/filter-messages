import json
import re
import shelve

from cachetools import TTLCache
from pyrogram import Client
from pyrogram.enums import ChatMembersFilter

admins_cache_file = 'admins_cache'

with shelve.open(admins_cache_file) as admins_db:
    admins_lists = admins_db.get('admins_lists', TTLCache(maxsize=1024, ttl=600))

with open("filter-list.json", "r") as f:
    filters_list = json.load(f)


def check_message(message_text):
    """
    check if the message contain not allow words and if it does return the action
    :param message_text: the message text to check
    :return: action on block word None otherwise
    """
    filter_patterns = {}
    for action, words in filters_list.items():
        filter_patterns[action] = re.compile(r"\b({})\b".format("|".join(map(re.escape, words))), re.IGNORECASE)
    for action, pattern in filter_patterns.items():
        if pattern.search(message_text):
            return action
    return None


async def is_admin_message(client: Client, message: Message) -> bool:
    """
    Check if a message is from an admin of the group or not
    :param client: client instance
    :param message: the message to check
    :return: True if the message is from an admin, False otherwise
    """
    c_id = message.chat.id
    if message.from_user:
        u_id = message.from_user.id
    else:
        u_id = message.sender_chat.id
    if c_id in admins_lists:
        return u_id in admins_lists[c_id]

    c_admin = [admin.user.id async for admin in client.get_chat_members(c_id, filter=ChatMembersFilter.ADMINISTRATORS)]
    admins_lists[c_id] = c_admin
    with shelve.open(admins_cache_file, writeback=True) as admins_cache:
        admins_cache['admins_lists'] = admins_lists
    return u_id in admins_lists[c_id] or c_id == u_id
