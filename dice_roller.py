import random
def main():
  dice_sum=0
  dice_rolls= int(input("How many dice do you want to roll?"))
  for i in range(0,dice_rolls):
    rnd=random.randint(1,6)
    dice_sum+=rnd 
    if (rnd ==1):
         print(f"{i}.You rolled a {rnd},!Critical Failure")
    elif (rnd==6):
         print(f"{i}.You rolled a {rnd},!Critical Success")
    else :  
         print(f'{i}.You rolled a {rnd} ')
    
  print(f" The sum is {dice_sum}")      
if __name__== "__main__":
  main()
