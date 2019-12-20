print ("Please think of a number between 0 and 100!")
char =''
low = 0;
high = 100;
ans =(high - low)/2
while(char!='c'):
    print("Is your secret number "+str(ans)+"?")
    char= raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if char == 'c':
        print "Game over.",
        print ("Your secret number was: "+str(ans))
        break
    elif char == 'h':
        high = ans
        ans = low + (high-low)/2
    elif char == 'l':
        low =ans
        ans = low + (high-low)/2
    else : 
        print("Sorry, I did not understand your input.")
        
    
             