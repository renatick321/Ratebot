from config import client, CHANNEL_ID


async def get_members_id():
    data = await client.get_chat_members(CHANNEL_ID)
    lst = await client.get_chat_members(CHANNEL_ID, filter="administrators")
    return list(map(lambda x: x.user.id, filter(lambda x: x not in lst, data)))


async def kick_chat_member(user_id):
    await client.kick_chat_member(CHANNEL_ID, user_id)
    await client.unban_chat_member(CHANNEL_ID, user_id)