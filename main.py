import telebot
import random
from config import (ADMIN_ID, BOT_TOKEN, cs_stg3, cs_stg3_onefile, cs_stg3_deleted, cs_apps)
import json
#---------------------
#استدعائات الكورس الاول
from global_vars import  (back_term1,term1_Table_of_lectures,chose_from, networks1_lab_title, networks1_theo_title, ai_lab_title, ai_theo_title,software_engineering_lab_title, software_engineering_theo_title, multimedia_lab_title, multimedia_theo_title, compilers1_lab_title, compilers1_theo_title, english_title, operations_research_title )
from term1_keyboard import ( main_term1_keyboard, ai_lab_buttons, ai_theo_buttons, software_eng_lab_buttons, software_eng_theo_buttons, multimedia_lab_buttons, multimedia_theo_buttons, networks1_lab_buttons, networks1_theo_buttons, compilers1_lab_buttons, compilers1_theo_buttons, operation_research_buttons, english_buttons,)
#---------------------
#استدعائات الكورس الثاني
from global_vars import (back_term2,term2_Table_of_lectures, networks2_lab_title, networks2_theo_title,data_enc_lab_title,data_enc_theo_title,data_mining_lab_title,data_mining_theo_title,dis_db_lab_title,dis_db_theo_title,compilers2_lab_title,compilers2_theo_title, web_prog_title)
from term2_keyboard import (give_rating, main_term2_keyboard, main_term_select, webProgramming_buttons, networks2_lab_buttons, networks2_theo_buttons, data_mining_lab_buttons, data_mining_theo_buttons, distributed_databases_lab_buttons, distributed_databases_theo_buttons, data_encryption_lab_buttons, data_encryption_theo_buttons, compilers2_lab_buttons, compilers2_theo_buttons)

#------------------------------------------------------
#---------- initialize bot and files process ----------
#------------------------------------------------------
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

file_path = 'terms_cmd2values.json'
commands_file_path = 'terms_btn2cmd.json'

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_commands():
    with open(commands_file_path, 'r') as file:
        return json.load(file)


