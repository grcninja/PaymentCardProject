# Payment Card Number Generation 

##Code Status:  WORKING

##Python Version: 3.4.3

##Summary:  

This project is aimed at creating a tool to generate legitimate credit card numbers based on partial user input.  This tool will be used as a training aid to demonstrate to users the quickness with which only *legitimate* credit card numbers can be generated then combined with OSINT to compromise their personally identifiable/financial information. The training should give the users a reality check and influence a change in behavior toward safer behavior. This tool is not intended for malicious use.

NOTES: 
The `payment_cards.py` file is a library that needs to be placed in a directory called `cards` and you need a blank `__init__.py` (without the spaces) file in the directory with it.  If you do not do this then the actual program `credit_card_builder.py` will not work

The file structure should look like this:
`_MyCardBuilder` (root folder you'll have to make it)

1. contains one file: `credit_card_builder.py`
2. root folder also contains another folder: cards (folder you'll have to make, no quotes)
3. the cards folder needs two files in it. 1st) `__init__.py` (it can be blank, just need one with this name) 2nd) `payment_card.py`
