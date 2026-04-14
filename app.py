async def aprovar_entrada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user

    try:
        # Aprova o usuário
        await join_request.approve()

        # Mensagem personalizada
        mensagem = f"""Fala {user.first_name}! 👊

Já liberei sua entrada para o MAIOR GRUPO DE APOSTAS ESPORTIVAS DO BRASIL!

A única coisa que você PRECISA fazer é seguir um simples passo a passo..
E logo em seguida, vou liberar um presente especial só pra você"""

        # Botão
        keyboard = [
            [InlineKeyboardButton("LIBERAR PRESENTE ESPECIAL 🎁", url=LINK_BOTAO)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envia no grupo
        await context.bot.send_message(
            chat_id=join_request.chat.id,
            text=mensagem,
            reply_markup=reply_markup
        )

        print(f"Entrada aprovada: {user.first_name} | Grupo: {join_request.chat.title}")

    except Exception as e:
        print(f"Erro ao aprovar entrada: {e}")
