# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

def playstep2(hand, dice):
	a=hand%10
	b=(hand//10)%10
	c=hand//100

	p=dice%10
	q=(dice//10)%10
	r=(dice//100)%10
	s=(dice//1000)%10

	if(a==b or a==c or b==c):
		z,y=highest(p,q,r)
		x=dicetoorderedhand(a,b,z)  	
		return x,y
	else:
		i,j=highest(a,b,c)	
		k=dicetoorderedhand(i,p,q)
		return k,s*10+r

def	highest(a,b,c):
	if(a>b):
		if(a>c):
			return a,c*10+b
		else:
			return c,b*10+a
	else:
		if(b>c):
			return b,c*10+a
		else:
			return c,b*10+a

def dicetoorderedhand(a, b, c):
	if(a==b==c):
		return a*100+b*10+c
	else:  			
		if(a>b):
			if(a>c):
				if(b>c):
					return a*100+b*10+c
				else:
					return a*100+c*10+b
			else:
				return c*100+a*10+b
		else:
			if(b>c):
				if(a>c):
					return b*100+a*10+c
				else:
					return b*100+c*10+a
			else:
				if(c>a):
					return c*100+b*10+a
  		
  		
	# your code goes here
	