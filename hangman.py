'''
	The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
	The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
	    
	 Output
	
	You have 6 tries left.                                                                                                                                           
	Used letters:                                                                                                                                                    
	Word: _ _ _ _                                                                                                                                                    
	Guess a letter: a 
	
	You have 6 tries left.                                                                                                                                           
	Used letters: a                                                                                                                                                  
	Word: _ a _ a                                                                                                                                                    
	Guess a letter: j    
	
	You have 6 tries left.                                                                                                                                           
	Used letters: j a                                                                                                                                                
	Word: j a _ a                                                                                                                                                    
	Guess a letter: v                                                                                                                                                
	You guessed the word java !
'''


from random import choice

words = ['ant','baboon','badger','bat','bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 
       'coyote', 'donkey', 'duck' ,'eagle','frog' ,'goat' ,'goose' ,'hawk',
       'lion' ,'lizard', 'monkey' , 'otter', 'owl' ,'panda',
       'parrot' ,'pigeon' ,'python' ,'rabbit' ,'raven' ,'rhino', 'salmon', 'seal' ,'shark' ,'sheep',
       'sloth' ,'snake' ,'spider' ,'swan' ,'tiger' ,'trout' ,'turkey', 'turtle',
       'turtle' ,'whale' ,'wolf' ,'wombat' ,'zebra']

secret_word=choice(words)
letters_guessed=''
failure_count=6

while failure_count>0:
    
    #ask the user for a letter
    guess=input("Enter a letter: ")
    
    #if the letter is correct 
    if guess in secret_word:
        print(f' Correct!, {guess} is in secret word')
        
    # if the letter is incorrect, decrease the number of tries
    else:
        failure_count-=1
        print(f' Sorry, {guess} is not in secret word. You have {failure_count} opportunities left')
    
    #actualized the list of all the letters guessed
    letters_guessed=letters_guessed + guess
    
    count_wrong=0
    
    for letter in secret_word:
        if letter in letters_guessed:
            print(f'{letter} ',end='')
        else:
            print(' _ ', end='')
            count_wrong+=1
    #if there are no wrong letter, then the user won         
    if count_wrong==0:
        print (f' Congratulations! you won, the secret was: {secret_word}')
        break
        
else:
    print (f'Sorry, you lose the word was: {secret_word}')