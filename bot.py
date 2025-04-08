
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت
TOKEN = "7848391242:AAHqvB5bbS6puxT-d25YByBmn_COxl_c7Gw"
bot = telebot.TeleBot(TOKEN)

# رسالة البداية
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("زيارة الروابط", callback_data="visit_links"),
        InlineKeyboardButton("الاشتراك بالقنوات", callback_data="join_channels")
    )
    keyboard.row(
        InlineKeyboardButton("رصيدي", callback_data="my_balance"),
        InlineKeyboardButton("السحب", callback_data="withdraw")
    )

    bot.send_message(message.chat.id,
        f"مرحباً {user}!\n\nاهلاً بك في بوت المهام والربح.\nاختر من القائمة أدناه:",
        reply_markup=keyboard
    )

# ردود الأزرار
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    if call.data == "visit_links":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "لا توجد روابط حالياً، تابعنا لاحقاً.")
    
    elif call.data == "join_channels":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "لا توجد قنوات حالياً، سيتم إضافتها قريباً.")
    
    elif call.data == "my_balance":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "رصيدك الحالي: 0.00000000 LTC")
    
    elif call.data == "withdraw":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "للسحب، أرسل عنوان محفظتك ومبلغ السحب (قريباً).")

# تشغيل البوت
bot.infinity_polling()
