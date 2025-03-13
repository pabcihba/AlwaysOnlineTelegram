from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.functions.users import GetUsersRequest
import asyncio
# значения из my.telegram.org/apps
api_id = 12341234
api_hash = '1234123412341234'
client = TelegramClient('session_name', api_id, api_hash)
async def keep_online():
    await client.start()
    print("Вечный онлайн работает")
    while True:
        try:
            me = await client.get_me()
            if me.status:
                if me.status.__class__.__name__ == "UserStatusOffline":
                    await client(UpdateStatusRequest(offline=False))
                    # print("статус обновлён на онлайн")
                else:
                    # print("уже онлайн")
            else:
                print("не смог распознать ваш статус")
        except Exception as e:
            print(f"{e}")
        #тут можно рыпнуться
        await asyncio.sleep(10)
with client:
    client.loop.run_until_complete(keep_online())
