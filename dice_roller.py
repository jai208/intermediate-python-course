import random
def main():
  dice_rolls=2
  dice_sum=0
  for i in range(0,dice_rolls):
     
     rnd=random.randint(1,6)
     print(f'{i}.You rolled a {rnd} ')
     dice_sum=dice_sum+rnd
     print(f"The sum is {dice_sum}")
if __name__== "__main__":
  main()
