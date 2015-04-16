#ClassPaymentCard
#created using python 3.4
#author twitter @grc_ninja


import datetime
import math
import string 
import sys
import types

class PaymentCard(object):
	tAllowedCardTypes = ("MC","VISA","AMEX","DC","DISC","UNK")
	tKnownCardTypes = ("MC","VISA","AMEX","DC","DISC")
	#ALL arguments must be strings except for the expiration_date which mush be a date value
	#python 3 allows isinstance(x, type) to check and see if the variable is the proper type
	#reference: https://docs.python.org/3.4/library/types.html
	
	def __init__(self, industry, brand, ccv, account_number, expiration_date, issuer_identification_number, first, MI, last, suffix):
       
		if (industry != "" and isinstance(industry,str)):
			self.industry = industry.rstrip()
			self.industry = industry.lstrip()
			self.industry = industry[:1]
		else: self.industry = None
		#self.industry = industry
		if (brand != "" and isinstance(industry,str)):
			if (len(brand.strip()) > 4): 
				brand.strip()
				self.brand = brand[:4]
			else: 
				self.brand = brand.strip()
		else: 
			self.brand = None
		#self.brand = brand
		if (ccv!= "" and isinstance(industry,str)):
			if (len(ccv.strip()) > 4): #AMEX ccv's are four digits, so make sure you don't change this to 3
				ccv.strip()
				self.ccv = ccv[:4]
			else: 
				self.ccv = ccv.strip()
		else: 
			self.ccv = None
		#self.ccv = ccv
		if (account_number != "" and isinstance(industry,str)):
			if (len(account_number.strip()) > 9): 	
				account_number.strip()
				self.account_number = account_number[:9]
			else: 
				self.account_number = account_number.strip()
		else: 
			self.account_number = None
		#self.account_number = account_number
		
		if (isinstance(expiration_date, datetime) and expiration_date > date.today()):
			self.expiration_date = expiration_date
		else: 
			self.expiration_date = None	
		#self.expiration_date = expiration_date
		
		if (issuer_identification_number != ""and isinstance(industry,str)):
			if (len(issuer_identification_number.strip()) > 6): 
				issuer_identification_number.strip()
				self.issuer_identification_number = issuer_identification_number[:6]
			else: 
				self.issuer_identification_number = issuer_identification_number.strip() #we should actually enforce there be exactly 6 chars
		else: 
			self.issuer_identification_number = None	
		#self.issuer_identification_number = issuer_identification_number
		if (owner_first_name != "" and isinstance(industry,str)):			
			if (len(first.strip()) > 25): 
				first.strip()
				self.owner_first_name = first[:25]
			else: 
				self.owner_first_name = first.strip()
		else: 
			self.owner_first_name = None	
		#self.first = first
		if (owner_MI != "" and isinstance(industry,str)):
			if (len(MI.strip()) > 2): 
				self.owner_MI = MI.strip()
				self.owner_MI = MI[:2] #we will be nice because some people have two middle names
			else: 
				self.owner_MI = MI.strip()
		else: 
			self.owner_MI = None
		#self.MI = MI
		if (owner_last_name != "" and isinstance(industry,str)):
			if (len(last.strip()) > 25): 
				last.strip()
				self.owner_last_name = last[:25]
			else: 
				owner_last_name = last.strip()
		else: 
			self.owner_last_name =  None	
		#self.last = last
		if (owner_suffix != "" and isinstance(industry,str)):
			if (len(suffix.strip()) > 4):
				suffix.strip()
				self.owner_suffix = suffix[:4]
			else:
				suffix.strip()
		else: 
			self.suffix =  None
		#self.suffix = suffix
		
	def industry(self):
		return self.industry
	def brand(self):
		return self.brand
	def ccv(self):
		return self.ccv
	def account_number(self):
		return self.account_number
	def expiration_date(self):
		return self.expiration_date
	def issuer_identification_number(self):
		return self.issuer_identification_number
	def owner_first_name(self):
		return self.owner_first_name
	def owner_MI(self):
		return self.owner_MI
	def owner_last_name(self):
		return self.owner_last_name
	def owner_suffix(self):
		return self.owner_suffix
	def industry_get(str_card_number):
		# 1 = Airline
		# 2 = Airline
		# 3 = Travel and Entertainment
		# 4 = Banking
		# 5 = Banking
		# 6 = Merchandising and Banking
		# 7 = Petroleum
		# 8 = Telecommunications
		# 9 = National Assignment
		try:
			industry = ""
			card_number = str_card_number.strip()
			val = int(card_number[0]) #the first digit of a credit card identifies it's industry
			
			if (1<= val <= 2): industry="Airline"
			elif val == 3: industry="Travel and Entertainment"
			elif (4<= val <=5): industry="Banking"
			elif val == 6:industry="Merchandising and Banking"
			elif val == 7:industry="Petroleum"
			elif val == 8:industry="Telecommunications"
			elif val == 9:industry="National Assignment"
			else:
				industry="Unknown"
		except ValueError:
			print("The card number value contains an invalid character at the 0th index.\n A null value has been returned for the industry.")
			industry = None
		return(industy)	
	def brand_get(str_card_number):
		# Visa = 4
		# MasterCard = 51, 52, 53, 54, 55
		# Discover = 6011, 644, 65,
		# Amex = 34, 37
		# Diner's Club = 36, 38
		brand, val = ""
		card_number = str_card_number.strip()
		try:
			val = card_number[:4]
			if val[0] == "4": brand = "VISA"
			if (51<= int(val[:2],10) <= 55): brand = "MC"
			if (val == "6011" or val[:3]=="644" or val=="65"): brand ="DISC"
			if (val[:2]=="34" or val[:2]=="37"): brand = "AMEX"
			if (val[:2]=="36" or val[:2]=="38"): brand = "DC"
			else:
				brand = "UNK"
		except ValueError:
			print("The card number value contains an invalid characters.\n A null value has been returned for the brand.")
			brand = None
		return(brand)	
	def ccv_set(digits, brand):
		Warnings = ""
		ccv = ""
		try:
			code = digits.strip()
			lbrand = brand.strip()
			need, x = 0
			
			if (lbrand in tKnownCardTypes and lbrand != "AMEX"): #note that a card type of UNK will not be processed
				if (len(code)>3): #if more than three digits were provided, use only the first three
					Warnings += ("\nMore than three digits were provided for the ccv code of a non-AMEX card.\n Only the first three were used.")
					ccv == code[:3]
				elif (len(code)<3):
					Warnings += ("\nNot enough digits were provided for the ccv code of a non-AMEX card.\n 0's have been added to the end.")
					need = (3 - len(code))
					for x in range(need):
						code.append("0")					
			elif lbrand == "AMEX":
				if (len(code)>4): #if more than three digits were provided, use only the first three
					Warnings += ("\nMore than four digits were provided for the ccv code of an AMEX card.\n Only the first four were used.")
					ccv == code[:4]
				elif (len(code)<4):
					Warnings += ("\nNot enough digits were provided for the ccv code of an AMEX card.\n 0's have been added to the end.")
					need = (4 - len(code))
					for x in range(need):
						code.append("0")
			else:
				code == None
				Warnings += ("\nThe brand either could not be determined or was 'UNK' and \n a null value has been returned for the ccv number.")
			if Warnings != "":
				print (Warnings)
		except ValueError:
			print("There was a problem with the digits or brand values passed to the set_ccv function.\n A null value has been returned for the ccv.")
			code = None
		return(code)
	def ccv_random(brand):
		Warnings = ""
		ccv = ""
		try:
			lbrand = brand.strip()
			if (lbrand in tAllowedCardTypes and lbrand != "AMEX"): #note this can be used even if the brand is "UNK"
				ccv = random.randint(000, 999)				
			else:
				ccv = random.randint(0000, 9999)	
		except ValueError:
			print("There was a problem with the digits or brand values passed to the set_ccv function.\n A null value has been returned for the ccv.")
			ccv = None
		return(ccv)
	def issuer_identification_number_get(str_card_number):
		card_number = str_card_number
		iin = ""
		#The IIN is the first 6 digits of the card number
		# Visa = 4
		# MasterCard = 51, 52, 53, 54, 55
		# Discover = 6011, 644, 65,
		# Amex = 34, 37
		# Diner's Club = 36, 38
		try:
			iin = int(card_number[:6], 10)
		except ValueError:
			print("The card number value contains an invalid characters that could not convert to integers. \nA null value has been returned for the iin.")
			iin = None
		return(iin)
	def owner_full_name_set(first_name, last_name, MI, suffix):
		owner_name = ""
		if (self.MI == ""):
			 owner_name = (self.owner_first_name+" "+self.owner_last_name+" "+self.owner_suffix)
			 owner_name.rstrip() #just in case there is no value for the suffix, remove the spaces at the end
		else:
			owner_name = (self.owner_first_name+" "+self.owner_MI+" "+self.owner_last_name+" "+self.owner_suffix)
			owner_name.rstrip() #just in case there is no value for the suffix, remove the spaces at the end
		
		return(owner_name)	
	#need a function for extracting the account number from the full card number
	#need a function for setting a random expiration date
