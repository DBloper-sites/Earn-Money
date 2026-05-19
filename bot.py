from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8983737799:AAEOfdwUx_aSN7qMrQ0N1m6T9OT0d2p1UFw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""💸 Зарабатывай деньги онлайн вместе с Money FAST EARN Tool!

🔥 Что можно делать:
• 🎮 Тестировать новые игры
• 📋 Проходить опросы от компаний
• 🌐 Проверять и тестировать сайты
• 📱 Выполнять простые онлайн-задания
• 💰 И многое другое!

🚀 Начни зарабатывать уже сейчас прямо со своего телефона!
""")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен")
app.run_polling()
