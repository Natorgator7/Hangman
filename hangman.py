#come up with a word
#count the letters in said word
	#the number of guesses is that number plus 3
#ask for a letter guess in caps
#if the guess is not a letter, print 'not on the right track, dumbass'
#if the guess is a letter, determine whether it is in the word or not
	#raise the guess counter by one
#if it is, determine which space it's in and how many ther are
#if not, print 'nope' and the number of guesses left
#print an equal number of asterisks and guessed letters as the number of letters in the word
	#replace however many asterisks with the guessed letter
#when there are no more asterisks, print 'you got it right! The word was indeed' the word
#if they run out of guesses, print 'the dude was shot to death a day before his scheduled execution. You failed him and his memory'
import random

word_list = ['GARFIELD', 'ODIE', 'JON', 'ARLENE', 'LIZ', 'NERMAL', 'POOKY', 'BART', 'LISA', 'HOMER', 'MARGE', 'MAGGIE', 'MOE']
word = random.choice(word_list)
word_length = len(word)
limbs_drawn = 0
guessed = False
guesses = []
display = ["_"] * word_length
print "\nI am thinking of a cartoon character from either the Garfield world or the Simpsons, who's name contains {} letters. Oh yea, and this is hangman-- someone might die...".format(word_length)
while limbs_drawn < 6 and guessed == False:
	print(' '.join(display))
	guess = raw_input('\nTake a letter guess in caps pls.')
	occurences = word.count(guess)
	print "{} of those".format(occurences)
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