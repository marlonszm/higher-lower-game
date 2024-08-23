#who has more followers game (higher lower)
import random
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Neymar',
        'followers': 224,
        'description': 'Football Player',
        'country': 'Brazil'
    },
    {
        'name': 'Cristiano Ronaldo',
        'followers': 636,
        'description': 'Football Player',
        'country': 'Portugal'
    },
    {
        'name': 'Florian Wirtz',
        'followers': 28,
        'description': 'Football Player',
        'country': 'Germany'
    },
    {
        'name': 'Bruno Fernandes',
        'followers': 9,
        'description': 'Football Player',
        'country': 'Portugal'
    },
    {
        'name': 'Joshua Zirkzee',
        'followers': 1,
        'description': 'Football Player',
        'country': 'Netherlands'
    },
]

game_stop = False
counter_times_won = 0

def check_right_wrong(user_choice, followersA, followersB):
  global counter_times_won, game_stop
  if user_choice == "A" and followersA > followersB:
    counter_times_won+=1
    return f"You're right! Current score: {counter_times_won}."
  elif user_choice == "A" and followersA < followersB:
    game_stop = True
    return f"Sorry, that's wrong! Final score: {counter_times_won}."
  if user_choice == "B" and followersB > followersA:
    counter_times_won+=1
    return f"You're right! Current score: {counter_times_won}."
  elif user_choice == "B" and followersB < followersA:
    game_stop = True
    return f"Sorry, that's wrong! Final score: {counter_times_won}."
    
print(logo)

while game_stop == False:
  list_sample = random.sample(data, 2)
  random_listA = list_sample[0]
  random_listB = list_sample[1]
  followersA = random_listA['followers']
  followersB = random_listB['followers']
  print(f"Compare A: {random_listA['name']}, a {random_listA['description']}, from {random_listA['country']}")
  print(vs)
  print(f"Compare B: {random_listB['name']}, a {random_listB['description']}, from {random_listB['country']}")
  user_choice = input("\nWho has more followers? Type 'A' or 'B' ").upper()
  print(f"{check_right_wrong(user_choice, followersA, followersB)}\n")
  clear()
  

  


