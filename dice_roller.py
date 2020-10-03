import random
def main():
  no_players=int(input("How many players?"))
  dice_sum=0
  dice_rolls= int(input("How many dice do you want to roll?"))
  dice_faces=int(input("How many faces does the dice have?"))
  for j in range(0,no_players):
     print(f"Rolling for Player {j+1}")            
     for i in range(0,dice_rolls):
            rnd=random.randint(1,dice_faces)
            dice_sum+=rnd 
            if (rnd ==1):
                print(f"{i+1}.You rolled a {rnd},!Critical Failure")
            elif (rnd==6):
                print(f"{i+1}.You rolled a {rnd},!Critical Success")
            else :  
                print(f'{i+1}.You rolled a {rnd} ')
    
     print(f" The sum is {dice_sum}")
     dice_sum=0
  print(j)  
if __name__== "__main__":
  main()
