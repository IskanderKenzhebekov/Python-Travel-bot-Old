# "Traver agent" bot
# Authors: Iskander Kenzhebekov

#1 Welcome message 
print("""Welcome! I am your friendly travel agent bot. I will ask you some questions , and make
a recommendation based on your answer .
If you are interested, I will provide you with a one-time password to create a user account on
our website .\n""")
#2 Ask user's name and
name=input("Enter Your Name --> ")
print("Hello Dear",name,"!\n")
age=int(input("What is Your Age --> "))
#3 Inform the user about a senior discount if the user is 65 or older and setting up a senior discount
if (age>64):
 print("""Great ! We offer a senior discount .
For every year over 64 , you get 1% off""")
 senior_discount=(age-64)
 print("\n")
else :
 senior_discount=0
 print("\n")
#4 Ask how long the trip will take (in days) and set up the expense
duration=int(input("How many nights are you planning to stay for ? "))
expense_V=((duration*143.84)+997.93)
te_V= expense_V-((senior_discount/100)*expense_V)
expense_B=((duration*235.35)+849.93)
te_B= expense_B-((senior_discount/100)*expense_B)
#5 Ask whether the user is interested in culture, classical music, or beaches and surfing.
destination_V=input("""Do you like culture and classical music ?
Please Answer: Y/N --> """)
destination_B=input("""Do you like beaches and surfing ?
Please Answer: Y/N --> """)
print()
#6 Based on the user’s replies, suggest and display the costs of one of two trips the travel agency currently offers or say that they do not have any offers matching the user’s preferences.
if (destination_V=="Y") & (destination_B=="N"):
 flight_expense=997.93
 hotel=143.84
 print(""" How about a trip to Vienna ?
 Flight Expense = 997.93 $
 Hotel Expense = 143.84 $ / night""")
 expense=((duration*hotel)+flight_expense)
 print("Discount : ",senior_discount,"%")
 print("Total Expense for",duration,"nights (incl. discounts) =",te_V,"$\n\n")
elif (destination_B=="Y") & (destination_V=="N"):
 flight_expense=997.93
 hotel=143.84
 print(""" How about a trip to Bali ?
 Flight Expense = 849.93 $
 Hotel Expense = 235.35 $ / night""")
 expense=((duration*hotel)+flight_expense)
 print("Discount :",senior_discount,"%")
 print("Total Expense for",duration,"nights (incl. discounts)=",te_B,"$\n\n")
elif (destination_B=="Y") & (destination_V=="Y") & (te_V < te_B):
 flight_expense=849.93
 hotel=235.35
 print("""How about a trip to Bali ?
 Flight Expense = 849.93 $
 Hotel Expense = 235.35 $ / night""")
 expense=((duration*hotel)+flight_expense)
 print("Discount :",senior_discount,"%")
 print("Total Expense for",duration,"nights (incl. discounts)=",te_B,"$\n\n")
elif (destination_B=="Y") & (destination_V=="Y") & (te_V > te_B):
 flight_expense=997.93
 hotel=143.84
 print("""How about a trip to Vienna ?
 Flight Expense = 997.93 $
 Hotel Expense = 143.84 $ / night""")
 expense=((duration*hotel)+flight_expense)
 print("Discount : ",senior_discount,"%")
 print("Total Expense for",duration,"nights (incl. discounts) =",te_V,"$\n\n")
elif (destination_B=="Y") & (destination_V=="Y") & (te_V == te_B):
 flight_expense=849.93
 hotel=235.35
 print("""How about a trip to Bali ?
 Flight Expense = 849.93 $
 Hotel Expense = 235.35 $ / night""")
 expense=((duration*hotel)+flight_expense)
 print("Discount :",senior_discount,"%")
 print("Total Expense for",duration,"nights (incl. discounts)=",te_B,"$\n\n")



else :
 print("I am sorry, we don’t have any trips to offer at this point.")
print()
#provide a one-time password for the user to enter on the travel agency website. If the user is not interested, the bot will say goodbye.
import random
password=input("Are you interested , and want to create a user account ?\nPlease answer Y/N --> ")
if (password=="Y"):
 l=len(name)
 l_i=name[l-1]
 f_i=name[0]
 n=(age%8)
 y=["0","1","2","3","4","5"]
 random_y= random.choice(y)
 y_int=int(random_y)
 x="!"
 print("One-Time Password : ",(l_i*n+f_i+y_int*x))
else :
 print("Sorry to hear that. Please consider using our service again.")
print("GoodBye")
