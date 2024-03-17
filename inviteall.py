
import aminofixfix as aminofix, concurrent.futures,time
import os

email="ZZZZZZZZ@gmail.com"
password="CONTRASEÑA"
client = aminofix.Client()
client.login(email=email,password=password)


chats = client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]


def inviteonlineusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = client.get_all_users(start=i, size=5000).profile.userId
			if onlineusers:
				for userId in onlineusers:
					print(f"{userId} Invited/")
					_ = [executor.submit(client.invite_to_chat, userId, chatx)]
			else:
				break
		for i in range(0, 20000, 250):
			publichats = client.get_public_chat_threads(type="recommended", start=i, size=5000).chatId
			chatsuin = client.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = client.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/....")
									_ = [executor.submit(client.invite_to_chat, userId, chatx)]
								except:
									pass
						else:
							break
							print("Invited All Online Users")

print("1.Invita a todos los online:")
inviteselect = input("Pon el numero: ")
if inviteselect == "1":
	inviteonlineusers()
