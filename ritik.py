from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Update
from telegram.ext import Application,ChatJoinRequestHandler,ContextTypes

TOKEN="8685961345:AAGwgqFhhVMbJOsBLIysT3ddsLCBYaeMp_g"
VIP="https://t.me/+GA2vczfFu4k1MTZl"
NUM="https://t.me/+dzfhjbg1IS0xY2Nl"
BEN="https://t.me/+8mQSkNmLeWg3NWU1"

TEXT="""<b>✅ BIG / SMALL + NUMBER
PREDICTION HACK</b>

💰 <b>OFFER ₹300 FREE DEPOSIT OF
FIRST MEMBER</b> 💎

🔥 <b>AAP AGAR FIRST MEMBER HAMARE VIP
CHANNEL AUR NUMBER CHANNEL ME JOIN HOTE HO
TO ₹300 KA FREE DEPOSIT MILEGA 🎁</b>"""

async def send(u:Update,c:ContextTypes.DEFAULT_TYPE):
    kb=InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 VIP CHANNEL",url=VIP)],
        [InlineKeyboardButton("🔢 NUMBER CHANNEL",url=NUM)],
        [InlineKeyboardButton("🎁 VIP BENEFITS",url=BEN)]
    ])
    await c.bot.send_message(
        u.chat_join_request.user_chat_id,
        text=TEXT,
        parse_mode="HTML",
        reply_markup=kb
    )
app=Application.builder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(send))
print("BOT STARTED")
app.run_polling()