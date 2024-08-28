#Program to roll a dice
import random
while True:
  num=random.randint(1,6)
  print(num)
  ch=input("Roll again? (y/n)")
  for ch in 'nN':
    break
  print("Thanks for playing..")
