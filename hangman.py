import random

words = ['jazz','buzzed','abruptly','absurd','awkward','bagpipes','bikini','blizzard','buffalo','cycle','faking','funny','galaxy','kepler','gossip','injury','jelly','juicy','jogging','kayak','kioks','length','lucky','luxury','matrix','oxygen','pajama','puppy','quizzes','strength','subway','transplant','twelve','syndrome','transcript','unknown','vaporize','vodka','wizard','zipper','zombie','whiskey']
word = random.choice(words)

#hangman drawing

hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]

  
def draw_hangman(errors):

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(errors):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)


def single(num):
    if num == 1:
        print('You have 1 guess left \n')
    else:
        print('You have ' + str(num) + ' guesses left \n')


def game(word):
    
    
    words = ['JAZZ','BUZZED','ABRUPTLY','ABSURD','AWKWARD','BAGPIPES','BIKINI','BLIZZARD','BUFFALO','CYCLE','FAKING','FUNNY','GALAXY','KEPLER','GOSSIP','INJURY','JELLY','JUICY','JOGGING','KAYAK','KIOSK','LENGTH','LUCKY','LUXURY','MATRIX','OXYGEN','PAJAMA','PUPPY','QUIZZES','STRENGTH','SUBWAY','TRANSPLANT','TWELVE','SYNDROME','TRANSCRIPT','UNKNOWN','VAPORIZE','VODKA','WIZARD','ZIPPER','ZOMBIE','WHISKEY']
    word = random.choice(words)

    print('Okay, this is your word! You have 10 guesses.')
    
    chances = 6
    progress = []
    mistakes = []
    hidden = list('_'*len(word))
    win = False
     
    print('\n'+''.join(hidden)+'\n')
    
    while (chances > 0) & (not win):

        letter = input('Choose a letter \n')
        
        if (letter.isalpha()) & (letter.upper() in list(word)):
            if letter.upper() in progress:
                draw_hangman(len(mistakes))
                print('You already guessed ' + letter.upper())
                single(chances)
                print('\n'+''.join(hidden)+'\n')
            else:
                progress.append(letter.upper())
                for n, i in enumerate(list(word)):
                    if i == letter.upper():
                        hidden[n] = letter.upper()
                draw_hangman(len(mistakes))
                print('\n'+''.join(hidden)+'\n')

                if '_' not in hidden:
                    win = True
                    print('You won!')
                else:
                    print('Good job! ' + letter.upper() + ' is in the word.')
                    single(chances)
                
            
        elif (letter.isalpha()) & (letter.upper() not in list(word)):
            if letter.upper() in mistakes:
                draw_hangman(len(mistakes))
                print('You already guessed ' + letter.upper())
                single(chances)
            else:
                mistakes.append(letter.upper())
                draw_hangman(len(mistakes))
                print('\n'+''.join(hidden)+'\n')
                print('Sorry, ' + letter.upper() + ' is not in the word.')
                chances -= 1
                single(chances)
            
        else:
            print('Your input is invalid, try again. \n')

    if not win:
        print('You lost! The word was: ' + word)

    repeat = input('Do you want to play again? (Y/N) \n')
    if repeat.upper() == 'Y':
        game(word)
    else:
        print('See you next time')


answer = input('Do you want to play Hangman? (Y/N) \n')
if answer.upper() == 'Y':
    game(word)
else:
    print('See you next time \n')


