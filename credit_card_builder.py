#!/usr/bin/env python
#This program is designed to identify valid credit card numbers given partial information
#coder syntax note:  I prefer to use the lower case g at the beginning of a global variable name to easily distinguish it for those nights when I'm up entirely too late and shouldn't be coding

from cards import payment_card
import datetime
import math
import os
import string
import sys


dt = datetime.date.today()
PaymentCard = payment_card.PaymentCard("0", "UNK", "000000", "000000000000", dt, "00000000", "John", "Q", "Doe", "")
gAllowedCardTypes = PaymentCard.tAllowedCardTypes
gAllowedCardInput = ("0","1","2","3","4","5","6","7","8","9","?") #this is a tuple, which cannot be modified unless deliberately converted to a list, modified then converted back to a tuple

def generateReplNumsList(count_of_unknown_numbers):
	"""
	The mathematical formula to calculate the number of permutations is n^r where n is the number of options
	in this case we have (0-9) giving us 10 options.  And r = the permutations, the count of unknown numbers
	"""
	unkNums = count_of_unknown_numbers
	count = 10**unkNums  #n^r
	my_list = list()
	i = 0
	for i in range (count):
		n = str(i)
		if len(n) < unkNums:
			padding = int(unkNums - len(n))
			n = n.zfill(padding+1)
			my_list.append(n)
		else:
			my_list.append(n)
	return(my_list)

def validateCard(cardstring):
	#perform a check using the Luhn algorithm
	#The following was written by https://github.com/jCh0x61/Luhn-Algorithm/blob/master/LuhnChecker.py
	y = cardstring
	c = len(y) - 1
	parity = len(y) & 1
	sum=0

	while True:
		n=int(y[c])
		if c & 1 == parity:
			n*=2
		if n > 9:
			n = n - 9
		sum=sum+n
		c += -1
		if c < 0:
			break
	return ((sum % 10) == 0)

def buildList(thelist, thecard):
	mylist = thelist
	mystring = thecard
	count = thecard.count("?")

	newlist = list()
	newstring = ""
	if len(mylist[1]) == count:
		for i in range (len(mylist)):
			newstring = mystring
			replchars = mylist[i]
			for x in range (count): 
				y=0
				y2 = len(replchars)
				for z in range (len(newstring)):
					if newstring[z] =="?":
						newstring = newstring.replace(newstring[z],replchars[y],1)
						y+=1
			newlist.append(newstring)				
	else:
		print("There is a problem with the replacement chars\n they are too short/long. \nThey have "+str(len(mylist[1]))+" characters and we need "+str(count))
	
	return newlist
			