#----------------------------------------
#---------- check join process ----------
#----------------------------------------
def is_user_member(user_id, chat_id):
    try:
        chat_member = bot.get_chat_member(chat_id, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

def check_and_respond(message, response_function, *args):
    user = message.from_user
    first_name = user.first_name
    user_id = message.from_user.id
    required_channels = ["@cs_stg3", "@cs_stg3_onefile", "@cs_stg3_deleted", "@cs_apps"]

    all_membership_valid = all(is_user_member(user_id, chat_id) for chat_id in required_channels)

    if all_membership_valid:
        response_function(message, *args)
    else:
        bot.send_message(message.chat.id,f"⤦ اوكف {first_name} شو ما مشترك بالقنوات ⁉️🫣\nاشترك وارجع اضغط على /start\n• قناة الملازم: @cs_stg3\n• قناة الملخصات: @cs_stg3_onefile\n• قناة المهملات: @cs_stg3_deleted\n• قناة البرامج: @cs_apps")


#--------------------------------------
#---------- start process ----------
#--------------------------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    def respond(message):
        welcome_text = (
            "• شلونهم ابطالنا 😌🦾\n\n"
            "• اختار من القائمة المادة 🎛⚡️\n\n"
            "• 👨🏻‍💻المطور : @ab0_alhasan"
        )
        bot.reply_to(message, welcome_text, reply_markup = main_term_select())
    check_and_respond(message, respond)


#------------------------------------------------
#---------- press main buttons process ----------
#------------------------------------------------
#fun to print اختار من القائمة and update open specific markup buttons menus
def chose_from_markup(message, reply_markup):
    bot.reply_to(message, chose_from, reply_markup = reply_markup)

about_bot_msg = ("<b>● عن بوت @cs_stg3_bot:</b>\n\n"
        "<b>• بوت ملازم وملخصات وأشياء مساعدة لطلاب المرحلة الثالثة قسم علوم الحاسوب في كلية علوم الحاسوب وتكنولوجيا المعلومات جامعة واسط دفعة 2022-2025.</b>\n\n"
        "<b>• البوت يسهل وصول الطالب للمادة وكل شيء يخصها من ملازم أصلية ومترجمة أو ملخصات أو البرامج التي يُطبق عليها الجانب العملي.</b>\n\n"
        "<b>• مصادر البوت هي من القنوات الرئيسية للمرحلة الثالثة دفعة 2022-2025:</b>\n\n"
        "  ⏎ قناة الكورس الثاني: \nرابط القناة: @cs_stg3\n\n"
        "  ⏎ قناة الكورس الأول + ملازم السنة السابقة: \nرابط القناة: @cs_stg3_deleted\n\n"
        "  ⏎ قناة المخلصات + الملازم المترجمة + الأسئلة والحلول: \nرابط القناة: @cs_stg3_onefile\n\n"
        "  ⏎ قناة البرامج: \nرابط القناة: @cs_apps\n\n"
        "<b>• تم إنشاء البوت بتاريخ 2024/7/28 بلغة Python مع مكتبة telebot من برمجة @ab0_alhasan.</b>\n\n"
        "<b>• إذا أعجبك البوت، يمكنك تقييمه من خلال /rating.</b>\n\n\n"
        "<b>• ملاحظات ⚠:</b>\n\n"
        "  • يُستخدم البوت أساسًا عبر الأزرار الموجودة في قائمة التحكم التي تحمل رمز 🎛، بالإضافة إلى الأوامر مثل /start لتحديث البوت و /term1 لعرض قائمة الكورس الأول و /term2 لعرض قائمة الكورس الثاني. يُطلب من المستخدمين عدم إرسال أي رسائل نصية مباشرة إلى البوت.\n\n"
        "  • جميع الرسائل المتبادلة بين المستخدم والبوت تظل سرية تمامًا ولن يتم تحويلها أو مشاركتها مع أي طرف آخر. الاستثناء الوحيد هو عند استخدام أزرار قائمة تقييم البوت، حيث سيتم إرسال تقييمات المستخدم إلى المسؤول عن البوت، @ab0_alhasan، و بأمكانه معرفة المعرف واسم الطالب.\n\n"
        "  • رغم ذلك، يُنصح بعدم كتابة رسائل خاصة وذات أهمية داخل البوت، حيث لا يمكن ضمان حماية 100% للخصوصية في جميع الحالات.\n\n"
        "<b>• السورس كود للبوت مع الملفات:</b> <a href='https://github.com/AboALhasanx/cs.stg3.bot'>https://github.com/AboALhasanx/cs.stg3.bot</a>\n\n"
        "<b>✍🏻 ابـوالــحسـن: @ab0_alhasan</b>")

@bot.message_handler(func=lambda message: message.text == "🪧 عن البوت 🪧")
def about_bot(message):
    bot.reply_to(message, about_bot_msg, parse_mode='HTML')


#term1 buttons and commands----------------------

@bot.message_handler(func=lambda message: message.text == "تقييم البوت")
def return_to_term1_menu(message):
    def respond(message):
        bot.reply_to(message, chose_from, reply_markup = give_rating())
    check_and_respond(message, respond)

@bot.message_handler(commands=['rating'])
def return_to_term1_menu(message):
    def respond(message):
        bot.reply_to(message, chose_from, reply_markup = give_rating())
    check_and_respond(message, respond)

import random

@bot.message_handler(func=lambda message: message.text in ["🎖🏆 واحد عراق 😶‍🌫✋🏻", "عاش يسطا 👀🔥", "الله على الروقان ✨😌", "جيد 👍🙂", "تحجي صدك 🦦؟"])
def handle_rating(message):
    rating = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    username = message.from_user.username or "غير معروف"  # Use 'غير معروف' if username is not set

    good_response = ["حبيب اخوك 😇", "حبيبي نورتني 😌", "صدك جذب تدلل 😊"]
    veryGood_response = ["اخويا ياسطا 😎🤙🏻", "تسلم يالقالي 😴🫶", "نورك هذا لو الشمس؟ عمي منورنا 😔❤️‍🔥", "يا هلا وغلا بالعزيز 🫂❤️‍🔥", "شهادة اعتزُ بيها 😌🤝🏻", "هاي الوردة تستاهلك 🌹🫴"]
    ok_response = ["خوش 🤨", "تمام 🙄", "ماشي 🙃", "اوك 🌚", "شوكران يمحترم 😒", "مثل تقديرك 🫠"]

    if rating == "تحجي صدك 🦦؟":
        response_text = "هاي ليش 💔🗿؟ \n راسلني وكلي اذا اكو مشكلة بالبوت @ab0_alhasan"
    elif rating == "الله على الروقان ✨😌":
        response_text = random.choice(good_response)
    elif rating == "جيد 👍🙂":
        response_text = random.choice(ok_response)
    else:
        response_text = random.choice(veryGood_response)
    bot.send_message(
        ADMIN_ID,
        f"اكلك هذا {user_name} الي معرفه (@{username}) يكول \n\"{rating}\" على البوت 🫣"
    )

    # Show the main menu again
    bot.send_message(
        message.chat.id, response_text, reply_markup=main_term_select()
    )


@bot.message_handler(commands=['term1']) #command
def update_buttons(message):
    def respond(message):
        chose_from_markup(message, main_term1_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == "الكورس الاول") #button
def to_term1_menu(message):
    def respond(message):
        chose_from_markup(message, main_term1_keyboard())
    check_and_respond(message, respond)


@bot.message_handler(func=lambda message: message.text == ai_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, ai_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == ai_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, ai_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == software_engineering_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, software_eng_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == software_engineering_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, software_eng_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == multimedia_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, multimedia_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == multimedia_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, multimedia_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == networks1_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, networks1_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == networks1_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, networks1_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == compilers1_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, compilers1_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == compilers1_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, compilers1_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == english_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, english_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == operations_research_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, operation_research_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == term1_Table_of_lectures) #الجدول
def redirect(message):
    def respond(message):
        bot.forward_message(message.chat.id, cs_stg3, 150)
    check_and_respond(message, respond)

#----------------------------------------------------------------------------
#term2 buttons and commands--------------------------------------------------
@bot.message_handler(commands=['term2']) #command
def update_buttons(message):
    def respond(message):
        bot.reply_to(message, chose_from, reply_markup = main_term2_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == "الكورس الثاني") #button
def to_term2_menu(message):
    def respond(message):
        chose_from_markup(message, main_term2_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == web_prog_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, webProgramming_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == compilers2_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, compilers2_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == compilers2_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, compilers2_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == networks2_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, networks2_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == networks2_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, networks2_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == dis_db_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, distributed_databases_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == dis_db_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, distributed_databases_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == data_enc_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, data_encryption_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == data_enc_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, data_encryption_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == data_mining_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, data_mining_lab_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == data_mining_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, data_mining_theo_buttons())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == term2_Table_of_lectures ) #الجدول
