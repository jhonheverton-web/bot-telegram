from flask import Flask, request
import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])

API = f"https://api.telegram.org/bot{TOKEN}"
app = Flask(__name__)

def tg(method, data):
    r = requests.post(f"{API}/{method}", json=data, timeout=20)
    return r.json()

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json(silent=True) or {}

    join_req = update.get("chat_join_request")
    if join_req:
        user = join_req["from"]
        user_id = user["id"]
        user_chat_id = join_req["user_chat_id"]
        first_name = user.get("first_name", "meu amigo")

        tg("sendMessage", {
            "chat_id": user_chat_id,
            "text": (
                f"Oi, {first_name} \n\n" "Clique aqui para garantir seu acesso ao meu GRUPO VIP DE VELAS ROSAS e a minha triplicagem de banca. 👇"
            ),
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "🏆 VIP EXCLUSIVO",
                        "url": "https://t.me/chefedoaviatooorbot?start=w52250639"
                    }
                ]]
            }
        })

        tg("approveChatJoinRequest", {
            "chat_id": CHAT_ID,
            "user_id": user_id
        })

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
