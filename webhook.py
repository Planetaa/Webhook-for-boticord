from flask import render_template
from flask import Flask, request
from send_message import send_message

app = Flask(__name__)

CHANNEL = #ID

@app.route('/webhook', methods=['POST'])
def new_bot_bump():
    try:
        json = request.get_json()
        type = json['type']
        data = json['data']
    except:
        return "Ошибка."
    if type == "new_bot_bump" or "new_server_bump":
        send_message(date['id'], CHANNEL)
        print(f"LOG: Новый ап!\nID {date[id]}")
    elif type == "test_webhook_message":
        print(f"LOG: Тестовое сообщение сработало.")   
    return "Успешно!"
    
 if __name__ == "__main__": app.run(port=80)  
