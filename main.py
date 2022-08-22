import telebot
from decouple import config
from weather import getCurrentWeather

 
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


weather = ["/weather" ,"/temp" ,"/temprature" ,"weather","temp","temprature"]
greetings = ["hello","hi","hey"]
whoAreYou = ["/who" ,"who" , "what" ]
ownerName = ["/owner" ,"owner" , "created", "aymen"]
botName = "TunisWeather"
fb = ["/facebook" ,"fb" , "facebook", "aymen fb"]
insta = ["/insta" ,"insta" , "instagram", "aymen insta"]
phone = ["/phone" ,"phone","num","number","whatsapp"]
helpme= ["/help","help"]

fblink =  "Facebook : facebook.com/ghniaaymen3/"
instalink = "instagram :instagram.com/aymen_ghnia"
phonenum = "+216 51 550 022"

@bot.message_handler(commands=["/start","start"])
def welcome(message):
    bot.send_message(message.chat.id,"Heyy 😍   ")
    bot.send_message(message.chat.id,"To know the weather  just write  ")
    bot.send_message(message.chat.id,"/weather    --OR--    /temp      --OR--    /temprature")

    
@bot.message_handler(commands=["/help","help"])
def welcome(message):
    bot.send_message(message.chat.id,"To know the weather  just write  ")
    bot.reply_to(message,"/weather    --OR--    /temp      --OR--    /temprature")
 
#answering every message not just commands 
def isMSg(message):
    return True

@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    if words[0].lower() in helpme :
        bot.send_message(message.chat.id,"Menu : /start - Start bot /help - Get some help /weather - To know the weather /temp - To know the weather /temprature - To know the weather /who - bot description /owner - To know the creator of this bot /facebook - My facebook /insta - My instagram /phone - My phone number  ")     
    if words[0].lower() in greetings :
        return bot.reply_to(message,"Hello !😍 how is going!")
    if words[0].lower() in weather :
        report = getCurrentWeather()
        return bot.send_message(message.chat.id,report or "failed to get weather !!")
    if words[0].lower() in ownerName :
        return bot.send_message(message.chat.id,"The owner is : Aymen Ghnia 😍 ") 
    if words[0].lower() in fb :
        return bot.reply_to(message,f"💻 :{fblink}") 
    if words[0].lower() in insta :
    
        return bot.reply_to(message,f"📱 :{instalink}")
    if words[0].lower() in phone :
        
        return bot.reply_to(message,f"📞 : {phonenum}")
    if words[0].lower() in whoAreYou :
         return bot.reply_to(message,f" i am {botName} 🇹🇳 -- Telegram bot to know Tunis weather, friendly and easy to use ! Created By Aymen Ghnia")
    else:
         return bot.reply_to(message,"that's not a command for me ! 😏")
 
bot.polling()
