import requests

TOKEN = ""

auth_json = {
  "Authorization": f"Bot {TOKEN}",
  "User-Agent": "DiscordBot ($url, $10)"
}

def get_user(id:int):
    return requests.get(f"https://discord.com/api/v10/users/{id}", headers=auth_json).json()
  

def send_message(id:int, chanel:int):
    dm = requests.post(f"https://discord.com/api/v10/users/@me/channels", headers=auth_json, json={"recipient_id": id}).json()['id']
    message_dm = {
        "content": "Привет! Спасибо за Ап!"
    }
    user = get_user(id)


    message_channel = {
        "content": f"{user['username']}#{user['discriminator']}(``{id}``) Апнул бота."+ f"\nJSON ```\n{user}```"
    }
    requests.post(f'https://discord.com/api/v10/channels/{dm}/messages', headers=auth_json,json=message_dm)
    requests.post(f'https://discord.com/api/v10/channels/{channel}/messages', headers=auth_json,json=message_channel)
  
