ASCII_IMAGE = """ Welcome to the fortune teller's tent, please touch the ball and don't let it go
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠾⠛⠋⠉⠉⠉⠉⢙⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⢇⣤⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⢹⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣤⡙⠻⢿⣿⣿⣿⣿⣿⣋⣠⣤⡶⠟⢁⣤⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⣤⣈⣉⠉⠛⠛⠉⣉⣠⣤⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣦⣀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢋⣠⣴⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣷⣶⣤⣬⣭⣉⣉⣉⣩⣭⣥⣤⣶⣾⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀
"""
import random


def lucky_number(name):
  number = len(name) * random.randint(1, 1000) // 100

  print("Oh, I see, " + name + "... I'm feeling it, your lucky number is " +
        str(number))


print(ASCII_IMAGE)
while True:
  name = input("May I know your name so I can guess your lucky number? ")
  lucky_number(name)
  replay = input("Do you want to play again? (yes/no) ")
  replay = replay.lower()
  if replay == "yes":
    continue
  elif replay == "no":
    print("Thank you for coming to my tent, have a nice day!")
    break
  else:
    print(
      "I see what you're trying to do, but not today! Not here, not now, please type 'yes' or 'no'."
    )
    break
