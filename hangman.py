from random import choice

word = choice(['python', 'java', 'kotlin', 'javascript'])
hidden = ['-' for _ in word]
tries = 8
typed = set()

def play():
    global tries, hidden, typed
    while tries > 0:
        print('\n', ''.join(hidden))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        elif not (letter.isascii() and letter.islower()):
            print('It is not an ASCII lowercase letter')
            continue
  
        if letter in typed:
            print('You already typed this letter')
            continue

        if letter not in word:
            print('No such letter in the word')
            tries -= 1
        else:
            hidden = [letter if word[i] == letter else hidden[i] for i in range(len(word))]
        typed.add(letter)
        if '-' not in hidden:
            print('You guessed the word!\nYou survived!')
            break
    else:
        print('You are hanged!')

print('H A N G M A N\n')
while True:
    action = input('Type "play" to play the game, "exit" to quit:')
    if action == 'play':
        play()
    elif action == 'exit':
        break 
    else:
        continue
        