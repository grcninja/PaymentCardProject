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
gValidCardNumbers = []
gAllowedCardTypes = PaymentCard.tAllowedCardTypes
gAllowedCardInput = ("0","1","2","3","4","5","6","7","8","9","?") #this is a tuple, which cannot be modified unless deliberately converted to a list, modified then converted back to a tuple

def generateNumberList(count_of_unknown_numbers):
	"""
	The mathematical formula to calculate the number of permutations is n^r where n is the number of options
	in this case we have (0-9) giving us 10 options.  And r = the permutations, the count of unknown numbers
	"""
	unkNums = count_of_unknown_numbers
	count = 10**unkNums  #n^r
	my_list = list() 
	i = 0	
	#generate the digits that will be needed, and store them in the list
	for i in range (count):
		n = str(i)
		if len(n) < unkNums:#we need to prepend 0's if the length of the string of numbers is less than the count of unknown numbers
			padding = unkNums - len(n) #figure out how many 0's we need
			n = n.zfill(padding)
			my_list.append(n)
		else:
			my_list.append(n)
	return(my_list)

def validateCard(fCardNumber):
	#The following code was written by JC-SoCal and can be found here:
	#    https://github.com/JC-SoCal/CC_Playground/blob/master/ccluhnbrute.py
	r = [int(ch) for ch in str(fCardNumber)][::-1]

	
def generateCardNumbers(pCardNumber, brand):
	partial_card = pCardNumber
	valid_numbers =()
	master_list = list() #not setting a max length leaves room for the list to grow, so we'll set it later
	lbrand = brand
	#This function expects the following values for brand: AMEX,DC,DISC,MC,VISA,UNK
	#Validate the user passed an acceptable values
	if lbrand.strip() in gAllowedCardTypes:
		if lbrand == "VISA": 	# Visa = 4
			partial_card = partial_card.replace(partial_card[0],"4")
			count_of_questionmarks = partial_card.count("?")
			master_list = generateNumberList(count_of_questionmarks)
			#get the first number in the list
			
			for i in (len(master_list)):
				for index_number in range(unknown_number_count):
					replacement_number_string = master_list[index_number]
					temp_card = partial_card
					for char_index in range(count_of_questionmarks):
						replacement_char = replacement_number_string[char_index]
						index_of_card_char_to_replace = temp_card.find("?")
						temp_card = temp_card.replace(temp_card[index_of_card_char_to_replace],replacement_char)
						print("\nthere are "+str(temp_card.count("?"))+" left to replace.")
					valid = False
					valid = validateCard(temp_card)#check to see if the new full card number is a valid one
					if valid == True:
					valid_numbers.append(temp_card)#if it's valid, add it to the list
		"""					
		elif lbrand == "MC": # MasterCard = 51, 52, 53, 54, 55
			#since MC has two known digits for all of its cards we only need to run the possible number set one
			partial_card = partial_card.replace(partial_card[0,2],"50")
			count = partial_card.count("?")
			master_list.maxlen = count
			master_list = generateNumberList(count)
			
			for i in range(5):
				for i == 1:
					partial_card[1] = "1"
					print("go make the 51 series card numbers")
				for i == 2:
					partial_card[1] = "2"
					print("go make the 52 series card numbers")
				for i == 3:
					partial_card[1] = "4"
					print("go make the 53 series card numbers")	
				for i == 4:
					partial_card[1] = "4"
					print("go make the 54 series card numbers")
				for i == 5:
					partial_card[1] = "5"
					print("go make the 55 series card numbers")
					
			print("gotta make master card numbers")	
		elif lbrand == "DISC":# Discover = 6011, 644, 65,
			i = 0
			for i in range (3):
				for i == 1:
					four = (partial_card.replace(partial_card[0,4] = "6011")					
					count = four.count("?")
					my_list4 = list()
					my_list4.maxlen = count
					my_list4 = generateNumberList(count)
					#now go iterate through the possible numbers for each item in the list, replacing each ? with a digit
				for i == 2:
					three = (partial_card = partial_card.replace[0,3] = "644")
					count = three.count("?")
					my_list3 = list()
					my_list3.maxlen = count
					my_list3 = generateNumberList(count)
					#now go iterate through the possible numbers for each item in the list, replacing each ? with a digit
				for i == 3:
					two = (partial_card = partial_card.replace[0,2] = "65")
					count = two.count("?")
					my_list2 = list()
					my_list2.maxlen = count
					my_list2 = generateNumberList(count)
					#now go iterate through the possible numbers for each item in the list, replacing each ? with a digit

			print("gotta make discover numbers")
		elif lbrand == "AMEX":# Amex = 34, 37
			#other areas of the code deal with 16 digits, let's, make sure there's only 15
			partial_card = partial_card[:15]
			#first let's just replace the the first two numbers
			partial_card = partial_card.replace(partial_card[0,2],"34")
			count = partial_card.count("?")
			master_list.maxlen = count
			master_list = generateNumberList(count)
			#now control the loop to generate card numbers and only do runs using 51-55
			print("gotta make amex numbers")			
		elif lbrand == "DC":# Diner's Club = 36, 38
			#first let's just replace the the first two numbers
			partial_card = partial_card.replace(partial_card[0,2],"36")
			count = partial_card.count("?")
			master_list.maxlen = count
			master_list = generateNumberList(count)
			#now control the loop to generate card numbers and only do runs using 51-55
			print("gotta make diners club numbers")		
		elif lbrand == "UNK":
			print("gotta make way too many numbers")
			generateNumberList(partial_card.count("?"))
		else:
			print(lbrand)
		"""
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
		PC.brand = findIssuer()
	else:
		PC.brand = PC.brand_get(str(partialPC))
		
	gValidCardNumbers = generateCardNumbers(partialPC, PC.brand) 
	
	for i in range(len(gValidCardNumbers)):
		with open("c:/temp/cardfile_"+str(datetime.now()), "w") as f:
			f.write(gValidCardNumbers[i]+"\t")
		f.close
	print("Your results file has been placed in c:/temp/ the file name is cardfile_'today's date and time'")



