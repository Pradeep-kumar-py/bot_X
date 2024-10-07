import telebot
from telebot import types

bot = telebot.TeleBot('7829556985:AAGyhH2KEO3fiCNcBI_qHQ-6LY6HtPQeZRE')

# Sample club data
club_details = {
    "Cultural Board": {
        "Faculty In-Charge": "Dr. Preeti Warrior - 1234567890",
        "BE Mentors": [
            "Ankana Sardar - 8995423162", 
            "Aryan Dabholkar - 7906799482", 
            "Simran - 7387883171", 
            "Arnav Singh - 9411678749"
        ],
        "Secretaries": [
            "Satyam Sathpati - 7297881135", 
            "Pallavi Shirsath - 8197761199"
        ],
        "Joint Secretaries": [
            "Piyush Kumar - 9256710877", 
            "Sandeep Mondal - 9257666997", 
            "Harita - 7989681871", 
            "Mukul Rewar - 9256564140"
        ]
    },
    "DDQ": {
        "Faculty In-Charge": "Mr. Manoj Khaladkar - 1234567890",
        "BE Mentors": [
            "Pankaj Rai - 6266017512", 
            "Tarush Pandey - 8284058266", 
            "Aryan Dabholkar - 7906799482", 
            "Reema Singh - 7654892389"
        ],
        "Secretaries": [
            "Chetan Singh - 9602866736", 
            "Rajat Singh - 7985001490"
        ],
        "Joint Secretaries": [
            "Sohila Kaur - 9999078811", 
            "Millan Patra - 9156384972", 
            "Mothitesh Thakur - 8988907990", 
            "Gaurav Yadav - 6367401971"
        ]
    },
    "Trinity":{
        "Faculty In-Charge": "Prof. Kuldeep Hule 1234567890",
        "BE Mentors": [
            "Harsh Bisht - 9103204360",
            "Aryan Dabholkar - 7906799482", 
            "Abrish - 6787453091", 
            "Yuvraj Singh - 8876593452"    
        ],
        "Secretaries": [
            "Nitin Mahala - 9462137180",
            "Roshnee Gouda - 8080870414"
        ],
        "Joint Secretaries ": [
            "Abhishek Kumar", "8923302946"
            "Gaurav Pilania", "9991267063"
            "Raj Kumar", "9034428909"
            "Palak Kundu", "8708234825"
            "Gaurav Kumar Singh", "7061526180"
            "Salit Yadav", "6398931639"
            "Sana Kamirkar", "9980520349"
            "Summanyu Nayak", "9903273669"

        ]
    
    },
    "TECHNICAL BOARD":{
        "Faculty in charge": "Dr. PB Karandikar 1234567890",
        "BE Mentors": [
            "Vansh Vatsal", "7620310340"
            "Anushna Pawar", "8667543781"
            "Aditya Tiwari", "9053182559"
            "Ayush Bhadoria", "9461050498"
        ],
        "Secretaries": [
            "Nabajit Das", "8509442084"
            "Nisha Dhaka", "7689690324"

        ],
        "Joint Secretaries": [
            "Sneha", "6387029949"
            "Sameer Sekhawat", "8708442966"
            "Shashank Tiwari", "8882465015"
            "Shreya", "7651965112"
            "Aditya Raj", "9140992004"
        ],
    },
    "EV": {
        "Faculty in charge": "Dr. name",
        "BE Mentors": [
            "Krishna Mohan Tripathi - 00000000000",
            "Palak Singh - 1111111111",
        ],
        "Secretaries": [
            "Asish Jatt - 83071 68970",
            "Abhishek kumar - 98522 32044"
        ],
        "Joint Secretar":[
            "Prateek Nehra - 84408 38097",
            "Nerander Dotasara - 87409 83912",
            "Ankit kumar - 80002 86292",
            "Hemita Sudan - ",
            "Harsh Kumar Dubey - ",
            "Rahool Yadav - ",
            "Baihav kumar - "
        ]
    },
    "CEAR": {
        "Faculty in charge": "Dr. name",
        "BE Mentors": [
            "Subham Tiwari - 00000000000",
            "Avinash Puniya - 1111111111",
            "Rahul Choudhary - ",
            "Vikas saran - ",
            "Aditi more - ",
            "Birendra Mohapatra - ",
            "Avinash Singh - ",
            "Ronak Bhakhar - ",
        ],
        "Secretaries": [
            "Meher Mitt Singh - ",
            "Nikita Choudhary - "
        ]      
    }
    
    # Other clubs can be added similarly
}

# To store user's selected club
user_club_selection = {}

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Technical Clubs', 'Non-Technical Clubs')
    bot.reply_to(message, "Welcome! Please select the type of clubs:", reply_markup=markup)

# Handling club type selection
@bot.message_handler(func=lambda message: message.text in ['Technical Clubs', 'Non-Technical Clubs'])
def club_type_selection(message):
    club_type = message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    if club_type == 'Technical Clubs':
        markup.add('Trinity', 'TECHNICAL BOARD', 'EV', 'CEAR')  # Add relevant technical clubs
    else:
        markup.add('Cultural Board', 'DDQ')  # Add relevant non-technical clubs

    bot.reply_to(message, f"Please select a club from {club_type}:", reply_markup=markup)

# Handling club selection and storing the selected club
@bot.message_handler(func=lambda message: message.text in ['Trinity', 'TECHNICAL BOARD', 'EV', 'CEAR', 'Cultural Board', 'DDQ'])
def club_selection(message):
    selected_club = message.text
    user_club_selection[message.chat.id] = selected_club  # Store the selected club for the user
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Faculty In-Charge', 'BE Mentors', 'Secretaries', 'Joint Secretaries')
    bot.reply_to(message, f"You selected {selected_club}. Please choose an option for more details:", reply_markup=markup)

# Providing the information based on the selected option
@bot.message_handler(func=lambda message: message.text in ['Faculty In-Charge', 'BE Mentors', 'Secretaries', 'Joint Secretaries'])
def info_selection(message):
    selected_option = message.text
    user_id = message.chat.id
    selected_club = user_club_selection.get(user_id)  # Retrieve the user's selected club

    if selected_club and selected_option in club_details.get(selected_club, {}):
        details = club_details[selected_club][selected_option]
        if isinstance(details, list):
            # If it's a list (like BE Mentors or Secretaries)
            info = "\n".join(details)
        else:
            # Single entry (like Faculty In-Charge)
            info = details

        bot.reply_to(message, f"Here are the details for {selected_option} of {selected_club}:\n{info}")
    else:
        bot.reply_to(message, "Sorry, no details available for this option.")

    # Offer more assistance or end session
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('End Session', 'More Assistance')
    bot.reply_to(message, "Would you like more assistance or to end the session?", reply_markup=markup)

# Ending the session
@bot.message_handler(func=lambda message: message.text == 'End Session')
def end_session(message):
    bot.reply_to(message, "Thank you for using the club info bot! Goodbye!")

# Handling additional assistance
@bot.message_handler(func=lambda message: message.text == 'More Assistance')
def more_assistance(message):
    send_welcome(message)

# Start polling
bot.polling()
