from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus


@Client.on_chat_member_updated(filters.group)
async def welcome(bot, message: ChatMemberUpdated):
    me = await bot.get_me()
    if (
         message.old_chat_member
         or message.old_chat_member.status == ChatMemberStatus.BANNED 
     ):
         return

    if not message.new_chat_member.user.id == me.id:
        ozz=await bot.send_message(chat_id=message.chat.id, text="heyy")
        await ozz.delete()
    else:
        ozz=await bot.send_message(chat_id=message.chat.id, text="heyy")
        await ozz.delete()