main()
	
	

	
	
	
	
	
	
	
	
	
	
	
	
"""
	gUserCardInput = whatDoWeKnow() #we start with a gUserCardInput value of "unknown" and the function whatDoWeKnow should update this

#Visa = 4
#MasterCard = 51, 52, 53, 54, 55
#Discover = 6011, 644, 65,
#Amex = 34, 37
#Diner's Club = 36, 38

if gUserCardInput[0] == "?": 
	gBrand = findIssuer(gUserCardInput) #we don't know the first number so let's see if the user can tell us who made the card
	generateCardNumber(gUserCardInput, gBrand)
elif gUserCardInput[0] == "4": generateCardNumber(gUserCardInput,"VISA") 
elif gUserCardInput[0] == "5": generateCardNumber(gUserCardInput,"MC") 
elif gUserCardInput[0] == "6": generateCardNumber(gUserCardInput,"DISC") 
else:#so the first must be a 3, in which case we can determine if it is an AMEX or Diner's Club card provided we have the 2nd digit
	if "AMEX" == isItAmexOrDC(gUserCardInput): generateCardNumber(gUserCardInput,"AMEX") 
	elif "DC" == isItAmexOrDC(gUserCardInput): generateCardNumber(gUserCardInput,"DC") 
	else: generateCardNumber(gUserCardInput,"UNK") 

	
	

#The following code was written by JC-SoCal and can be found on git hub at 
#https://github.com/JC-SoCal/CC_Playground/blob/master/ccluhnbrute.py
#It has been modified to serve as the card builder for this program


	
#The following code was written by SecurityForUs and an be found on git hub at 
#https://github.com/SecurityForUs/PythonUtils/blob/master/luhnalgo.py
#It has been converted into a function here and the ValidCard variable has been added


"""
