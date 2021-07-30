from telethon import TelegramClient,events
import pandas as pd

api_id = 1608914
api_hash = 'd14e4656d092e2e6aba94f60bb7c58a6'
client = TelegramClient('first', api_id, api_hash)
client.start()

print('go')
#
@client.on(events.NewMessage)
async def handler(event):
    resuts = []
    frame = pd.DataFrame(columns=['id','username','phone','first_name','lastname'])
    if event.original_update.message.peer_id.channel_id == 1592229178:
            print('start')
            b = await client.get_participants(1536898630,aggressive=True)
            for zi,i in enumerate(b):
                frame.loc[zi] = [i.id,i.username,i.phone,i.first_name,i.last_name]
                print(i.id,i.username,i.phone,i.first_name,i.last_name)

    frame.to_csv('1536898630.csv', mode='a', index=False,sep=';', encoding='cp1251', errors='ignore')
#     if event.original_update.chat_id == 515226529:



# print(client.get_participants(-100515226529))
# async def qwe():
#
#     chat = 515226529
#     # q = await client.get_participants(chat,limit=10)
#     # print(q)
#     all_participants = []

# # '1121648983'
# # for i in client.get_dialogs():
# #     if i.name == 'Реальный запуск за 3 дня':
# #         print(i.message.peer_id.channel_id)
# #
# if __name__ == '__main__':
#
#     asyncio.run(handler())
client.run_until_disconnected()

