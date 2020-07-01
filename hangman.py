import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ['GARFIELD', 'ODIE', 'JON', 'ARLENE', 'LIZ', 'NERMAL','POOKY', 'BART', 'LISA', 'HOMER', 'MARGE', 'MAGGIE', 'MOE']
word = random.choice(word_list)
word_length = len(word)
limbs_drawn = 0
guessed = False
guesses = []
display = ["_"] * word_length
print "I am thinking of a cartoon character from either the Garfield world or the Simpsons, who's name contains {} letters. Oh yea, and this is hangman-- someone might die...\n".format(word_length)
while limbs_drawn < 6 and guessed == False:
	print HANGMANPICS[limbs_drawn]
	print(' '.join(display))
	guess = raw_input('\nTake a letter guess in caps pls.\n')
	occurences = word.count(guess)
	print "\n{} of those".format(occurences)
	if guess in guesses or guess not in word:
		if guess in guesses:
			print "already guessed"
			limbs_drawn += 1
		else:
			print "sorry :("
			guesses.append(guess)
			limbs_drawn +=1
	if guess in word:
		for i in range(0,len(word)):
			if word[i] == guess:
				display[i] = guess
				guesses.append(guess)
	if '_' not in display:
		guessed = True
if limbs_drawn == 6:
	print '\nThe dude was shot to death a day before his scheduled execution. You failed both him and his memory.'
if guessed == True:
	print "\nSad. No death today."