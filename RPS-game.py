#Rock,Paper,Scissors

import random

def play():
  user=input("What is your choice? 'r' for rock, 'p' for paper or 's' for scissors?:")
  computer=random.choice(['r','p','s'])

  if(user==computer):
    return 'It is a tie'

  if is_win(user,computer):
    return 'You won! Congrats.'
  
  #else:
    return 'Better luck next time'
  
def is_win(player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='r') or (player=='p' and opponent=='r'):
      return True
      #print('{} wins'.format(player))

print(play())