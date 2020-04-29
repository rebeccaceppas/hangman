import random

words = ['jazz','buzzed','abruptly','absurd','awkward','bagpipes','bikini','blizzard','buffalo','cycle','faking','funny','galaxy','kepler','gossip','injury','jelly','juicy','jogging','kayak','kioks','length','lucky','luxury','matrix','oxygen','pajama','puppy','quizzes','strength','subway','transplant','twelve','syndrome','transcript','unknown','vaporize','vodka','wizard','zipper','zombie','whiskey']
word = random.choice(words)


def game(word):
    
    
    words = ['JAZZ','BUZZED','ABRUPTLY','ABSURD','AWKWARD','BAGPIPES','BIKINI','BLIZZARD','BUFFALO','CYCLE','FAKING','FUNNY','GALAXY','KEPLER','GOSSIP','INJURY','JELLY','JUICY','JOGGING','KAYAK','KIOSK','LENGTH','LUCKY','LUXURY','MATRIX','OXYGEN','PAJAMA','PUPPY','QUIZZES','STRENGTH','SUBWAY','TRANSPLANT','TWELVE','SYNDROME','TRANSCRIPT','UNKNOWN','VAPORIZE','VODKA','WIZARD','ZIPPER','ZOMBIE','WHISKEY']
    word = random.choice(words)

    print('Okay, this is your word!')
    chances = 10
    progress = []
    mistakes = []
    hidden = list('_'*len(word))
    #guess = False
    
    print(''.join(hidden))
    
    while (chances > 0):
        
        
        letter = input('Choose a letter')
        
        if (letter.isalpha()) & (letter.upper() in list(word)):
            #if '_' not in hidden:
                #guess == True
            if letter.upper() in progress:
                print('You already guessed ' + letter.upper())
            else:
                progress.append(letter.upper())
                for n, i in enumerate(list(word)):
                    if i == letter.upper():
                        hidden[n] = letter.upper()
                print(''.join(hidden))
                print('Good job! ' + letter.upper() + ' is in the word.')
                
            
        elif (letter.isalpha()) & (letter.upper() not in list(word)):
            mistakes.append(letter.upper())
            print(''.join(hidden))
            print('Sorry, ' + letter.upper() + ' is not in the word. Try again.')
            chances -= 1
            
        else:
            print('Your input is invalid, try again.')

answer = input('Do you want to play Hangman? (Y/N)')
if answer.upper() == 'Y':
    game(word)
else:
    print('See you next time')