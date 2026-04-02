from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name or "meu amigo"

    mensagem = f"""👋 Fala {first_name}, seja muito bem-vindo ao meu canal de ODDS ALTAS!!⚡️

🎁 Pra começar com o pé direito, vou te dar a oportunidade de participar do meu grupo de alavancagem totalmente de graça!

👇 Clique no botão abaixo e garanta sua participação agora mesmo!"""

    keyboard = [
        [InlineKeyboardButton("🎁 GARANTIR PARTICIPAÇÃO", url="https://t.me/Jhontipss_bot?start=w52112396")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(mensagem, reply_markup=reply_markup)

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN não configurado.")

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot rodando...")
    application.run_polling()

if __name__ == "__main__":
    main()
