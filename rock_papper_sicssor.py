import random
Rock='r'
Paper='p'
Sisscor='s'

emojis={'r':'🪨','p':'📃','s':'✂️'}
choices=tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice=input("Rock,papper,scissor?(r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Involid choice!')

def displaying_choices(user_choice,computer_choice):
    print(f'Your choice{emojis[user_choice]}') 
    print(f'computer choice{emojis[computer_choice]}')  
    
def determining_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif ((user_choice == 'r' and computer_choice =='s') or 
        (user_choice == 's' and computer_choice =='p') or  
        (user_choice == 'p' and computer_choice =='r')):
        print('You Win')
    else:
        print('You Loss')                 
           
    
def play_game():
    while True:
        user_choice=get_user_choice()
        

        computer_choice=random.choice(choices) 
        
        displaying_choices(user_choice,computer_choice)  
        
        determining_winner(user_choice,computer_choice)    
        should_continue=input('continue(y/n)!: ').lower() 
        if should_continue == 'n':
         break
play_game()    
            
        
    
      