def generateCardNumbers(pCardNumber, brand):
	partial_card = pCardNumber
	valid_numbers = list()
	replnum_list = list() 
	temp_list = list()
	lbrand = brand
	#This function expects the following values for brand: AMEX,DC,DISC,MC,VISA,UNK
	#Validate the user passed an acceptable values
	if lbrand.strip() in gAllowedCardTypes:
		if lbrand == "VISA": 	# Visa = 4
			partial_card = partial_card.replace(partial_card[0],"4",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			valid_numbers = buildList(replnum_list, partial_card)
							
		elif lbrand == "MC": # MasterCard = 51, 52, 53, 54, 55
			#since MC has two known digits for all of its cards we only need to run the possible number set one
			partial_card = partial_card.replace(partial_card[:2],"50",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			
			for i in range(5):
				partial_card = partial_card.replace(partial_card[1],str(i+1),1)
				temp_list = (buildList(replnum_list, partial_card))
				for x in range(len(temp_list)):
					valid_numbers.append(temp_list[x])
				
		elif lbrand == "DISC":# Discover = 6011, 644, 65,
			partial_card = partial_card.replace(partial_card[:4],"6011",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for x in range(len(temp_list)):
				valid_numbers.append(temp_list[x])
			
			partial_card = partial_card.replace(partial_card[:3],"644",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for y in range(len(temp_list)):
				valid_numbers.append(temp_list[y])
			
			partial_card = partial_card.replace(partial_card[:2],"65",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for z in range(len(temp_list)):
				valid_numbers.append(temp_list[z])

		elif lbrand == "AMEX":# Amex = 34, 37
			#other areas of the code deal with 16 digits, let's, make sure there's only 15
			partial_card = partial_card[:15]
			partial_card = partial_card.replace(partial_card[:2],"34",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for x in range(len(temp_list)):
				valid_numbers.append(temp_list[x])
			
			partial_card = partial_card.replace(partial_card[:2],"37",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for y in range(len(temp_list)):
				valid_numbers.append(temp_list[y])	
					
		elif lbrand == "DC":# Diner's Club = 36, 38
			partial_card = partial_card.replace(partial_card[:2],"36",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for x in range(len(temp_list)):
				valid_numbers.append(temp_list[x])
			
			partial_card = partial_card.replace(partial_card[:2],"38",1)
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			temp_list = (buildList(replnum_list, partial_card))
			for y in range(len(temp_list)):
				valid_numbers.append(temp_list[y])	
		
		elif lbrand == "UNK":
			unks = partial_card.count("?")
			replnum_list = generateReplNumsList(unks)
			valid_numbers = buildList(replnum_list, partial_card)
		else:
			print(lbrand)
	
	else: 
		print("An invalid card type has been passed to the card generator.\n Allowed inputs are "+gAllowedCardTypes)
	
	return(valid_numbers)

def findIssuer():
	brand = "UNK"
	try:
		BrandKnown = int(input("\nDo you know the card brand i.e. Visa? Enter 1 for Yes, 2 for No:  "))
	except ValueError:
		print ("\nERROR:  That isn't a number! Goodbye!")
	if BrandKnown == 1:
		try:
			brand = int(input("\nEnter the number representing the brand\n 1 American Express\n 2 Diner's Club\n 3 Discover\n 4 MasterCard\n 5 Visa\n\nThe corresponding number for the brand is:"))
			if brand == 1:   brand = "AMEX" 
			elif brand == 2: brand = "DC"
			elif brand == 3: brand = "DISC"
			elif brand == 4: brand = "MC"
			elif brand == 5: brand = "VISA"
			else:
				print ("The number you entered is not valid entry. Goodbye!")
		except ValueError:
			print ("\nERROR:  That isn't a number! Goodbye!")
	else:
		#we don't know the card brand, and we do not know the first digit, which will would tell us the brand
		print("\n(\_/)\n(>.<)\n  .")
		brand = "UNK"
	return(brand)

def cleanUpInput(userInput):
	CardNumberUserInput = userInput
	Warnings = ""
	InvalidChars =""
	try:
		ModuleReport =("\nYou entered: "+CardNumberUserInput)
    	#Time to clean up user input from the people who can't follow directions
		
		#remove any spaces the user should not have entered
		CardNumberUserInput = CardNumberUserInput.replace(" ","")
		Warnings +=("\nIf your entry contained spaces, they were removed.")
		
		#truncate it down to the first 16 characters
		if len(CardNumberUserInput) > 16:
			Warnings += ("\nYou entered " + str(len(CardNumberUserInput)) +" characters only the first 16 were used.")
			CardNumberUserInput = (CardNumberUserInput[:16]) 
			Warnings += ("\nYour input was truncated to: "+CardNumberUserInput)
		else: 
			Warnings += ("\nYour input did not have a minimum of 16 characters so ? were added to the end.")
			for x in range(16-len(CardNumberUserInput)): #append question marks to the end if there are less than 16 digits provided
				CardNumberUserInput = CardNumberUserInput+"?"
		#replace anything that isn't a number or a question mark with a question mark character
		print("\n++++Your input is being validated for numbers and question marks.++++")
		for i in range(len(CardNumberUserInput)): #this could be hard coded to say 0,17, but it would interfere if there is only 14-digit Diners Club card
			if CardNumberUserInput[i] not in gAllowedCardInput:
					InvalidChars += CardNumberUserInput[i]+","
					CardNumberUserInput = CardNumberUserInput.replace(CardNumberUserInput[i],"?")
			else:
				CardNumberUserInput
		if InvalidChars is not "": Warnings += "\nThe following invalid characters "+InvalidChars+ " were replaced with a ?"
	except ValueError:
		print("\nYou entered non string characters. Now go away.")
	if Warnings != "": print("\n****The following WARNINGS were noted in processing your input\n"+Warnings+"\n****\n\nYour partial card number after validation is "+CardNumberUserInput)
	else: print("\nYour input has passed all validation checks.")
	return(CardNumberUserInput)
	
def main():	
	exp_dt = datetime.date.today()
	PC = payment_card.PaymentCard("0", "UNK", "000000", "000000000000", exp_dt, "00000000", "John", "Q", "Doe", "")
	UserInput = ""
	partialPC = ""
	semiFinalCardList = list()
	validCardNumbers = list()

	try:
		UserInput = str(input("\nEnter the numbers you know. \n Replace unknown numbers with the ? symbol \n and do not use spaces or dashes.\n For example ????567890123456:\nThe numbers I know are:  "))
		partialPC = cleanUpInput(UserInput)
	except ValueError:
		print("You have entered values that are not allowed. The program is exiting.")
	
	#if the first digit provided is unknown, it will be a ?, so let's try one other way to figure out the brand
	#ask the user if they can discern the issuer based on the logo
	#otherwise we send the brand_get function a ? for the first char and we are guaranteed to get "UNK" back
	if partialPC[0] == "?":
		PC.brand = findIssuer()
	else:
		PC.brand = PC.brand_get(str(partialPC))
		
	semiFinalCardList = generateCardNumbers(partialPC, PC.brand) 
	print("Before validation are "+str(len(semiFinalCardList))+" possible valid card numbers.")
	
	for i in range(len(semiFinalCardList)):
		if (validateCard(semiFinalCardList[i]) == True):
			validCardNumbers.append(semiFinalCardList[i])
	print("After validation there are "+str(len(validCardNumbers))+" possible VALID card numbers.")
	
	now = datetime.datetime.now() #generates a result of ""YYYY-MM-DD hh:mm:ss.######""
	sNow = str(now)
	sNow = sNow.replace(" ","_")
	sNow = sNow.replace(":","")
	sNow = sNow[:15]
	file_name = "c:/temp/cardfile_"+sNow+".txt"	
	
	with open(file_name, "w") as f:
		for i in range(len(validCardNumbers)):
			f.write(validCardNumbers[i]+"\t")
	f.close
	print("\n(\_/)\n^.^)\n\nYour results file has been placed in c:/temp/ the file name is cardfile_'today's date and time'")



main()
