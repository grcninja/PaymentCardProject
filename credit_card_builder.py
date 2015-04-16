#!/usr/bin/env python
#This program is designed to guess possible credit card numbers give partial information
#coder syntax note:  I prefer to use the lower case g at the beginning of a global variable name to easily distinguish it for those nights when I'm up entirely too late and shouldn't be coding

from cards import payment_card
import datetime
import math
import string
import sys

dt = datetime.date.today()
PaymentCard = payment_card.PaymentCard("0", "UNK", "000000", "000000000000", dt, "00000000", "John", "Q", "Doe", "")
gPossibleCardNumbers = []
gAllowedCardTypes = PaymentCard.tAllowedCardTypes
gAllowedCardInput = ("0","1","2","3","4","5","6","7","8","9","?") #this is a tuple, which cannot be modified unless deliberately converted to a list, modified then converted back to a tuple

def getIndexesOfUnknownNumbers(pCardNumber):
	card = pCardNumber
	unknownNumberIndexes = []
	x = 0
	for x in range(len(card)):
		if card[x] == "?": #figure out what the index is of the question mark
			unknownNumberIndexes.append(x) #add that index to the array holding the position number for the unknown numbers
		else: 
			unknownNumberIndexes
	return(unknownNumberIndexes)

def generateCardNumber(pCardNumber, brand):
	lbrand = brand
	pCardNumber = pCardNumber
	indexesOfUnknownsNums = getIndexesOfUnknownNumbers(pCardNumber)
	
	#This function expects the following values for brand: AMEX,DC,DISC,MC,VISA,UNK
	#Validate the user passed an acceptable values
	if lbrand.strip() in gAllowedCardTypes:
		if lbrand == "VISA": 
			print("gotta make visa numbers")
		elif lbrand == "MC":
			print("gotta make master card numbers")
		elif lbrand == "DISC":
			print("gotta make discover numbers")
		elif lbrand == "AMEX":
			print("gotta make amex numbers")
		elif lbrand == "DC":
			print("gotta make diners club numbers")
		elif lbrand == "UNK":
			print("gotta make way too many numbers")
		else: 
			print(lbrand)
	else: 
		print("An invalid card type has been passed to the card generator.\n Allowed inputs are "+gAllowedCardTypes)
	return()

def findIssuer(pCardNumber):
	unknownCardNumber = pCardNumber
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
		print("\n(\_/)\n(>.<)\nThis is going to be more difficult than expected.")
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
		Warnings +=("\nYour entry contained spaces, they were removed.")
		
		#truncate it down to the first 16 characters
		if len(CardNumberUserInput) > 16:
			Warnings += ("\nYou entered " + str(len(CardNumberUserInput)) +" characters only the first 16 were used.")
			CardNumberUserInput = (CardNumberUserInput[:16]) 
			Warnings += ("\nYour input was truncated to: "+CardNumberUserInput)
		else: 
			for x in range(16-len(CardNumberUserInput)): #append question marks to the end if there are less than 16 digits provided
				CardNumberUserInput.append("?")
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
	if Warnings != "": print("\n****The following WARNINGS were noted in processing your input\n"+Warnings+"\n****\n\nYour final card number after validation is "+CardNumberUserInput)
	else: print("\nYour input has passed all validation checks.")
	return(CardNumberUserInput)
	
def main():	
	exp_dt = datetime.date.today()
	PC = payment_card.PaymentCard("0", "UNK", "000000", "000000000000", exp_dt, "00000000", "John", "Q", "Doe", "")
	UserInput = ""
	partialPC = ""
	try:
		UserInput = str(input("\nEnter the numbers you know. \n Replace unknown numbers with the ? symbol \n and do not use spaces or dashes.\n For example ????567890123456:\nThe numbers I know are:  "))
		partialPC = cleanUpInput(UserInput)
	except ValueError:
		print("You have entered values that are not allowed. The program is exiting.")
	
	#if the first digit provided is unknown, it will be a ?, so let's try one other way to figure out the brand
	#ask the user if they can discern the issuer based on the logo
	#otherwise we send the brand_get function a ? for the first char and we are guaranteed to get "UNK" back
	if partialPC[0] == "?":
		PC.brand = findIssuer(partialPC)
	else:
		PC.brand = PC.brand_get(partialPC)
		
	generateCardNumber(partialPC, PC.brand) 


main()
