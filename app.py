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
        [InlineKeyboardButton("🎁 RESGATAR PRESENTE", url="https://t.me/Jhontipss_bot?start=w52112396")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(mensagem, reply_markup=reply_markup)

def main():
    if not TOKEN:
        raise ValueError("A variável BOT_TOKEN não foi configurada no Render.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
