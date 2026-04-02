from flask import Flask, request
import requests
import os
from threading import Thread

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"
app = Flask(__name__)

session = requests.Session()

def tg(method, data):
    r = session.post(f"{API}/{method}", json=data, timeout=5)
    try:
        result = r.json()
    except Exception:
        result = {"ok": False, "raw": r.text}
    print(f"{method}: {result}")
    return result

def send_welcome_message(user_chat_id, first_name):
    tg("sendMessage", {
        "chat_id": user_chat_id,
        "text": (
            f"Fala, {first_name}, seja muito bem-vindo ao meu canal de ODDS ALTAS!!⚡️

🎁 Pra começar com o pé direito, vou te dar a oportunidade de participar do meu grupo de alavancagem totalmente de graça!

👇 Clique no botão abaixo e garanta sua participação agora mesmo!"
        ),
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "🎁 RESGATAR PRESENTE",
                    "url": "https://t.me/Jhontipss_bot?start=w52112396"
                }
            ]]
        }
    })

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json(silent=True) or {}
    join_req = update.get("chat_join_request")

    if join_req:
        user = join_req["from"]
        user_id = user["id"]
        user_chat_id = join_req["user_chat_id"]
        first_name = user.get("first_name", "meu amigo")
        chat_id = join_req["chat"]["id"]

        # 1) aprova imediatamente
        tg("approveChatJoinRequest", {
            "chat_id": chat_id,
            "user_id": user_id
        })

        # 2) manda a mensagem em paralelo
        Thread(
            target=send_welcome_message,
            args=(user_chat_id, first_name),
            daemon=True
        ).start()

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
