import random
from datetime import datetime
def Greet_n_intro():
    print("Hi ! I am Knowledge Bot.")
    print( "I can help you to know the details like Capital, language, most popular places of respective States in India. ")
def get_timeofday():
    current_time = datetime.now()
    timeofday_greeting = "Good morning"
    if current_time.hour > 12 and current_time.hour<=17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour > 17 and current_time.hour<=22:
        timeofday_greeting = "Good evening"
    elif current_time.hour > 22:
        timeofday_greeting = "Hi, That's late"
    return timeofday_greeting

def welcome():
    name=input("Enter your sweet name:")
    messages = [
        "Nice to meet you!"+" "+name,
        "Good to see you!"+" "+name
    ]
    print (get_timeofday())
    print(random.choice(messages))
    print()
def show_choices():
    print("The tasks that can be done by me....")
    print("1.Do you Want to know about details of respective states ?")
    print("2.Now its time to quit this chat.")
    print()
def choice_selection():
    try:
        return int(input("Enter your choice : "))
    except:
        print("Invalid, I didn't get you. ")
        
def show_states():
    print()
    print("1: Andhra Pradesh, 2: Arunachal Pradech, 3: Assam, 4: Bihar, 5: Cchattisgarh, 6: Goa, 7: Gujarat, 8: Haryana, 9: Himachal Pradesh, 10: JharKand  ")
    print("11: Karnataka, 12: Kerala, 13: Madhyapradesh, 14: Maharashtra, 15: Manipur, 16: Meghalaya, 17: Mizoram ,18: Nagaland ,19: Odisha ,20: Punjab ")
    print("21: Rajasthan, 22: Sikkim, 23:Tamil nadu, 24: Telangana, 25: Tripura, 26: Uttar Pradesh, 27: Uttarakhand, 28: West Bengal, 29: Jammu & kashmir")
    print()



def States_in_India(select):
   
    details = {
        1: "Andhra Pradesh  - Capital: Visakapatnam(Executive), Amaravathi(legislative), karnool(Judiciary) - language: Telugu - Most popular place: Tirupathi.",
        2: "Arunachal Pradesh -  Capital: Itanagar - language: English  - Most popular place: Ziro valley." ,
        3: "Assam - Capital: dispur - language: Assamese - Most popular place: Kaziranga National Park.",
        4: "Bihar - Capital: Patna - language: Hindi - Most popular place: Bodh Gaya.",
        5: "Cchattisgarh - capital: Naya Raipur -language: Hindi- Most popular place: Chitrakote Waterfalls.",
        6: "Goa - capital: Panaji - language: konkani - Most popular place:  Calangute Beach.",
        7: "Gujarat - Capital: Gandhinagar - language: Gujarati - Most popular place: Gir National Park.",
        8: "Haryana - Capital: Chandigarh - language: Hindi - Most popular place: Firoz Shah Palace.",
        9: "Himachal Pradesh - Capital: Shimla(summer), Dharmashala(winter) - language: Hindi - Most popular place: Manali.",
        10: "JharKand - Capital: Ranchi - language: Hindi - Most popular place: Dassam Falls.",
        11: "Karnataka - Capital: Bangalore - language: Kannada - Most popular place: Bannerghatta National Park.",
        12: "Kerala - Capital: Tiruvananthapuram - language: Malayalam - Most popular place: Athirapally Vazhachal Waterfalls.",
        13: "Madhyapradesh - Capital: Bhopal - language: Hindi - Most popular place: Pachmarhi.",
        14: "Maharashtra - Capital: Mumbai(Summer),Nagpur(Winter) - language: Marathi - Most popular place: Ajanta Caves.",
        15: "Manipur - Capital: Imphal - language: Meitei - Most popular place: Loktak Lake.",
        16: "Meghalaya - Capital: Shillong - language: English - Most popular place: Seven Sisters Waterfalls.",
        17: "Mizoram - Capital: Aizwal - language: Mizo - Most popular place: Blue National Park.",
        18: "Nagaland - Capital: Kohima - language: English - Most popular place: Naga Hills.",
        19: "Odisha - Capital: Bhubaneshwar - language: Odia - Most popular place: Chilika Lake.",
        20: "Punjab - Capital: Chandigarh - language: Punjabi - Most popular place: Golden Temple.",
        21: "Rajasthan - Capital: Jaipur - language: Hindi - Most popular place: Hawa Mahal.",
        22: "Sikkim - Capital: Gangtok - Language: Nepali - Most popular place: Rumtek Monastery.",
        23: "Tamil nadu - Capital: Chennai - language: Tamil - Most popular place: Rameshwaram.",
        24: "Telangana - Capital: Hyderabad - language: Telugu - Most popular place: Golconda Fort.",
        25: "Tripura - Capital: Agarthala - language: Bengali and Kokborok - Most popular place:  Ujjayanta Palace.",
        26: "Uttar Pradesh - Capital: Lucknow - language: Hindi - Most popular place: Taj Mahal.",
        27: "Uttarakhand - Capital: Gairsain(Summer),Dehradun(Winter) - language: Hindi - Most popular place: Mussoorie.",
        28: "West Bengal - Capital: Kolkata - language: Bengali,nepali - Most popular place: Victoria Memorial.",
        29: "Jammu & kashmir - Capital: Srinagar -language: Dogri - Most popular place: Pahalgam."
        }
    print(details.get(select, "Please select from above numbers "))
def Knowledgebot():
    Greet_n_intro()
    get_timeofday()
    welcome()
    show_choices()
    choice=choice_selection()
    while choice !=2:
        if choice == 1 :
            show_states()
            try:

                select=int(input("Enter the number of corresponding State: "))
                print(States_in_India(select)) 
            except:
                print("Enter only integers")      
        
        else:
            print("Please enter numbers 1 or 2")
        print("Would you like to know the details of any other states?")
        print()   
        show_choices()
        choice=choice_selection()
Knowledgebot()

 