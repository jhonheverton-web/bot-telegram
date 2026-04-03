from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ChatJoinRequestHandler,
)
import os

TOKEN = os.getenv("BOT_TOKEN")

LINK_BOTAO = "https://t.me/Jhontipss_bot?start=w52112396"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name or "meu amigo"

    mensagem = f"""👋 Fala {first_name}, seja muito bem-vindo ao meu canal de ODDS ALTAS!!⚡️

🎁 Pra começar com o pé direito, vou te dar a oportunidade de participar do meu grupo de alavancagem totalmente de graça!

👇 Clique no botão abaixo e resgate seu presente agora mesmo!"""

    keyboard = [
        [InlineKeyboardButton("🎁 RESGATAR PRESENTE", url=LINK_BOTAO)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(mensagem, reply_markup=reply_markup)

async def aprovar_entrada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request

    try:
        await join_request.approve()
        print(f"Entrada aprovada: {join_request.from_user.first_name} | Grupo: {join_request.chat.title}")
    except Exception as e:
        print(f"Erro ao aprovar entrada: {e}")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN não configurado.")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(ChatJoinRequestHandler(aprovar_entrada))

    print("Bot rodando...")
    application.run_polling()

if __name__ == "__main__":
    main()
