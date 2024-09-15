import random

choice = ('r', 'p', 's')

emojis = {'r': '🪨', 's':'✂️', 'p': '📃'}

while True:
  user_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
  if user_choice not in choice:
    print("Invalid choice")
    continue

  computer_choice  = random.choice(choice)

  print(f'You chose {emojis[user_choice]}') 
  print(f'Computeer chose {emojis[computer_choice]}')

  if user_choice ==  computer_choice:
    print("Tie!")
  elif (
  (user_choice == "r" and computer_choice == "s") or
  (user_choice == "s" and computer_choice == 'p') or 
  (user_choice == 'p' and computer_choice == 'r')):
    print("You win!")
  else:
    print("You loose")

  should_continue = input("Continue? (y/n): ").lower()
  if should_continue == 'n':
    break

  