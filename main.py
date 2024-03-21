import time
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! '🎲Tavakkalni Top' o'yini boshlash uchun /play buyrug'ini bering!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("O'yinni boshlash uchun /play tugmasini bosing!")


async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["1", "2", "3"], ["4", "5", "6"]]
    await update.message.reply_text(
        "Quyidagi sonlarning birini tavakkal qiling!",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False, resize_keyboard=True
        ),
    )


async def dice_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        choice = int(update.message.text)
        if 0 < choice < 7:
            r = await update.message.reply_dice(emoji="")
            time.sleep(4)
            if choice == r.dice.value:
                await update.message.reply_text(
                    f"{update.effective_user.first_name} yutdingiz!🥳"
                )
            else:
                await update.message.reply_text(
                    f"{update.effective_user.first_name} yutqazdingiz☹️, yana urinib ko'ring!"
                )
        else:
            await update.message.reply_text(
                "Iltimos faqat 1 dan 6 gacha bo'lgan sonlardan tanlang!"
            )
    except:
        await echo(update, context)


def main() -> None:
    app = Application.builder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", dice))
    app.add_handler(MessageHandler(filters.TEXT, dice_result))
    app.add_handler(MessageHandler(filters.ALL, echo))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
