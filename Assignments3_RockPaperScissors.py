# Assignemnt 3
# Author: Iskander Kenzhebekov

# We import random for random computer choices
import random

#We use a list of strings to represent the five possible items
actions = ["scissors", "rock", "paper", "lizard", "spock"]

#Create the function for the following actions
def beat(x,y):
  if x == "scissors" and y == "paper":
    return True
  elif x == "paper" and y == "rock":
    return True
  elif x == "rock" and y == "lizard":
    return True
  elif x == "lizard" and y == "spock": 
    return True 
  elif x == "spock" and y == "scissors":
    return True
  elif x == "scissors" and y == "lizard":
    return True
  elif x == "lizard" and y == "paper":
    return True
  elif x == "paper" and y == "spock":
    return True
  elif x == "spock" and y == "rock":
    return True 
  elif x=="rock" and y == "scissors":
    return True
  else:
    return False

# Create the fucntion for the results of the fight
users_wins = 0
computers_wins = 0
draws = 0
def results(x,y):
  if beat(x, y) == True:
    print ("You win this round!")
  elif beat(x, y) == False and x == y:
    print ("It's a draw!")
  else:
    print("I win this round!")
  

# Create a function that will convert the number to the name and vise versa
def number_to_name(num):
  if num == "1":
    return "rock"
  elif num == "2":
    return "paper"
  elif num == "3":
    return "scissors"
  elif num == "4":
    return "lizard"
  elif num == "5":
    return "spock"

def name_to_number(name):
  if name == "rock":
    return "1"
  elif name == "paper":
    return "2"
  elif name == "scissors":
    return "3"
  elif name == "lizard":
    return "4"
  elif name == "spock":
    return "5"

#create the fuction for the percentage
def percentage(i, n):
  percent = float(i)/ float(n)*100
  return format(percent, ",.1f")

#Set up the dictionaries for the statistics
users_history = {"1":0,"2":0,"3":0,"4":0,"5":0}
computers_history = {"1":0,"2":0,"3":0,"4":0,"5":0}

#Greet and ask the user how many times they would like to play
print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
number_of_rounds = int(input("How many rounds do you want to play? ==> "))
for i in range (1, number_of_rounds+1): 
  print("\nRound", i , "of", str(number_of_rounds)+":")
  print ("What item do you choose? \n1 - rock\n2 - paper\n3 - scissors\n4 - lizard\n5 - spock")
  users_choice = input ("your answer ==> ")
  users_history [users_choice] += 1
  users_choice = number_to_name(users_choice)
  computers_choice = random.choice(actions)
  computers_history [name_to_number(computers_choice)] += 1
  print ("I chose:", computers_choice)
  results(users_choice, computers_choice)
  if beat(users_choice, computers_choice) == True:
    users_wins += 1
  elif beat(users_choice, computers_choice) == False and users_choice == computers_choice:
    draws += 1
  else:
    computers_wins += 1 
  
# Start the statistic part: 
print("\nStatistics:")
# calculate number of times user and computer used rock, paper, scissors, spock and lizard in digit and percentage.
print("You chose rock",users_history["1"], "time(s) ("+ percentage(users_history["1"], number_of_rounds)+ "%).")
print("I chose rock",computers_history["1"], "time(s) ("+ percentage(computers_history["1"], number_of_rounds)+ "%).")

print("You chose paper",users_history["2"], "time(s) ("+ percentage(users_history["2"], number_of_rounds)+ "%).")
print("I chose paper",computers_history["2"], "time(s) ("+ percentage(computers_history["2"], number_of_rounds)+ "%).")

print("You chose scissors",users_history["3"], "time(s) ("+ percentage(users_history["3"], number_of_rounds)+ "%).")
print("I chose scissors",computers_history["3"], "time(s) ("+ percentage(computers_history["3"], number_of_rounds)+ "%).")

print("You chose lizard",users_history["4"], "time(s) ("+ percentage(users_history["4"], number_of_rounds)+ "%).")
print("I chose lizard",computers_history["4"], "time(s) ("+ percentage(computers_history["4"], number_of_rounds)+ "%).")

print("You chose spock",users_history["5"], "time(s) ("+ percentage(users_history["5"], number_of_rounds)+ "%).")
print("I chose spock",computers_history["5"], "time(s) ("+ percentage(computers_history["5"], number_of_rounds)+ "%).")

#print the number of wins from each side
print("You won", users_wins, "round(s) ("+percentage(users_wins, number_of_rounds)+"%).")
print("I won", computers_wins, "round(s) ("+percentage(computers_wins, number_of_rounds)+"%).")
print("We had", draws, "draw(s) ("+percentage(draws, number_of_rounds)+"%).\n")

def who_is_the_winner ():
  if users_wins > computers_wins:
    print("You are the winner!")
  elif computers_wins > users_wins:
    print ("I am the winner!")
  else: 
    print ("There is no winner.")

who_is_the_winner()