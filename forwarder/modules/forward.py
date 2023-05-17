import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='bot.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
)

import time
import datetime


from typing import Union

from telegram import Update, Message, MessageId
from telegram.error import ChatMigrated
from telegram.ext import MessageHandler, filters, ContextTypes

from forwarder import bot, CONFIG, REMOVE_TAG, LOGGER
from forwarder.utils import get_source, get_destenation


async def send_message(message: Message, chat_id: int) -> Union[MessageId, Message]:
    if REMOVE_TAG:
        return await message.copy(chat_id)
    return await message.forward(chat_id)


async def forwarder(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    source = update.effective_chat

    if not message or not source:
        return

    for chat_id, chat_name in get_destenation(source.id, CONFIG).items():
        try:
            await send_message(message, chat_id)
            an = datetime.datetime.now()
            tarih = datetime.datetime.strftime(an, '%x, %X')

            print(tarih)
            print("Waiting")
            logging.info(f"Waiting")
            time.sleep(3)

            LOGGER.info(f"Message forwarded from {source.title} to {chat_name} ({chat_id})")
            logging.info(f"Message forwarded from {source.title} to {chat_name} ({chat_id})")
        except ChatMigrated as err:
            await send_message(message, err.new_chat_id)
            LOGGER.warning(
                f"Chat {chat_id} has been migrated to {err.new_chat_id}!! Edit the config file!!"
            )
        except Exception:
            LOGGER.warning(f"Failed to forward message from {source.title} to {chat_name} ({chat_id})")





FORWARD_HANDLER = MessageHandler(
    filters.Chat(get_source(CONFIG)) & ~filters.COMMAND & ~filters.StatusUpdate.ALL,
    forwarder,
)
bot.add_handler(FORWARD_HANDLER)