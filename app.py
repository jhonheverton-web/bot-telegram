from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ChatJoinRequestHandler,
)
import os

TOKEN = os.getenv("BOT_TOKEN")

LINK_BOTAO = "https://t.me/Jhontipssbot?start=w52972625"

MENSAGEM = """Fala jogador! 👊

Já vou liberar seu acesso ao MAIOR GRUPO DE APOSTAS ESPORTIVAS DO BRASIL!

A única coisa que você PRECISA fazer é seguir um simples passo a passo..
E logo em seguida, vou liberar um presente especial só pra você"""

def get_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("LIBERAR PRESENTE ESPECIAL 🎁", url=LINK_BOTAO)]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENSAGEM, reply_markup=get_keyboard())

async def aprovar_entrada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user

    try:
        # Aprova entrada
        await join_request.approve()

        # TENTA enviar no privado
        try:
            await context.bot.send_message(
                chat_id=user.id,
                text=MENSAGEM.replace("jogador", user.first_name),
                reply_markup=get_keyboard()
            )
            print(f"Mensagem enviada no privado para {user.first_name}")

        except Exception as e:
            print(f"Não conseguiu enviar no privado: {e}")

        print(f"Entrada aprovada: {user.first_name}")

    except Exception as e:
        print(f"Erro geral: {e}")

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
