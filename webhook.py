from flask import render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def new_bot_bump():
    json = request.get_json()
    type = json['type']
    data = json['data']
    if type == "new_bot_bump" or "new_server_bump":
        print(f"LOG: Новый ап!\nID {date[id]}")
    elif type == "test_webhook_message":
        print(f"LOG: Тестовое сообщение сработало.")   
    return "Успешно!"
    
 if __name__ == "__main__": app.run(port=80)  
