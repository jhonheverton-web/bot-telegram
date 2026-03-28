from flask import Flask, request
import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"
app = Flask(__name__)

def tg(method, data):
    r = requests.post(f"{API}/{method}", json=data, timeout=10)
    try:
        result = r.json()
    except Exception:
        result = {"ok": False, "raw": r.text}
    print(f"{method}: {result}")
    return result

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

        # 1) aprova primeiro
        tg("approveChatJoinRequest", {
            "chat_id": chat_id,
            "user_id": user_id
        })

        # 2) manda a mensagem depois
        tg("sendMessage", {
            "chat_id": user_chat_id,
            "text": (
                f"Oi, {first_name} 👋\n\n"
                "Clique aqui para garantir sua vaga no meu GRUPO VIP DE VELAS ROSAS "
                "e na minha TRIPLICAGEM DE BANCA, de forma 100% gratuita 👇"
            ),
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "🏆 VIP EXCLUSIVO",
                        "url": "https://t.me/chefedoaviatooorbot?start=w52112396"
                    }
                ]]
            }
        })

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