def redirect(message):
    def respond(message):
        bot.forward_message(message.chat.id, cs_stg3, 151)
    check_and_respond(message, respond)

#--------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == back_term1)
def return_to_term1_menu(message):
    def respond(message):
        bot.reply_to(message, chose_from, reply_markup = main_term1_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == back_term2)
def return_to_term2_menu(message):
    def respond(message):
            bot.reply_to(message, chose_from, reply_markup=main_term2_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text in ["القائمة الرئيسية","خروج من التقييم"])
def return_to_main_menu(message):
    def respond(message):
        bot.reply_to(message, "القائمة الرئيسية", reply_markup=main_term_select())
    check_and_respond(message, respond)

#--------------------------------------
#---------- Get file process ----------
#--------------------------------------
# Load the command mappings
button_to_command = load_commands()

@bot.message_handler(func=lambda message: message.text in button_to_command.keys())
def handle_button(message):
    command = button_to_command.get(message.text)
    get_file_command(message, command)

def get_file_command(message, command):
    data = load_data(file_path)
    post_id_or_list = data['commands'].get(command)

    if '_full' in command:
        CHANNEL_ID = cs_stg3
    elif '_lectures' in command:
        CHANNEL_ID = cs_stg3_onefile
    elif '_old' in command:
        CHANNEL_ID = cs_stg3_deleted
    elif '_app' in command:
        CHANNEL_ID = cs_apps
    else:
        bot.reply_to(message, "⏳ماكو حاليا هذا الملف")
        return

    message_text = "⬆️⬆️🫡"
    if post_id_or_list:
        try:
            if isinstance(post_id_or_list, list):
                for post_id in post_id_or_list:
                    bot.forward_message(message.chat.id, CHANNEL_ID, post_id)
                bot.reply_to(message, message_text)
            else:
                bot.forward_message(message.chat.id, CHANNEL_ID, post_id_or_list)
                bot.reply_to(message, message_text)

        except Exception as e:
            bot.reply_to(message, f"💢اكو مشكلة من البوت.\n Error: {e}")
    else:
        bot.reply_to(message, "⏳ماكو حاليا هذا الملف")



bot.polling()
